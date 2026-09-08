#!/usr/bin/env python3
"""
verify_l2_stress.py

COVERS = ["[P4, S3.2]", "[P4, S5.3]"]

The two tables of [P4] that were computed once and never regenerated.  This
script does not try to reproduce the printed cells; it fixes the definitions the
sections leave implicit, regenerates both rows from them, and asserts the
structural conclusions the sections actually draw.

Definitions adopted, and they differ between the two sections -- which is the
thing the paper does not say:

  Sec. 3  sectors are indexed by u = 5 (mod 6) with the window (u^2, (u+2)^2);
          a survivor is a CELL with both members surviving the lines q <= u;
          P(u) = prod_{5<=q<=u}(1-2/q) and C(u) is the cell count, so that
          T(U) = sum survivors and M(U) = sum C(u)P(u).  Pinned in
          verify_window_transfer.py against the printed T = 2920.0, M = 3535.3.

  Sec. 5  sectors are indexed by EVERY integer u with the window (u^2,(u+1)^2),
          again sieved by the lines q <= u.  X(U) is the number of cells swept,
          which is what makes the printed X + U^2 column come out exactly, and

              D_r(U) = (all strikes of r over the sectors u >= r) - 2X/r .

          The mechanism this makes explicit: at moving depth the line r does not
          act before sector r, so it misses about r/3 of the strikes a uniform
          model would give it, and sum (r/3)^2 over the primes is the main term
          of sum |D_r|^2 -- which is also where the effective exponent near 3
          comes from, since sum_{p<=U} p^2 is of order U^3/log U.

Modes:  --fast (U <= 600)   default (U <= 1200)   --full (U <= 2400)
"""
import sys, math
from sympy import primerange
import numpy as np

COVERS = ["[P4, S3.2]", "[P4, S5.3]"]
FAST = "--fast" in sys.argv
FULL = "--full" in sys.argv
fails = 0
def check(name, ok, detail=""):
    global fails
    print(("  PASS  " if ok else "  FAIL  ") + name + ("   " + detail if detail else ""))
    if not ok: fails += 1
print("verify_l2_stress.py   mode:", "fast" if FAST else ("full" if FULL else "default"))

def cells(lo, hi):
    b0 = lo//6 + 1; b1 = (hi - 1)//6
    if b1 < b0: return np.empty(0, dtype=np.int64)
    b = np.arange(b0, b1 + 1, dtype=np.int64)
    return b[(6*b - 1 > lo) & (6*b + 1 < hi)]

# ------------------------------------------------------------- [P4, S3.2]
print("\n1. [P4, S3.2]: T/M at moving depth, regenerated")
UMAX = 600 if FAST else (1600 if not FULL else 1600)
bins = [(2, 50), (51, 150), (151, 300), (301, 600), (601, 1000), (1001, 1600)]
PP = list(primerange(5, UMAX + 2))
acc = {b: [0, 0.0] for b in bins}
P = 1.0; k = 0
for n in range(2, UMAX + 1):
    while k < len(PP) and PP[k] <= n: P *= (1 - 2.0/PP[k]); k += 1
    if n % 6 != 5: continue
    b = cells(n*n, (n + 2)**2); C = b.size
    keep = np.ones(C, dtype=bool)
    for q in PP:
        if q > n: break
        c = pow(6, -1, q)
        keep &= (b % q != c % q) & (b % q != (-c) % q)
    for bb in bins:
        if bb[0] <= n <= bb[1]: acc[bb][0] += int(keep.sum()); acc[bb][1] += C*P
row = [(bb, acc[bb][0]/acc[bb][1]) for bb in bins if acc[bb][1] > 0]
print("     " + " ; ".join("%s: %.5f" % (str(b), v) for b, v in row))
tot = (sum(acc[b][0] for b in bins), sum(acc[b][1] for b in bins))
print("     cumulative over the whole range: T/M = %.5f" % (tot[0]/tot[1]))
check("every bin sits between 0.75 and 0.90", all(0.75 < v < 0.90 for _, v in row),
      "spread %.4f -- the regenerated row fluctuates more than the printed one, which"
      " is what a per-bin rather than cumulative reading gives"
      % (max(v for _, v in row) - min(v for _, v in row)))
check("the cumulative ratio is near 0.80, which is the claim the section boxes",
      0.78 < tot[0]/tot[1] < 0.84, "%.5f" % (tot[0]/tot[1]))
print("     for reference: (e^gamma/2)^2 = %.6f, the squared dimension-one correction"
      % ((math.exp(0.5772156649015329)/2)**2))

# ------------------------------------------------------------- [P4, S5.3]
# CORRECTED 2026-09-08.  The earlier version of this block subtracted 2X/r with
# X the cells of ALL sectors up to U, charging the line r with 2/r of the cells
# of the sectors below its own birth.  That deterministic term is 98 per cent of
# the numbers it printed.  Below, both normalisations are printed and only the
# corrected one is asserted.  The quantity (5.1) actually needs is the nested
# deviation of Thm 3, which is in verify_l2_nested.py.
print("\n2. [P4, S5.3]: the L^2 stress test, with the normalisation corrected")
Us = [300, 600] if FAST else ([300, 600, 1200] if not FULL else [300, 600, 1200, 2400])
printed_XU = {300: 1.05e5, 600: 4.20e5, 1200: 1.68e6, 2400: 6.72e6}
printed_lines = {300: 60, 600: 107, 1200: 194, 2400: 355}
res = []
for U in Us:
    PR = [q for q in primerange(5, U + 1)]
    hits = {r: 0 for r in PR}; Xr = {r: 0 for r in PR}; X = 0
    for n in range(2, U + 1):
        b = cells(n*n, (n + 1)**2)
        if b.size == 0: continue
        X += b.size
        for r in PR:
            if r > n: break
            c = pow(6, -1, r); Xr[r] += b.size
            hits[r] += int(((b % r == c % r) | (b % r == (-c) % r)).sum())
    S     = sum((hits[r] - 2.0*Xr[r]/r)**2 for r in PR)
    S_old = sum((hits[r] - 2.0*X/r)**2     for r in PR)
    det   = sum((2.0*(X - Xr[r])/r)**2     for r in PR)
    res.append((U, len(PR), X, S, X + U*U, S/(X + U*U), S_old/(X + U*U), det/(X + U*U)))
    print("     U = %-5d lines %3d   X = %d   sum|D_r|^2 = %.4g   X+U^2 = %.3g   ratio = %.4f"
          "   [old normalisation %.2f, deterministic part %.2f]"
          % (U, len(PR), X, S, X + U*U, S/(X + U*U), S_old/(X + U*U), det/(X + U*U)))

check("X + U^2 reproduces the printed column to its three printed digits",
      all(abs(r[4] - printed_XU[r[0]])/printed_XU[r[0]] < 1e-3 for r in res),
      ", ".join("%d" % r[4] for r in res))
check("the line counts reproduce the printed column exactly",
      all(r[1] == printed_lines[r[0]] for r in res))
check("with each line normalised by the sectors it has been born in, the ratio is flat below 0.01",
      all(r[5] < 0.01 for r in res)
      and max(r[5] for r in res) < 1.5*min(r[5] for r in res),
      " -> ".join("%.4f" % r[5] for r in res))
check("the deterministic term supplies at least 95 per cent of the old ratio at every U",
      all(r[7] > 0.95*r[6] for r in res),
      " -> ".join("%.2f of %.2f" % (r[7], r[6]) for r in res))

print("\n%d of the checks failed." % fails)
sys.exit(0 if fails == 0 else 1)
