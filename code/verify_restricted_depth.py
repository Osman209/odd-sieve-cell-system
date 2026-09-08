#!/usr/bin/env python3
"""
verify_restricted_depth.py

COVERS = ["[P4, S5.3]"]

The restricted-depth row of [P4, S5.3], where the sieve depth is capped at a
fixed z = U^(1/2) instead of tracking u.  Same objects as the main row of that
section (see verify_l2_stress.py): sectors (u^2,(u+1)^2) over every integer u,
X the cells swept, D_r = (strikes of r over the sectors u >= r) - 2X/r.

It is separated out because it is cheap: with the depth capped there are only
about sqrt(U) lines, and the strikes of one line in a contiguous range of cells
are a difference of two floors rather than a scan, so the whole row to
U = 38,400 runs in seconds rather than hours.

Reading fixed by measurement: z is a FIXED cap U^(1/2).  A per-sector cap
u^(1/2) gives a ratio of 430 at U = 2400 where the printed row gives 0.00831.

WHAT THIS ROW SHOWS, and it is not what the printed row shows.  Regenerated, the
ratio is 0.00532, 0.00512, 0.00538, 0.00542, 0.00538 at U = 2400 ... 38400 --
FLAT, growth exponent 0.00.  The printed row is 0.00831 ... 0.85696, growth
exponent 1.67, and the gap between them widens from a factor 1.6 to a factor
159.  So the two are not the same quantity to within a constant: capping the
depth at a fixed z removes the growth entirely on this range, and the sentence
the row supports -- that restricting the depth "does not flatten the observed
trend" -- is not what a fixed cap gives.  The main row of the section is
unaffected: it is regenerated and does rise, 1.68 to 10.31.

Modes:  --fast (to 2400)   default (to 9600)   --full (to 38400, the printed row)

STATUS, 2026-09-08: the restricted-depth row this file regenerates is no longer
printed in [P4, S5.3]; it was withdrawn together with the main row when the
normalisation of D_r was corrected.  Kept as the record of the measurement.
"""
import sys, math
from sympy import primerange

COVERS = ["[P4, S5.3]"]
FAST = "--fast" in sys.argv
FULL = "--full" in sys.argv
fails = 0
def check(name, ok, detail=""):
    global fails
    print(("  PASS  " if ok else "  FAIL  ") + name + ("   " + detail if detail else ""))
    if not ok: fails += 1
print("verify_restricted_depth.py   mode:", "fast" if FAST else ("full" if FULL else "default"))

def cell_range(u):
    """first and last cell index b with u^2 < 6b-1 and 6b+1 < (u+1)^2"""
    lo, hi = u*u, (u + 1)**2
    b0 = lo//6 + 1
    while 6*b0 - 1 <= lo: b0 += 1
    b1 = (hi - 1)//6
    while b1 >= b0 and 6*b1 + 1 >= hi: b1 -= 1
    return b0, b1

def count_res(b0, b1, res, r):
    if b1 < b0: return 0
    return (b1 - res)//r - (b0 - 1 - res)//r

Us = [2400] if FAST else ([2400, 4800, 9600] if not FULL else
                          [2400, 4800, 9600, 19200, 38400])
print("     U        lines   X            sum|D_r|^2      ratio")
out = []
for U in Us:
    Z = U ** 0.5
    PR = [r for r in primerange(5, int(Z) + 1)]
    inv = {r: pow(6, -1, r) for r in PR}
    hits = {r: 0 for r in PR}
    X = 0
    for u in range(2, U + 1):
        b0, b1 = cell_range(u)
        if b1 < b0: continue
        X += b1 - b0 + 1
        for r in PR:
            if r > u: break
            c = inv[r]
            hits[r] += count_res(b0, b1, c % r, r) + count_res(b0, b1, (-c) % r, r)
    S = sum((hits[r] - 2.0*X/r)**2 for r in PR)
    out.append((U, len(PR), X, S, S/(X + U*U)))
    print("     %-8d %-6d %-12d %-14.4g  %.5f" % (U, len(PR), X, S, S/(X + U*U)))

printed = {2400: 0.00831, 4800: 0.02220, 9600: 0.08504, 19200: 0.20556, 38400: 0.85696}
check("the cheap count agrees with the scan of verify_l2_stress.py at U = 2400",
      abs(out[0][4] - 0.00532) < 1e-4, "%.5f against 0.00532" % out[0][4])
print("     printed row for comparison: " +
      ", ".join("%g:%.5f" % (U, printed[U]) for U, *_ in out))
# THE FINDING: the regenerated row is flat, the printed one grows like U^{5/3}.
check("the regenerated restricted row is flat in U",
      max(r[4] for r in out)/min(r[4] for r in out) < 1.2,
      " -> ".join("%.5f" % r[4] for r in out))
if len(out) > 1:
    e = (math.log(out[-1][4]) - math.log(out[0][4]))/(math.log(out[-1][0]) - math.log(out[0][0]))
    pe = (math.log(printed[out[-1][0]]) - math.log(printed[out[0][0]])) / \
         (math.log(out[-1][0]) - math.log(out[0][0]))
    print("     growth exponent of the ratio: regenerated %.2f, printed %.2f" % (e, pe))
    check("the printed row grows while the regenerated one does not, so the two "
          "are different objects and not a constant factor apart",
          pe > 1.0 and abs(e) < 0.2, "regenerated %.2f, printed %.2f" % (e, pe))
    r0 = printed[out[0][0]]/out[0][4]; r1 = printed[out[-1][0]]/out[-1][4]
    print("     printed / regenerated: %.2f at U = %d, %.2f at U = %d"
          % (r0, out[0][0], r1, out[-1][0]))

print("\n%d of the checks failed." % fails)
sys.exit(0 if fails == 0 else 1)
