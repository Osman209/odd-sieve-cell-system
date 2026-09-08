#!/usr/bin/env python3
"""
verify_four_tests.py  --  generator for Paper 10, "Four Tests of the Cell System".

Covers Proposition 1 with its saturation table, the counting-bound table of
Sec. 2.4, the squares-versus-cubes exponent table, the pair-count table of
Sec. 2.5, Theorems 1 and 2 with the a = p+4t+2 identity, and Theorems 3, 4
and 7 with the collision table of Sec. 2.14.

UNRESOLVED: the no-repeat claim of Theorem 7.  Under the definition of Sec. 2.11
(all pairs u < v in S_p with u^2 = v^2 mod N), restricted to the belt, Delta does
repeat.  The published run counts 267,575 collisions on 1,121 lines below 2x10^4,
far fewer than this definition gives, so the counted set is narrower.  The script
reports the numbers instead of asserting the claim.

NOT regenerated here: the three tables that need a sieve to X = 10^10 (the
NN window/cycle row of Layer 2, the Layer-3 residual, and the Richert-weight
table).  Those rest on the original runs, not on this script.  The Sigma_B
model of Sec. 2.6 is the object of code/verify_singular_series_order.py.

Modes:  --fast (seconds)   default (minutes)   --full (the published ranges)
"""

COVERS = ["[P10, S2.3]", "[P10, S2.4]", "[P10, S2.5]", "[P10, S2.8]", "[P10, S2.11]", "[P10, S2.12]", "[P10, S2.14]"]

import sys, math
from sympy import isprime, primerange, factorint
import numpy as np

FAST = "--fast" in sys.argv
FULL = "--full" in sys.argv
def rng(f, d, u=None):
    return f if FAST else ((u if u is not None else d) if FULL else d)
def fact(n):
    # sympy may be backed by python-flint, whose fmpz keys do not compare
    # with floats; force plain ints so `P0 < p` works on every install.
    return {int(k): int(v) for k, v in factorint(n).items()}

fails = 0
def check(name, ok, detail=""):
    global fails
    print(("  PASS  " if ok else "  FAIL  ") + name + ("   " + detail if detail else ""))
    if not ok: fails += 1
print("verify_four_tests.py  (Paper 10)   mode:",
      "fast" if FAST else ("full" if FULL else "default"))

# ---------------------------------------------- Prop 1: saturation of the runs
print("\n1. Proposition 1: saturation of the extremal runs")
def extremal_run(ps):
    P = math.prod(ps)
    cov = np.zeros(P, dtype=bool)
    for p in ps: cov[::p] = True
    d = np.concatenate((cov, cov))
    best = (0, None); run = 0
    for i, c in enumerate(d):
        run = run + 1 if c else 0
        if run > best[0]: best = (run, i - run + 1)
    return best
exp = {(2,3): (3, [2,1], [2,1]), (2,3,5): (5, [3,2,1], [3,2,1]),
       (2,3,5,7): (9, [5,3,2,1], [5,3,2,2]),
       (2,3,5,7,11): (13, [7,5,3,2,1], [7,5,3,2,2]),
       (2,3,5,7,11,13): (21, [11,7,5,3,2,1], [11,7,5,3,2,2])}
ok = True; det = []
for ps, (L, meas, ceilv) in exp.items():
    Lm, start = extremal_run(list(ps))
    cover = [sum(1 for i in range(start, start+Lm) if i % p == 0) for p in ps]
    ceils = [-(-Lm // p) for p in ps]
    ok = ok and Lm == L and cover == meas and ceils == ceilv
    det.append("%s:L=%d" % (list(ps), Lm))
check("the five rows of the saturation table", ok, "; ".join(det))

print("\n2. Sec. 2.4: why the counting condition yields no bound")
def jm1(k):
    return extremal_run(list(primerange(2, list(primerange(2, 100))[k-1] + 1)))[0]
# k = 10 is NOT recomputed: P_10 = 6,469,693,230, out of reach by direct search.
# The value j(P_10) - 1 = 45 in the paper is the tabulated one [16], not a
# measurement of this script.
tru = {3: 5, 5: 13}
got = {k: jm1(k) for k in tru}
ok = got[3] == 5 and got[5] == 13
check("true j(P_k) - 1 = 5 and 13 at k = 3, 5 (k = 10 is cited, not recomputed)",
      ok, "%s" % got)
L0 = 20000
ok = all(sum(-(-L0 // p) for p in list(primerange(2, 100))[:k]) >= L0 for k in (3, 5, 10))
check("the counting condition still holds at L = 2x10^4 for k = 3, 5, 10", ok)

print("\n3. Sec. 2.5: the squares-versus-cubes exponent table")
tab = {(0.5, 0.25): 2.000, (0.5, 1/3): 1.500, (0.5, 0.5): 1.000,
       (2/3, 0.25): 2.667, (2/3, 1/3): 2.000, (2/3, 0.5): 1.333}
check("every entry is alpha/theta", all(abs(a/t - v) < 5e-4 for (a, t), v in tab.items()))
check("the exponent gap at Omega <= 2 is 1/6, i.e. 33%",
      abs((2/3)/0.5 - 0.5/0.5 - 1/3) < 1e-12)

print("\n4. Sec. 2.5: the pair-count table")
def pair_counts(m, ks=(2, 3, 8)):
    # the window's objects are the ODD integers: 2m+2 of them, which is why the
    # Omega <= 8 column is close to 2m.
    lo, hi = m*m, (m+2)**2
    om = {n: sum(fact(n).values()) for n in range(lo+2, hi, 2)}
    out = {}
    for k in ks:
        out[k] = sum(1 for n in range(lo+2, hi-2, 2)
                     if om[n] <= k and om.get(n+2, 99) <= k)
    return out
exp = {101: (408, 66, 138, 202, 4.7), 1001: (4008, 375, 1114, 1998, 21.0)}
if not FAST: exp.update({5001: (20008, 1388, 4703, 9982, 68.9),
                         10001: (40008, 2513, 8767, 19954, 117.9)})
if FULL:     exp[20001] = (80008, 4454, 16512, 39880, 203.9)
ok = True; got = {}
for m, (wl, c2, c3, c8, mm) in exp.items():
    pc = pair_counts(m); got[m] = (4*m+4, pc[2], pc[3], pc[8])
    ok = ok and got[m] == (wl, c2, c3, c8) and abs(m/math.log(m)**2 - mm) < 0.1
check("the pair-count table (window length, Omega <= 2, 3, 8)", ok,
      "m = 101 -> %s" % (got[101],))

print("\n5. Theorems 1 and 2: a shared cofactor forces q = p + 2")
K = rng(200, 600, 1000)
tot = comp = badq = 0
for k in range(3, K, 2):
    lo, hi = k*k, (k+2)**2
    ps = [p for p in primerange(3, hi) if p*p < hi]
    for i, p in enumerate(ps):
        for q in ps[i+1:]:
            a0 = lo//p + 1
            for a in range(max(a0, q) | 1, hi//q + 1, 2):
                if lo < p*a and q*a < hi:
                    tot += 1
                    if not isprime(a): comp += 1
                    if q - p != 2: badq += 1
check("no sharing pair with a >= q has q - p != 2", badq == 0,
      "%d pairs, %d with composite cofactor (odd k < %d)" % (tot, comp, K))
n = 0; bad = 0
for p in primerange(3, rng(300, 1200, 2000)):
    t = 1
    while 2*t*t < p:
        k = p + 2*t; a = p + 4*t + 2
        n += 1
        if not (k*k < p*a and (p+2)*a < (k+2)**2): bad += 1
        t += 1
check("the identity a = p+4t+2 puts both strikes in W_k whenever 2t^2 < p",
      bad == 0, "%d instances" % n)
check("the witness a = p+6 works for every twin",
      all((p+2)**2 < p*(p+6) and (p+2)*(p+6) < (p+4)**2
          for p in primerange(3, 5000) if isprime(p+2)))

print("\n6. Theorems 3, 4 and 7: collisions inside the sharing set")
def S_and_collisions(p, vmax=None):
    """u^2 = v^2 (mod N) is an equality of residues, so group by n^2 mod N
    instead of testing all pairs: O(|S|) rather than O(|S|^2)."""
    N = p + 2
    S = [n for n in range(1, (p-1)//2 + 1) if (2*n*n)//p == (2*n*n)//N]
    g = {}
    for n in S: g.setdefault((n*n) % N, []).append(n)
    col = []
    for cls in g.values():
        if len(cls) < 2: continue
        for i, u in enumerate(cls):
            for v in cls[i+1:]:
                if vmax is None or v <= vmax: col.append((u, v))
    return S, col
bad = []
for p in range(9, rng(401, 3001), 2):
    _, col = S_and_collisions(p)
    if (len(col) == 0) != isprime(p+2): bad.append(p)
check("Theorem 3: E_p = 0 if and only if p+2 is prime", not bad,
      "odd p from 9 to %d, exceptions %s" % (rng(401, 3001)-2, bad))
exc = []
for p in range(9, rng(401, 3001), 2):
    if isprime(p+2): continue
    N = p + 2
    _, col = S_and_collisions(p)
    if not any(math.isqrt(N) < v <= (p+11)//6 for _, v in col): exc.append(p)
check("Theorem 4: the eight exceptions are 23,31,47,49,67,85,119,121",
      exc == [23,31,47,49,67,85,119,121] if not FAST else
      exc == [e for e in [23,31,47,49,67,85,119,121] if e < rng(401,3001)],
      "%s" % exc)
# The set Theorem 7's verification line counts, pinned exactly:
#   lines  -- primes p = 5 (mod 6), which is 3 not dividing N, and p > 121,
#             the hypothesis of Theorem 4.  Below 2e4 there are exactly 1,121.
#   pairs  -- u < v in S_p with u^2 = v^2 (mod N) and v <= (N+9)/6 = H, the top
#             of the belt of Theorems 4 and 5.  On those lines there are exactly
#             267,575 of them, on 789 lines that carry at least one.
# Both numbers are reproduced below under --full.  Dropping either condition
# breaks the theorem: with all p the Delta values repeat (p = 61: the pairs
# (6,27) and (15,27) both give 9513), and with v < N/6 instead of v <= H the
# count falls to 267,342.
LINE_HI = rng(2000, 6000, 20000)
ndup = 0; ncol = 0; nlines = 0; badid = 0; nsq = 0; badmod = 0; nconsidered = 0
for p in primerange(122, LINE_HI):
    if p % 6 != 5: continue
    nconsidered += 1
    N = p + 2
    S, col = S_and_collisions(p, vmax=(N + 9)//6)
    if not col: continue
    nlines += 1
    seen = set()
    for u, v in col:
        ncol += 1
        X = N - 6*u; B = N - 6*v
        num = X*X - B*B
        if num % (24*N): badid += 1; continue     # t must be an integer
        t = num // (24*N)
        Delta = B*B + 48*t
        if X*X - Delta != 24*t*p: badid += 1
        if math.isqrt(Delta) ** 2 == Delta: nsq += 1
        if Delta % 24 != 1: badmod += 1
        if Delta in seen: ndup += 1
        seen.add(Delta)
check("Theorem 7: no value of Delta repeats inside a list", ndup == 0,
      "%d collisions on %d of the %d lines considered" % (ncol, nlines, nconsidered))
check("no Delta is a square", nsq == 0)
check("Delta = 1 (mod 24) at every collision", badmod == 0)
check("the identity X^2 - Delta = 24tp holds at every collision", badid == 0)
if FULL:
    check("the published counts are reproduced: 1,121 lines and 267,575 collisions",
          nconsidered == 1121 and ncol == 267575,
          "%d lines, %d collisions" % (nconsidered, ncol))

print("\n%d of the checks failed." % fails)
sys.exit(0 if fails == 0 else 1)
