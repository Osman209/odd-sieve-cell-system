#!/usr/bin/env python3
"""
verify_weighted_l2.py

COVERS = ["[P4, S5.1]", "[P4, S3.2]"]

The weighted L^2 quantity of [P4, S5.1], written 2026-10-02.  Every integer
sector (n^2,(n+1)^2), strict at both ends, sieved by every line p <= n.
P(n) = prod_{5<=p<=n}(1-2/p), M(U) = sum_{2<=n<=U} C(n)P(n), T(U) = survivors.
For each line p:  eps_p(n) = D_p(n) - 2 N_{p-}(n)/p  (strikes of p on the
survivors of the smaller lines, minus the cyclic prediction), and

    B_p(U) = - sum_{p<=n<=U} P(n) eps_p(n) / P(p),

so that  sum_p B_p(U) = T(U) - M(U)  exactly (Theorem 3).  With
k(U) = #{5 <= p <= U} and E(U) = sum_p B_p(U)^2, Cauchy-Schwarz gives
|T - M| <= sqrt(k E), hence with Q = k E / M^2:

    T(U) >= M(U) (1 - sqrt(Q(U))).

What it checks: the telescoping identity at every sample; the Cauchy
inequality; T against an independent ordinary sieve of the twin pairs;
Q < 1 at every sample (a finite measurement -- no bound on Q is proved);
the independent count is run for U <= 10000;
and the printed rows of [P4, S5.1] to six decimals.

The comparison value e^{2 gamma}/4 = 0.7930547 is the limit of T/M under
the Hardy-Littlewood conjecture; it is printed, never assumed.

Modes: --fast (U <= 4800)   default (U <= 10000)   --full (U <= 100000, ~1 min)
Integer counts are exact; weights and energies are floating point.
"""
import sys, math
import numpy as np
from sympy import primerange

COVERS = ["[P4, S5.1]", "[P4, S3.2]"]
FAST = "--fast" in sys.argv
FULL = "--full" in sys.argv
fails = 0
def check(name, ok, detail=""):
    global fails
    print(("  PASS  " if ok else "  FAIL  ") + name + ("   " + detail if detail else ""))
    if not ok: fails += 1

# printed in [P4, S5.1]: U -> (T/M, Q)
PRINTED = {1200: (0.805010, 0.063546), 10000: (0.795771, 0.074875),
           50000: (0.793829, 0.085126), 100000: (0.793733, 0.090695)}

CAP = 100000 if FULL else (4800 if FAST else 10000)
SAMPLES = [u for u in (300, 600, 1200, 2400, 4800, 10000, 20000, 50000, 100000) if u <= CAP]

primes = [int(p) for p in primerange(5, CAP + 1)]
pc = np.ones(CAP + 1); prod = 1.0; prev = 0; pr = {}
for p in primes:
    pc[prev:p] = prod; prod *= 1 - 2 / p; pr[p] = prod; prev = p
pc[prev:] = prod

# cells (6b-1, 6b+1), b = 1..length; drop the O(U) cells touching or crossing a square
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
mprefix = np.cumsum(counts * pc)

sumB = {u: 0.0 for u in SAMPLES}; sumB2 = {u: 0.0 for u in SAMPLES}; k = {u: 0 for u in SAMPLES}
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
    e = np.zeros(CAP + 1); e[p:] = hits[p:] - 2.0 * counts[p:] / p
    w = np.cumsum(pc * e)
    for u in SAMPLES:
        if p <= u:
            B = -float(w[u]) / pr[p]
            sumB[u] += B; sumB2[u] += B * B; k[u] += 1
    counts -= hits
tprefix = np.cumsum(counts)

# independent twin count: ordinary Eratosthenes on [0, (min(CAP,10000)+1)^2)
TWCAP = min(CAP, 10000)
N = (TWCAP + 1) ** 2
isp = np.ones(N, dtype=bool); isp[:2] = False
for q in range(2, int(N ** 0.5) + 1):
    if isp[q]: isp[q * q::q] = False
tw = np.nonzero(isp[5:N - 2] & isp[7:N])[0] + 5        # p >= 5, p+2 < N

HL = math.exp(2 * 0.5772156649015329) / 4
print(f"\n  {'U':>7} {'T':>10} {'T/M':>9} {'Q':>9} {'1-sqrt(Q)':>10} {'E log^3U/U^3':>13}")
Qs = []
for u in SAMPLES:
    T = int(tprefix[u]); M = float(mprefix[u]); E = sumB2[u]; Q = k[u] * E / M ** 2; Qs.append(Q)
    print(f"  {u:>7} {T:>10} {T/M:>9.6f} {Q:>9.6f} {1-math.sqrt(Q):>10.6f} {E*math.log(u)**3/u**3:>13.6f}")
    check(f"U={u}: sum B_p = T - M", abs(sumB[u] - (T - M)) < 1e-7 * M)
    check(f"U={u}: Cauchy  E >= (T-M)^2/k", E + 1e-8 >= (T - M) ** 2 / k[u])
    if u <= TWCAP:
        check(f"U={u}: T equals the ordinary twin count", T == int(np.sum(tw + 2 < (u + 1) ** 2)))
    check(f"U={u}: Q < 1 (finite measurement)", Q < 1)
    if u in PRINTED:
        a, b = PRINTED[u]
        check(f"U={u}: printed T/M and Q", abs(T / M - a) < 5e-7 and abs(Q - b) < 5e-7,
              f"{T/M:.6f} {Q:.6f}")
print(f"\n  Hardy-Littlewood limit of T/M (conditional, not used): e^(2 gamma)/4 = {HL:.7f}")
print("  Q rises on the last samples: " + ", ".join(f"{q:.4f}" for q in Qs[-4:])
      + "  -- no uniform bound on Q is proved or measured.")
sys.exit(1 if fails else 0)
