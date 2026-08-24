#!/usr/bin/env python3
"""
verify_transfer_layers.py — regenerates every number in the block
"How much is lost in that transfer, measured" added to

    paper_V_where_the_framework_stops.md  §7.6

The block compares the cycle law of [II, Thm 2] against a direct census over
consecutive square windows [M^2,(M+2)^2] near X, at sieve depth z = X^(1/u),
and separates the comparison into three layers.

    Layer 1  mean inheritance depth              -> ratio 1.0000
    Layer 2  state totals                        -> e^(2 gamma)/4
    Layer 3  conditional depth law inside OO     -> a residual that saturates
    then     Richert's weight itself             -> 0.36% relative error

    python3 verify_transfer_layers.py --fast   # X <= 1e8,  ~3 min
    python3 verify_transfer_layers.py          # X <= 1e9,  ~12 min
    python3 verify_transfer_layers.py --deep   # adds X = 1e10, ~35 min

Rows above the run's cutoff are SKIPPED and listed as a REDUCED RUN; they never
set the exit code.  Exits nonzero if any executed check fails.
--force-fail exercises the gate.
"""
import sys, math, argparse
import numpy as np

GAMMA = 0.5772156649015329
BUCHSTAB2 = math.exp(2 * GAMMA) / 4          # 0.793055
FAIL, SKIP = [], []


def check(tag, got, want, tol):
    ok = abs(got - want) <= tol
    print(f"  [{'ok ' if ok else 'FAIL'}] {tag:<54} {got:9.5f}  vs {want:9.5f} (tol {tol:g})")
    if not ok:
        FAIL.append(tag)


def primes_upto(n):
    if n < 2:
        return []
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return [int(p) for p in np.flatnonzero(s)]


# ---------------------------------------------------------------- cycle law
def cycle_dist(z):
    """Expand prod_{5<=q<=z} ((q-2) + x u + x v), normalised.
    Returns P[state, j];  state 0 = NN, 1 = NO, 2 = ON, 3 = OO."""
    ps = [p for p in primes_upto(int(z)) if p >= 5]
    J = len(ps) + 1
    P = np.zeros((4, J))
    P[0, 0] = 1.0
    for q in ps:
        Q = P * ((q - 2) / q)
        w = 1 / q
        for a, b in [(0, 1), (1, 1), (2, 3), (3, 3)]:      # strike the left rail
            Q[b, 1:] += P[a, :-1] * w
        for a, b in [(0, 2), (2, 2), (1, 3), (3, 3)]:      # strike the right rail
            Q[b, 1:] += P[a, :-1] * w
        P = Q
    return P


def window_dist(X, z, nwin):
    """Census of (state, depth) over nwin consecutive square windows near X."""
    ps = [p for p in primes_upto(int(z)) if p >= 5]
    inv = {p: (pow(6, -1, p) % p, (-pow(6, -1, p)) % p) for p in ps}
    J = len(ps) + 1
    hist = np.zeros((4, J), dtype=np.int64)
    M = int(X ** 0.5) | 1
    for _ in range(nwin):
        lo = (M * M) // 6 + 1
        hi = ((M + 2) ** 2) // 6 + 1
        L = hi - lo
        dl = np.zeros(L, np.int16)
        dr = np.zeros(L, np.int16)
        for p in ps:
            r1, r2 = inv[p]
            dl[(r1 - lo) % p::p] += 1
            dr[(r2 - lo) % p::p] += 1
        st = (dl > 0).astype(np.int8) + 2 * (dr > 0).astype(np.int8)
        np.add.at(hist, (st, (dl + dr).astype(np.int64)), 1)
        M += 2
    return hist / hist.sum()


# ---------------------------------------------------------------- Richert weight
LO, HI, STEP = -6.0, 1.0, 0.002
NB = int((HI - LO) / STEP) + 1


def _idx(w):
    return np.clip(((w - LO) / STEP).astype(int), 0, NB - 1)


def richert(X, nwin):
    """Distribution of w = 1 - sum_{q | m, z<=q<y} (1 - log q/log y) over the
    survivors of sifting by p < z, with z = X^(1/4) and y = X^(1/2).
    Returns (cycle ratios, window ratios) for mean w and for sum max(0,w)."""
    Z0, Y = int(X ** 0.25), int(X ** 0.5)
    WP = [p for p in primes_upto(Y - 1) if p >= Z0]
    C = np.array([1 - math.log(p) / math.log(Y) for p in WP])

    P = np.zeros(NB)
    P[_idx(np.array([1.0]))[0]] = 1.0
    for p, c in zip(WP, C):
        sh = int(round(c / STEP))
        Q = P * (1 - 1 / p)
        src = P * (1 / p)
        if sh > 0:
            Q[:-sh] += src[sh:]
        else:
            Q += src
        P = Q

    sift = [p for p in primes_upto(Z0 - 1) if p >= 5]
    H = np.zeros(NB)
    tot = 0
    M = int(X ** 0.5) | 1
    for _ in range(nwin):
        lo = (M * M) // 6 + 1
        hi = ((M + 2) ** 2) // 6 + 1
        L = hi - lo
        alive = np.ones(L, bool)
        w = np.ones(L)
        for p in sift:
            alive[((-pow(6, -1, p)) % p - lo) % p::p] = False
        for p, c in zip(WP, C):
            w[((-pow(6, -1, p)) % p - lo) % p::p] -= c
        ww = w[alive]
        np.add.at(H, _idx(ww), 1)
        tot += len(ww)
        M += 2
    H /= tot
    g = LO + STEP * np.arange(NB)
    return ((g * H).sum() / (g * P).sum(),
            (np.maximum(0, g) * H).sum() / (np.maximum(0, g) * P).sum())


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fast", action="store_true")
    ap.add_argument("--deep", action="store_true")
    ap.add_argument("--force-fail", action="store_true")
    a = ap.parse_args()
    top = 10 ** 8 if a.fast else (10 ** 10 if a.deep else 10 ** 9)
    print(f"cutoff for this run: X <= {top:.3g}\n")

    print("--- Layer 1: the mean inheritance depth transfers exactly ---")
    X = 10 ** 8
    for u, nwin in [(4.0, 400), (3.0, 400), (2.0, 400)]:
        z = X ** (1.0 / u)
        Pc, Pe = cycle_dist(z), window_dist(X, z, nwin)
        J = min(Pc.shape[1], Pe.shape[1])
        Pc, Pe = Pc[:, :J], Pe[:, :J]
        j = np.arange(J)
        mc = (j * Pc.sum(0)).sum()
        me = (j * Pe.sum(0)).sum()
        check(f"1.  X=1e8, u={u}: mean depth window/cycle", me / mc, 1.0, 2e-3)

    print("\n--- Layer 2: the NN total converges to e^(2 gamma)/4 ---")
    want = {6: (1.0113, 20000), 7: (0.9814, 12000), 8: (0.8653, 6000),
            9: (0.8071, 3000), 10: (0.7953, 1500)}
    for e, (w_, nwin) in want.items():
        X = 10 ** e
        if X > top:
            SKIP.append(f"Layer 2 row X=1e{e}")
            continue
        z = X ** 0.5
        Pc, Pe = cycle_dist(z), window_dist(X, z, nwin)
        r = Pe[0].sum() / Pc[0].sum()
        check(f"2.  X=1e{e}: NN window/cycle", r, w_, 5e-3)
        if e == 10:
            check("3.  X=1e10: distance to e^(2 gamma)/4", r - BUCHSTAB2, 0.002, 3e-3)

    print("\n--- Layer 3: the conditional depth law inside OO does not converge ---")
    want3 = {8: (-1.51, 0.042, 6000), 9: (-1.89, 0.046, 3000), 10: (-1.78, 0.045, 1500)}
    for e, (bias, tv_, nwin) in want3.items():
        X = 10 ** e
        if X > top:
            SKIP.append(f"Layer 3 row X=1e{e}")
            continue
        z = X ** 0.5
        Pc, Pe = cycle_dist(z), window_dist(X, z, nwin)
        J = min(Pc.shape[1], Pe.shape[1])
        c, w = Pc[3, :J], Pe[3, :J]
        j = np.arange(J)
        mc = (j * c).sum() / c.sum()
        me = (j * w).sum() / w.sum()
        tv = 0.5 * np.abs(c / c.sum() - w / w.sum()).sum()
        check(f"4.  X=1e{e}: OO conditional-mean bias (%)", 100 * (me / mc - 1), bias, 0.15)
        check(f"5.  X=1e{e}: TV of the OO conditional law", tv, tv_, 5e-3)

    print("\n--- Richert's weight, ranges scaled with X ---")
    wantR = {8: (0.99860, 0.99610, 3000), 9: (0.99886, 0.99628, 1500),
             10: (0.99892, 0.99638, 700)}
    for e, (m_, p_, nwin) in wantR.items():
        X = 10 ** e
        if X > top:
            SKIP.append(f"Richert row X=1e{e}")
            continue
        rm, rp = richert(X, nwin)
        check(f"6.  X=1e{e}: mean w window/cycle", rm, m_, 1e-3)
        check(f"7.  X=1e{e}: sum max(0,w) window/cycle", rp, p_, 1e-3)

    if a.force_fail:
        check("99. forced failure gate", 1.0, 0.0, 0.0)

    print("\n" + "=" * 62)
    if SKIP:
        print(f"REDUCED RUN — {len(SKIP)} rows skipped (height above this run's cutoff):")
        for s in SKIP:
            print("   skipped:", s)
    if FAIL:
        print(f"FAILED: {len(FAIL)} check(s): " + "; ".join(FAIL))
        return 1
    print("all executed checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
