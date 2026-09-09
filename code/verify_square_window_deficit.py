#!/usr/bin/env python3
"""The measurements of [P12, Section 9]: where the four-factor deficit sits.

COVERS = "[P12, Section 6 stability check and Section 9] the deficit, the excess profile, the required savings, and the corner check on the two published constants"

At theta = 1/2 and r = 4 the weight coefficient is negative. This script
regenerates every number in Section 9 of [P12] from one floating-point solution
of the dimension-two Diamond-Halberstam-Richert system:

  the optimised parameters and the deficit C_4;
  the split of the subtracted estimate into its floor and its excess;
  the distribution of the weighted excess of F_2 - 1 across bands of s;
  the saving lambda that an upper bound sieve would need on each tail s >= S;
  the sensitivity of Section 9.5, replacing F_2 by its infimum 1;
  the crossings in the window-length exponent quoted in Section 9;
  the corner check of Section 6 on the two published transition constants.

These are measurements, not enclosures. The certified coefficients of [P12,
Prop. 1] are in verify_paired_almost_primes.py, which is a separate interval
certificate and does not depend on anything here.

Run:  python3 code/verify_square_window_deficit.py
"""
import numpy as np, sys

COVERS = "[P12, Section 9] the deficit, the excess profile and the required savings"

GAMMA = 0.57721566490153286
E2 = np.exp(2 * GAMMA)
ALPHA2, BETA2 = 5.3577, 4.2664          # Kao, Section 4, Theorem 2
H = 2e-4
W, U, THETA, R = 16.9155, 2.8215, 0.5, 4   # the optimised parameters of [P12, Section 9]


def dhr(alpha2=None, beta2=None):
    alpha2 = ALPHA2 if alpha2 is None else alpha2
    beta2 = BETA2 if beta2 is None else beta2
    s = np.arange(0.0, 14.0 + H / 2, H)
    n = len(s)
    sig = np.zeros(n)
    m = (s > 0) & (s <= 2)
    sig[m] = s[m] ** 2 / (8 * E2)
    m = (s > 2) & (s <= 4)
    sig[m] = (2 * (s[m] - 1) ** 2 - s[m] ** 2 * np.log(s[m] / 2)) / (4 * E2)
    i4, i2 = int(round(4 / H)), int(round(2 / H))
    g = np.zeros(n)
    idx = np.arange(i4, n)
    g[idx] = sig[idx - i2] / s[idx] ** 3
    cum = np.concatenate([[0.0], np.cumsum((g[i4:-1] + g[i4 + 1:]) / 2 * H)])
    sig[i4:] = s[i4:] ** 2 * (sig[i4] / 16 - 2 * cum)
    F = np.zeros(n); f = np.zeros(n)
    ia, ib, i1 = int(round(alpha2 / H)), int(round(beta2 / H)), int(round(1 / H))
    F[1:ia + 1] = 1 / sig[1:ia + 1]
    for i in range(1, n):
        a, b = s[i - 1], s[i]
        if i > ib:
            f[i] = (a * a * f[i - 1] + H * (2 * a * F[i - 1 - i1] + 2 * b * F[i - i1]) / 2) / (b * b)
        if i > ia:
            F[i] = (a * a * F[i - 1] + H * (2 * a * f[i - 1 - i1] + 2 * b * f[i - i1]) / 2) / (b * b)
    return s, F, f


S, F, f = dhr()
Ff = lambda x: np.interp(x, S, F)
ff = lambda x: np.interp(x, S, f)
assert abs(Ff(13.0) - 1) < 1e-3 and abs(ff(13.0) - 1) < 1e-3, "DHR march lost its normalisation"

al, be = 1 / W, 1 / U
t = np.linspace(al, be, 2000001)
eta = R + 1 - U
pos = eta * ff(THETA * W)
base = 2 * np.trapezoid(1 / t - U, t)
sub = 2 * np.trapezoid((1 / t - U) * Ff(W * (THETA - t)), t)
deficit = sub - pos

print("w = %.4f   u = %.4f   theta = %.3f   r = %d" % (W, U, THETA, R))
print("  positive term (r+1-u) f_2(%.5f) = %.6f" % (THETA * W, pos))
print("  subtracted term                   = %.6f" % sub)
print("  C_4                               = %+.6f" % (pos - sub))
print("  f_2 at %.5f = %.6f ; raising it to 1 would save %.6f"
      % (THETA * W, ff(THETA * W), eta * (1 - ff(THETA * W))))
print("  subtracted term = floor %.6f + excess %.6f" % (base, sub - base))

smin, smax = W * (THETA - be), W * (THETA - al)
xs = np.linspace(smin, smax, 2000001)
rho = (2 / W) * (1 / (THETA - xs / W) - U)
ex = (Ff(xs) - 1) * rho
total = np.trapezoid(ex, xs)

print("\nweighted excess of F_2 - 1, by band of s   (s runs %.4f to %.4f)" % (smin, smax))
edges = [smin, 2.5, 3.0, 4.0, 4.3, 5.0, ALPHA2, 6.0, smax]
for a, b in zip(edges, edges[1:]):
    v = np.trapezoid(np.where((xs >= a) & (xs <= b), ex, 0), xs)
    print("  [%6.4f, %6.4f]   %.7f   %5.2f%%" % (a, b, v, 100 * v / total))

print("\nsaving an upper bound sieve would need on the tail s >= S")
tails = {}
for Sv in [smin, 3.0, 3.5, 4.0, 4.3, 5.0, ALPHA2]:
    v = np.trapezoid(np.where(xs >= Sv, ex, 0), xs)
    tails[Sv] = v
    print("  S = %6.4f   E = %.6f   lambda = %5.2f%%" % (Sv, v, 100 * deficit / v))

above = np.trapezoid(np.where(xs >= 4.3, ex, 0), xs)
print("\nshare of the weighted excess above s = 4.3 : %.1f%%" % (100 * above / total))


# ---- Section 9.5: what remains if F_2 is replaced by its infimum 1
print("\nSection 9.5, with F_2 replaced by 1 at the same parameters:")
print("  C_4 = %+.6f" % (pos - base))

# ---- Section 9: the crossings in the window-length exponent
def excess_at(beta):
    tt = np.linspace(al, be, 400001)
    return 2 * np.trapezoid((1 / tt - U) * (Ff(W * (beta - tt)) - 1), tt)


def coeff_at(beta, w=W, u=U, r=R):
    a2, b2 = 1 / w, 1 / u
    tt = np.linspace(a2, b2, 400001)
    return (r + 1 - u) * ff(beta * w) - 2 * np.trapezoid((1 / tt - u) * Ff(w * (beta - tt)), tt)


def bisect(g, lo, hi):
    for _ in range(60):
        mid = (lo + hi) / 2
        if g(mid):
            hi = mid
        else:
            lo = mid
    return hi


e_half = excess_at(0.5)
b_frozen = bisect(lambda x: excess_at(x) < e_half - deficit, 0.5, 0.55)
b_moving = bisect(lambda x: coeff_at(x) > 0, 0.5, 0.55)
print("\nSection 9, window-length exponent beta = (1+vartheta)/2:")
print("  E(1/2) = %.6f" % e_half)
print("  frozen positive term: crossing at beta = %.6f  (vartheta = %.4f)" % (b_frozen, 2 * b_frozen - 1))
print("  moving positive term: crossing at beta = %.6f  (vartheta = %.4f)" % (b_moving, 2 * b_moving - 1))
print("  at the certified row, C_4(0.513; 16.42405, 2.79166) = %+.6f"
      % coeff_at(0.513, 16.42405, 2.79166))

# ---- Section 6: corner check on the two published constants
print("\nSection 6 stability, at the corners of a rectangle a hundred times wider")
print("than the brackets the certificate uses:")
CERT = [(5, 0.5, 16.0, 3.0), (5, 0.38, 23.430, 3.376),
        (4, 0.513, 16.42405, 2.79166), (3, 0.78, 10.028, 2.257)]
for a2, b2 in ((5.3550, 4.2680), (5.3600, 4.2650)):
    s2, F2c, f2c = dhr(a2, b2)
    Fc = lambda x: np.interp(x, s2, F2c)
    fc = lambda x: np.interp(x, s2, f2c)
    vals = []
    for r, th, w, u in CERT:
        tt = np.linspace(1 / w, 1 / u, 400001)
        vals.append((r + 1 - u) * fc(th * w) - 2 * np.trapezoid((1 / tt - u) * Fc(w * (th - tt)), tt))
    print("  alpha_2 = %.4f, beta_2 = %.4f :  " % (a2, b2) + "  ".join("%+.5f" % v for v in vals))
    assert min(vals) > 0, "a coefficient turned negative at a corner"

ok = (deficit > 0
      and abs(base + total - sub) < 1e-4
      and eta * (1 - ff(THETA * W)) < 0.05 * deficit
      and above > 0.5 * total)
print("\nthe deficit is not in the lower sifting function, and most of the excess is in the tail."
      if ok else "\nFAILED")
sys.exit(0 if ok else 1)
