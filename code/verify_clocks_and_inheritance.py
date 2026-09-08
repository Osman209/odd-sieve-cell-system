#!/usr/bin/env python3
"""
verify_clocks_and_inheritance.py  --  generator for Paper 7,
"Clocks and Inheritance / Primality as a Zero-Test".

Covers Theorem 1 with Corollaries 1-2, Theorem 2 with the worked example at
p = 11, Theorem 3, Theorem 4, Proposition 1, Theorem 5, Corollary 3, and
Appendix B (Theorems B1-B3, Corollary B1) with both of its tables.

Clock convention, from [P4, (2.2)]:  phi_q(n) = ((q-n)/2) mod q  for odd q, n.

One reading worth recording: the window of Proposition 1 holds 1540 cells, and
the "-1" in N_empty = 4aB - 1 is the centre cell at (p+1)^2, which the census
excludes.  With it in, N_empty is 540 and the identity misses by one.

Modes:  --fast (seconds)   default (minutes)
"""

COVERS = ["[P7, S2]", "[P7, S3]", "[P7, App. A]"]

import sys, math
from sympy import isprime, primerange
import numpy as np

FAST = "--fast" in sys.argv
def rng(fast, default): return fast if FAST else default
fails = 0
def check(name, ok, detail=""):
    global fails
    print(("  PASS  " if ok else "  FAIL  ") + name + ("   " + detail if detail else ""))
    if not ok: fails += 1

def phi(q, n): return ((q - n) // 2) % q
def inv6(q): return pow(6, -1, q)
print("verify_clocks_and_inheritance.py  (Paper 7)   mode:", "fast" if FAST else "default")

# ------------------------------------------------------------------ Theorem 1
print("\n1. Theorem 1: the shift law, and primality as a zero-test")
n = bad = 0
for q in primerange(3, rng(200, 400)):
    for p in range(3, rng(400, 1200), 2):
        n += 1
        if phi(q, p + 2) != (phi(q, p) - 1) % q: bad += 1
check("phi_q(p+2) = phi_q(p) - 1 (mod q) for every old line", bad == 0, "%d instances" % n)
check("the insertion rule phi_p(p+2) = p-1", all(phi(p, p+2) == p-1 for p in primerange(3, 500)))
bad = 0
for p in range(5, rng(601, 2000), 2):
    zero = any(phi(q, p) % q == 0 for q in primerange(3, p))
    if zero != (not isprime(p)): bad += 1
check("Corollary 1: p is composite iff some old clock reads 0 at its birth", bad == 0)
seq = [phi(3, m) for m in (6*7-1, 6*7+1, 6*7+3)]
check("Corollary 2: the L_3 clock cycles 2 -> 1 -> 0", seq == [2, 1, 0], "seq %s" % seq)

# ------------------------------------------------------------------ Theorem 2
print("\n2. Theorem 2: surviving cofactors are prime")
bad = []
for p in (11, 13, 17, 101, 499):
    for t in range(p + 2, 9*p + 1, 2):
        if all(t % r for r in primerange(3, p)) and not isprime(t): bad.append((p, t))
check("every cofactor p < t <= 9p surviving all lines below p is prime", not bad,
      "checked p = 11,13,17,101,499")
p = 11
W = [ (2*(j+1)**2)//p - (2*j*j)//p for j in range(p) ]
H = [w + 2 for w in W]
kap = [0]
for h in H[:-1] + [H[-1]]: kap.append(kap[-1] + h)
J = []
for j in range(p):
    J.append(sum(1 for i in range(kap[j], kap[j+1]) if isprime(13 + 2*i)))
check("worked example at p = 11: kappa_j",
      kap[:12] == [0,2,4,7,10,14,18,22,27,32,38,44], "%s" % kap[:12])
check("worked example at p = 11: H_j = W_j + 2", H == [2,2,3,3,4,4,4,5,5,6,6], "%s" % H)
check("worked example at p = 11: clocks phi_3, phi_5, phi_7 = 2, 2, 5",
      [phi(3,p), phi(5,p), phi(7,p)] == [2, 2, 5])
check("worked example at p = 11: J_j", J == [1,2,1,2,1,3,1,2,3,2,2], "%s" % J)

# ------------------------------------------------------------------ Theorem 3
print("\n3. Theorem 3: a row reads primality off originality")
inst = bad = 0
for p in primerange(3, rng(60, 400)):
    for t in range(p, p*p, 2):
        inst += 1
        original = all(t % r for r in primerange(3, p))
        if original != isprime(t): bad += 1
check("p(p+2j) is original below p iff p+2j is prime", bad == 0, "%d instances" % inst)
check("the twin test sits at (p+1)^2 - 1", all(p*(p+2) == (p+1)**2 - 1 for p in (5,11,17,29)))

# ------------------------------------------------------------------ Theorem 4
print("\n4. Theorem 4: the sector inheritance law B(M+6Q) = B(M) + 12S")
def B(r, lines):
    a0 = 6*r*(r+1) + 2; a1 = 6*(r+1)*(r+2) + 2
    b = np.arange(a0, a1, dtype=np.int64)
    keep = np.ones(b.size, dtype=bool)
    for q in lines:
        c = inv6(q); keep &= (b % q != c % q) & (b % q != (-c) % q)
    return int(keep.sum())
ok = True; det = []
for lines in ([5], [5,7], [5,7,11]):
    Q = math.prod(lines); S = math.prod(q-2 for q in lines)
    good = all(B(r + Q, lines) - B(r, lines) == 12*S for r in range(1, rng(6, 20)))
    det.append("%s: 12S = %d %s" % (lines, 12*S, "ok" if good else "FAILED"))
    ok = ok and good
check("the law is exact for the three line sets", ok, "; ".join(det))

# --------------------------------------------------------------- Proposition 1
print("\n5. Proposition 1: a window synchronised with its lines")
p = 2309; Sset = [5, 7, 11]; P = math.prod(Sset)
A = math.prod(r-1 for r in Sset); Bb = math.prod(r-2 for r in Sset); a = (p+1)//(6*P)
lo = (p*p + 1)//6 + (1 if (p*p+1) % 6 else 0); hi = ((p+2)**2 - 1)//6
cnt = {"n":0, "L":0, "R":0, "B":0}
centre = (p+1)**2 // 6        # the -1 in N_empty: the centre cell is not counted
for b in range(lo, hi+1):
    if b == centre: continue
    l = any((6*b-1) % r == 0 for r in Sset); rr = any((6*b+1) % r == 0 for r in Sset)
    cnt["B" if (l and rr) else ("L" if l else ("R" if rr else "n"))] += 1
tot = sum(cnt.values())
check("the direct census of the window matches the four exact counts",
      (cnt["n"], cnt["L"], cnt["R"], cnt["B"]) == (4*a*Bb-1, 4*a*(A-Bb), 4*a*(A-Bb), 4*a*(P-2*A+Bb)),
      "%d cells (centre cell excluded): %d + %d + %d + %d"
      % (tot, cnt["n"], cnt["L"], cnt["R"], cnt["B"]))

# ------------------------------------------------------------------ Theorem 5
print("\n6. Theorem 5 and Corollary 3: the capacity of one new line")
Q = 385
cap = {}
for q in primerange(13, 102):
    c = inv6(q); best = 0
    for x in range(q):
        best = max(best, sum(1 for t in range(12) if (x + t*Q) % q in (c % q, (-c) % q)))
    D = pow(3*Q, -1, q); d = min(D, q-D); cap[q] = (best, d)
check("a line q > 11 closes at most two copies of any family",
      all(b <= 2 for b, _ in cap.values()))
check("capacity is two exactly when d_q <= 11",
      all((b == 2) == (d <= 11) for b, d in cap.values()),
      "d_13 = %d, d_17 = %d, d_101 = %d" % (cap[13][1], cap[17][1], cap[101][1]))
thr = 33*Q + 1
bad = [q for q in primerange(13, rng(3000, 20000))
       if q > thr and min(pow(3*Q,-1,q), q-pow(3*Q,-1,q)) <= 11]
check("every q > 33Q+1 = %d closes at most one copy" % thr, not bad)

# ---------------------------------------------------------------- Appendix B.1
print("\n7. Appendix B: the distance-6 closing budget")
def cycle_graph(lines):
    Qp = math.prod(lines); L = 6*Qp
    surv = np.zeros(L, dtype=bool)
    x = np.arange(L)
    ok = ((x % 6 == 1) | (x % 6 == 5))
    for q in lines: ok &= (x % q != 0)
    surv[ok] = True
    idx = np.nonzero(surv)[0]
    nxt = surv[(idx + 6) % L]
    T = int(nxt.sum())
    mid = np.where(idx % 6 == 1, idx + 4, idx + 2)
    D = int((nxt & surv[mid % L]).sum())
    comp = {}
    seen = np.zeros(L, dtype=bool)
    for v in idx:
        if seen[v] or surv[(v - 6) % L]: continue
        k = 0; u = v
        while surv[u % L] and not seen[u % L]:
            seen[u % L] = True; k += 1; u += 6
        comp[k] = comp.get(k, 0) + 1
    return int(surv.sum()), T, D, comp
rows = {}
for lines in ([5], [5,7], [5,7,11], [5,7,11,13]):
    rows[tuple(lines)] = cycle_graph(lines)
exp_c = {(5,7): {1:4,2:4,3:4,4:6}, (5,7,11): {1:68,2:56,3:44,4:42},
         (5,7,11,13): {1:1100,2:788,3:524,4:378}}
ok = True
for k, c in exp_c.items():
    V, T, D, comp = rows[k]
    cover = sum(v//2 * n for v, n in comp.items())
    U = sum(max(0, v-2)*n for v, n in comp.items())
    Q4 = sum(max(0, v-3)*n for v, n in comp.items())
    ok = ok and comp == c and cover == T - U + Q4
check("Theorem B1: the component census and tau = T - U + Q", ok,
      "{5,7} cover = %d" % sum(v//2*n for v, n in rows[(5,7)][3].items()))
exp_t = {(5,): (8,6,4,2), (5,7): (48,30,16,14), (5,7,11): (480,270,128,142),
         (5,7,11,13): (5760,2970,1280,1690)}
ok = all((rows[k][0], rows[k][1], rows[k][2], rows[k][1]-rows[k][2]) == v
         for k, v in exp_t.items())
check("the (V, T, D, G) table is reproduced", ok,
      "{5,7,11,13} -> %s" % (str((rows[(5,7,11,13)][0], rows[(5,7,11,13)][1],
                                  rows[(5,7,11,13)][2],
                                  rows[(5,7,11,13)][1]-rows[(5,7,11,13)][2]))))
seq = [(5,), (5,7), (5,7,11), (5,7,11,13)]
ok = True
for i in range(len(seq)-1):
    r = seq[i+1][-1]
    V, T, D, _ = rows[seq[i]]; V2, T2, D2, _ = rows[seq[i+1]]
    ok = ok and T2 == (r-2)*T and D2 == (r-3)*D and (T2-D2) == (r-2)*(T-D) + D
check("Theorem B2: T' = (r-2)T, D' = (r-3)D, G' = (r-2)G + D", ok)
ok = True
for pp, rho in [(23,0.4358),(53,0.3607),(101,0.3151),(199,0.2746),(499,0.2367),(997,0.2138)]:
    R = math.prod((s-2)/(s-1) for s in primerange(5, pp+1))
    ok = ok and abs(R - rho) < 5e-5
check("Corollary B1: T/V = rho_p at the six sample p", ok)
ok = True
for pp, th in [(23,0.3606),(53,0.2967),(101,0.2588),(199,0.2253),(499,0.1941),(997,0.1753)]:
    Th = (2/3)*math.prod((s-3)/(s-2) for s in primerange(7, pp+1))
    ok = ok and abs(Th - th) < 5e-5
check("Corollary B1: D/T = theta_p at the six sample p", ok)
V, T, D, _ = rows[(5,7,11)]
check("and the two ratios agree with the cycle counts at p = 11",
      abs(T/V - math.prod((s-2)/(s-1) for s in primerange(5,12))) < 1e-12 and
      abs(D/T - (2/3)*math.prod((s-3)/(s-2) for s in primerange(7,12))) < 1e-12)

# ---------------------------------------------------------------- Theorem B3
print("\n8. Theorem B3: tail compression")
bad = []
for P in (243, 251, 401):
    for q in primerange(P//3 + 1, P):
        for x in range(((P*P)//q + 1)*q, 9*P*P, q):
            if x % 2 == 0: continue
            r = x // q
            if r < q: continue
            if all(x % s for s in primerange(3, q)) and not isprime(r): bad.append((P, q, x))
check("for P >= 243 and P/3 < q < P every new strike is q times a prime", not bad)

print("\n%d of the checks failed." % fails)
sys.exit(0 if fails == 0 else 1)
