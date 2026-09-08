#!/usr/bin/env python3
"""
verify_dimension_two_sieve.py

Checks the numerical claim behind the weighted-sieve argument for a pair
a, a+2 with Omega(a), Omega(a+2) <= 5 inside a window between squares:

        3 f_2(8) - 2 J > 0,
        J = int_{1/16}^{1/3} (1-3t)/t * F_2(8-16t) dt.

STATUS, 2026-09-08.  The Omega <= 5 claim this file was written for is no
longer stated in any paper; [P10, S2.5] now states the far weaker Omega <= 8.
The file is kept as the record of the computation and NOT as support for any
printed statement.  Two cautions, both of which the output makes visible:

  * the beta it finds by its own no-crossing condition is 4.834, the
    Rosser-Iwaniec beta-sieve value, not the Diamond-Halberstam-Richert
    4.2664 quoted in the papers.  The two systems differ by more than the
    value of beta -- DHR carries its own sigma function and a second
    transition alpha_2 -- so substituting 4.2664 into THIS system does not
    produce the DHR bound, and the row that does so is labelled UNVERIFIED.
  * an earlier draft asserted f_2(8) > 0.870 and J < 1.269.  The computed
    values f_2(8) = 0.99504 and J = 1.20317 SATISFY both of those
    inequalities; what they do not reproduce is the margin the draft read
    off them.  Part 3 below shows the two asserted numbers cannot come from
    one solution.

Method.  The beta-sieve (Ankeny-Onishi) functions of dimension kappa solve
        (s^k F(s))' = k s^{k-1} f(s-1),
        (s^k f(s))' = k s^{k-1} F(s-1)   for s > beta,
with F = A s^{-k}, f = 0 on (0, beta].  The delay is 1, so the system is a
pure quadrature and is integrated forward by the trapezoid rule.  A is fixed
by F, f -> 1.  beta is fixed by the no-crossing condition F >= f (see below).

Calibration.  kappa = 1 must return A = 2 e^gamma, F(3.5) = 1.0651936,
f(3.5) = 0.9325601, and beta_1 = 2.  All four are checked.
"""

COVERS = ["[P10, S2.5]"]

import numpy as np, sys

def solve(kappa, beta, Smax=40.0, h=1.0/4096, A=1.0):
    N = int(round(1.0/h)); h = 1.0/N
    n = int(round(Smax/h))+1
    s = np.arange(n)*h
    F = np.zeros(n); f = np.zeros(n)
    ib = int(round(beta/h)); beta = ib*h
    F[1:ib+1] = A*s[1:ib+1]**(-kappa)
    P = np.zeros(n); Q = np.zeros(n); P[ib] = A
    for i in range(ib+1, n):
        si, sm = s[i], s[i-1]
        P[i] = P[i-1] + 0.5*h*(kappa*sm**(kappa-1)*f[i-1-N] + kappa*si**(kappa-1)*f[i-N])
        Q[i] = Q[i-1] + 0.5*h*(kappa*sm**(kappa-1)*F[i-1-N] + kappa*si**(kappa-1)*F[i-N])
        F[i] = P[i]/si**kappa; f[i] = Q[i]/si**kappa
    return s, F, f, beta

def normalised(kappa, beta, h=1.0/4096):
    s, F, f, b = solve(kappa, beta, h=h)
    A = 1.0/(0.5*(F[-1]+f[-1]))
    return s, A*F, A*f, b, A

def crosses(kappa, beta, h=1.0/4096):
    s, F, f, b = solve(kappa, beta, h=h)
    i0 = int(round((b+0.5)/h))
    return bool(np.any((F-f)[i0:] < 0))

def sifting_limit(kappa, lo, hi, h=1.0/4096):
    for _ in range(30):
        mid = 0.5*(lo+hi)
        if crosses(kappa, mid, h): lo = mid
        else: hi = mid
    return hi

def J_of(s, F):
    t = np.linspace(1/16, 1/3, 400001)
    return np.trapezoid((1-3*t)/t*np.interp(8-16*t, s, F), t)

fails = 0
def check(name, ok, detail=""):
    global fails
    print(("  PASS  " if ok else "  FAIL  ") + name + ("   " + detail if detail else ""))
    if not ok: fails += 1

print("1. Calibration on the linear sieve (kappa = 1)")
s, F, f, b, A = normalised(1.0, 2.0)
i = lambda x: int(round(x*4096))
check("A_1 = 2 e^gamma", abs(A - 2*np.exp(np.euler_gamma)) < 1e-5, "A = %.7f" % A)
check("F_1(3.5) = 1.0651936", abs(F[i(3.5)] - 1.0651936) < 1e-6, "F = %.7f" % F[i(3.5)])
check("f_1(3.5) = 0.9325601", abs(f[i(3.5)] - 0.9325601) < 1e-6, "f = %.7f" % f[i(3.5)])
b1 = sifting_limit(1.0, 1.5, 2.5)
check("no-crossing threshold recovers beta_1 = 2", abs(b1-2.0) < 2e-3, "beta_1 = %.5f" % b1)

print("\n2. Dimension two")
b2 = sifting_limit(2.0, 4.0, 6.5)
print("     beta_2 (no-crossing threshold of this system) = %.5f" % b2)
vals = []
for h in (1/2048, 1/4096, 1/8192):
    s, F, f, bb, A = normalised(2.0, b2, h=h)
    f28 = f[int(round(8/h))]; J = J_of(s, F)
    vals.append((f28, J, 3*f28-2*J))
    print("     h = 1/%-5d   A_2 = %.4f   f_2(8) = %.6f   J = %.6f   3f-2J = %+.6f"
          % (1/h, A, f28, J, 3*f28-2*J))
spread = max(v[2] for v in vals) - min(v[2] for v in vals)
check("margin converged in step size", spread < 1e-3, "spread = %.2e" % spread)
f28, J, margin_ = vals[1]
margin = margin_
check("margin 3 f_2(8) - 2J is positive", margin > 0, "margin = %+.5f" % margin)

print("\n3. The two asserted numbers, tested for mutual consistency")
def at(beta):
    s, F, f, bb, A = normalised(2.0, beta)
    return f[i(8)], J_of(s, F)
lo, hi = b2, 7.0
for _ in range(40):
    m = 0.5*(lo+hi); (lo, hi) = (m, hi) if at(m)[0] > 0.870 else (lo, m)
bf = 0.5*(lo+hi); Jf = at(bf)[1]
lo, hi = b2, 7.0
for _ in range(40):
    m = 0.5*(lo+hi); (lo, hi) = (lo, m) if at(m)[1] > 1.269 else (m, hi)
bJ = 0.5*(lo+hi); ff = at(bJ)[0]
print("     f_2(8) = 0.870 belongs to beta = %.4f, where J = %.4f  -> margin %+.4f" % (bf, Jf, 3*0.870-2*Jf))
print("     J = 1.269      belongs to beta = %.4f, where f_2(8) = %.4f  -> margin %+.4f" % (bJ, ff, 3*ff-2*1.269))
print("     FINDING: no single solution gives both; they differ by %.2f in beta." % abs(bf-bJ))
print("              taken at face value, f_2(8) = 0.870 makes the margin NEGATIVE.")

print("\n4. How far the architecture reaches: sweep of the free parameters")
# Free parameters:  z = U^(1/w)  so the sifting ratio is s = theta*w
#                   y = U^(1/u)  so the Richert weight is (1 - u t)
#                   c            the weight budget,  w(b) = c - B(a) - B(a+2)
# Positivity of w(b) forces Omega <= c + u - 1, so a target r needs c + u = r + 1.
# theta is the exponent of the level of distribution D = U^theta (theta = 1/2 is
# free here: it is the interval length, no equidistribution hypothesis is used).
def _mk(beta):
    s, F, f, bb, A = normalised(2.0, beta)
    return (lambda x: np.interp(x, s, F)), (lambda x: np.interp(x, s, f))

def margin_of(Fi, fi, w, u, c, theta=0.5):
    if u >= w or theta*w - w/u <= 0.05: return -9e9
    t = np.linspace(1.0/w, 1.0/u, 3001)
    return c*fi(theta*w) - 2*np.trapezoid((1-u*t)/t*Fi(theta*w - w*t), t)

def best(Fi, fi, target, theta=0.5):
    b = (-9e9, 0, 0, 0)
    for w in np.arange(8.0, 60.01, 1.0):
        for u in np.arange(2.10, float(target), 0.05):
            m = margin_of(Fi, fi, w, u, target+1-u, theta)
            if m > b[0]: b = (m, w, u, target+1-u)
    return b

Fi, fi = _mk(b2)
m_his = margin_of(Fi, fi, 16, 3, 3)
check("the draft's own choice w=16,u=3,c=3 reproduces part 2", abs(m_his-margin_) < 1e-3,
      "margin = %+.4f" % m_his)
m5, w5, u5, c5 = best(Fi, fi, 5)
print("     Omega <= 5, best over (w,u):  w = %g, u = %.2f, c = %.2f  ->  margin %+.4f"
      % (w5, u5, c5, m5))
check("Omega <= 5 survives the optimisation", m5 > 0.5)
check("the draft's choice is near-optimal", m5 - m_his < 0.20, "gain only %+.4f" % (m5-m_his))
m4, w4, u4, c4 = best(Fi, fi, 4)
print("     Omega <= 4, best over (w,u):  w = %g, u = %.2f, c = %.2f  ->  margin %+.4f"
      % (w4, u4, c4, m4))
check("Omega <= 4 is NOT reached at beta_2 = %.5f" % b2, m4 < 0, "margin = %+.4f" % m4)

# beta = 4.2664 is quoted from memory as the DHR sifting limit for kappa = 2.
# IT HAS NOT BEEN CHECKED AGAINST A SOURCE.  Everything below depends on it.
BETA_DHR_UNVERIFIED = 4.2664
Fi2, fi2 = _mk(BETA_DHR_UNVERIFIED)
m4d = best(Fi2, fi2, 4)[0]
print("     Omega <= 4 at the (UNVERIFIED) DHR limit %.4f: margin %+.4f" % (BETA_DHR_UNVERIFIED, m4d))
check("Omega <= 4 is razor thin even there", 0 < m4d < 0.05, "margin = %+.4f" % m4d)

print("     level of distribution needed for Omega <= 4 at beta_2 = %.5f:" % b2)
prev = None
for th in (0.50, 0.55, 0.60, 0.65):
    mth = best(Fi, fi, 4, th)[0]
    print("        D = U^%.2f  ->  margin %+.4f" % (th, mth))
    if th == 0.55: cross55 = mth
check("Omega <= 4 turns positive between D = U^0.50 and U^0.55", m4 < 0 < cross55)

print("\nVerdict: at beta_2 = %.5f the margin is %+.5f, not the asserted +0.072;" % (b2, margin))
print("f_2(8) = %.5f (not 0.870) and J = %.5f (not 1.269)." % (f28, J))
print("\n%d of the checks failed." % fails)
sys.exit(0 if fails == 0 else 1)
