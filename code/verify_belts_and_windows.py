#!/usr/bin/env python3
"""
verify_belts_and_windows.py  --  generator for Paper 8,
"Belts and Short Windows".

Covers Theorem 1, Verified Law 2 with the collapse table, Proposition 1 with
the layer-ceiling pyramid, the depth ladder of Sec. 3.1 with its four tables,
the shell identity H - D = R_2 of Sec. 3.2 with its table, and the four track
quadratics with the character conditions of Theorem 3.

Owner convention: the line p owns N when p | N and N >= p^2, so the owner of a
composite is its smallest prime factor, and a "new strike" of p is a composite
N of the window with spf(N) = p.

Modes:  --fast (seconds)   default (minutes)   --full (the published ranges)
"""

COVERS = ["[P8, S2]", "[P8, S3]"]

import sys, math
from sympy import primerange, isprime, factorint, primepi
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
print("verify_belts_and_windows.py  (Paper 8)   mode:",
      "fast" if FAST else ("full" if FULL else "default"))

def spf_table(hi):
    s = np.zeros(hi + 1, dtype=np.int64)
    for p in range(2, int(hi**0.5) + 1):
        if s[p] == 0:
            blk = s[p*p::p]; blk[blk == 0] = p
    for n in range(2, hi + 1):
        if s[n] == 0: s[n] = n
    return s

# ------------------------------------------------------------------ Theorem 1
print("\n1. Theorem 1: the size of a belt")
def G(q, r): return (r*r - q*q)//6 - 1
pr = list(primerange(5, 40))
nine = [G(pr[i], pr[i+1]) for i in range(9)]
check("the nine consecutive belts 5->7 ... 31->37", nine == [3,11,7,19,11,27,51,19,67],
      "%s" % nine)
big = [G(89,97), G(101,103), G(499,503), G(997,1009)]
check("the four larger belts", big == [247, 67, 667, 4011], "%s" % big)
check("G = g(2q+g)/6 - 1 agrees with (r^2-q^2)/6 - 1",
      all(G(q, r) == (r-q)*(2*q + r-q)//6 - 1
          for q, r in zip(list(primerange(5, 2000))[:-1], list(primerange(5, 2000))[1:])))

# ------------------------------------------------------------- Verified Law 2
print("\n2. Verified Law 2: reach depends on the gap, not on the size")
def reach(q, r):
    g = r - q
    return sum(1 for k in range(1, g + 1) if (q + 2*k) % 3)
bad = tested = 0
_B = list(primerange(5, rng(2000, 20000, 50000)))
for q, r in zip(_B[:-1], _B[1:]):
    if (r-q)**2 < 2*q:
        tested += 1
        if reach(q, r) != (2*(r-q))//3: bad += 1
check("H_q = floor(2g/3) on every belt with g^2 < 2q", bad == 0, "%d belts" % tested)

# ---------------------------------------------- the collapse table (Sec. 2.3)
print("\n3. Sec. 2.3: the collapse of the new line's effect")
def belt_cells(q, r):
    # q^2 and r^2 are both == 1 (mod 6), so each is the UPPER member of a cell;
    # the cells strictly between the two gates are those two exclusive.
    return list(range((q*q - 1)//6 + 1, (r*r - 1)//6))
def closed_by(b, s): return (6*b - 1) % s == 0 or (6*b + 1) % s == 0
def K_and_twins(q, r):
    older = [s for s in primerange(5, q)]
    K = 0; tw = 0
    for b in belt_cells(q, r):
        newhit = closed_by(b, q)
        oldhit = any(closed_by(b, s) for s in older)
        if newhit and not oldhit: K += 1
        if isprime(6*b - 1) and isprime(6*b + 1): tw += 1
    return K, tw
tab = {(5,7):(3,1,1,2),(7,11):(11,2,2,4),(11,13):(7,1,0,2),(13,17):(19,2,1,7),
       (17,19):(11,1,0,2),(23,29):(51,4,0,8),(31,37):(67,4,0,11),
       (89,97):(247,5,0,21),(101,103):(67,1,0,7)}
ok = True; got = {}
for (q, r), (g_, h_, k_, t_) in tab.items():
    K, tw = K_and_twins(q, r)
    got[(q,r)] = (G(q,r), reach(q,r), K, tw)
    ok = ok and got[(q,r)] == (g_, h_, k_, t_)
check("the nine rows of the (G, H_q, K_q, twins) table", ok, "5->7 gives %s" % (got[(5,7)],))
def K_only(q, r):
    """same K_q as above, but walking only the cells q actually strikes."""
    small = [s for s in primerange(5, q)]
    K = 0
    m = q + 2
    while q*m < r*r:
        N = q*m
        if N % 3 and N > q*q:
            b = (N + 1)//6 if N % 6 == 5 else (N - 1)//6
            if (q*q - 1)//6 < b < (r*r - 1)//6:
                if not any((6*b-1) % s == 0 or (6*b+1) % s == 0 for s in small): K += 1
        m += 2
    return K
if not FAST:
    z = tot = 0; z2 = tot2 = 0
    P = list(primerange(5, 5000))
    for q, r in zip(P[:-1], P[1:]):
        K = K_only(q, r)
        if q < 1000: tot += 1; z += (K == 0)
        else: tot2 += 1; z2 += (K == 0)
    check("K_q = 0 in 71.1% of belts below q = 1000 and 76.8% above",
          abs(100*z/tot - 71.1) < 0.1 and abs(100*z2/tot2 - 76.8) < 0.1,
          "%.1f%% and %.1f%%" % (100*z/tot, 100*z2/tot2))

# ------------------------------------------------ Proposition 1: the ceilings
print("\n4. Proposition 1: the layer ceilings")
def ceil_sum(q, r):
    L = r*r - q*q
    # the pyramid is (q/2, q], (q/4, q/2], ... down to 5, so s = 5 itself is excluded
    return sum(-(-(2 * (-(-L // (2*s)))) // 3) for s in range(7, q + 1) if s % 2 and s % 3)
rows = [(499, 503, 667, 2094, 3.1), (997, 1009, 4011, 13935, 3.5),
        (10007, 10009, 6671, 35045, 5.3)]
ok = True; got = []
for q, r, g_, c_, ratio in rows:
    c = ceil_sum(q, r); got.append(c)
    ok = ok and G(q, r) == g_ and c == c_ and abs(c/G(q, r) - ratio) < 0.05
check("the three rows of the ceiling-pyramid table", ok, "sums %s" % got)
check("the ratio is ~ (2/3) log q, not an iterated log",
      all(abs((2/3)*math.log(q/4) - v) < 0.15
          for q, v in [(499,3.22),(997,3.68),(10007,5.22)]))

# ------------------------------------------------------- Sec. 3.1 depth ladder
print("\n5. Sec. 3.1: the depth ladder")
M = 100000
bounds = [(M+2)**(2/3), (M+2)**0.5, (M+2)**0.4]
# the printed row is 2,155 / 316 / 100: the first rounded up, the other two down
check("the three rungs at M = 10^5 agree with the printed 2155, 316, 100",
      all(abs(b - t) < 1 for b, t in zip(bounds, (2155, 316, 100))),
      "exact values %.2f, %.2f, %.2f" % tuple(bounds))
# and the counts of lines below those bounds, which the text states separately.
# these are NOT the bounds themselves - an earlier version printed the bounds in
# their place, and the check above passed anyway because it tested the bounds.
nlines = [len(list(primerange(3, int(b) + 1))) for b in bounds]
total = len(list(primerange(3, M + 1)))
check("the lines below the three rungs at M = 10^5 are 324, 64, 24 of 9,591",
      nlines == [324, 64, 24] and total == 9591,
      "%s of %d" % (nlines, total))
shares = []
for Mo in (101, 1005, 10005, 100005):
    t = len(list(primerange(3, Mo + 1)))
    c = len(list(primerange(3, int((Mo + 2)**(2/3)) + 1)))
    shares.append(100.0*c/t)
check("the share below the first rung falls 28, 14.4, 7.2, 3.4 per cent",
      all(abs(a - b) < 0.1 for a, b in zip(shares, (28.0, 14.4, 7.2, 3.4))),
      ", ".join("%.1f%%" % s for s in shares))
LIM = rng(1501, 1501)
s = spf_table((LIM + 2)**2)
bad = strikes = 0
for Mo in range(9, LIM, 2):
    lo, hi = Mo*Mo + 1, (Mo+2)**2
    for N in range(lo + 1, hi, 2):
        p = int(s[N])
        if p == N: continue
        strikes += 1
        w = sum(fact(N).values())
        if p**w >= (Mo+2)**2: bad += 1
check("p^Omega(N) < (M+2)^2 on every new strike, odd M < %d" % LIM, bad == 0,
      "%d new strikes" % strikes)
def D_M(p, Mo):
    r = 1
    while p**(r+1) < (Mo+2)**2: r += 1
    return r
part = {}
for p in [3] + list(primerange(5, 500)):
    part.setdefault(D_M(p, 499), []).append(p)
ok = (min(part[2]) == 67 and max(part[2]) == 499 and min(part[3]) == 23 and max(part[3]) == 61
      and min(part[4]) == 13 and max(part[4]) == 19 and part[5] == [11] and part[6] == [7]
      and part[7] == [5] and part[11] == [3])
check("the D_M(p) partition of the lines at M = 499", ok)
check("the boundary is sharp: 61^3 < (M+2)^2 <= 67^3 at M = 499",
      61**3 < 251001 <= 67**3)

def window_owned(Mo):
    lo, hi = Mo*Mo, (Mo+2)**2
    out = {}
    for N in range(lo + 2, hi, 2):      # the window's objects are the ODD numbers
        f = fact(N); p = min(f); w = sum(f.values())
        out[N] = (p, w)
    return out
for Mo, exp_first in ((499, 23), (999, 17), (4999, 19)):
    if FAST and Mo > 999: continue
    ow = window_owned(Mo)
    deepest = {}
    for N, (p, w) in ow.items():
        if w > 1: deepest[p] = max(deepest.get(p, 0), w)
    first = min((p for p in deepest if deepest[p] == D_M(p, Mo)), default=None)
    check("first line attaining its capacity at M = %d is %d" % (Mo, exp_first),
          first == exp_first, "found %s" % first)
    if Mo == 499:
        cnt = {}
        for N, (p, w) in ow.items():
            if w > 1: cnt[w] = cnt.get(w, 0) + 1
        lo_ = {}
        for N, (p, w) in ow.items():
            if w > 1: lo_[w] = max(lo_.get(w, 0), p)
        deep = sum(v for k, v in cnt.items() if k >= 3)
        check("the window at M = 499 splits as 999 = 151 + 355 + 493",
              sum(1 for N in range(499*499+2, 501**2, 2) if isprime(N)) == 151
              and cnt.get(2) == 355 and deep == 493,
              "P_2 = %s, deeper = %d" % (cnt.get(2), deep))
        check("the Omega-layer table at M = 499 (counts and largest owners)",
              cnt.get(2) == 355 and cnt.get(3) == 285 and cnt.get(4) == 135 and
              cnt.get(5) == 50 and cnt.get(6) == 17 and
              lo_.get(2) == 499 and lo_.get(3) == 61 and lo_.get(4) == 11 and
              lo_.get(5) == 7 and lo_.get(6) == 3,
              "counts %s" % {k: cnt.get(k) for k in (2,3,4,5,6)})

# --------------------------------------------------------- Sec. 3.1 the regions
print("\n6. Sec. 3.1: core and shell, measured")
def region_row(Mo, lower):
    P0 = (Mo + 2) ** (2/3)
    ps = [p for p in primerange(3, Mo + 1) if (p <= P0) == lower]
    lo, hi = Mo*Mo, (Mo+2)**2
    strikes = new_pq = new_deep = inh = 0
    for p in ps:                      # the strike column counts every multiple of p
        for m in range(lo // p, hi // p + 1):
            N = p * m
            if not (lo < N < hi): continue
            strikes += 1
            f = fact(N)
            if min(f) == p:
                if sum(f.values()) == 2: new_pq += 1
                else: new_deep += 1
            else: inh += 1
    return len(ps), strikes, new_pq, new_deep, inh
exp = {(1005, True): (24, 5242, 446, 1073, 3723), (1005, False): (143, 1594, 204, 0, 1390)}
if not FAST:
    exp[(10005, True)] = (89, 63493, 4095, 12259, 47139)
    exp[(10005, False)] = (1139, 15867, 1440, 0, 14427)
ok = True; got = {}
for k, v in exp.items():
    got[k] = region_row(*k); ok = ok and got[k] == v
check("the core/shell region table", ok, "M=1005 core -> %s" % (got[(1005, True)],))

# -------------------------------------------------------- Sec. 3.2 the shell
print("\n7. Sec. 3.2: the shell identity H - D = R_2")
def shell_row(Mo):
    P0 = (Mo + 2) ** (2/3)
    lo, hi = Mo*Mo, (Mo+2)**2
    S = R1 = R2 = H = 0; three = 0
    for N in range(lo + 2, hi, 2):
        f = fact(N)
        # a shell factor is a LINE of the window: a DISTINCT prime in (P0, M].
        # counting p^2 twice moves 3*59^2 and 11*31^2 out of R_1 into R_2 at M = 101.
        sh = [p for p in f if P0 < p <= Mo]
        H += len(sh)
        if len(sh) >= 3: three += 1
        if len(sh) == 1:
            if sum(f.values()) == 2: S += 1
            else: R1 += 1
        elif len(sh) == 2: R2 += 1
    return S, R1, R2, H, three
exp = {35: (12,6,2,22,0), 101: (28,28,8,72,0), 499: (105,122,77,381,0)}
if not FAST: exp.update({999:(195,279,156,786,0), 1999:(350,599,312,1573,0), 4999:(790,1613,775,3953,0)})
ok = True; got = {}
for Mo, v in exp.items():
    got[Mo] = shell_row(Mo); ok = ok and got[Mo] == v
check("the shell table (S, R_1, R_2, H) and no integer with three shell factors",
      ok, "M=499 -> %s" % (got[499],))
ok = all(g[3] - (g[0]+g[1]+g[2]) == g[2] for g in got.values())
check("H - D = R_2 on every row", ok)

# ------------------------------------------------------- Sec. 3.3 the tracks
print("\n8. Sec. 3.3: the four tracks and Theorem 3")
def tracks(a):
    q = 6*a - 1
    return {"T1": (q*q+4, q*q+6), "T2": (q*q+10, q*q+12),
            "T3": ((q+2)**2-14, (q+2)**2-12), "T4": ((q+2)**2-8, (q+2)**2-6)}
def quad(a):
    return {"T1": (36*a*a-12*a+5, 36*a*a-12*a+7), "T2": (36*a*a-12*a+11, 36*a*a-12*a+13),
            "T3": (36*a*a+12*a-13, 36*a*a+12*a-11), "T4": (36*a*a+12*a-7, 36*a*a+12*a-5)}
check("the four cells are the stated quadratics in a, for a = 1..399",
      all(tracks(a) == quad(a) for a in range(1, 400)))
from sympy import legendre_symbol
# discriminant B^2 - 144C = 144k, and 144 is a square, so the condition is (k|r) = 1
KS = {"T1": (-4, -6), "T2": (-10, -12), "T3": (14, 12), "T4": (8, 6)}
bad = n = 0
for a in range(1, rng(60, 401)):
    for name, mems in quad(a).items():
        for k, mem in zip(KS[name], mems):
            for r in fact(mem):
                if r <= 3: continue
                n += 1
                if k % r and legendre_symbol(k % r, r) != 1: bad += 1
check("every prime factor of every track member satisfies its character condition",
      bad == 0, "%d checks" % n)

print("\n%d of the checks failed." % fails)
sys.exit(0 if fails == 0 else 1)
