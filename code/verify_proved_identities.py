#!/usr/bin/env python3
"""
verify_proved_identities.py  --  checks for statements that were measured in
earlier releases and are now proved in the papers.

  [P4, S4.2]  Identity B: over any cycle of M_S consecutive sectors,
              sum eta_S = 2^|S| - prod_{r in S} (2 + (2/r)).  Checked for single
              lines and for sets of lines, from several starts, on the family
              u = 6n-1, the family u = 6n+1, and their union.
  [P4, S4.1]  Identity A: the mean of eps_r over a full period of
              M = prod_{5<=q<=r} q consecutive sectors of the family of S3
              (u = 5 mod 6, v = u+2, all lines <= u acting) is exactly
              -(chi_r/r) Q_{r-}.  Exact rational arithmetic.
  [P4, S4.3]  The two printed pairs (T-M, E_mean) at U = 1000 and 2000.  They
              are taken on windows between squares of CONSECUTIVE integers
              coprime to 6 (u = 5, 7, 11, 13, ...), the union of the two families.
  [P8, S2.2]  Theorem 2: the number of belt cells struck by the line q is
              #{s = +-1 (mod 6) : q < s < (r^2-2)/q}, and it equals floor(2g/3)
              when g^2 < 2q.  The count is taken independently, from the cell
              classes 6m = +-1 (mod q) inside the belt.
  [P8, S3.2]  Proposition 4: above T+ the handover difference
              q_min(p-2) - q_max(p) is 2(floor(X/(p-2)) + 1 - ceil(X/p)),
              X = 2(s+1)^2, and so only 0 or 2.  q_min and q_max are computed
              from their definitions.
  [P10, S2.11] Theorem 3, steps (ii)-(v): the identity 2v^2 = (k+2)N - Delta/2,
              failure iff 0 < Delta <= 4k+8, the bound on k, both branches of
              step (iv) (the k = 1 branch is the Pell family), and the rescue.
  [P10, S2.12] Theorem 4: for a = 3 the ordinary witness fails only at
              p = 31, 49, 67, 85, 103, 121.
  [P3, S4.1]  The multiplicity factor on the cycle modulo prod q^2: the
              census of cells by (multiplicity, rail) equals the product of
              (q^2-2q) + (q-1)x(u+v) + x^2(u+v) on the full cycle.
  [P3, S6.2]  Corollary 5: the exact variances 4/25 -> 1104/4225 and
              72/245 -> 13164/41405 at L = 6 under the entry of 13, from the
              cycle formula, which is also checked against a brute-force count.

Modes:  --fast (seconds)   default (about a minute)   --full (minutes; the
ranges quoted in the papers)
"""

COVERS = ["[P3, S4.1]", "[P3, S6.2]", "[P4, S4.1]", "[P4, S4.2]", "[P4, S4.3]", "[P8, S2.2]", "[P8, S3.2]",
          "[P10, S2.11]", "[P10, S2.12]"]

import sys, math
from fractions import Fraction
from itertools import combinations
import numpy as np
from sympy import primerange, legendre_symbol, isprime

FAST = "--fast" in sys.argv
FULL = "--full" in sys.argv
def rng(f, d, u=None):
    return f if FAST else ((u if u is not None else d) if FULL else d)

fails = 0
def check(name, ok, detail=""):
    global fails
    print(("  PASS  " if ok else "  FAIL  ") + name + ("   " + detail if detail else ""))
    if not ok: fails += 1
print("verify_proved_identities.py  (Papers 3, 4, 8, 10)   mode:",
      "fast" if FAST else ("full" if FULL else "default"))

def chi(r): return legendre_symbol(2, r)

# ------------------------------------------------------------- Identity B
print("\n1. [P4, S4.2] Identity B")
def roots_of_one(M):
    return [x for x in range(M) if (x * x - 1) % M == 0]
def cells(u, v):
    return (u * u + 5) // 6, (v * v - 7) // 6          # 6L = u^2+5, 6R = v^2-7
def struck_by_all(L, R, M, classes):
    # number of m in [L, R] with m = c (mod M) for some c in classes
    return sum((R - c) // M - (L - 1 - c) // M for c in classes)
def cycle_sum(S, family, n0):
    M = math.prod(S); inv6 = pow(6, -1, M)
    classes = [rho * inv6 % M for rho in roots_of_one(M)]
    tot = Fraction(0)
    for n in range(n0, n0 + M):
        pairs = []
        if family in ("minus", "union"): pairs.append((6 * n - 1, 6 * n + 1))
        if family in ("plus", "union"):  pairs.append((6 * n + 1, 6 * n + 5))
        for u, v in pairs:
            L, R = cells(u, v)
            tot += struck_by_all(L, R, M, classes) - Fraction(2 ** len(S) * (R - L + 1), M)
    return tot
def predicted(S):
    return 2 ** len(S) - math.prod(2 + chi(r) for r in S)

bad = 0; n = 0
for r in primerange(5, rng(32, 60, 110)):
    for fam in ("minus", "plus", "union"):
        for n0 in (1, 2, 7, r, 3 * r + 1, 50):
            got = cycle_sum((r,), fam, n0)
            want = predicted((r,)) * (2 if fam == "union" else 1)
            n += 1; bad += (got != want)
check("single line: the cycle sum is -(2/r)", bad == 0, "%d cycles, %d mismatches" % (n, bad))
published = {(5, 7): 1, (5, 11): 3, (7, 17): -5, (7, 11): 1, (11, 13): 3, (5, 13): 3, (5, 7, 11): 5}
ok = all(cycle_sum(S, "minus", 1) == v == predicted(S) for S, v in published.items())
check("the seven published multi-line values", ok)
bad = 0; n = 0
for k in (2, 3):
    for S in combinations(list(primerange(5, rng(14, 20, 24))), k):
        if math.prod(S) > rng(1200, 6000, 20000): continue
        for n0 in (1, 11):
            n += 1; bad += (cycle_sum(S, "minus", n0) != predicted(S))
check("every set of two or three small lines", bad == 0, "%d cycles, %d mismatches" % (n, bad))

# ------------------------------------------------------------- Identity A
print("\n2. [P4, S4.1] Identity A (exact mean over a full period)")
def Q_minus(r):
    q = Fraction(1)
    for s in primerange(5, r): q *= 1 - Fraction(2 + chi(s), s)
    return q
def period_mean(r, n0):
    lines = list(primerange(5, r)); M = math.prod(primerange(5, r + 1))
    sD = 0; sN = 0
    for n in range(n0, n0 + M):
        u, v = 6 * n - 1, 6 * n + 1
        L, R = cells(u, v)
        x = 6 * np.arange(L, R + 1, dtype=np.int64)
        open_ = np.ones(x.size, dtype=bool)
        for q in lines:
            m = x % q; open_ &= (m != 1) & (m != q - 1)
        m = x % r; hit = (m == 1) | (m == r - 1)
        sN += int(open_.sum()); sD += int((open_ & hit).sum())
    return (Fraction(sD) - Fraction(2 * sN, r)) / M
for r in [5, 7, 11] + ([13] if FULL else []):
    for n0 in ((r + 1) // 6 + 1, 17):
        got = period_mean(r, n0); want = -Fraction(chi(r), r) * Q_minus(r)
        check("r = %d, start n = %d: mean = %s" % (r, n0, want), got == want, "measured %s" % got)

# -------------------------------------------- the two pairs printed in S4.3
print("\n3. [P4, S4.3] T - M and the mean part, on consecutive coprime-to-6 roots")
UMAX = 2000 if FULL else 1000
lim = (UMAX + 10) ** 2 + 10
sv = np.ones(lim, dtype=bool); sv[:2] = False
for i in range(2, int(lim ** 0.5) + 1):
    if sv[i]: sv[i * i::i] = False
plist = [int(x) for x in primerange(5, UMAX + 10)]
def P_(z):
    v = 1.0
    for r in plist:
        if r > z: break
        v *= 1 - 2 / r
    return v
def Qz(z):
    v = 1.0
    for r in plist:
        if r > z: break
        v *= 1 - (2 + chi(r)) / r
    return v
us = [u for u in range(5, UMAX + 10) if u % 6 in (1, 5)]
for U, wantTM, wantE in ((1000, -2057.1, -6.93), (2000, -6479.5, -11.24)):
    if U > UMAX: continue
    T = 0; M = 0.0; E = 0.0
    for u, v in zip(us, us[1:]):
        if u > U: break
        L, R = cells(u, v)
        m = np.arange(L, R + 1)
        P = P_(u); M += (R - L + 1) * P; E += P - Qz(u)
        T += int((sv[6 * m - 1] & sv[6 * m + 1]).sum())
    check("U = %d: T - M = %.1f and E_mean = %.2f" % (U, wantTM, wantE),
          abs(T - M - wantTM) < 0.06 and abs(E - wantE) < 0.006, "%.2f, %.3f" % (T - M, E))

# ------------------------------------------------------------- [P8] belts
print("\n4. [P8, S2.2] Theorem 2: the reach of the line born at a gate")
QMAX = rng(2000, 20000, 200000)
ps = [int(x) for x in primerange(5, QMAX + 200)]
nb = 0; bad_exact = 0; bad_floor = 0; nhyp = 0; bad_bound = 0
for q, r in zip(ps, ps[1:]):
    if q >= QMAX: break
    g = r - q; nb += 1
    L, R = (q * q + 5) // 6, (r * r - 7) // 6
    direct = struck_by_all(L, R, q, [pow(6, -1, q), (-pow(6, -1, q)) % q])
    formula = sum(1 for s in range(q + 1, (r * r - 2 + q - 1) // q + 1)
                  if s % 6 in (1, 5) and q * s < r * r - 2)
    bad_exact += (direct != formula)
    if g * g < 2 * q:
        nhyp += 1; bad_floor += (direct != 2 * g // 3)
    if not (2 * g // 3 <= direct <= 2 * g // 3 + (g * g - 2) / (3 * q) + 1): bad_bound += 1
check("exact formula equals the direct count", bad_exact == 0, "%d belts, q < %d" % (nb, QMAX))
check("floor(2g/3) whenever g^2 < 2q", bad_floor == 0, "%d belts satisfy the hypothesis" % nhyp)
check("floor(2g/3) <= H_q <= floor(2g/3) + (g^2-2)/(3q) + 1 in every belt", bad_bound == 0)

print("\n5. [P8, S3.2] Proposition 4: the handover above T+ is 0 or 2")
MMAX = rng(301, 1001, 3001)
npair = 0; bad_val = 0; bad_form = 0
for Mw in range(5, MMAX, 2):
    lo, hi = Mw * Mw, (Mw + 2) ** 2
    for p in range(5, Mw + 1, 2):
        if 2 * p * (Mw + 1) <= hi: continue                 # p <= T+
        qmax = (hi - 1) // p
        if qmax % 2 == 0: qmax -= 1
        qmin = lo // (p - 2) + 1
        if qmin % 2 == 0: qmin += 1
        d = qmin - qmax; s = (Mw - p) // 2; X = 2 * (s + 1) ** 2
        npair += 1
        bad_val += d not in (0, 2)
        bad_form += d != 2 * (X // (p - 2) + 1 - (-(-X // p)))
check("q_min(p-2) - q_max(p) is 0 or 2", bad_val == 0, "%d adjacent odd pairs, odd M < %d" % (npair, MMAX))
check("and equals 2(floor(X/(p-2)) + 1 - ceil(X/p))", bad_form == 0)

# --------------------------------------------------------- [P10] Theorem 3
print("\n6. [P10, S2.11-2.12] Theorems 3 and 4: the witness inside S_p")
LIM = rng(20000, 200000, 3000000)
spf = np.arange(LIM + 3, dtype=np.int64)
for i in range(2, int((LIM + 2) ** 0.5) + 1):
    if spf[i] == i:
        blk = spf[i * i::i]; blk[blk == np.arange(i * i, LIM + 3, i)[:blk.size]] = i
spf = spf.tolist()
def divisors(n):
    ds = [1]
    while n > 1:
        q = spf[n]; e = 0
        while n % q == 0: n //= q; e += 1
        ds = [d * q ** k for d in ds for k in range(e + 1)]
    return ds
def inS(s, p, N): return (2 * s * s) // p == (2 * s * s) // N
nf = 0; nfail = 0; ps_fail = set(); nprime = 0; nk1 = 0
bad = {"identity": 0, "criterion": 0, "b>3a": 0, "k-bound": 0, "k>=2 bounds": 0,
       "k=1 Pell": 0, "rescue": 0, "square": 0}
a3 = []
for p in range(9, LIM + 1, 2):
    N = p + 2
    if spf[N] == N: continue
    r_ = math.isqrt(N)
    if r_ * r_ == N and spf[r_] == r_:
        if not (inS(r_, p, N) and inS(2 * r_, p, N) and 2 * r_ <= (p - 1) // 2): bad["square"] += 1
    for a in divisors(N):
        if a < 3 or a * a >= N: continue
        b = N // a; nf += 1
        u, v = (b - a) // 2, (b + a) // 2
        k = b // (2 * a); c = 2 * a * (k + 1) - b; D = b * c - a * a
        if 2 * (2 * v * v) != 2 * (k + 2) * N - D: bad["identity"] += 1
        fail = not (inS(v, p, N) and inS(u, p, N))
        if fail != (0 < D <= 4 * k + 8): bad["criterion"] += 1
        if not fail: continue
        nfail += 1; ps_fail.add(p); nprime += isprime(p)
        if a == 3: a3.append(p)
        if not b > 3 * a: bad["b>3a"] += 1
        if k * (2 * a - 4) > a * a - 2 * a + 9: bad["k-bound"] += 1
        Rr = 4 * a * a - D // 2
        if k >= 2 and not (0 < Rr < N - 2 * (k + 5)): bad["k>=2 bounds"] += 1
        if k == 1:
            nk1 += 1
            if not ((b - 2 * a) ** 2 - 3 * a * a == -2 and 2 * (Rr - N) == (a - c) ** 2): bad["k=1 Pell"] += 1
        u3, v3 = (b - 3 * a) // 2, (b + 3 * a) // 2
        if not (u3 >= 1 and v3 <= (p - 1) // 2 and inS(v3, p, N) and inS(u3, p, N)): bad["rescue"] += 1
for key, val in bad.items():
    check("Theorem 3: %s" % key, val == 0, "%d violations" % val)
check("factorisations examined, odd p <= %d" % LIM, nf > 0,
      "%d factorisations, %d failing at %d values of p (%d at prime p), %d on the k = 1 branch"
      % (nf, nfail, len(ps_fail), nprime, nk1))
if FULL:
    check("the counts quoted in [P10, S2.11]: 112 / 111 / 32 / 5",
          (nfail, len(ps_fail), nprime, nk1) == (112, 111, 32, 5))
check("Theorem 4: for a = 3 the ordinary witness fails only at 31, 49, 67, 85, 103, 121",
      a3 == [31, 49, 67, 85, 103, 121], "%s" % a3)

# ------------------------------------------------- [P3, S4.1] multiplicity
print("\n7. [P3, S4.1] the multiplicity factor on the cycle modulo prod q^2")
from collections import Counter
def vq(n, q):
    a = 0
    while n % q == 0: n //= q; a += 1
    return a
for Qs in ([5, 7], [5, 7, 11]) if not FAST else ([5, 7],):
    Mq2 = math.prod(q * q for q in Qs); direct = Counter()
    for b in range(1, Mq2 + 1):
        lo, hi = 6 * b - 1, 6 * b + 1
        direct[(sum(min(vq(lo, q), 2) for q in Qs), sum(min(vq(hi, q), 2) for q in Qs),
                sum(1 for q in Qs if lo % q == 0), sum(1 for q in Qs if hi % q == 0))] += 1
    pred = Counter({(0, 0, 0, 0): 1})
    for q in Qs:
        opts = [((0, 0, 0, 0), q * q - 2 * q), ((1, 0, 1, 0), q - 1), ((0, 1, 0, 1), q - 1),
                ((2, 0, 1, 0), 1), ((0, 2, 0, 1), 1)]
        new = Counter()
        for k, w in pred.items():
            for d, c in opts: new[tuple(a + b for a, b in zip(k, d))] += w * c
        pred = new
    check("lines %s: direct census equals the product, every state" % Qs, direct == pred,
          "%d states" % len(direct))

# ------------------------------------------------------- [P3] Corollary 5
print("\n8. [P3, S6.2] Corollary 5: the variance is not carried by a fixed factor")
def Kq(q, h): return q - 2 if h % q == 0 else (q - 3 if h % q in (1, q - 1) else q - 4)
def var(Q, L):
    M = math.prod(Q); T = math.prod(q - 2 for q in Q)
    C = lambda h: math.prod(Kq(q, h) for q in Q)
    return Fraction(L * T + 2 * sum((L - h) * C(h) for h in range(1, L)), M) - Fraction(L * T, M) ** 2
Q = [3, 5, 7]; Mq = math.prod(Q)
A = [1 if all((2 * x + 1) % q and (2 * x + 3) % q for q in Q) else 0 for x in range(Mq)]
Ns = [sum(A[(s + j) % Mq] for j in range(6)) for s in range(Mq)]
brute = Fraction(sum(n * n for n in Ns), Mq) - Fraction(sum(Ns), Mq) ** 2
check("the variance formula equals a brute-force count ({3,5,7}, L = 6)", brute == var(Q, 6))
vals = (var([3, 5], 6), var([3, 5, 13], 6), var([3, 5, 7], 6), var([3, 5, 7, 13], 6))
check("4/25 -> 1104/4225 and 72/245 -> 13164/41405",
      vals == (Fraction(4, 25), Fraction(1104, 4225), Fraction(72, 245), Fraction(13164, 41405)),
      "ratios %.3f and %.3f" % (vals[1] / vals[0], vals[3] / vals[2]))

print("\n%d of the checks failed." % fails)
sys.exit(0 if fails == 0 else 1)
