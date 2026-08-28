#!/usr/bin/env python3
"""
verify_cell_transfer.py — regenerates every number added to

    paper_III_from_cycle_to_window.md   §6.1  (pattern transfer, Proposition 2)
    paper_V_where_the_framework_stops.md §3.2 (prediction row, the R/C decades)
    paper_V_where_the_framework_stops.md Appendix B (the survival-product bullet)

Checks 1-6   : closed forms and the Buchstab prediction row.
Checks 7-10  : the four-state decade table at the cut z = X^(1/3).
Checks 11-13 : the survival product prod(1 - delta_p) and where its deviation lives.
Check  14    : the pattern-transfer table J/L.

    python3 verify_cell_transfer.py --fast    # X <= 1e7,   ~30 s
    python3 verify_cell_transfer.py           # X <= 1e9,   ~10 min
    python3 verify_cell_transfer.py --deep    # adds X = 4e9, ~40 min, needs ~1 GB

Rows needing a height above the run's cutoff are SKIPPED and listed as a
REDUCED RUN; they never set the exit code.  Exits nonzero if any check fails.
"""
import sys, math, argparse
import numpy as np

GAMMA = 0.5772156649015329
FAIL = []
SKIP = []


def check(tag, got, want, tol, note=""):
    ok = (want is None) or (abs(got - want) <= tol)
    print(f"  [{'ok ' if ok else 'FAIL'}] {tag:<52} {got:.6f}"
          + (f"  vs {want:.6f} (tol {tol:g})" if want is not None else "")
          + (f"   {note}" if note else ""))
    if not ok:
        FAIL.append(tag)


# ---------------------------------------------------------------- primes
def primes_upto(n):
    if n < 2:
        return []
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return [int(p) for p in np.flatnonzero(s)]


# ---------------------------------------------------------------- Buchstab
def buchstab(h=1e-5, U=8.0):
    n = int(U / h) + 1
    u = np.arange(n) * h
    w = np.zeros(n)
    m = (u >= 1) & (u <= 2)
    w[m] = 1.0 / u[m]
    i0 = int(round(2 / h))
    st = int(round(1 / h))
    val = 2 * w[i0]
    for i in range(i0, n - 1):
        val += h * (w[i - st] + w[i + 1 - st]) / 2
        w[i + 1] = val / u[i + 1]
    return lambda x: float(np.interp(x, u, w))


# ---------------------------------------------------------------- sieves
def four_states(X, block=1 << 22):
    """Cut z = X^(1/3).  Classify every surviving cell 6n-1, 6n+1 as P or P_2.
    Returns (N_PP, N_PP2, N_P2P, N_P2P2)."""
    z = X ** (1.0 / 3.0)
    ps = [p for p in primes_upto(int(math.isqrt(X))) if p >= 5]
    N = (X - 1) // 6
    cnt = np.zeros(4, dtype=np.int64)
    lo = 1
    while lo <= N:
        hi = min(lo + block, N + 1)
        L = hi - lo
        ra = np.ones(L, bool); rb = np.ones(L, bool)
        pa = np.ones(L, bool); pb = np.ones(L, bool)
        for p in ps:
            inv6 = pow(6, -1, p)
            s1 = (inv6 - lo) % p
            s2 = ((-inv6) % p - lo) % p
            na = (p + 1) // 6 if (p + 1) % 6 == 0 else None   # 6n-1 = p
            nb = (p - 1) // 6 if (p - 1) % 6 == 0 else None   # 6n+1 = p
            ka = (pa[na - lo], ra[na - lo]) if (na is not None and lo <= na < hi) else None
            kb = (pb[nb - lo], rb[nb - lo]) if (nb is not None and lo <= nb < hi) else None
            pa[s1::p] = False; pb[s2::p] = False
            if p <= z:
                ra[s1::p] = False; rb[s2::p] = False
            if ka is not None:
                pa[na - lo], ra[na - lo] = ka[0], (ka[1] if p <= z else ra[na - lo])
            if kb is not None:
                pb[nb - lo], rb[nb - lo] = kb[0], (kb[1] if p <= z else rb[nb - lo])
        S = ra & rb
        code = (2 * (~pa).astype(np.int8) + (~pb).astype(np.int8))[S]
        cnt += np.bincount(code, minlength=4).astype(np.int64)
        lo = hi
    return tuple(int(c) for c in cnt)


def phi_rough(X, block=1 << 23):
    """#{n <= X : n has no prime factor <= X^(1/3)}, excluding those primes themselves."""
    z = X ** (1.0 / 3.0)
    ps = primes_upto(int(z))
    cnt = 0
    lo = 2
    while lo <= X:
        hi = min(lo + block, X + 1)
        s = np.ones(hi - lo, bool)
        for p in ps:
            s[(-lo) % p::p] = False
        cnt += int(s.sum())
        lo = hi
    return cnt


def delta_profile(X):
    """Sequential twin-cell sieve; returns (list of (p, delta_p), survivors, N)."""
    N = (X - 1) // 6
    alive = np.ones(N + 1, dtype=bool); alive[0] = False
    ps = [p for p in primes_upto(int(math.isqrt(X))) if p >= 5]
    surv = N
    rows = []
    for p in ps:
        inv6 = pow(6, -1, p)
        r1, r2 = inv6 % p, (-inv6) % p
        cells = [c for c, cond in (((p + 1) // 6, (p + 1) % 6 == 0),
                                   ((p - 1) // 6, (p - 1) % 6 == 0)) if cond and 1 <= c <= N]
        keep = [bool(alive[c]) for c in cells]
        s1 = r1 if r1 >= 1 else r1 + p
        s2 = r2 if r2 >= 1 else r2 + p
        k = int(alive[s1::p].sum()) + int(alive[s2::p].sum()) - sum(keep)
        alive[s1::p] = False; alive[s2::p] = False
        for c, st in zip(cells, keep):
            alive[c] = st
        rows.append((p, k / surv))
        surv -= k
    return rows, surv, N


def nu(p, hs):
    inv6 = pow(6, -1, p)
    return len({(inv6 - h) % p for h in hs} | {(-inv6 - h) % p for h in hs})


def local_factor(z, hs):
    k = len(hs)
    v = 1.0
    for p in primes_upto(int(z)):
        if p < 5:
            continue
        v *= (1 - nu(p, hs) / p) / (1 - 2.0 / p) ** k
    return v


def pattern_transfer(X, u, pats, block=1 << 23):
    z = X ** (1.0 / u)
    ps = [p for p in primes_upto(int(z)) if p >= 5]
    inv = {p: (pow(6, -1, p) % p, (-pow(6, -1, p)) % p) for p in ps}
    N = (X - 1) // 6
    hmax = max(h[-1] for h in pats)
    tot = {h: 0 for h in pats}
    base = ncells = 0
    lo = 1
    while lo <= N:
        hi = min(lo + block, N + 1)
        S = np.ones(hi + hmax - lo, dtype=bool)
        for p in ps:
            for r in inv[p]:
                S[(r - lo) % p::p] = False
        base += int(S[:hi - lo].sum()); ncells += hi - lo
        for h in pats:
            m = S[:hi - lo].copy()
            for hh in h[1:]:
                m &= S[hh:hh + hi - lo]
            tot[h] += int(m.sum())
        lo = hi
    pS = base / ncells
    out = {}
    for h in pats:
        c = tot[h]
        J = (c / ncells) / pS ** len(h)
        out[h] = (c, J, local_factor(z, h), J / local_factor(z, h))
    return pS, out


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fast", action="store_true")
    ap.add_argument("--deep", action="store_true")
    ap.add_argument("--force-fail", action="store_true", help="exercise the failure gate")
    a = ap.parse_args()
    top = 10 ** 7 if a.fast else (4 * 10 ** 9 if a.deep else 10 ** 9)
    print(f"cutoff for this run: X <= {top:.3g}\n")

    om = buchstab()

    print("--- [V, 3.2] closed forms ---")
    check("1.  omega(3) = (1+log2)/3", om(3.0), (1 + math.log(2)) / 3, 1e-7)
    from scipy.integrate import quad
    check("2.  int_{1/3}^{1/2} da/(a(1-a)) = log 2",
          quad(lambda t: 1 / (t * (1 - t)), 1 / 3, 1 / 2)[0], math.log(2), 1e-9)
    check("3.  limit R/C = 2(1-1/(1+log2))",
          2 * (1 - 1 / (1 + math.log(2))), 0.818768, 1e-5)
    check("4.  limit T/C = 1/(1+log2)^2",
          1 / (1 + math.log(2)) ** 2, 0.348827, 1e-5)

    print("\n--- [V, 3.2] the prediction row ---")
    for uu, want in [(5.08, 1.2988), (4.02, 1.1139), (3.58, 1.0040),
                     (3.00, 0.8188), (2.63, 0.6564), (2.38, 0.4872)]:
        check(f"5.  u={uu}: 2(1-1/u.omega(u))", 2 * (1 - 1 / (uu * om(uu))), want, 5e-4)

    print("\n--- [V, 3.2] the decade table (cut z = X^(1/3)) ---")
    want = {"1e6": (10 ** 6, 19303, 8168, 0.7038, 0.4231, 1.6683, 1.0633),
            "1e7": (10 ** 7, 142921, 58979, 0.7208, 0.4127, 1.6753, 1.0694),
            "1e8": (10 ** 8, 1096286, 440311, 0.7355, 0.4016, 1.6783, 1.0354),
            "1e9": (10 ** 9, 8775268, 3424505, 0.7527, 0.3902, 1.6893, 1.0237),
            "4e9": (4 * 10 ** 9, 30857268, 11944437, 0.7575, 0.3871, None, 1.0203)}
    for e, row in want.items():
        X = row[0]
        if X > top:
            SKIP.append(f"decade table X={e}"); continue
        A, B, C_, D = four_states(X)
        C = A + B + C_ + D
        R = B + C_ + 2 * D
        T = A
        _, wC, wT, wRC, wTC, wPhi, wOR = row
        check(f"6.  X={e}: C", C, wC, 0.5)
        check(f"7.  X={e}: T", T, wT, 0.5)
        check(f"8.  X={e}: R/C", R / C, wRC, 5e-4)
        check(f"9.  X={e}: T/C", T / C, wTC, 5e-4)
        check(f"10. X={e}: odds ratio", A * D / (B * C_), wOR, 5e-4)
        if wPhi is None:
            SKIP.append(f"Phi(x,x^(1/3)) at X={e} (not tabulated in the paper)")
        else:
            ph = phi_rough(X)
            check(f"11. X={e}: Phi(x,x^(1/3)) log x / x", ph * math.log(X) / X, wPhi, 5e-4)
        if e == "1e9":
            pix = 50847534                       # pi(10^9), standard tabulated value
            share = (2 * C - R) / (2 * C)
            check("12. X=1e9: pi/Phi reproduces the measured prime share",
                  (pix * math.log(X) / X) / (ph * math.log(X) / X), share, 1e-3)

    print("\n--- [V, App. B] the survival product ---")
    wantE = {6: 0.9436, 7: 0.9221, 8: 0.8996, 9: 0.8840}
    for e in [6, 7, 8, 9]:
        X = 10 ** e
        if X > top:
            SKIP.append(f"survival product X=1e{e}"); continue
        rows, surv, N = delta_profile(X)
        ld = sum(math.log1p(-d) for _, d in rows)
        ln = sum(math.log1p(-2.0 / p) for p, _ in rows)
        check(f"13. X=1e{e}: identity R_0 prod(1-delta_p) = survivors",
              math.exp(ld) * N, float(surv), 1.0)
        check(f"14. X=1e{e}: prod(1-delta)/prod(1-2/p)", math.exp(ld - ln), wantE[e], 5e-4)
        if e == 9:
            # delta_p = 2/p below X^(1/4);  partial ratio = (e^gamma omega(u))^2
            for lo_u, hi_u, w in [(5.0, 12.0, 1.0000), (4.0, 5.0, 1.0017)]:
                v = [d / (2.0 / p) for p, d in rows
                     if lo_u <= math.log(X) / math.log(p) < hi_u]
                check(f"15. X=1e9: mean delta_p/(2/p), u in [{lo_u},{hi_u})",
                      float(np.mean(v)), w, 5e-4)
            for uu, w in [(3.0, 1.0033), (4.0, 0.9995), (6.0, 1.0000)]:
                z = X ** (1.0 / uu)
                ld2 = sum(math.log1p(-d) for p, d in rows if p <= z)
                ln2 = sum(math.log1p(-2.0 / p) for p, _ in rows if p <= z)
                check(f"16. X=1e9: partial ratio / (e^g.omega({uu}))^2",
                      math.exp(ld2 - ln2) / (math.exp(GAMMA) * om(uu)) ** 2, w, 2e-3)

    print("\n--- [III, 6.1] admissibility and pattern transfer ---")
    check("17. nu_5({0,1,2}) = 5 (consecutive cells inadmissible)", nu(5, (0, 1, 2)), 5, 0)
    pats = [(0, 1), (0, 1, 3), (0, 1, 3, 5), (0, 1, 3, 5, 6)]
    for h in pats:
        assert all(nu(p, h) < p for p in primes_upto(200) if p >= 5), h
    tab = {(4.0, (0, 1)): (1688188, 1.0000), (4.0, (0, 1, 3)): (142416, 1.0002),
           (4.0, (0, 1, 3, 5)): (19817, 0.9985), (4.0, (0, 1, 3, 5, 6)): (727, 0.9887),
           (3.0, (0, 1)): (567431, 1.0007), (3.0, (0, 1, 3)): (27527, 0.9964),
           (3.0, (0, 1, 3, 5)): (2167, 0.9762), (3.0, (0, 1, 3, 5, 6)): (51, 1.0780),
           (2.0, (0, 1)): (85884, 1.0113), (2.0, (0, 1, 3)): (1703, 1.0640),
           (2.0, (0, 1, 3, 5)): (50, 1.0053)}
    XP = 4 * 10 ** 9
    if XP > top:
        SKIP.append("pattern table at X=4e9 (needs --deep)")
        # still test the claim itself at the run's cutoff: J/L = 1 within 3 sigma
        Xs = min(top, 10 ** 8)
        for uu in [4.0, 3.0]:
            pS, out = pattern_transfer(Xs, uu, pats)
            for h in pats:
                c, J, L, r = out[h]
                if c < 200:
                    SKIP.append(f"J/L u={uu} {h} at X={Xs:.0g} (only {c} events)"); continue
                check(f"18. X={Xs:.0g} u={uu} {h}: J/L within 3 sigma of 1",
                      r, 1.0, 3.0 / math.sqrt(c))
    else:
        for uu in [4.0, 3.0, 2.0]:
            pS, out = pattern_transfer(XP, uu, pats if uu != 2.0 else pats[:3])
            for h in (pats if uu != 2.0 else pats[:3]):
                c, J, L, r = out[h]
                wc, wr = tab[(uu, h)]
                check(f"18. X=4e9 u={uu} {h}: count", c, wc, 0.5)
                check(f"19. X=4e9 u={uu} {h}: J/L", r, wr, 5e-4)

    if a.force_fail:
        check("99. forced failure gate", 1.0, 0.0, 0.0)

    print("\n" + "=" * 62)
    if SKIP:
        print(f"REDUCED RUN — {len(SKIP)} rows skipped (height above this run's cutoff):")
        for s in SKIP:
            print("   skipped:", s)
    if FAIL:
        print(f"FAILED: {len(FAIL)} check(s): " + ", ".join(FAIL))
        return 1
    print("all executed checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
