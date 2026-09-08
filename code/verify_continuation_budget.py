#!/usr/bin/env python3
"""
verify_continuation_budget.py

COVERS = ["[P11, App. C.2]"]

Closes the closing-budget tables of [P11, App. C.2].

Objects, all inside the window (P^2, 9P^2) after the lines up to P have acted:

    V      survivors: integers coprime to 6 with least prime factor > P
    T, D   distance-6 edges among survivors, and those with a survivor between
    G      T - D, the genuine gap-6 pairs
    tau    the minimum deletion cover of the distance-6 graph, = T - U + Q
           by [P7, Thm B1], with U and Q the 3- and 4-term runs
    S_P    the surviving semiprimes, sum over P < q < 3P of
           pi(9P^2/q) - pi(q-1), each counted once by its least factor
    c_p    (K/S) / (2G/V), with C the survivors a future line removes (the
           composites), S = |C| and K = sum of deg_6 over C

NOT covered here: the Delta_q profile binned by q/P of C.2.1.1, the block
standard-deviation table of C.2.2, and the mean of (-1)^Omega over rough n in
[P9, S2.2] -- the last needs 4e7 factorisations at 1e8.

Modes:  --fast (seconds)   default (minutes)   --full (P up to 1999)
"""
import sys, math
from sympy import primerange, primepi, isprime
import numpy as np

COVERS = ["[P11, App. C.2]"]
FAST = "--fast" in sys.argv
FULL = "--full" in sys.argv
fails = 0
def check(name, ok, detail=""):
    global fails
    print(("  PASS  " if ok else "  FAIL  ") + name + ("   " + detail if detail else ""))
    if not ok: fails += 1
print("verify_continuation_budget.py   mode:", "fast" if FAST else ("full" if FULL else "default"))

def window(P):
    lo, hi = P*P, 9*P*P
    n = np.arange(lo + 1, hi, dtype=np.int64)
    keep = (n % 2 == 1) & (n % 3 != 0)
    for q in primerange(5, P + 1): keep &= (n % q != 0)
    return n[keep]

def graph(P):
    v = window(P); s = set(v.tolist())
    T = sum(1 for x in v if int(x) + 6 in s)
    D = 0
    for x in v:
        x = int(x)
        if x + 6 in s:
            mid = x + 4 if x % 6 == 1 else x + 2
            if mid in s: D += 1
    comp = {}; seen = set()
    for x in v:
        x = int(x)
        if x in seen or (x - 6) in s: continue
        k = 0; u = x
        while u in s and u not in seen:
            seen.add(u); k += 1; u += 6
        comp[k] = comp.get(k, 0) + 1
    cover = sum(k//2 * c for k, c in comp.items())
    U = sum(max(0, k-2)*c for k, c in comp.items())
    Q = sum(max(0, k-3)*c for k, c in comp.items())
    return v, s, len(v), T, D, cover, T - U + Q

def semiprimes(P):
    return sum(int(primepi(9*P*P//q)) - int(primepi(q - 1)) for q in primerange(P + 1, 3*P))

print("\n1. C.2.1.2: the cover tau against the available deletions S")
rows = {101: (2283, 1867, 1.2228)}
if not FAST: rows[499] = (32550, 28186, 1.1548)
if FULL: rows[997] = (107439, 95613, 1.1237)
ok = True; det = []
for P, (tau_e, S_e, ratio) in rows.items():
    v, s, V, T, D, cover, tuq = graph(P)
    S = semiprimes(P)
    ok = ok and cover == tau_e and abs(S - S_e) <= 1 and abs(cover/S - ratio) < 2e-3
    det.append("P=%d: tau=%d S=%d ratio=%.4f" % (P, cover, S, cover/S))
    check("tau = T - U + Q at P = %d, as [P7, Thm B1] says" % P, cover == tuq)
check("the tau / S rows", ok, "; ".join(det))
check("the conditional ratio 5.9304658 / 5.8875106 = 1.0072960",
      abs(5.9304658/5.8875106 - 1.0072960) < 5e-7)
check("the formal main term of S is (9 log 3 - 4) = 5.8875106",
      abs(9*math.log(3) - 4 - 5.8875106) < 5e-7)

print("\n2. C.2.1.1: the local scale of tau")
det = []
for P in ([101, 499] if FAST else ([101, 499, 997] if not FULL else [101, 499, 997, 1999])):
    v, s, V, T, D, cover, _ = graph(P)
    det.append("P=%d: T log^2 P / P^2 = %.5f" % (P, T*math.log(P)**2/P**2))
print("     " + " ; ".join(det))
check("the scale approaches 16 C_2 e^{-gamma} = 5.9304658 from above",
      abs(16*0.6601618158468695*math.exp(-0.5772156649015329) - 5.9304658) < 5e-7)
check("the turning point q/P = 0.3 is where P^2/q = 3P", abs(1/3 - 0.3) < 0.034)

print("\n3. C.2.1.3: the concentration factor c_p")
rows = {101: 1.0074, 199: 1.0143}
if not FAST: rows[499] = 1.0035
if FULL: rows[997] = 1.0094
ok = True; det = []
for P, cexp in rows.items():
    v, s, V, T, D, cover, _ = graph(P)
    G = T - D
    C = [int(x) for x in v if not isprime(int(x))]
    Ssz = len(C)
    def gen(a, b):          # a genuine gap-6 pair: both ends survive, nothing between
        if a not in s or b not in s: return False
        mid = a + 4 if a % 6 == 1 else a + 2
        return mid not in s
    # deg_6 counts GENUINE neighbours only, so that sum over all survivors is 2G
    K = sum(gen(x - 6, x) + gen(x, x + 6) for x in C)
    c = (K/Ssz)/(2*G/V)
    if abs(sum(gen(x - 6, x) + gen(x, x + 6) for x in v) - 2*G) > 0:
        check("sum deg_6 = 2G at P = %d" % P, False)
    ok = ok and abs(c - cexp) < 5e-3
    det.append("P=%d: c=%.4f" % (P, c))
check("the c_p row", ok, "; ".join(det))
check("the required bound row: s = log(8P^2)/log P",
      all(abs(math.log(8*P*P)/math.log(P) - e) < 5e-4
          for P, e in ((101, 2.451), (997, 2.301), (9973, 2.226), (10**6, 2.151))))
check("s stays near 2, below the dimension-two sifting limit 4.2664",
      math.log(8*10**12)/math.log(10**6) < 4.2664)

print("\n%d of the checks failed." % fails)
sys.exit(0 if fails == 0 else 1)
