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
# The script count is written out in words and is now above twenty, so the words
# are compound.  Match the compound BEFORE the unit, or "twenty-seven" is read as
# "seven" and every count reads wrong.
UNITS = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
TENS  = {"twenty":20,"thirty":30,"forty":40,"fifty":50}
def wordnum(w):
    w = w.replace("\u2013","-").strip()
    if "-" in w:
        a, b = w.split("-", 1)
        return TENS.get(a, 0) + UNITS.get(b, 0)
    return TENS.get(w, UNITS.get(w, NUM.get(w, 0)))
WORDNUM_RE = (r"(?:twenty|thirty|forty|fifty)(?:[-\u2013](?:one|two|three|four|five|six|seven|eight|nine))?"
              r"|seven|eight|nine|ten|eleven|twelve")
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
    for m in re.finditer(r'\b(' + WORDNUM_RE + r')\s+verification scripts\b', s):
        if wordnum(m.group(1)) != nscripts:
            prob.append(f"[{fn}] says '{m.group(0)}' but there are {nscripts} in code/")


# ---------------------------------------------------------------- check 4b
# COVERAGE.md must have one row per verification script and no row without one.
# A COVERS line names a section; the coverage row names the DEFINITION, which is
# where three review passes each found a script passing against a quantity the
# paper never stated.
_cov = os.path.join(ROOT, "COVERAGE.md")
if os.path.exists(_cov):
    _c = open(_cov, encoding="utf-8").read()
    _scripts = sorted(os.path.basename(x) for x in glob.glob(os.path.join(ROOT, "code", "verify_*.py")))
    for _s in _scripts:
        if _s not in _c:
            prob.append(f"[COVERAGE.md] no row for {_s}")
    for _m in set(re.findall(r"`(verify_[a-z0-9_]+\.py)`", _c)):
        if _m not in _scripts:
            prob.append(f"[COVERAGE.md] row for {_m}, which is not in code/")
else:
    prob.append("COVERAGE.md is missing")

# ---------------------------------------------------------------- check 4c
# The DOI is written in six places and must be the same in all of them, and must
# not still be the placeholder when a release is cut.  code/set_doi.py writes all
# six at once; this check is what stops a push with a dead link.
_doi = set()
for _rel in ("README.md", "CITATION.cff", os.path.join("code", "build_site.py"),
             os.path.join("docs", "index.html")):
    _p = os.path.join(ROOT, _rel)
    if not os.path.exists(_p): continue
    for _m in re.findall(r"10\.5281/zenodo\.(?:\d+|RESERVED)", open(_p, encoding="utf-8").read()):
        if _m != "10.5281/zenodo.21638887":      # the other repository's DOI
            _doi.add((_rel, _m))
_vals = {v for _, v in _doi}
if len(_vals) > 1:
    prob.append(f"the DOI differs between files: {sorted(_doi)}")
if "10.5281/zenodo.RESERVED" in _vals:
    prob.append("the DOI is still the placeholder — reserve one on Zenodo and run "
                "code/set_doi.py before publishing")

# ---------------------------------------------------------------- check 4d
# A release must not carry the working files.  They are listed in .gitignore
# under a comment saying so; this check reads that list rather than repeating it,
# so the two cannot drift apart.
_gi = os.path.join(ROOT, ".gitignore")
if os.path.exists(_gi):
    _lines = open(_gi, encoding="utf-8").read().splitlines()
    try:
        _start = next(i for i, l in enumerate(_lines) if l.startswith("# working files"))
        _work = [l.strip() for l in _lines[_start:] if l.strip() and not l.startswith("#")]
    except StopIteration:
        _work = []
    _here = [w for w in _work if os.path.exists(os.path.join(ROOT, w))]
    if _here and os.environ.get("RELEASE_BUILD"):
        prob.append("working files present in a release build: " + ", ".join(_here))

# ---------------------------------------------------------------- check 5
# A bracket must not mean two things.  Sibling papers are [P1]-[P11]; a bare
# [n] must be an entry in that file's own reference list, and nothing else.
import glob as _glob, re as _re, os as _os
CODE_ = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "code")
for _fn in sorted(_glob.glob(_os.path.join(D, "*.md"))):
    _t = open(_fn, encoding="utf-8").read()
    _base = _os.path.basename(_fn)
    _m = _re.search(r"^#+\s*References\s*$", _t, _re.M)
    _refs = set()
    if _m:
        for _r in _re.finditer(r"^\s*(?:\[(\d+)\]|(\d+)\.)\s", _t[_m.end():], _re.M):
            _refs.add(int(_r.group(1) or _r.group(2)))
    _body = _t[:_m.start()] if _m else _t
    _bad = sorted({int(_c.group(1)) for _c in _re.finditer(r"(?<!P)\[(\d+)\]", _body)} - _refs)
    if _bad:
        prob.append(f"[{_base}] bare citation(s) {_bad} with no entry in this "
                    f"file's reference list - a bracket number must not also name a paper")
    _badp = sorted({int(_c.group(1)) for _c in _re.finditer(r"\[P(\d+)", _t)} - set(range(1, 12)))
    if _badp:
        prob.append(f"[{_base}] sibling citation(s) {['P'+str(_x) for _x in _badp]} outside the range P1-P11")

# every verification script declares what it covers
for _sc in sorted(_glob.glob(_os.path.join(CODE_, "verify_*.py"))):
    if not _re.search(r"^COVERS\s*=", open(_sc, encoding="utf-8").read(), _re.M):
        prob.append(f"[{_os.path.basename(_sc)}] has no COVERS line")

print("\n".join(prob) if prob else "no problems found")
print(f"\n--- {len(prob)} item(s)")
sys.exit(1 if prob else 0)
