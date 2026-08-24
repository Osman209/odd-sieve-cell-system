#!/usr/bin/env python3
"""
seg.py — the level decomposition of  Sigma_B(C) = sum_{h<C} (1-h/C) (S_B(h)-1)
         computed by segmented factorisation, so that C can reach Q7 = 37,182,145
         without holding a smallest-prime-factor table for 3C.

  S_B(h) = G * prod_{p|h} A_p * prod_{p|9h^2-1} B_p ,
  A_p = (1-2/p)/(1-4/p) = 1 + 2/(p-4),   B_p = (1-3/p)/(1-4/p) = 1 + 1/(p-4),
  G   = prod_{p>=5} (1-4/p)/(1-2/p)^2 .

Expanding the two products by the number of primes involved gives
  S_B(h)/G = sum_k e_k(h),
where e_k(h) is the k-th elementary symmetric function of the multiset
  { 2/(p-4) : p | h } u { 1/(p-4) : p | 3h-1 or p | 3h+1 },   p >= 5.
The three events are mutually exclusive, so each prime contributes at most once.

Against it we set the ensemble expectation: p | h with density 1/p and
p | 9h^2-1 with density 2/p, so the expected per-prime increment is
  lambda_p = (1/p)(2/(p-4)) + (2/p)(1/(p-4)) = 4/(p(p-4)),
and G * prod_p (1 + lambda_p) = 1 exactly.  The level-k deviation is
  D_k(C) = G * [ sum_{h<C} (1-h/C) e_k(h)  -  W(C) * e_k({lambda_p}) ],
  W(C)   = sum_{h<C} (1-h/C),
and  Sigma_B(C) = sum_k D_k(C).

CONVENTION, which matters: e_k({lambda_p}) is taken over ALL primes up to
PB = 3*HM+1, the largest prime that can divide any 3h+-1 in range.  The
subtracted term is of size C, so a tail in the expectation is amplified by C;
two runs with different prime bounds do NOT agree.  Keep PB tied to HM.

  python3 seg.py --hm 1616615   # reproduces the Q6 checksum, ~1 min
  python3 seg.py                # full run to Q7, ~15 min

Outputs D_1..D_8+, their total, and the wave moments M, J, W at each grid point.
"""
import argparse, math, sys, time
import numpy as np

KM = 8                      # levels 1..KM-1 separately, KM = "KM and above"


def primes_upto(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.flatnonzero(s)


def lambda_power_sums(PB, J=24, seg=1 << 22):
    """p_j = sum_{p>=5, p<=PB} lambda_p^j  by a segmented sieve (no prime list kept)."""
    base = primes_upto(int(PB ** 0.5) + 1)
    ps = np.zeros(J + 1)
    lo = 2
    while lo <= PB:
        hi = min(lo + seg - 1, PB)
        blk = np.ones(hi - lo + 1, dtype=bool)
        for p in base:
            if p * p > hi:
                break
            st = max(p * p, ((lo + p - 1) // p) * p)
            blk[st - lo::p] = False
        if lo <= 1:
            blk[:2 - lo] = False
        pr = (np.flatnonzero(blk) + lo).astype(np.float64)
        pr = pr[pr >= 5]
        if pr.size:
            lam = 4.0 / (pr * (pr - 4.0))
            cur = np.ones_like(lam)
            for j in range(1, J + 1):
                cur *= lam
                ps[j] += cur.sum()
                if ps[j] == 0.0 and j > 4:
                    break
        lo = hi + 1
    return ps


def esym_from_power_sums(ps, K):
    """Newton's identities:  k e_k = sum_{i=1..k} (-1)^{i-1} e_{k-i} p_i."""
    e = [1.0] + [0.0] * K
    for k in range(1, K + 1):
        acc = 0.0
        for i in range(1, k + 1):
            acc += ((-1) ** (i - 1)) * e[k - i] * ps[i]
        e[k] = acc / k
    return e


def run(HM, block, grid):
    t0 = time.time()
    PB = 3 * HM + 1
    ps = lambda_power_sums(PB)
    # analytic tail  sum_{p>PB} 4/(p(p-4)) ~ 4/(PB log PB):  the subtracted term is
    # of size C, so an unclosed tail here shows up as a spurious linear-in-C drift.
    ps[1] += 4.0 / (PB * math.log(PB))
    Efull = esym_from_power_sums(ps, 24)
    G = 1.0 / sum(Efull)                       # since G * sum_k e_k(lambda) = 1
    Elam = Efull[1:KM] + [sum(Efull[KM:])]
    print(f"# PB={PB}  G={G:.9f}  sum_k e_k(lambda)={sum(Efull):.9f}"
          f"  [{time.time()-t0:.1f}s]", flush=True)

    base = primes_upto(int((3 * HM + 2) ** 0.5) + 2)
    base = base[base >= 5]

    S = np.zeros(KM)          # running sum_h e_k(h)
    Sh = np.zeros(KM)         # running sum_h h e_k(h)
    W = 0.0
    Wh = 0.0
    out = {}
    gset = sorted(grid)

    lo = 1
    while lo <= HM:
        hi = min(lo + block - 1, HM)
        n = hi - lo + 1
        h = np.arange(lo, hi + 1, dtype=np.int64)

        E = np.zeros((KM + 1, n))
        E[0] = 1.0

        def apply(idx, val):
            """multiply the generating polynomial by (1 + val) at positions idx"""
            for k in range(KM, 0, -1):
                E[k][idx] += E[k - 1][idx] * val

        for v0, step, coef in ((lo, 1, 2.0), (3 * lo - 1, 3, 1.0), (3 * lo + 1, 3, 1.0)):
            R = (v0 + step * np.arange(n, dtype=np.int64))
            for small in (2, 3):                # 2 and 3 are not lines: strip, don't record
                while True:
                    m = (R % small == 0)
                    if not m.any():
                        break
                    R = np.where(m, R // small, R)
            vmax = v0 + step * (n - 1)
            for p in base:
                p = int(p)
                if p > vmax:
                    break
                # index of the first term of the progression divisible by p
                i0 = ((-v0) * pow(step, -1, p)) % p
                if i0 >= n:
                    continue
                idx = np.arange(i0, n, p)
                apply(idx, coef / (p - 4.0))
                q = R[idx]
                while True:
                    m = (q % p == 0)
                    if not m.any():
                        break
                    q = np.where(m, q // p, q)
                R[idx] = q
            big = R > 1                        # leftover = one large prime
            if big.any():
                v = coef / (R[big].astype(np.float64) - 4.0)
                for k in range(KM, 0, -1):
                    E[k][big] += E[k - 1][big] * v

        ek = np.vstack([E[1:KM], E[KM:].sum(0)])          # shape (KM, n)
        cs = np.cumsum(ek, axis=1)
        csh = np.cumsum(ek * h, axis=1)
        cw = np.arange(1, n + 1, dtype=np.float64)
        cwh = np.cumsum(h.astype(np.float64))

        for C in gset:
            if lo <= C <= hi:
                j = C - lo
                Sk = S + cs[:, j]
                Skh = Sh + csh[:, j]
                Wc = W + cw[j]
                Wch = Wh + cwh[j]
                D = G * ((Sk - Skh / C) - (Wc - Wch / C) * np.array(Elam))
                Du = G * (Sk - Wc * np.array(Elam))          # unweighted sum_{h<=C}
                out[C] = (D, Du.sum())
        S += cs[:, -1]
        Sh += csh[:, -1]
        W += cw[-1]
        Wh += cwh[-1]
        print(f"#   block to {hi}  [{time.time()-t0:.1f}s]", flush=True)
        lo = hi + 1

    lab = [f"D{i+1}" for i in range(KM - 1)] + [f"D{KM}+"]
    print("\n" + f"{'C':>10} {'t':>6} " + " ".join(f"{l:>8}" for l in lab)
          + f"{'weighted':>10} {'plain':>10} {'M':>7} {'J':>7} {'W':>7}")
    prev = None
    for C in sorted(out):
        D, U = out[C]
        t = math.log(C)
        row = f"{C:10d} {t:6.2f} " + " ".join(f"{x:8.3f}" for x in D) + f"{D.sum():10.3f} {U:10.3f}"
        if prev:
            Cp, Dp, tp = prev
            d = -(D - Dp) / (t - tp)
            M = d.sum()
            J = sum((k + 1) * d[k] for k in range(KM)) / M
            V = sum(((k + 1) - J) ** 2 * d[k] for k in range(KM)) / M
            row += f" {M:7.3f} {J:7.3f} {abs(V)**0.5:7.3f}"
        print(row, flush=True)
        prev = (C, D, t)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--hm", type=int, default=37_182_145)
    ap.add_argument("--block", type=int, default=1_000_000)
    a = ap.parse_args()
    g = sorted({int(round(10 ** (5 + 0.15 * j))) for j in range(0, 30)
                if 10 ** (5 + 0.15 * j) <= a.hm} | {1_616_615, a.hm} - {0})
    g = [c for c in g if 1 <= c <= a.hm]
    run(a.hm, a.block, g)
