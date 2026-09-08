#!/usr/bin/env python3
"""
verify_parity_mean.py

COVERS = ["[P9, S2.3]"]

Regenerates the parity table of [P9, S2.3]: the mean of (-1)^Omega over the
z-rough integers of a stretch at 1e8, and over those whose partner n+2 is also
rough.  The point of the table is that the two means agree, i.e. the partner
condition changes which n are counted and not the parity of their factorisations.

Conventions taken from the section: the cut is u = 3, so z = X^(1/u) with
X = 1e8; rough means no prime factor <= z; the stretch is 4e7 integers at 1e8.
The predicted value for the first row is 1 - 2/(1 + log 2) = -0.181232.

Every rough n below 1.4e8 has all prime factors above z = 464, so Omega(n) <= 3
and the factorisation is found by dividing out the primes up to sqrt(1.4e8).

Modes:  --fast (1e6 stretch)   default (4e6)   --full (4e7, the published row)
"""
import sys, math
import numpy as np
from sympy import primerange

COVERS = ["[P9, S2.3]"]
FAST = "--fast" in sys.argv
FULL = "--full" in sys.argv
fails = 0
def check(name, ok, detail=""):
    global fails
    print(("  PASS  " if ok else "  FAIL  ") + name + ("   " + detail if detail else ""))
    if not ok: fails += 1
print("verify_parity_mean.py   mode:", "fast" if FAST else ("full" if FULL else "default"))

X = 10**8
L = 10**6 if FAST else (4*10**7 if FULL else 4*10**6)
u = 3
z = X ** (1.0/u)
start, end = X, X + L + 2                     # +2 so the partner of the last n exists
print("     stretch of %g integers at %g, cut u = %d, z = %.2f" % (L, X, u, z))

small = [p for p in primerange(2, int(z) + 1)]
n = np.arange(start, end, dtype=np.int64)
rough = np.ones(n.size, dtype=bool)
for p in small:
    first = (-start) % p
    rough[first::p] = False

idx = np.nonzero(rough)[0]
vals = n[idx]
omega = np.ones(vals.size, dtype=np.int8)     # the residual cofactor, counted below
res = vals.copy()
for p in primerange(int(z) + 1, int(math.isqrt(int(end))) + 1):
    hit = np.nonzero(res % p == 0)[0]
    while hit.size:
        res[hit] //= p
        omega[hit] += 1
        hit = hit[res[hit] % p == 0]
omega[res == 1] -= 1                          # the residual was 1, not a prime
sign = np.where(omega % 2 == 0, 1, -1).astype(np.int64)

roughset = rough.copy()
partner = np.zeros(vals.size, dtype=bool)
partner_idx = idx + 2
ok_idx = partner_idx < rough.size
partner[ok_idx] = roughset[partner_idx[ok_idx]]

keep = vals < start + L
m1 = sign[keep]
m2 = sign[keep & partner]
def mean_pm(a):
    mu = a.mean(); se = a.std(ddof=1)/math.sqrt(a.size)
    return a.size, mu, se
s1, mu1, se1 = mean_pm(m1)
s2, mu2, se2 = mean_pm(m2)
print("     z-rough n                    : %d, mean %.6f +- %.6f" % (s1, mu1, se1))
print("     z-rough n with n+2 also rough: %d, mean %.6f +- %.6f" % (s2, mu2, se2))

pred = 1 - 2/(1 + math.log(2))
check("the predicted value is 1 - 2/(1 + log 2) = -0.181232", abs(pred + 0.181232) < 5e-7)
check("the two means agree within their errors",
      abs(mu1 - mu2) < 3*math.sqrt(se1*se1 + se2*se2),
      "difference %.6f against %.6f" % (abs(mu1-mu2), 3*math.sqrt(se1*se1+se2*se2)))
# the published row meets the prediction at three standard errors only because
# its stretch is 4e7; on a shorter one the fluctuation is larger, so the tight
# test is asserted under --full and a loose one otherwise.
if FULL:
    check("the first mean meets the prediction within three standard errors",
          abs(mu1 - pred) < 3*se1, "%.6f against %.6f +- %.6f" % (pred, mu1, se1))
else:
    check("the first mean is near the prediction", abs(mu1 - pred) < 0.02,
          "%.6f against %.6f; run --full for the three-sigma test" % (mu1, pred))
check("the rough density matches the published 3,637,619 / 4e7 = 0.09094",
      abs(s1/L - 0.09094) < 5e-4, "%.5f" % (s1/L))
if FULL:
    check("the published row: 3,637,619 and 436,828 with means -0.182713 and -0.183596",
          s1 == 3637619 and s2 == 436828
          and abs(mu1 + 0.182713) < 1e-5 and abs(mu2 + 0.183596) < 1e-5,
          "%d / %d, %.6f / %.6f" % (s1, s2, mu1, mu2))

print("\n%d of the checks failed." % fails)
sys.exit(0 if fails == 0 else 1)
