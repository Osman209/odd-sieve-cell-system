#!/usr/bin/env python3
"""
verify_line_routes.py — every number in [V, 3.4]: the four-state census at the
depth cut, and the five routes through the line geometry that the section
closes by measurement (prime gaps, line capacity, the two endpoints, the two
small factors, and the determinant-one relation).

  python3 verify_line_routes.py --fast   # the first window only,  ~1 min
  python3 verify_line_routes.py          # all three windows,      ~3 min

Exits non-zero if any check fails.  --force-fail exercises the gate.
"""
import argparse
import sys

import numpy as np

M0S = [448353, 448353 + 510510, 448353 + 2 * 510510]
FAIL = []


def check(tag, got, want):
    ok = got == want
    print(f"  [{'ok ' if ok else 'FAIL'}] {tag:<58} {str(got):>14}  vs {str(want):>14}")
    if not ok:
        FAIL.append(tag)


def close(tag, got, want, tol):
    ok = abs(got - want) <= tol
    print(f"  [{'ok ' if ok else 'FAIL'}] {tag:<58} {got:>14.5f}  vs {want:>14.5f}")
    if not ok:
        FAIL.append(tag)


def primes_upto(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.flatnonzero(s).astype(np.int64)


class Window:
    """the window (M0^2, (M0+210)^2), cut at the largest prime with z^3 < X"""

    def __init__(self, M0):
        self.M0 = M0
        self.X = X = (M0 + 210) ** 2
        self.lo = lo = M0 * M0
        self.L = X - lo
        self.m0 = m0 = (lo + 1) // 6 + 1
        self.m1 = m1 = (X - 1) // 6
        self.N = N = m1 - m0 + 1
        P = primes_upto(M0 + 210)
        self.P = P
        self.z = z = int(max(int(p) for p in P if int(p) ** 3 < X))
        rl = np.ones(N, dtype=bool)
        rh = np.ones(N, dtype=bool)
        for p in P[(P >= 5) & (P <= z)]:
            p = int(p)
            r = pow(6, -1, p)
            rl[(r - m0) % p::p] = False
            rh[((p - r) % p - m0) % p::p] = False
        self.roughL, self.roughH = rl, rh
        pl, ph = rl.copy(), rh.copy()
        for p in P[P > z]:
            p = int(p)
            r = pow(6, -1, p)
            pl[(r - m0) % p::p] = False
            ph[((p - r) % p - m0) % p::p] = False
        self.primeL, self.primeH = pl, ph          # endpoint survives every p <= sqrt X
        self.cell = rl & rh
        self.R = int(self.cell.sum())
        self.HL = int((self.cell & ~pl).sum())
        self.HR = int((self.cell & ~ph).sum())
        self.H = self.HL + self.HR
        self.Csq = int((self.cell & ~pl & ~ph).sum())
        self.T = int((self.cell & pl & ph).sum())

    def spf(self, side):
        """smallest prime factor above z, for every position on one rail"""
        out = np.zeros(self.N, dtype=np.int32)
        for q in self.P[self.P > self.z]:
            q = int(q)
            r = pow(6, -1, q)
            rr = r if side == "L" else (q - r) % q
            st = (rr - self.m0) % q
            sub = out[st::q]
            z = sub == 0
            if z.any():
                sub[z] = q
                out[st::q] = sub
        return out


def four_cycles(li, ri):
    """K_2,2 count of the bipartite graph, no scipy.

    The neighbour list of each right vertex is deduplicated, so the count is
    that of a SIMPLE graph.  This matters: a degree-preserving shuffle creates
    a hundred or so multi-edges, and counting them inflates the null by a
    quarter and reverses the sign of the comparison.  The real graph is simple
    by the pr > N argument checked above.
    """
    o = np.argsort(ri, kind="stable")
    ls, rs = li[o], ri[o]
    bounds = np.flatnonzero(np.diff(rs)) + 1
    keys = []
    for a, b in zip(np.r_[0, bounds], np.r_[bounds, len(rs)]):
        g = np.unique(ls[a:b])
        if len(g) < 2:
            continue
        u, v = np.triu_indices(len(g), 1)
        keys.append(g[u].astype(np.int64) * (1 << 20) + g[v])
    if not keys:
        return 0
    keys = np.concatenate(keys)
    _, co = np.unique(keys, return_counts=True)
    return int((co * (co - 1) // 2).sum())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fast", action="store_true")
    ap.add_argument("--force-fail", action="store_true")
    a = ap.parse_args()

    print("--- the window and the depth cut ---")
    W = Window(M0S[0])
    check("1.  X = (M0+210)^2", W.X, 201208764969)
    check("2.  the cut z, largest prime with z^3 < X", W.z, 5857)
    check("3.  z^3 < X < (next prime)^3", (5857 ** 3 < W.X, 5861 ** 3 > W.X), (True, True))
    check("4.  cells in the window", W.N, 31392060)

    print("\n--- the four-state census at the cut ---")
    check("5.  surviving cells R", W.R, 1049024)
    check("6.  P2 endpoints H", W.H, 857695)
    check("7.  cells with both endpoints P2", W.Csq, 174791)
    check("8.  twins T", W.T, 366120)
    check("9.  T = R - H + C", W.R - W.H + W.Csq, W.T)
    check("10. H - C equals R - T identically", W.H - W.Csq, W.R - W.T)
    endp = 2 * W.R
    prime_end = endp - W.H
    check("11. prime endpoints", prime_end, 1240353)
    close("12. prime share against 1/(1+log 2)", prime_end / endp, 0.590616, 0.001)

    print("\n--- survivors of every line up to M0 ---")
    old = np.ones(W.N, dtype=bool)
    for p in W.P[(W.P >= 5) & (W.P <= W.M0)]:
        p = int(p)
        r = pow(6, -1, p)
        old[(r - W.m0) % p::p] = False
        old[((p - r) % p - W.m0) % p::p] = False
    U0 = int(old.sum())
    check("13. U0 = survivors of all lines <= M0", U0, 366130)
    check("14. U0 - T, the composite survivors", U0 - W.T, 10)

    print("\n--- route 1: prime gaps carry no bias ---")
    big = [int(q) for q in W.P[(W.P > W.z) & (W.P <= W.M0 + 210)]]
    gap = {big[i]: big[i + 1] - big[i] for i in range(len(big) - 1)}
    import math
    obs, exp, gg, qq = [], [], [], []
    for q in big[:-1]:
        r = pow(6, -1, q)
        t = 0
        for rr in (r, (q - r) % q):
            st = (rr - W.m0) % q
            if st < W.N:
                t += int(W.cell[st::q].sum())
        obs.append(t)
        exp.append(2 * (W.L / q) / (2 * math.log(W.X / q)))
        gg.append(gap[q])
        qq.append(q)
    obs = np.array(obs, dtype=float); exp = np.array(exp); gg = np.array(gg); qq = np.array(qq)
    k = obs.sum() / exp.sum()
    zmax = 0.0
    for g in np.unique(gg):
        s = gg == g
        if s.sum() < 20:
            continue
        e = exp[s].sum() * k
        zmax = max(zmax, abs((obs[s].sum() - e) / math.sqrt(e)))
    check("15. every gap class within 2 sd of the flat prediction", zmax < 2.0, True)
    ed = np.unique(np.quantile(qq, np.linspace(0, 1, 9)))
    worst = 0.0
    for lo_, hi_ in zip(ed[:-1], ed[1:]):
        s = (qq >= lo_) & (qq < hi_)
        worst = max(worst, abs(obs[s].sum() / exp[s].sum() / k - 1))
    check("16. the same ratio binned by q is flat to 1 per cent", worst < 0.01, True)
    check("17. mean gap rises with q, so the classes are confounded",
          gg[qq < ed[1]].mean() < gg[qq >= ed[-2]].mean(), True)

    print("\n--- route 2: capacity equals the output ---")
    raw = 0
    onrough = 0
    above = 0
    cut = W.L / W.z
    nabove = 0
    for q in big:
        r = pow(6, -1, q)
        t = 0
        for rr in (r, (q - r) % q):
            st = (rr - W.m0) % q
            if st >= W.N:
                continue
            raw += (W.N - 1 - st) // q + 1
            t += int(W.cell[st::q].sum())
        onrough += t
        if q > cut:
            above += t
            nabove += 1
    check("18. lines in (z, sqrt X]", len(big), 36824)
    check("19. raw strikes available to them", raw, 25353670)
    check("20. strikes landing on a rough cell", onrough, 857712)
    check("21. capacity minus output", onrough - W.H, 17)
    check("22. the ceiling a single twin needs, R - 1", W.R - 1, 1049023)
    check("23. the vacuous point q = L/z", round(cut), 32159)
    check("24. lines above it", nabove, 34145)
    check("25. P2 endpoints they own", above, 509602)
    close("26. their share of H", above / W.H, 0.594, 0.001)
    free = int((W.roughL & ~W.primeL).sum()) + int((W.roughH & ~W.primeH).sum())
    check("27. the same count without the partner condition", free, 4997471)
    close("28. the factor the partner condition supplies", W.H / free, 0.1716, 0.0005)

    print("\n--- route 4: the two small factors are independent ---")
    idx = np.flatnonzero(W.cell & ~W.primeL & ~W.primeH)
    p = W.spf("L")[idx].astype(np.int64)
    r = W.spf("R")[idx].astype(np.int64)
    check("29. P2P2 cells", len(idx), 174791)
    check("30. no cell has p = r", int((p == r).sum()), 0)
    lp, lr = np.log(p), np.log(r)
    c = float(np.corrcoef(lp, lr)[0, 1])
    rng = np.random.default_rng(0)
    null = [float(np.corrcoef(lp, rng.permutation(lr))[0, 1]) for _ in range(20)]
    zc = (c - np.mean(null)) / np.std(null)
    check("31. corr(log p, log r) is within 2 sd of the null", abs(zc) < 2.0, True)
    B = 8
    qs = np.quantile(lp, np.linspace(0, 1, B + 1)); qs[0] -= 1; qs[-1] += 1
    qt = np.quantile(lr, np.linspace(0, 1, B + 1)); qt[0] -= 1; qt[-1] += 1
    Hh = np.zeros((B, B))
    np.add.at(Hh, (np.digitize(lp, qs) - 1, np.digitize(lr, qt) - 1), 1)
    E = np.outer(Hh.sum(1), Hh.sum(0)) / len(idx)
    chi = float(((Hh - E) ** 2 / E).sum())
    dof = (B - 1) ** 2
    check("32. chi-square within 2 sd of its degrees of freedom",
          abs(chi - dof) < 2 * math.sqrt(2 * dof), True)

    print("\n--- route 5: the determinant-one relation is local ---")
    m = (idx + W.m0).astype(object)
    P_ = p.astype(object); R_ = r.astype(object)
    low, high = 6 * m - 1, 6 * m + 1
    q_ = low // P_; s_ = high // R_
    check("33. p q = 6j-1 and r s = 6j+1", bool((P_ * q_ == low).all() and (R_ * s_ == high).all()), True)
    aa = (R_ - P_) // 2; bb = (q_ - s_) // 2
    check("34. as - pb = 1 for every P2P2 cell", bool((aa * s_ - P_ * bb == 1).all()), True)
    key = p * (10 ** 7) + r
    check("35. every pair (p, r) occurs once", len(np.unique(key)), 174791)
    check("36. the reason: p r exceeds the window", int(p.min()) ** 2 > W.N, True)
    o = np.argsort(np.array([int(x) for x in m]))
    A_ = [int(x) for x in aa[o]]; PP = [int(x) for x in P_[o]]
    dif = np.array([abs(A_[i] * PP[i + 1] - A_[i + 1] * PP[i]) for i in range(len(A_) - 1)], dtype=float)
    check("37. consecutive cells that are Farey neighbours", int((dif == 1).sum()), 0)
    check("38. the smallest such quantity anywhere", int(dif.min()), 4604)
    v = np.array([A_[i] / PP[i] for i in range(len(A_))])
    check("39. nothing telescopes: total variation far exceeds the ends",
          np.abs(np.diff(v)).sum() > 1000 * abs(v[-1] - v[0]), True)
    lu, li = np.unique(p, return_inverse=True)
    ru, ri = np.unique(r, return_inverse=True)
    c4 = four_cycles(li, ri)
    check("40. four-cycles in the (p, r) graph", c4, 16289)
    rng = np.random.default_rng(0)
    sh = [four_cycles(li, rng.permutation(ri)) for _ in range(3)]
    check("41. within 5 per cent of a degree-preserving shuffle",
          abs(c4 / np.mean(sh) - 1) < 0.05, True)

    print("\n--- route 3: the two endpoints are independent ---")
    wins = [W] + ([] if a.fast else [Window(x) for x in M0S[1:]])
    want_C = [174791, 334340, 484350]
    want_T = [366120, 699726, 1010734]
    for i, w in enumerate(wins):
        hL, hR = w.HL / w.R, w.HR / w.R
        check(f"42.{i} C in window {i}", w.Csq, want_C[i])
        check(f"43.{i} T in window {i}", w.T, want_T[i])
        close(f"44.{i} C against independence", w.Csq / (w.R * hL * hR), 1.0, 0.005)
        close(f"45.{i} T against independence", w.T / (w.R * (1 - hL) * (1 - hR)), 1.0, 0.005)
        close(f"46.{i} tolerance with C discarded", (w.R - 1) / w.H, 1.223, 0.001)
        close(f"47.{i} tolerance with C kept", (w.R - 1 + w.Csq) / w.H, 1.427, 0.001)

    if a.force_fail:
        check("99. forced failure gate", 1, 0)

    print("\n" + "=" * 62)
    if FAIL:
        print(f"FAILED: {len(FAIL)} check(s): " + "; ".join(FAIL))
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
