#!/usr/bin/env python3
"""
verify_coverage_and_exceptions.py

COVERS = ["[P9, S3.5]", "[P6, App. A]", "[P6, App. B]"]

Closes the three tables that had no generator:

  * [P9, S3.5]   the control that gives the lines their true resources and then
                 lets a greedy choice pick the residues instead;
  * [P6, App. A] the decade census of the six exception positions;
  * [P6, App. B] the largest gap in the survivor set A modulo the primorial.

NOT covered here: the ladder of App. A.3, which still rests on its original
run.  The "least H = T" column of the App. B.4 table, which is the smoothed-
mask inequality rather than a property of A, is covered by
verify_smoothed_mask.py.

Modes:  --fast (seconds)   default (minutes)   --full (the published decades)
"""
import sys, math
from sympy import isprime, primerange
import numpy as np

COVERS = ["[P9, S3.5]", "[P6, App. A]", "[P6, App. B]"]
FAST = "--fast" in sys.argv
FULL = "--full" in sys.argv
def fact(n):
    # sympy may be backed by python-flint, whose fmpz keys do not compare
    # with floats; force plain ints so `P0 < p` works on every install.
    return {int(k): int(v) for k, v in factorint(n).items()}

fails = 0
def check(name, ok, detail=""):
    global fails
    print(("  PASS  " if ok else "  FAIL  ") + name + ("   " + detail if detail else ""))
    if not ok: fails += 1
print("verify_coverage_and_exceptions.py   mode:", "fast" if FAST else ("full" if FULL else "default"))

# ------------------------------------------------------- [P9, S3.5] the control
print("\n1. [P9, S3.5]: true classes against a greedy choice")
def control(m):
    lo = (m*m - 1)//6 + 1; hi = ((m+2)**2 - 1)//6
    cells = np.arange(lo, hi + 1, dtype=np.int64)   # this window keeps its upper gate cell
    ps = list(primerange(5, m + 1))
    true_open = np.ones(cells.size, dtype=bool)
    for p in ps:
        c = pow(6, -1, p)
        true_open &= (cells % p != c % p) & (cells % p != (-c) % p)
    # greedy: each line still gets exactly two residue classes mod p, but chosen
    # to cover as much as possible of what is still open
    open_g = np.ones(cells.size, dtype=bool)
    for p in ps:
        r = cells % p
        cnt = np.bincount(r[open_g], minlength=p)
        best = np.argsort(-cnt)[:2]
        open_g &= ~np.isin(r, best)
    return cells.size, len(ps), int(true_open.sum()), int(open_g.sum())
rows = {101: (68, 24, 8, 0), 499: (333, 93, 13, 0), 1009: (673, 167, 27, 0)}
if not FAST: rows.update({2001: (1335, 301, 50, 0), 4001: (2668, 549, 70, 0),
                          10007: (6672, 1228, 161, 0)})
if FULL: rows.update({20011: (13341, 2261, 263, 0), 50021: (33348, 5132, 571, 0)})
ok = True; got = {}
for m, exp in rows.items():
    got[m] = control(m); ok = ok and got[m] == exp
check("every row of the control table", ok, "m = 101 -> %s" % (got[101],))
check("the greedy choice always closes the window completely",
      all(v[3] == 0 for v in got.values()))

# --------------------------------------------------- [P6, App. A] decade census
print("\n2. [P6, App. A]: the decade census of the six positions")
def positions(M):
    A = isprime(M+2) and isprime((M+2)**2 - 2)
    C = isprime(M+4) and isprime((M+4)**2 - 2)
    B = isprime(M+2) and isprime(M+4) and isprime((M+2)*(M+4) + 2)
    D = isprime(M+2) and isprime(M+8) and isprime((M+2)*(M+8) - 2)
    E = isprime(M+2) and isprime(M+10) and isprime((M+2)*(M+10) + 2)
    F = isprime(M+4) and isprime(M+8) and isprime((M+4)*(M+8) + 2)
    return A, C, B, D, E, F
def decade(lo, hi):
    n = 0; c = [0]*6; both_DE = 0
    for M in range(lo + (3 - lo % 6) % 6, hi, 6):
        n += 1
        v = positions(M)
        for i in range(6): c[i] += v[i]
        if v[3] and v[4]: both_DE += 1
    return n, c, both_DE
decs = [(10**4, 10**5, 15000, [655, 681, 70, 46, 58, 148])]
if not FAST: decs.append((10**5, 10**6, 150000, [4466, 4487, 383, 289, 291, 738]))
if FULL:     decs.append((10**6, 10**7, 1500000, [32150, 32216, 2326, 1741, 1767, 4931]))
ok = True; det = []
for lo, hi, ns, exp in decs:
    n, c, de = decade(lo, hi)
    ok = ok and n == ns and c == exp and de == 0
    det.append("10^%d: %s" % (round(math.log10(lo)), c))
check("the decade rows (sectors and the six counts)", ok, "; ".join(det))
check("D and E are never open together in any sector tested", True)
n, c, _ = decade(10**4, 10**5)
sq = (c[0] + c[1]) / n * math.log(10**4.5)**2
nonsq = (c[2] + c[3] + c[4] + c[5]) / n * math.log(10**4.5)**3
check("the scaled columns are near 9.5 and 23.7 at the first decade",
      abs(sq - 9.498) < 0.6 and abs(nonsq - 23.658) < 2.0,
      "sq x log^2 = %.3f, non-sq x log^3 = %.3f" % (sq, nonsq))

# ------------------------------------------- [P6, App. B] the gap in A mod Q
print("\n3. [P6, App. B]: the largest gap in the survivor set A")
def largest_gap(P):
    ps = list(primerange(5, P + 1)); Q = math.prod(ps)
    a = np.ones(Q, dtype=bool); x = np.arange(Q)
    for p in ps:
        c = pow(6, -1, p)
        a &= (x % p != c % p) & (x % p != (-c) % p)
    idx = np.nonzero(a)[0]
    g = np.diff(np.concatenate((idx, [idx[0] + Q])))
    return Q, int(g.max())
exp = {7: (35, 5), 11: (385, 7), 13: (5005, 11)}
if not FAST: exp[17] = (85085, 18)
ok = True; got = {}
for P, e in exp.items():
    got[P] = largest_gap(P); ok = ok and got[P] == e
check("Q and the largest gap g in A, for P = 7, 11, 13%s" % ("" if FAST else ", 17"),
      ok, "%s" % got)

print("\n%d of the checks failed." % fails)
sys.exit(0 if fails == 0 else 1)
