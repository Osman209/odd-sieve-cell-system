#!/usr/bin/env python3
"""
verify_l2_nested.py

COVERS = ["[P4, S5.3]"]

Re-test of the L^2 stress test of [P4, S5.3], written 2026-09-08 during the
second review pass.  It computes three quantities on the same sectors as
verify_l2_stress.py (every integer u, window (u^2,(u+1)^2), lines q <= u):

  1. the printed quantity  D_r = (strikes of r over sectors u >= r) - 2X/r,
     where X counts ALL cells up to U, including the sectors u < r where the
     line r is not active;
  2. the same with the honest normalisation  D'_r = hits - 2 X_r / r, where
     X_r counts only the cells of the sectors u >= r;
  3. the NESTED deviations of [P4, Thm 3]:  eps_r(u) = (strikes of r on the
     survivors of the lines below r in sector u) - (2/r) N_{r^-}(u), summed
     over u, and the terms B_r of Theorem 3, whose sum is T - M exactly.

What it shows: the growth of sum |D_r|^2 in the printed table is the
deterministic term (2(X - X_r)/r)^2 -- the line r is charged 2/r of cells
it never saw -- and with X_r in place of X the ratio is FLAT at about 0.005.
That raw quantity is trivially small (one progression in a union of
intervals misses its mean by O(1) per sector), so it is not evidence for
or against anything.  The object Theorem 3 needs is the nested one, and its
L^2 sum grows like U^2.4 on 300 <= U <= 1200: neither U^2 log^A nor a power
is separated on this range.

Modes: --fast (U <= 600)   default (U <= 1200)
"""
import sys, math
from sympy import primerange
import numpy as np

COVERS = ["[P4, S5.3]"]
FAST = "--fast" in sys.argv
fails = 0
def check(name, ok, detail=""):
    global fails
    print(("  PASS  " if ok else "  FAIL  ") + name + ("   " + detail if detail else ""))
    if not ok: fails += 1

def cells(lo, hi):
    b0 = lo//6 + 1; b1 = (hi - 1)//6
    if b1 < b0: return np.empty(0, dtype=np.int64)
    b = np.arange(b0, b1 + 1, dtype=np.int64)
    return b[(6*b - 1 > lo) & (6*b + 1 < hi)]

Us = [300, 600] if FAST else [300, 600, 1200]
rows = []
for U in Us:
    PR = list(primerange(5, U + 1))
    hits = {r: 0 for r in PR}; Xr = {r: 0 for r in PR}
    eps = {r: 0.0 for r in PR}; Bw = {r: 0.0 for r in PR}
    Pcum = {}; P = 1.0; k = 0
    for n in range(2, U + 1):
        while k < len(PR) and PR[k] <= n: P *= (1 - 2.0/PR[k]); k += 1
        Pcum[n] = P
    X = 0; T = 0; M = 0.0
    for n in range(2, U + 1):
        b = cells(n*n, (n + 1)**2)
        if b.size == 0: continue
        X += b.size; keep = np.ones(b.size, dtype=bool); Pn = Pcum[n]
        for r in PR:
            if r > n: break
            c = pow(6, -1, r)
            raw = (b % r == c % r) | (b % r == (-c) % r)
            hits[r] += int(raw.sum()); Xr[r] += b.size
            N0 = int(keep.sum()); hit = keep & raw
            e = int(hit.sum()) - 2.0*N0/r
            eps[r] += e; Bw[r] += Pn*e
            keep &= ~hit
        T += int(keep.sum()); M += b.size*Pn
    Pr = {}; P = 1.0
    for r in PR: P *= (1 - 2.0/r); Pr[r] = P
    B = [-Bw[r]/Pr[r] for r in PR]
    S_old = sum((hits[r] - 2.0*X/r)**2 for r in PR)
    S_new = sum((hits[r] - 2.0*Xr[r]/r)**2 for r in PR)
    S_det = sum((2.0*(X - Xr[r])/r)**2 for r in PR)
    S_eps = sum(eps[r]**2 for r in PR)
    base = X + U*U
    rows.append((U, S_old/base, S_new/base, S_det/base, S_eps/base, S_eps, T, M, sum(B)))
    print("  U = %-5d  printed ratio %.3f   honest ratio %.4f   deterministic term %.3f"
          "   nested ratio %.4f   T = %d  M = %.1f  T-M = %.1f  sum B_r = %.1f"
          % (U, S_old/base, S_new/base, S_det/base, S_eps/base, T, M, T - M, sum(B)))

check("the deterministic term accounts for more than 95 per cent of the printed sum at every U",
      all(r[3] > 0.95*r[1] for r in rows))
check("with the honest normalisation the ratio is flat below 0.01 at every U",
      all(r[2] < 0.01 for r in rows) and max(r[2] for r in rows) < 1.5*min(r[2] for r in rows))
check("sum B_r reproduces T - M exactly (Theorem 3)",
      all(abs(r[8] - (r[6] - r[7])) < 1e-6*max(1.0, abs(r[7])) for r in rows))
if len(rows) >= 2:
    e = (math.log(rows[-1][5]) - math.log(rows[0][5]))/(math.log(rows[-1][0]) - math.log(rows[0][0]))
    print("  effective exponent of the nested sum |sum_u eps_r(u)|^2 against U: %.2f" % e)
    check("the nested exponent lies between 2 and 3 on the tested range", 2.0 < e < 3.0, "%.2f" % e)
print("\n%d failure(s)" % fails)
sys.exit(1 if fails else 0)
