#!/usr/bin/env python3
"""Structural audit of the eleven papers and the overview. Reports only problems.

Run from anywhere:  python3 audit.py
Exits non-zero when it finds something, so it can gate a push.
"""
import re, sys, os, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(ROOT, "papers")
FILES = sorted(os.path.basename(f) for f in glob.glob(os.path.join(D, "*.md")))
KINDS = ["Theorem", "Proposition", "Corollary", "Lemma", "Definition"]
prob = []
def P(f, msg): prob.append(f"[{f}] {msg}")

texts = {}
for f in FILES:
    texts[f] = open(os.path.join(D, f), encoding="utf-8").read()

# paper number -> filename, taken from the filesystem rather than a fixed list
PAPER = {}
for f in FILES:
    m = re.match(r'paper_(\d+)_', f)
    if m: PAPER[int(m.group(1))] = f

def strip_math(t):
    t = re.sub(r'\$\$.*?\$\$', ' ', t, flags=re.S)
    t = re.sub(r'\$[^$\n]*\$', ' ', t)
    t = re.sub(r'`[^`]*`', ' ', t)
    return t

def headings(t):
    """Every section and appendix label declared in t, with ancestors."""
    s = set()
    for m in re.finditer(r'(?:^|\n)#{2,5}\s+(\d+(?:\.\d+)*)\.?\s', t):
        p = m.group(1).split('.')
        for i in range(1, len(p) + 1): s.add('.'.join(p[:i]))
    for m in re.finditer(r'(?:^|\n)#{2,5}\s+(?:Appendix\s+)?([A-Z](?:\.\d+)*)[\s\u2014-]', t):
        p = m.group(1).split('.')
        for i in range(1, len(p) + 1): s.add('.'.join(p[:i]))
    return s

def declared(t, kind):
    d = set()
    alt = '(?:Theorem|Verified Law)' if kind == 'Theorem' else re.escape(kind)
    for m in re.finditer(r'(?:^|\n)(?:#{2,4}[^\n]*?|>\s*\*\*|\|\s*\*\*)%s\s+(\d+[a-z]?)[\.:\s\*]' % alt, t):
        d.add(m.group(1))
    return d

for f in FILES:
    t = texts[f]
    lines = t.split("\n")

    # ---- 1. statement numbering: in order of appearance, no duplicates
    for kind in KINDS:
        alt = '(?:Theorem|Verified Law)' if kind == 'Theorem' else re.escape(kind)
        pat = re.compile(r'(?:^|\n)(?:#{2,4}[^\n]*?|>\s*\*\*)%s\s+(\d+)([a-z]?)[\.:\s]' % alt)
        nums = [(int(m.group(1)), m.group(2), m.start()) for m in pat.finditer(t)]
        if not nums: continue
        # letter-suffixed variants (Corollary 2a) do not open a new base slot, and may
        # legitimately sit in an appendix after later base numbers
        base = []
        for n, s, _ in nums:
            if s: continue
            if not base or base[-1] != n: base.append(n)
        if not base: continue
        # every part numbers its own results from one, so the sequence must start at
        # one, be in order, and have no gap
        if base[0] != 1: P(f, f"{kind}: sequence starts at {base[0]}, not 1")
        if base != sorted(base): P(f, f"{kind}: headings out of order: {base}")
        miss = [x for x in range(1, max(base) + 1) if x not in base]
        if miss: P(f, f"{kind}: numbering gap, missing {miss} (present {base})")
        dup = [x for x in set(base) if base.count(x) > 1]
        if dup: P(f, f"{kind}: duplicate base numbers {sorted(dup)}")
        for n, s, pos in nums:
            if s and n not in base: P(f, f"{kind} {n}{s}: no base {kind} {n}")

    # ---- 2. equation tags: declared vs cited
    tags = (re.findall(r'\\tag\{([^}]+)\}', t)
            + re.findall(r'\\text\{\(([0-9A-Z]+\.[0-9]+)\)\}', t)
            + re.findall(r'^\s*\((\d+\.\d+)\)\s*$', t, re.M))
    tagset = [x.strip() for x in tags]
    dupt = [x for x in set(tagset) if tagset.count(x) > 1]
    if dupt: P(f, f"duplicate equation tag(s): {sorted(dupt)}")
    body = strip_math(t)
    for tg in set(tagset):
        cited = len(re.findall(r'\(' + re.escape(tg) + r'\)', body)) > 0 or ('eqref{%s}' % tg) in t
        if not cited: P(f, f"equation tag ({tg}) is never cited")

    # ---- 3. internal statement references resolve
    body_nocite = re.sub(r'\[P?\d+[a-z]?\s*,[^\]]*\]', ' ', body)
    for kind in KINDS:
        d = declared(t, kind)
        if not d: continue
        for m in re.finditer(r'\b%s\s+(\d+[a-z]?)\b' % kind, body_nocite):
            if m.group(1) not in d:
                P(f, f"reference to {kind} {m.group(1)} but it is not declared here (declared: {sorted(d)})")
                break

    # ---- 4. section numbering contiguity
    secs = [int(m.group(1)) for m in re.finditer(r'(?:^|\n)##\s+(\d+)\.', t)]
    if secs:
        u = []
        for s in secs:
            if not u or u[-1] != s: u.append(s)
        if u != sorted(u): P(f, f"sections out of order: {u}")
        miss = [x for x in range(min(u), max(u) + 1) if x not in u]
        if miss: P(f, f"section numbering gap, missing {miss} (present {u})")

    # ---- 4b. numbered sections must precede the appendices
    first_app, last_sec = None, None
    for m in re.finditer(r'(?:^|\n)##\s+(?:(\d+)\.|Appendix\s)', t):
        if m.group(1) is None and first_app is None: first_app = m.start()
        if m.group(1) is not None: last_sec = m.start()
    if first_app is not None and last_sec is not None and last_sec > first_app:
        P(f, "a numbered section appears after the first appendix")

    # ---- 5. unlabelled internal section and appendix references resolve
    subs = headings(t)
    body_nx = re.sub(r'\[[^\]]*\]', ' ', body)
    for m in re.finditer(r'(?:\u00a7|\bSection\s+)(\d+(?:\.\d+)+)', body_nx):
        if m.group(1) not in subs:
            P(f, f"reference to \u00a7{m.group(1)} which has no heading here")
    for m in re.finditer(r'App(?:\.|endix)\s+([A-Z](?:\.\d+)*)', body_nx):
        if m.group(1) not in subs:
            P(f, f"reference to Appendix {m.group(1)} which has no heading here "
                 f"(if it is in a companion paper, write it as [Pn, App. {m.group(1)}])")

    # ---- 6. reference list: contiguous, no duplicate numbers, declared == cited
    entries = [int(x) for x in re.findall(r'^(\d+)\.\s', t.split("## References")[-1], re.M)] \
              if "## References" in t else []
    if entries:
        dupr = [x for x in set(entries) if entries.count(x) > 1]
        if dupr: P(f, f"reference list: number(s) used twice: {sorted(dupr)}")
        if entries != list(range(1, len(entries) + 1)):
            P(f, f"reference list is not numbered 1..{len(entries)}: {entries}")
        refs = set(entries)
        cited = set(int(m.group(1)) for m in re.finditer(r'(?<!P)\[(\d+)(?:,\s*[^\]\d][^\]]*)?\]', body))
        un = sorted(refs - cited)
        if un: P(f, f"reference(s) never cited: {un}")
        bad = sorted(cited - refs)
        if bad: P(f, f"citation(s) to non-existent reference: {bad}")

    # ---- 7. tables: header separator present, consistent column count
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith("|") and lines[i].count("|") >= 2:
            j = i
            while j < len(lines) and lines[j].strip().startswith("|"): j += 1
            blk = lines[i:j]
            if len(blk) >= 2:
                if not re.match(r'^\s*\|[\s:|-]+\|\s*$', blk[1]):
                    P(f, f"table at line {i+1}: no header separator row")
                widths = {r.count("|") for r in blk}
                if len(widths) > 1:
                    P(f, f"table at line {i+1}: inconsistent column count {sorted(widths)}")
            i = j
        else:
            i += 1

    # ---- 8. delimiters
    for k, ln in enumerate(lines, 1):
        if ln.count("**") % 2: P(f, f"line {k}: odd number of ** (bold unbalanced)")
    if t.count("$$") % 2: P(f, "unbalanced $$ across the file")
    for k, ln in enumerate(lines, 1):
        s = re.sub(r'\$\$', '', ln)
        if s.count("$") % 2: P(f, f"line {k}: odd number of inline $")

    # ---- 9. damaged brackets left by an editing pass
    for k, ln in enumerate(lines, 1):
        if re.search(r'\[[^\]]*\]\]', ln): P(f, f"line {k}: doubled closing bracket ']]'")
        if "\u00a7[" in ln: P(f, f"line {k}: section mark before a bracket, '\u00a7['")

    # ---- 9b. phrases left over from the pre-split structure
    for pat, why in [(r'one of (six|seven) papers', "pre-split paper count"),
                     (r'\b(six|seven) (short )?papers\b', "pre-split paper count"),
                     (r'\btwo test cases\b', "Paper 10 runs four tests"),
                     (r'\[\[P\d', "malformed companion citation '[[P'"),
                     (r'\((?:0|I{1,3}|IV|V),\s*(?:Theorem|Thm|Cor|Prop)', "legacy paren citation")]:
        m = re.search(pat, t, re.I)
        if m: P(f, f"stale phrase '{m.group(0)}' ({why})")

    # ---- 9c. the overview declares no results, so every reference in it must be qualified
    if not re.match(r'paper_\d+_', f):
        nb = re.sub(r'\[[^\]]*\]', ' ', body)
        for m in re.finditer(r'(Theorems?|Thms?|Corollar(?:y|ies)|Cors?|Propositions?|Props?|'
                             r'Verified Laws?)\.?\s+(\d+[a-z]?)', nb):
            P(f, f"unqualified reference '{m.group(0)}' - this document declares no results, "
                 f"so it must be written as [Pn, ...]")
            break

    # ---- 10. no legacy labels from the pre-split numbering
    for m in re.finditer(r'\b(?:Paper|Papers)\s+[^.]{0,20}?\b(0|I{1,3}|IV|V)\b(?!\w)', body):
        P(f, f"legacy label '{m.group(0)}' from the pre-split numbering")
        break
    for m in re.finditer(r'\[(0|I{1,3}|IV|V)\s*,', body):
        P(f, f"legacy cross-reference '{m.group(0)}...]' from the pre-split numbering")
        break

# ---- 11. cross-paper references [Pn, ...] point at something that exists
ABB = {"Thm": "Theorem", "Thms": "Theorem", "Prop": "Proposition", "Props": "Proposition",
       "Cor": "Corollary", "Cors": "Corollary", "Lem": "Lemma", "Def": "Definition",
       "Theorem": "Theorem", "Theorems": "Theorem", "Proposition": "Proposition",
       "Corollary": "Corollary", "Lemma": "Lemma", "Definition": "Definition",
       "Verified Law": "Theorem"}
for f in FILES:
    body = strip_math(texts[f])
    for m in re.finditer(r'\[P(\d{1,2})\s*,\s*([^\]]+)\]', body):
        n, ref = int(m.group(1)), m.group(2).strip()
        tgt = PAPER.get(n)
        if not tgt:
            P(f, f"cross-reference [P{n}, ...] but there is no paper {n}")
            continue
        if tgt == f:
            P(f, f"self-citation [P{n}, {ref}] - a paper should not cite itself by label")
        tt = texts[tgt]
        for kk, num in re.findall(r'(Thms|Thm|Theorems|Theorem|Props|Prop|Proposition|'
                                  r'Cors|Cor|Corollary|Lemma|Verified Law)\.?\s*(\d+[a-z]?)', ref):
            if num not in declared(tt, ABB[kk]):
                P(f, f"cross-reference [P{n}, {ref}] -> {ABB[kk]} {num} not declared in paper {n}")
        h = headings(tt)
        for s in re.findall(r'\u00a7+\s*(\d+(?:\.\d+)*)', ref):
            if s not in h: P(f, f"cross-reference [P{n}, \u00a7{s}] has no such heading in paper {n}")
        for a in re.findall(r'App(?:\.|endix)?\s+([A-Z](?:\.\d+)*)', ref):
            if a not in h: P(f, f"cross-reference [P{n}, App. {a}] has no such appendix in paper {n}")

# ---- 12. the counts stated in the metadata match the filesystem
npapers = len(PAPER)
nover = len(FILES) - npapers
nscripts = len(glob.glob(os.path.join(ROOT, "code", "verify_*.py")))
NUM = {"seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12}
for fn in ("README.md", "CITATION.cff", ".zenodo.json", os.path.join("code", "build_site.py")):
    p = os.path.join(ROOT, fn)
    if not os.path.exists(p): continue
    s = open(p, encoding="utf-8").read().lower()
    for m in re.finditer(r'\b(seven|eight|nine|ten|eleven|twelve)\s+(papers|documents)\b', s):
        w, kind = m.group(1), m.group(2)
        if kind == "documents":
            prob.append(f"[{fn}] says '{m.group(0)}'; count papers and the overview separately "
                        f"({npapers} papers, {nover} overview)")
        elif NUM[w] != npapers:
            prob.append(f"[{fn}] says '{m.group(0)}' but there are {npapers} papers on disk")
    for m in re.finditer(r'\b(seven|eight|nine|ten)\s+verification scripts\b', s):
        if NUM[m.group(1)] != nscripts:
            prob.append(f"[{fn}] says '{m.group(0)}' but there are {nscripts} in code/")

print("\n".join(prob) if prob else "no problems found")
print(f"\n--- {len(prob)} item(s)")
sys.exit(1 if prob else 0)
