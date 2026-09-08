#!/usr/bin/env python3
"""
verify_exception_certificate.py

COVERS = ["[P6, S2.3]"]

The certificate behind "the ceiling of 31 cannot be lowered by any finite set of
lines" — the part `verify_exception_dichotomy.py` does not emit.  That script
reaches the ceiling, the nine extremal alignments and the surviving alignment;
this one produces the objects the argument rests on:

  1. the maximal configurations at those alignments — the paper says 28, and 28
     is what comes out, each carrying 31 cells and 27 to 30 linear conditions;
  2. the elimination of 27 of them by a fixed prime divisor, with the primes
     named, reported in an order-independent form (every prime that kills each
     configuration, not only the first one tried);
  3. the survivor, its 59 polynomials of total degree 90, and an admissible
     residue for EVERY prime, with the bound that makes the check finite.

The finiteness is the point of the third item.  A configuration is impossible if
some prime divides one of its polynomials for every residue of t.  The system has
total degree 90, so for q > 90 the polynomials have at most 90 roots together and
a residue always survives; only q <= 90 has to be examined, and the script
examines every prime to 200 to leave margin.

What a configuration is.  Over a block of 35 sectors under the twinless
hypothesis, each sector carries a state in {N, P, Q}: which of M+2, M+4 is forced
prime, never both.  A cell of type X at sector i is counted when the states at i
and i+1 are what NEED[X] requires and the cell is open to the lines 5..17.  A
configuration is the resulting SET OF COUNTED CELLS together with the states
those cells force; two optimal state sequences that differ only where no cell is
counted are the same configuration, which is why the raw count of optimal
sequences (357,210) is not the number reported.

Run: python3 verify_exception_certificate.py [--fast]
     --fast checks the survivor and its admissibility only, skipping the scan
     over all 2431 alignments that locates the nine.
"""
COVERS = ["[P6, S2.3]"]

import sys
from collections import Counter
from sympy import primerange

FAST = "--fast" in sys.argv
FAIL = []
def check(tag, got, want):
    ok = got == want
    print(("  [ok ] " if ok else "  [FAIL] ") + f"{tag:<62} {str(got)[:26]:>26}  vs {want}")
    if not ok: FAIL.append(tag)

KEYS = "ABCDEF"
QUADS = {"A": lambda n: 6*n*n+10*n+4, "B": lambda n: 6*n*n+12*n+6,
         "C": lambda n: 6*n*n+14*n+8, "D": lambda n: 6*n*n+16*n+9,
         "E": lambda n: 6*n*n+18*n+11, "F": lambda n: 6*n*n+18*n+13}
NEED = {"A": (("P", 0),), "B": (("P", 0), ("Q", 0)), "C": (("Q", 0),),
        "D": (("P", 0), ("P", 1)), "E": (("P", 0), ("Q", 1)), "F": (("Q", 0), ("P", 1))}
# the partner of each cell: (offset a, constant b), the partner being (M+a)^2 + b
PART = {"A": (2, -2), "B": (3, +1), "C": (4, -2), "D": (5, -11), "E": (6, -14), "F": (6, -2)}
ST = ("N", "P", "Q")
LINES = (5, 7, 11, 13, 17)
PERIOD = 510510
KNOWN_EXTREMAL = [57963, 86103, 115503, 166323, 205593, 238563, 358263, 401943, 448353]

def open6(n):
    out = set()
    for k in KEYS:
        m = QUADS[k](n); a, b = 6*m - 1, 6*m + 1
        if all(a % p and b % p for p in LINES): out.add(k)
    return out

def hitset(O, s0, s1):
    return {k for k in O if all((s0 if d == 0 else s1) == v for v, d in NEED[k])}

def ceiling(Os):
    NEG = -10**9; dp = {s: 0 for s in ST}
    for O in Os:
        nd = {s: NEG for s in ST}
        for s0, v in dp.items():
            if v == NEG: continue
            for s1 in ST:
                w = v + len(hitset(O, s0, s1))
                if w > nd[s1]: nd[s1] = w
        dp = nd
    return max(dp.values())

def optimal_cellsets(Os):
    """Every set of counted cells attaining the ceiling, deduplicated."""
    N = len(Os); NEG = -10**9
    suf = [{s: NEG for s in ST} for _ in range(N+1)]
    for s in ST: suf[N][s] = 0
    for i in range(N-1, -1, -1):
        for s0 in ST:
            suf[i][s0] = max(len(hitset(Os[i], s0, s1)) + suf[i+1][s1] for s1 in ST)
    best = max(suf[0].values())
    out = set()
    def walk(i, s, cells):
        if i == N: out.add(tuple(cells)); return
        for s1 in ST:
            h = hitset(Os[i], s, s1)
            if len(h) + suf[i+1][s1] == suf[i][s]:
                walk(i+1, s1, cells + [tuple(sorted(h))])
    for s in ST:
        if suf[0][s] == best: walk(0, s, [])
    return best, out

def forced_states(cells):
    req = {}
    for i, cs in enumerate(cells):
        for k in cs:
            for v, d in NEED[k]: req[i+d] = v
    return tuple(sorted(req.items()))

def system(cells, f):
    lin = [6*i + (2 if v == "P" else 4) for i, v in f]
    quad = []
    for i, cs in enumerate(cells):
        for k in cs:
            a, b = PART[k]; quad.append((6*i + a, b))
    return lin, quad

def admissible_count(M0, lin, quad, q):
    n = 0
    for t in range(q):
        M = (M0 + PERIOD*t) % q
        if any((M + c) % q == 0 for c in lin): continue
        if any(((M + a)**2 + b) % q == 0 for a, b in quad): continue
        n += 1
    return n

print("verify_exception_certificate.py   mode:", "fast" if FAST else "full")

# ------------------------------------------------------------------ step 1
if FAST:
    extremal = KNOWN_EXTREMAL
    print("\n1. the nine extremal alignments (taken as given in fast mode)")
else:
    print("\n1. scanning all 2431 alignments for the ceiling")
    vals = []; starts = []
    for phase in range(2431):
        n0 = next(phase + 2431*t for t in range(35) if (phase + 2431*t) % 35 == 0)
        starts.append(n0); vals.append(ceiling([open6(n0 + i) for i in range(35)]))
    mx = max(vals)
    extremal = sorted((6*starts[i] + 3) % PERIOD for i, v in enumerate(vals) if v == mx)
    check("the ceiling", mx, 31)
    check("alignments attaining it", len(extremal), 9)
    check("and they are", extremal, KNOWN_EXTREMAL)

# ------------------------------------------------------------------ step 2
print("\n2. the maximal configurations at those alignments")
configs = []
for M0 in extremal:
    n0 = (M0 - 3)//6
    Os = [open6(n0 + i) for i in range(35)]
    best, cellsets = optimal_cellsets(Os)
    for cells in cellsets:
        configs.append((M0, cells, forced_states(cells)))
configs = sorted(set(configs))
check("distinct maximal configurations", len(configs), 28)
check("every one carries 31 cells",
      set(sum(len(c) for c in cells) for _, cells, _ in configs), {31})
lincount = Counter(len(f) for _, _, f in configs)
print("     linear conditions per configuration:", dict(sorted(lincount.items())))
check("linear conditions lie between 27 and 30",
      (min(lincount), max(lincount)), (27, 30))

# ------------------------------------------------------------------ step 3
print("\n3. the fixed-prime-divisor test, every killer named")
killed = {}; survivors = []
for M0, cells, f in configs:
    lin, quad = system(cells, f)
    ks = [q for q in primerange(5, 120) if admissible_count(M0, lin, quad, q) == 0]
    if ks: killed[(M0, f)] = ks
    else: survivors.append((M0, cells, f, lin, quad))
allk = Counter(q for ks in killed.values() for q in ks)
least = Counter(min(ks) for ks in killed.values())
print("     killed by a fixed prime divisor:", len(killed), "of", len(configs))
print("     every prime that kills, with how many configurations it kills:", dict(sorted(allk.items())))
print("     the LEAST killer of each:", dict(sorted(least.items())))
print("     killers per dead configuration:", dict(sorted(Counter(len(k) for k in killed.values()).items())))
check("27 of the 28 are killed", len(killed), 27)
check("the killers are exactly 19, 23, 31", sorted(allk), [19, 23, 31])
check("exactly one configuration survives", len(survivors), 1)
check("and it is the alignment at 448,353", survivors[0][0], 448353)

# ------------------------------------------------------------------ step 4
print("\n4. the survivor, and its admissibility at every prime")
M0, cells, f, lin, quad = survivors[0]
deg = len(lin) + 2*len(quad)
print(f"     {len(lin)} linear and {len(quad)} quadratic conditions"
      f" = {len(lin)+len(quad)} polynomials of total degree {deg}")
check("59 polynomials", len(lin) + len(quad), 59)
check("total degree 90", deg, 90)
rows = sorted((admissible_count(M0, lin, quad, q), q) for q in primerange(5, 200))
print("     tightest primes (admissible residues of t, q):", rows[:4])
check("every prime 5 <= q < 200 leaves an admissible residue", all(n > 0 for n, _ in rows), True)
check("the primes leaving exactly one residue", [q for n, q in rows if n == 1], [19, 31, 47])
check("the degree bound makes q > 90 automatic, so the check above is complete",
      deg < 91 and all(n > 0 for n, q in rows if q <= 90), True)

if "--force-fail" in sys.argv: check("99. forced failure gate", 1, 0)
print()
if FAIL:
    print(f"FAILED: {len(FAIL)} check(s): " + "; ".join(FAIL)); sys.exit(1)
print("all checks passed."); sys.exit(0)
