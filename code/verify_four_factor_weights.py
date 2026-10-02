#!/usr/bin/env python3
"""Certificates for the overlap weight and the total-seven weight of [P12, §5-§6].

COVERS: [P12] Lemma 3 (exact admissibility of the overlap weight), Proposition 2
(its coefficient at theta = 1/2 and theta = 0.499) and Proposition 3 (the
coefficient of the total-seven weight at the same two lengths).

Part 1 is exact: Fraction arithmetic over the vertices of every bilinear piece of
the overlap weight, as in the proof of [P12, Lemma 3].  Part 2 encloses the dimension-two DHR
functions F_2 and f_2 exactly as code/verify_paired_almost_primes.py does, on a
finer grid (step 0.0001), and returns rigorous lower bounds for

    C_*(theta) = (5-u) f_2(w theta) - 2 int_{1/w}^{1/u} (1/t-u) F_2(w(theta-t)) dt
                 + kappa int int h(t)h(v)/(tv) f_2(w(theta-t-v)) dt dv,

    C_7(theta) = (8-2u') f_2(w' theta) - 2 int_{1/w'}^{1/u'} (1/t-u') F_2(w'(theta-t)) dt.

Inputs taken from the literature and NOT reproved: the DHR dimension-two system
(Kao, Section 4, Theorem 2); F_2 decreasing, f_2 increasing; alpha_2 in
[5.3576, 5.3578], beta_2 in [4.2662, 4.2665].  Standard library only.
Exits non-zero if any claimed bound fails.

    python3 code/verify_four_factor_weights.py
"""
import sys, json
from fractions import Fraction as Q

COVERS = "[P12] Lemma 3, Proposition 2 and Proposition 3: the overlap weight and the total-seven weight"

from decimal import Decimal as D, getcontext
import json, sys


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

H = D('0.0001')                             # grid step (exact terminating)
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



# ===================================================== Part 1: Lemma 3, exact
w, u, A, L, kappa = map(Q, ('18.48', '2.7253', '0.422', '1.5972', '0.3345'))
eta = 5 - u
assert A >= 0 and L >= 0

def boundary(j, bad=False):
    """Vertices (x, H_j(x)) of the admissible x-range for j distinct middle primes."""
    if j == 0:
        return [] if bad else [(Q(0), Q(0))]
    lo = max(Q(0), j - u); hi = j*(1 - u/w)
    if bad: lo = max(lo, eta)
    if lo > hi: return []
    kink = j*(u*A + L)/(u + L)
    xs = sorted(set([lo, hi] + ([kink] if lo <= kink <= hi else [])))
    return [(x, min(x, j*A + L*(j - x)/u)) for x in xs]

JMAX = int(w)                                  # at most 18 middle primes
allv = [p for j in range(JMAX + 1) for p in boundary(j)]
badv = [p for j in range(JMAX + 1) for p in boundary(j, True)]
worst = max(eta - x - y + kappa*C*E for x, C in badv for y, E in allv)
ratio = min((x + y - eta)/(C*E) for x, C in badv for y, E in allv if C*E > 0)
gmax = max(eta - x - y + kappa*C*E for x, C in allv for y, E in allv)
ok = worst == 0 and kappa <= ratio and gmax == eta and kappa*eta < 1
print('Lemma 3: bad-region maximum %s, largest admissible kappa %s = %.9f, global maximum %s  %s'
      % (worst, ratio, float(ratio), gmax, 'OK' if ok else 'FAILED'), file=sys.stderr)
assert ok, 'Lemma 3 fails'

# ================================================ Part 2: Propositions 2 and 3
def upper_linear(th, wd, ud, M):
    """Upper Riemann bound of 2 int_{1/w}^{1/u} (1/t-u) F_2(w(theta-t)) dt."""
    left = (I(1)/I(wd)).lo; right = (I(1)/I(ud)).hi
    step = I(right - left)/M; J = I(0)
    for k in range(M):
        a = I(left) + k*step; b = a + step
        J = J + I(b.hi - a.lo)*(I(1)/I(a.lo) - I(ud))*F_up(I(wd)*(I(th) - I(b.hi)))
    return 2*J

def lower_overlap(th, wd, ud, Ad, Ld, delta):
    """Lower Riemann bound of int int h(t)h(v)/(tv) f_2(w(theta-t-v)) on an inner grid."""
    AL = I(1)/I(wd); BE = I(1)/I(ud)
    first = int(AL.hi/delta) + 1; last = int(BE.lo/delta)
    phi = []
    for j in range(first + 1, last + 1):
        t = D(j)*delta
        a = I(1)/I(t) - I(ud); b = I(Ad)/I(t) + I(Ld)
        phi.append(I(max(D(0), min(a.lo, b.lo))))
    J = I(0)
    for i, pi in enumerate(phi):
        ti = D(first + 1 + i)*delta
        for j in range(i, len(phi)):
            tj = D(first + 1 + j)*delta
            arg = I(wd)*(I(th) - I(ti) - I(tj))
            if arg.lo <= 0: continue
            node = int(arg.lo/H)
            if node <= 0 or flo[node] <= 0: continue
            v = pi*phi[j]*I(flo[node])*I(delta)**2
            J = J + (v if i == j else 2*v)
    return J

out = {'grid_step': str(H), 'lemma3': {'bad_max': str(worst), 'kappa_max': str(ratio),
       'global_max': str(gmax)}, 'prop2': [], 'prop3': []}
Wd, Ud, Ad, Ld, Kd = map(D, ('18.48', '2.7253', '0.422', '1.5972', '0.3345'))
CLAIM2 = {'0.5': D('0.0064'), '0.499': D('0.0017')}
for th in ('0.5', '0.499'):
    lin = I(5 - Ud)*f_lo(I(Wd)*I(D(th))) - upper_linear(D(th), Wd, Ud, 50000)
    J = lower_overlap(D(th), Wd, Ud, Ad, Ld, D('0.00018'))
    C = lin + I(Kd)*J
    good = C.lo > CLAIM2[th]; ok = ok and good
    out['prop2'].append({'theta': th, 'linear_lower': str(lin.lo), 'overlap_integral_lower': str(J.lo),
                         'C_star_lower': str(C.lo), 'claimed': str(CLAIM2[th])})
    print('Prop 2, theta=%s: linear >= %s, J >= %s, C_* >= %s  %s'
          % (th, str(lin.lo)[:10], str(J.lo)[:9], str(C.lo)[:10], 'OK' if good else 'FAILED'), file=sys.stderr)

W7, U7 = D('18.75'), D('2.38')
CLAIM3 = {'0.5': D('0.42'), '0.499': D('0.41')}
for th in ('0.5', '0.499'):
    assert D(1)/U7 < D(th) - D(1)/W7
    C = I(8 - 2*U7)*f_lo(I(W7)*I(D(th))) - upper_linear(D(th), W7, U7, 20000)
    good = C.lo > CLAIM3[th]; ok = ok and good
    out['prop3'].append({'theta': th, 'w': str(W7), 'u': str(U7), 'C_7_lower': str(C.lo),
                         'claimed': str(CLAIM3[th])})
    print('Prop 3, theta=%s: C_7 >= %s  %s' % (th, str(C.lo)[:10], 'OK' if good else 'FAILED'),
          file=sys.stderr)

print(json.dumps(out, indent=1))
sys.exit(0 if ok else 1)
