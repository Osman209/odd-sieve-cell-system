#!/usr/bin/env python3
"""
verify_parity_rails.py

COVERS = ["[P11, S2.5]"]

Regenerates every number printed in [P11, S2.5], "The identity of [P9, S2.3]
needs a sign, not a bound".

Definitions taken from that section.  With z = x^(1/3), a z-rough integer below
x has Omega = 1 or 2, since three factors above x^(1/3) exceed x.  Write A and B
for the counts of the two kinds among the z-rough integers to x that are coprime
to 6.  Each such n is one endpoint of a cell: its partner is n+2 when n = 5 mod 6
and n-2 when n = 1 mod 6.  alpha and beta are the proportions of each kind whose
partner is also z-rough.  The mean of (-1)^Omega over the endpoints of open cells
is then (B*beta - A*alpha) / (A*alpha + B*beta), which is negative if and only if

    beta/alpha  <  A/B  ->  1/log 2 = 1.442695 .

The conditional extension of the section uses the linear-sieve functions

    F(s) = 2 e^gamma / s              (1 <= s <= 3)
    f(s) = 2 e^gamma log(s-1) / s     (2 <= s <= 4)

with F continued above s = 3 by s F(s) = 2 e^gamma + int_3^s f(t-1) dt.  Two
facts the section rests on are checked here: F/f = 1/log 2 exactly at s = 3, and
f/F = log(s-1) on [2,3], which is what turns the condition into s > u.

Modes:  --fast (heights to 1e6)   default (to 1e7)   --full (to 1e8, the printed row)
"""
import sys, math
import numpy as np
from sympy import primerange

COVERS = ["[P11, S2.5]"]
FAST = "--fast" in sys.argv
FULL = "--full" in sys.argv
fails = 0


def check(name, ok, detail=""):
    global fails
    print(("  PASS  " if ok else "  FAIL  ") + name + ("   " + detail if detail else ""))
    if not ok:
        fails += 1


print("verify_parity_rails.py   mode:", "fast" if FAST else ("full" if FULL else "default"))

# ---------------------------------------------------------------- sieve functions
GAMMA = 0.57721566490153286061
A2 = 2 * math.exp(GAMMA)


def f_lin(s):
    return A2 * math.log(s - 1) / s


def F_lin(s, n=20000):
    if s <= 3:
        return A2 / s
    h = (s - 3.0) / n                       # trapezoid on int_3^s f(t-1) dt
    tot = 0.5 * (f_lin(2.0) + f_lin(s - 1))
    for i in range(1, n):
        tot += f_lin(3.0 + i * h - 1)
    return (A2 + tot * h) / s


THRESH = 1 / math.log(2)
check("the threshold is 1/log 2 = 1.442695", abs(THRESH - 1.442695) < 5e-7, "%.6f" % THRESH)
check("F/f = 1/log 2 exactly at s = 3", abs(F_lin(3.0) / f_lin(3.0) - THRESH) < 1e-12,
      "%.9f against %.9f" % (F_lin(3.0) / f_lin(3.0), THRESH))
check("f/F = log(s-1) on [2,3]",
      max(abs(f_lin(s) / F_lin(s) - math.log(s - 1)) for s in (2.2, 2.5, 2.8, 3.0)) < 1e-12)
F35, f35 = F_lin(3.5), f_lin(3.5)
check("the printed F(3.5) = 1.0652 and f(3.5) = 0.9326",
      abs(F35 - 1.0652) < 5e-5 and abs(f35 - 0.9326) < 5e-5, "%.6f, %.6f" % (F35, f35))
check("the printed ratio F(3.5)/f(3.5) = 1.1422", abs(F35 / f35 - 1.1422) < 5e-5,
      "%.6f" % (F35 / f35))
check("the mean is at most -0.116 at s = 3.5",
      abs((F35 / f35 - 1) / (F35 / f35 + 1) - 0.0664) < 5e-4
      and (1 - f35 / F35) / (1 + f35 / F35) > 0,
      "bound on beta/alpha is %.4f, below the threshold %.4f" % (F35 / f35, THRESH))
naive = (A2 / 3.5) / f35
check("the closed form 2e^gamma/s at 3.5 would give F/f = 1.0914, and is not valid there",
      abs(naive - 1.0914) < 5e-5 and naive < F35 / f35, "%.6f" % naive)

# ---------------------------------------------------------------- the two rails
def rails(x):
    """A, B, alpha, beta over the z-rough integers to x coprime to 6, z = x^(1/3)."""
    z = int(x ** (1.0 / 3))
    rough = np.ones(x + 3, dtype=bool)
    for p in primerange(2, z + 1):
        rough[0::p] = False
    rough[:z + 1] = False
    vals = np.nonzero(rough[:x + 1])[0].astype(np.int64)
    res, om = vals.copy(), np.zeros(vals.size, dtype=np.int8)
    for p in primerange(z + 1, math.isqrt(x) + 1):
        hit = np.nonzero(res % p == 0)[0]
        while hit.size:
            res[hit] //= p
            om[hit] += 1
            hit = hit[res[hit] % p == 0]
    om[res > 1] += 1                        # the surviving cofactor is one more prime
    keep = (vals % 6 == 1) | (vals % 6 == 5)
    v, o = vals[keep], om[keep]
    partner = np.where(v % 6 == 5, v + 2, v - 2)
    ok = rough[partner]
    isA, isB = (o == 1), (o == 2)
    return int(isA.sum()), int(isB.sum()), float(ok[isA].mean()), float(ok[isB].mean()), o, ok


top = 6 if FAST else (8 if FULL else 7)
printed = {5: 1.0008, 6: 1.0085, 7: 0.9990, 8: 1.0005}
print("     x        A          B        B/A      alpha     beta    beta/alpha")
last = None
for e in range(5, top + 1):
    A, B, al, be, o, ok = rails(10 ** e)
    r = be / al
    print("    1e%d  %9d  %9d   %.4f   %.5f  %.5f    %.4f" % (e, A, B, B / A, al, be, r))
    check("beta/alpha at 1e%d reproduces the printed %.4f" % (e, printed[e]),
          abs(r - printed[e]) < 5e-5, "%.4f" % r)
    check("beta/alpha at 1e%d is below the threshold 1.4427" % e, r < THRESH)
    if e == top:
        last = (A, B, al, be, o, ok)

A, B, al, be, o, ok = last
mu_direct = np.where(o[ok] % 2 == 0, 1.0, -1.0).mean()
mu_formula = (B * be - A * al) / (A * al + B * be)
check("the mean over the endpoints of open cells equals (B beta - A alpha)/(A alpha + B beta)",
      abs(mu_direct - mu_formula) < 1e-9, "%.9f against %.9f" % (mu_direct, mu_formula))
check("that mean is negative", mu_direct < 0, "%.6f" % mu_direct)
check("B/A is still short of its limit log 2 = 0.6931 at this height", B / A < math.log(2),
      "%.4f" % (B / A))

# -------------------------------------------- the neighbour sieve is not monotone
x = 10 ** 5
z = int(x ** (1.0 / 3))
rough = np.ones(x + 3, dtype=bool)
for p in primerange(2, z + 1):
    rough[0::p] = False
rough[:z + 1] = False
vals = np.nonzero(rough[:x + 1])[0].astype(np.int64)
res, om = vals.copy(), np.zeros(vals.size, dtype=np.int8)
for p in primerange(z + 1, math.isqrt(x) + 1):
    hit = np.nonzero(res % p == 0)[0]
    while hit.size:
        res[hit] //= p
        om[hit] += 1
        hit = hit[res[hit] % p == 0]
om[res > 1] += 1
keep = (vals % 6 == 1) | (vals % 6 == 5)
v, o = vals[keep], om[keep]
partner = np.where(v % 6 == 5, v + 2, v - 2)
sgn = np.where(o % 2 == 0, 1.0, -1.0)
means = {}
for y in (41, 43):
    ny = np.ones(x + 3, dtype=bool)
    for p in primerange(2, y + 1):
        ny[0::p] = False
    sel = ny[partner]
    means[y] = float(sgn[sel].mean())
print("     neighbour sifted to y = 41: mean %.4f;  to y = 43: mean %.4f"
      % (means[41], means[43]))
check("the printed pair -0.3519 and -0.3484",
      abs(means[41] + 0.3519) < 5e-5 and abs(means[43] + 0.3484) < 5e-5)
check("adding the line 43 raises the mean, so no line-by-line accumulation is available",
      means[43] > means[41], "%.4f -> %.4f" % (means[41], means[43]))

print("\n%d of the checks failed." % fails)
sys.exit(0 if fails == 0 else 1)
