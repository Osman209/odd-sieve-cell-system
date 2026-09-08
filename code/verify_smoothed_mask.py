#!/usr/bin/env python3
"""
verify_smoothed_mask.py

Regenerates the table of [P6, App. B.4] "One further route, closed by an
implication": the least half-width H = T for which the double-tent smoothing of
the survivor mask keeps its deviation below its own mean at every centre, and
the largest gap g in that mask.

It also checks the statement made about the two columns, which is the support
bound 4H - 3 >= g, and checks that the statement the appendix used to make -
that 2H equals g to within one - is false, so that it cannot creep back.

COVERS = ["[P6, App. B.4]"]
"""
import sys
import numpy as np
from sympy import primerange

FAIL = []


def check(name, got, want):
    ok = got == want
    print("  %-4s %-58s %s" % ("PASS" if ok else "FAIL", name, got))
    if not ok:
        FAIL.append("%s (got %r, want %r)" % (name, got, want))


def mask(P):
    """The cells of Z/QZ surviving every line 5 <= q <= P, as in [P2, Thm 3]."""
    qs = list(primerange(5, P + 1))
    Q = 1
    for q in qs:
        Q *= q
    idx = np.arange(Q)
    A = np.ones(Q, dtype=bool)
    for q in qs:
        c = pow(6, -1, q)
        A &= (idx % q != c % q) & (idx % q != (-c) % q)
    return Q, A


def largest_gap(A):
    pos = np.flatnonzero(A)
    return int(max(np.diff(pos).max(), pos[0] + len(A) - pos[-1]))


def least_half_width(Q, A, cap=40):
    """Least H = T with |smoothed count - mean| < mean at every centre."""
    mean_density = A.sum() / Q
    f = np.fft.fft(A.astype(float))
    for H in range(1, cap + 1):
        w = np.array([1 - abs(u) / H for u in range(-(H - 1), H)])          # sums to H
        q = np.array([(1 - abs(t) / H) / H for t in range(-(H - 1), H)])    # sums to 1
        ker = np.convolve(q, w)                                            # support 4H-3
        pad = np.zeros(Q)
        pad[:len(ker)] = ker
        pad = np.roll(pad, -(len(ker) // 2))
        conv = np.real(np.fft.ifft(f * np.fft.fft(pad)))
        if abs(conv - H * mean_density).max() < H * mean_density:
            return H
    return None


def main():
    print("verify_smoothed_mask.py   [P6, App. B.4]\n")
    rows = []
    for P in (7, 11, 13, 17, 19):
        Q, A = mask(P)
        rows.append((P, Q, int(A.sum()), largest_gap(A), least_half_width(Q, A)))
        print("     P = %-3d Q = %-9d |A| = %-7d largest gap g = %-3d least H = T = %d"
              % rows[-1])

    check("the printed Q column", [r[1] for r in rows],
          [35, 385, 5005, 85085, 1616615])
    check("the printed least H = T column", [r[4] for r in rows], [2, 3, 5, 7, 10])
    check("the printed largest-gap column", [r[3] for r in rows], [5, 7, 11, 18, 25])

    # the support bound the appendix now states
    check("the support 4H-3 covers the gap in every row",
          [4*r[4] - 3 >= r[3] for r in rows], [True] * 5)
    check("the lower bound ceil((g+3)/4) reads 2, 3, 4, 6, 7",
          [-(-(r[3] + 3) // 4) for r in rows], [2, 3, 4, 6, 7])
    check("and is attained in the first two rows only",
          [-(-(r[3] + 3) // 4) == r[4] for r in rows],
          [True, True, False, False, False])

    # the withdrawn claim, kept as a negative check so it cannot return
    check("the withdrawn claim |2H - g| <= 1 fails in the last two rows",
          [abs(2*r[4] - r[3]) <= 1 for r in rows],
          [True, True, True, False, False])

    print("\n%d of the checks failed." % len(FAIL))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
