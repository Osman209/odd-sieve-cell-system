#!/usr/bin/env python3
"""
verify_overlap_bound.py

COVERS = ["[P9, Thm 5]"]

Regenerates the pair-overlap bound of [P9, Thm 5] in its sharpened form: the
complete region of coefficients for which the pointwise inequality holds, the
two vertices of that region, and the moment totals of the four worked windows.

The pointwise statement, for integers 0 <= l, r <= m:

    1_{l = r = 0}  >=  1 - l - r + a [ C(l,2) + C(r,2) ] + b l r ,

and it holds for every such pair if and only if

    a <= 2/m ,   b <= 1 ,   m(m-1) a + m^2 b <= 2m - 1 .

Since A, B >= 0 the best choice is at a vertex of that region, so with
H = sum(l+r) the summed bound is

    T >= max{ 0, C - H + max( (2/m) A + B/m^2 , B - ((m-1)/m) A ) } .

Two conventions are needed to reproduce the windows and neither is optional.
A line L_q strikes n only from q^2 upward, so a prime is never struck by its
own line and survives every cut; and l, r count DISTINCT primes, so n = q^2
contributes one striking line and not two.  Dropping the first loses the seven
twin cells whose members both lie below the cut; dropping the second turns
A = 0 into A = 54 at z = 100 and breaks every row.

Modes:  --fast (windows to 2e5)   default (to 1e6, the printed rows)
"""
import sys, math
from fractions import Fraction as Fr
from sympy import factorint, isprime

COVERS = ["[P9, Thm 5]"]
FAST = "--fast" in sys.argv
fails = 0


def check(name, ok, detail=""):
    global fails
    print(("  PASS  " if ok else "  FAIL  ") + name + ("   " + detail if detail else ""))
    if not ok:
        fails += 1


print("verify_overlap_bound.py   mode:", "fast" if FAST else "default")


def rhs(l, r, a, b):
    return 1 - l - r + a * (math.comb(l, 2) + math.comb(r, 2)) + b * l * r


# ---------------------------------------------------------- the coefficient region
tot = bad = 0
for m in range(2, 41):
    for a, b in ((Fr(2, m), Fr(1, m * m)), (Fr(-(m - 1), m), Fr(1))):
        for l in range(m + 1):
            for r in range(m + 1):
                tot += 1
                if rhs(l, r, a, b) > (1 if l == r == 0 else 0):
                    bad += 1
check("both vertices satisfy the inequality for every state, 2 <= m <= 40",
      bad == 0, "%d exact checks, %d violations" % (tot, bad))

nec_ok = True
for m in (2, 3, 5, 9, 40):
    nec_ok &= (rhs(m, 0, Fr(2, m) + Fr(1, 10**6), Fr(1, m * m)) > 0)       # a <= 2/m
    nec_ok &= (rhs(1, 1, Fr(2, m), 1 + Fr(1, 10**6)) > 0)                  # b <= 1
    b_edge = (Fr(2 * m - 1) - m * (m - 1) * Fr(1, 2 * m)) / (m * m)
    nec_ok &= (rhs(m, m, Fr(1, 2 * m), b_edge + Fr(1, 10**6)) > 0)         # third face
check("the three faces are necessary: crossing any one of them breaks a state", nec_ok)

out = viol = 0
for m in (2, 3, 4, 7):
    for eps in (Fr(1, 1000), Fr(1, 50)):
        edge_b = (Fr(2 * m - 1) - m * (m - 1) * (Fr(2, m) - eps)) / (m * m)
        for a, b in ((Fr(2, m) + eps, Fr(1, m * m)),
                     (Fr(-(m - 1), m), 1 + eps),
                     (Fr(2, m) - eps, edge_b + eps)):
            out += 1
            if any(rhs(l, r, a, b) > (1 if l == r == 0 else 0)
                   for l in range(m + 1) for r in range(m + 1)):
                viol += 1
check("every sampled point just outside the region breaks some state",
      viol == out, "%d of %d" % (viol, out))

m = 3
check("at m = 3 the region is a <= 2/3, b <= 1, 6a + 9b <= 5, with vertices "
      "(2/3, 1/9) and (-2/3, 1)",
      6 * Fr(2, 3) + 9 * Fr(1, 9) == 5 and 6 * Fr(-2, 3) + 9 * Fr(1) == 5)


# ------------------------------------------------------------------ the windows
def window(z, hi):
    """C, H, A, B, T over the cells with both endpoints strictly inside (1, hi)."""
    C = H = A = B = T = 0
    for b in range(1, (hi - 1) // 6 + 1):
        n1, n2 = 6 * b - 1, 6 * b + 1
        if n1 <= 1 or n2 >= hi:
            continue
        ls = []
        for n in (n1, n2):
            f = factorint(n)
            if any(p <= z and p * p <= n for p in f):      # a line strikes only from q^2
                ls = None
                break
            ls.append(sum(1 for p in f if p > z and p * p <= n))   # distinct primes
        if ls is None:
            continue
        l, r = ls
        C += 1
        H += l + r
        A += math.comb(l, 2) + math.comb(r, 2)
        B += l * r
        if l == 0 and r == 0:
            T += 1
    return C, H, A, B, T


hi = 2 * 10**5 if FAST else 10**6
printed = {32: (31051, 34003, 5491, 9301, 1743, 2689),
           40: (29370, 30586, 4078, 7977, 2389, 4043),
           60: (23748, 20205, 687, 4355, 4485, 7440),
           100: (19303, 13588, 0, 2453, 5988, 8168)}
print("      z       C     H(=R_hit)      A       B       T   published  optimized")
for z in (32, 40, 60, 100):
    C, H, A, B, T = window(z, hi)
    v1 = Fr(2, 3) * A + Fr(1, 9) * B
    v2 = B - Fr(2, 3) * A
    b1 = max(0, math.ceil(C - H + v1))
    b2 = max(0, math.ceil(C - H + max(v1, v2)))
    print("    %4d  %7d   %7d   %6d  %6d  %6d   %7d   %7d" % (z, C, H, A, B, T, b1, b2))
    check("both bounds hold at z = %d" % z, b1 <= T and b2 <= T)
    check("the optimized bound is at least the published one at z = %d" % z, b2 >= b1)
    if not FAST:
        p = printed[z]
        check("the printed row at z = %d: C, R_hit, A, B = %s" % (z, p[:4]),
              (C, H, A, B) == p[:4], "%s" % ((C, H, A, B),))
        check("the printed bounds at z = %d: %d and %d" % (z, p[4], p[5]),
              (b1, b2) == (p[4], p[5]), "%d and %d" % (b1, b2))

if not FAST:
    C, H, A, B, T = window(100, 10**6)
    check("at the cubic cut A = 0, so the second vertex returns the identity T = C - R + S",
          A == 0 and C - H + B == T, "C - H + B = %d, T = %d" % (C - H + B, T))
    check("the published vertex loses 8B/9 there",
          Fr(8, 9) * B == (C - H + B) - (C - H + Fr(1, 9) * B), "8B/9 = %s" % (Fr(8, 9) * B))


# ------------------------------------------------ what A actually counts
if not FAST:
    from collections import Counter
    for z, want in ((32, (5172, 319)), (40, (3816, 262)), (60, (609, 78)), (100, (0, 0))):
        three = rep = other = 0
        for b in range(1, (10**6 - 1) // 6 + 1):
            n1, n2 = 6 * b - 1, 6 * b + 1
            if n1 <= 1 or n2 >= 10**6:
                continue
            ends = []
            for n in (n1, n2):
                f = factorint(n)
                if any(pp <= z and pp * pp <= n for pp in f):
                    ends = None
                    break
                ends.append((sum(1 for pp in f if pp > z and pp * pp <= n),
                             sum(f.values()), len(f)))
            if ends is None:
                continue
            for l, Om, om in ends:
                c = math.comb(l, 2)
                if not c:
                    continue
                if Om != 3:
                    other += c
                elif om == 3:
                    three += c
                else:
                    rep += c
        check("A at z = %d comes only from endpoints with three prime factors: %d + %d"
              % (z, want[0], want[1]),
              (three, rep, other) == (want[0], want[1], 0),
              "%d distinct-triple, %d repeated, %d other" % (three, rep, other))


def sector(p, q, z):
    C = R = S = T = 0
    for b in range((p * p + 6) // 6, (q * q - 1) // 6 + 1):
        n1, n2 = 6 * b - 1, 6 * b + 1
        if n1 <= p * p or n2 >= q * q:
            continue
        if any(any(x <= z and x * x <= n for x in factorint(n)) for n in (n1, n2)):
            continue
        c1, c2 = not isprime(n1), not isprime(n2)
        C += 1
        R += c1 + c2
        S += c1 and c2
        T += (not c1) and (not c2)
    return C, R, S, T


check("the sector (29^2, 31^2) at z = 9 gives (C, R, S, T) = (8, 8, 2, 2)",
      sector(29, 31, 9) == (8, 8, 2, 2), "%s" % (sector(29, 31, 9),))
if not FAST:
    check("the sector (1009^2, 1013^2) at z = 100 gives (146, 110, 18, 54)",
          sector(1009, 1013, 100) == (146, 110, 18, 54), "%s" % (sector(1009, 1013, 100),))

print("\n%d of the checks failed." % fails)
sys.exit(0 if fails == 0 else 1)
