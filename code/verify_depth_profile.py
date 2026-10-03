#!/usr/bin/env python3
"""
verify_depth_profile.py

COVERS = ["[P4, S3.2]"]

Where the deficit T - M of [P4, S3.2] comes from, by line depth, written
2026-10-02.  Sectors and symbols as in verify_weighted_l2.py: every integer
sector (n^2,(n+1)^2), lines p <= n, P(n) = prod_{5<=p<=n}(1-2/p).  Each pair
(sector n, line p) gives the term

    c(n,p) = - P(n) eps_p(n) / P(p),      sum over all (n,p) = T - M exactly,

and the term is put in a bin by the depth a = log p / log n of the line in
its own sector.  For a single sector the same telescoping gives

    sum_{p <= n^a} c(n,p) = P(n) ( N_z(n)/P(z) - C(n) ),   z = n^a,

with N_z(n) the cells surviving the lines up to z.  So the cumulative curve
over a <= a0, divided by M, measures how far the survivors at the cut n^a sit
from the sieve product.  It is compared with

    (e^gamma omega(2/a0))^2 - 1,      omega = Buchstab's function,

which is what the curve would be if the two ends of a cell behaved like
independent integers free of primes below n^a.  That comparison model is a
heuristic; at a0 = 1 it is the Hardy-Littlewood value e^{2 gamma}/4 - 1.
Nothing here proves it.

What it checks: the identity (bins sum to T - M); omega(2) = 1/2,
omega(3) = (1+log 2)/3; the largest gap between measured and model curves;
that the cumulative value is near zero up to a = 0.5; and the printed
values of [P4, S3.2].

Modes: --fast (U = 10000)   default (U = 30000, ~10 s)   --full (U = 100000)
"""
import sys, math
import numpy as np
from sympy import primerange

COVERS = ["[P4, S3.2]"]
FAST = "--fast" in sys.argv
FULL = "--full" in sys.argv
fails = 0
def check(name, ok, detail=""):
    global fails
    print(("  PASS  " if ok else "  FAIL  ") + name + ("   " + detail if detail else ""))
    if not ok: fails += 1

G = 0.5772156649015329
CAP = 100000 if FULL else (10000 if FAST else 30000)
NB = 20
# printed in [P4, S3.2] at U = 100000 (a0 -> measured cumulative / M); gap bound per mode
PRINTED = {0.5: -0.00007, 0.7: 0.01830, 0.8: 0.00204, 1.0: -0.20627}
GAP = {10000: 0.004, 30000: 0.002, 100000: 0.001}[CAP]

def buchstab(umax=40.0, h=1e-4):
    u = np.arange(1.0, umax + h, h); w = np.empty_like(u); kk = int(round(1 / h))
    w[:kk + 1] = 1 / u[:kk + 1]
    F = u * w
    for i in range(kk + 1, len(u)):
        F[i] = F[i - 1] + h * 0.5 * (w[i - kk - 1] + w[i - kk]); w[i] = F[i] / u[i]
    return lambda x: float(np.interp(x, u, w))
om = buchstab()
check("omega(2) = 1/2", abs(om(2) - 0.5) < 1e-6)
check("omega(3) = (1+log 2)/3", abs(om(3) - (1 + math.log(2)) / 3) < 1e-5)

primes = [int(p) for p in primerange(5, CAP + 1)]
pc = np.ones(CAP + 1); prod = 1.0; prev = 0; pr = {}
for p in primes:
    pc[prev:p] = prod; prod *= 1 - 2 / p; pr[p] = prod; prev = p
pc[prev:] = prod
length = ((CAP + 1) ** 2 - 2) // 6
alive = np.ones(length, dtype=bool)
ns = np.arange(2, CAP + 1, dtype=np.int64)
counts = np.zeros(CAP + 1, dtype=np.int64)
counts[2:] = ((ns + 1) ** 2 - 2) // 6 - ((ns * ns + 1) // 6 + 1) + 1
sq = np.arange(2, CAP + 2, dtype=np.int64) ** 2
near = np.unique(np.concatenate([sq // 6 + j for j in (-1, 0, 1)]))
near = near[(near >= 1) & (near <= length)]
low = 6 * near - 1; sec = np.sqrt(low).astype(np.int64)
ok = (sec >= 2) & (sec <= CAP) & (low > sec ** 2) & (low + 2 < (sec + 1) ** 2)
alive[near[~ok] - 1] = False
check("initial cell count equals sum of C(n)", int(alive.sum()) == int(counts.sum()))
M = float(np.sum(counts[2:] * pc[2:]))
logn = np.log(np.arange(CAP + 1, dtype=float).clip(2))
binsum = np.zeros(NB)
for p in primes:
    c = pow(6, -1, p); first = (p * p + 6) // 6
    hits = np.zeros(CAP + 1, dtype=np.int64)
    for r in (c, (-c) % p):
        b0 = first + (r - first) % p
        for s in range(b0 - 1, length, p * 1000000):
            idx = np.arange(s, min(length, s + p * 1000000), p, dtype=np.int64)
            rem = idx[alive[idx]]
            hits += np.bincount(np.sqrt(6 * (rem + 1) - 1).astype(np.int64), minlength=CAP + 1)
            alive[rem] = False
    cc = -pc[p:] * (hits[p:] - 2.0 * counts[p:] / p) / pr[p]
    bi = np.minimum((math.log(p) / logn[p:] * NB).astype(int), NB - 1)
    binsum += np.bincount(bi, weights=cc, minlength=NB)
    counts[p:] -= hits[p:]
T = int(counts[2:].sum())
check(f"U={CAP}: bins sum to T - M", abs(binsum.sum() - (T - M)) < 1e-7 * M,
      f"T/M = {T/M:.6f}")

print(f"\n  {'a0':>5} {'measured':>10} {'model':>10}")
cum = 0.0; gap = 0.0; got = {}
for j in range(NB):
    cum += binsum[j] / M; a0 = (j + 1) / NB
    pred = (math.exp(G) * om(2 / a0)) ** 2 - 1
    gap = max(gap, abs(cum - pred)); got[round(a0, 2)] = cum
    if j % 2 == 1: print(f"  {a0:>5.2f} {cum:>+10.5f} {pred:>+10.5f}")
check(f"largest gap from the model < {GAP}", gap < GAP, f"{gap:.5f}")
check("cumulative up to a = 0.5 is below 0.001 in size", abs(got[0.5]) < 1e-3, f"{got[0.5]:+.5f}")
check("cumulative near a = 0.7 is between +1.5% and +2.2%", 0.015 < got[0.7] < 0.022, f"{got[0.7]:+.5f}")
if FULL:
    for a0, v in PRINTED.items():
        check(f"printed cumulative at a0 = {a0}", abs(got[a0] - v) < 5e-6, f"{got[a0]:+.5f}")
sys.exit(1 if fails else 0)
