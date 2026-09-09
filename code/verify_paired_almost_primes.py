#!/usr/bin/env python3
"""Interval certificate for paired almost primes in intervals of length x^theta.

COVERS: the four weight coefficients C_r(theta; w, u) declared in [P12],
Proposition 2 and Theorem 1 -- it encloses the dimension-two DHR functions
F_2 and f_2 and returns a rigorous lower bound for each coefficient.

Proves C_r(theta; w, u) > 0 for three parameter sets, where

    C_r = (r+1-u) f_2(theta*w) - 2 * int_{1/w}^{1/u} (1/t - u) F_2(w(theta-t)) dt.

Inputs taken from the literature and NOT reproved here: the DHR dimension-two
system as stated in Kao, Section 4, Theorem 2; F_2 decreasing with F_2 >= 1;
f_2 increasing with f_2 <= 1; alpha_2 in [5.3576, 5.3578]; beta_2 in [4.2662, 4.2665]. The lower-bound
integral for f_2 starts at the grid node at or above BETA_HI, so no part of it
can fall below beta_2.
Everything else is computed with outward-rounded interval arithmetic and
monotone Riemann enclosures.  Standard library only.
"""
from decimal import Decimal as D, getcontext
import json, sys

COVERS = "[P12] Proposition 1: the four weight coefficients C_r(theta; w, u)"

getcontext().prec = 34

class I:
    __slots__ = ('lo', 'hi')
    def __init__(self, a, b=None):
        if isinstance(a, I):
            self.lo, self.hi = a.lo, a.hi
        else:
            self.lo = D(a); self.hi = D(a if b is None else b)
    @staticmethod
    def wrap(lo, hi):
        r = I(0); r.lo = lo.next_minus(); r.hi = hi.next_plus(); return r
    def __add__(a, b):
        b = I(b); return I.wrap(a.lo + b.lo, a.hi + b.hi)
    __radd__ = __add__
    def __neg__(a): return I(-a.hi, -a.lo)
    def __sub__(a, b): return a + -I(b)
    def __rsub__(a, b): return I(b) + -a
    def __mul__(a, b):
        b = I(b); v = [x*y for x in (a.lo, a.hi) for y in (b.lo, b.hi)]
        return I.wrap(min(v), max(v))
    __rmul__ = __mul__
    def __truediv__(a, b):
        b = I(b)
        assert not (b.lo <= 0 <= b.hi), 'division by an interval containing 0'
        v = [x/y for x in (a.lo, a.hi) for y in (b.lo, b.hi)]
        return I.wrap(min(v), max(v))
    def __rtruediv__(a, b): return I(b)/a
    def __pow__(a, n):
        r = I(1)
        for _ in range(n): r = r*a
        return r
    def ln(a):
        assert a.lo > 0
        return I.wrap(a.lo.ln(), a.hi.ln())
    def exp(a): return I.wrap(a.lo.exp(), a.hi.exp())
    def lst(a): return [str(a.lo), str(a.hi)]

# ---------------------------------------------------------------- constants
gamma = I('0.5772156649015328606065120900824024310',
          '0.5772156649015328606065120900824024311')
E2 = (2*gamma).exp()                       # e^{2 gamma}

H = D('0.0002')                             # grid step (exact terminating)
SMAX = D('10')
N = int(SMAX/H) + 1
def idx(x): return int(D(x)/H)             # largest grid node at or below x
def idx_up(x):                             # smallest grid node at or above x
    k = idx(x)
    return k if D(k)*H == D(x) else k + 1
S = [I(D(i)*H) for i in range(N)]

ALPHA_LO = D('5.3576')                     # <= alpha_2
ALPHA_HI = D('5.3578')                     # >= alpha_2
BETA_LO  = D('4.2662')                     # <= beta_2
BETA_HI  = D('4.2665')                     # >= beta_2

# ------------------------------------------------------- sigma_2 enclosures
# sigma_2(s) = s^2/(8 e^{2g})           0 < s <= 2
# sigma_2(s) = (2(s-1)^2 - s^2 log(s/2))/(4 e^{2g})   2 < s <= 4
# s^{-2} sigma_2(s) = sigma_2(4)/16 - 2 int_4^s sigma_2(t-2)/t^3 dt   s > 4
slo = [D(0)]*N; shi = [D(0)]*N
for i in range(1, N):
    s = S[i]
    if s.hi <= 2:
        v = s**2/(8*E2)
    elif s.hi <= 4:
        v = (2*(s-1)**2 - s**2*(s/2).ln())/(4*E2)
    else:
        break
    slo[i], shi[i] = v.lo, v.hi
i4 = idx('4'); i2 = idx('2'); iAlo = idx(ALPHA_LO); iAhi = idx(ALPHA_HI)
Alo = I(0); Ahi = I(0)                     # enclosures of the integral
for i in range(i4+1, iAhi+1):
    a, b = S[i-1], S[i]
    # sigma increasing => integrand sigma(t-2)/t^3 in [sig(a-2)/b^3, sig(b-2)/a^3]
    Alo = Alo + I(slo[i-1-i2])*H/b**3
    Ahi = Ahi + I(shi[i-i2])*H/a**3
    lo = (b**2*(I(slo[i4])/16 - 2*Ahi)).lo
    hi = (b**2*(I(shi[i4])/16 - 2*Alo)).hi
    assert lo > 0, 'sigma enclosure lost positivity at s=%s' % b.lo
    slo[i], shi[i] = lo, hi

# F_2 = 1/sigma_2 on (0, alpha_2];  valid on (0, ALPHA_LO] for sure
Flo = [D(0)]*N; Fhi = [D(0)]*N
flo = [D(0)]*N; fhi = [D(0)]*N
for i in range(1, iAlo+1):
    t = I(1)/I(slo[i], shi[i])
    Flo[i] = max(t.lo, D(1))               # F_2 >= 1 everywhere
    Fhi[i] = t.hi
Fhi[0] = D('1e30')

# ------------------------------------------------------------- the march
# s^2 f_2(s)  = int_{beta_2}^s 2t F_2(t-1) dt          (s > beta_2)
# s^2 F_2(s) is increasing everywhere; for s >= ALPHA_HI,
# s^2 F_2(s) <= ALPHA_HI^2 F_2(ALPHA_LO) + int_{ALPHA_LO}^s 2t f_2(t-1) dt
# s^2 F_2(s) >= ALPHA_LO^2 F_2(ALPHA_LO) + int_{ALPHA_HI}^s 2t f_2(t-1) dt
ibL = idx(BETA_LO); ibH = idx_up(BETA_HI); i1 = idx('1')
flo_acc = I(0); fhi_acc = I(0)
Flo_acc = I(ALPHA_LO)**2*I(Flo[iAlo])
Fhi_acc = I(ALPHA_HI)**2*I(Fhi[iAlo])
for i in range(1, N):
    a, b = S[i-1], S[i]
    d = b**2 - a**2
    if i > ibH:                            # lower bound for f: start late, F at b-1
        flo_acc = flo_acc + d*I(Flo[i-i1])
        v = (flo_acc/b**2).lo
        flo[i] = max(D(0), min(v, D(1)))
    if i > ibL:                            # upper bound for f: start early, F at a-1
        fhi_acc = fhi_acc + d*I(Fhi[max(i-i1-1, 0)])
        fhi[i] = min((fhi_acc/b**2).hi, D(1))
    if i > iAhi:                           # F above alpha_2
        Flo_acc = Flo_acc + d*I(flo[max(i-i1-1, 0)])
        Fhi_acc = Fhi_acc + d*I(fhi[i-i1])
        Flo[i] = max(D(1), (Flo_acc/b**2).lo, )
        Fhi[i] = min((Fhi_acc/b**2).hi, Fhi[i-1])
    elif i > iAlo:                         # the sliver: F decreasing only
        Flo[i] = D(1); Fhi[i] = Fhi[iAlo]

def F_up(x):                               # x an interval; F decreasing -> use left grid pt
    k = int(x.lo/H)
    assert 0 < k < N, 'argument %s outside the grid' % x.lo
    return I(Fhi[k])
def f_lo(x):
    k = int(x.lo/H)
    assert 0 < k < N
    return I(flo[k])

# ------------------------------------------------------------ the ladder
CASES = [('square window, Omega<=5', 5, D('0.5'), D('16'), D('3')),
         ('Omega<=5', 5, D('0.38'), D('23.43'),  D('3.376')),
         ('Omega<=4', 4, D('0.513'), D('16.42405'), D('2.79166')),
         ('Omega<=3', 3, D('0.78'), D('10.028'), D('2.257'))]
M = 20000
# the conservative bounds quoted in [P12, Prop. 1]; the run must clear each
CLAIM = {'square window, Omega<=5': D('0.91558'), 'Omega<=5': D('0.08793'),
         'Omega<=4': D('0.00621'), 'Omega<=3': D('0.05351')}
out = {'grid_step': str(H), 'alpha_2_bracket': [str(ALPHA_LO), str(ALPHA_HI)],
       'beta_2_bracket': [str(BETA_LO), str(BETA_HI)],
       'F_2_samples': {}, 'f_2_samples': {}, 'cases': []}
for x in ['4', '5', '5.356', '6', '7', '8', '9']:
    out['F_2_samples'][x] = [str(Flo[idx(x)]), str(Fhi[idx(x)])]
    out['f_2_samples'][x] = [str(flo[idx(x)]), str(fhi[idx(x)])]

ok = True
for name, r, th, w, u in CASES:
    # 1/w and 1/u are not exact decimals: enclose them, and cover [1/w, 1/u]
    # from the outside so no part of the integral is omitted.
    AL = I(1)/I(w)
    BE = I(1)/I(u)
    sD = I(th)*I(w)
    eta = I(r+1) - I(u)
    lo, hi = AL.lo, BE.hi
    step = I(hi - lo)/M
    J = I(0)
    for j in range(M):
        a = I(lo) + j*step                 # interval enclosing the left node
        b = a + step                       # interval enclosing the right node
        wt = I(1)/I(a.lo) - I(u)           # 1/t - u decreases in t: largest at t = a
        arg = I(w)*(I(th) - I(b.hi))       # the F_2 argument is smallest at t = b
        J = J + I(b.hi - a.lo)*wt*F_up(arg)
    C = eta*f_lo(sD) - 2*J
    good = C.lo > CLAIM[name]
    ok = ok and good
    out['cases'].append({'target': name, 'r': r, 'theta': str(th), 'w': str(w),
                         'u': str(u), 's_D': sD.lst(), 'eta': eta.lst(),
                         'f_2(s_D)_lower': str(f_lo(sD).lo), 'J_upper': str(J.hi),
                         'C_lower': str(C.lo), 'positive': good})
    print('%-9s r=%d theta=%s w=%s u=%s : f_2(%s) >= %s , J <= %s , C >= %s  %s'
          % (name, r, th, w, u, str(sD.lo)[:6], str(f_lo(sD).lo)[:8], str(J.hi)[:8],
             str(C.lo)[:9], 'OK' if good else 'FAILED'), file=sys.stderr)
    assert good, 'coefficient not certified positive for ' + name

print(json.dumps(out, indent=1))
sys.exit(0 if ok else 1)
