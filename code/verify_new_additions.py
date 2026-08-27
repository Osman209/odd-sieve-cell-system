#!/usr/bin/env python3
"""Verification for the additions of 2026-08-25:
   [I, 3.5] the exact phase set of twin rows
   [I, 3.6] the centre of a diamond and its four generators
   [II, 3]  the line-3 channel in the refined generating function
   [II, 4]  the pair count (p-3)^2+1
Run: python3 verify_new_additions.py [--fast]"""
import sys, argparse
from sympy import isprime, primerange, symbols, expand

FAIL = []
def check(name, got, want):
    ok = got == want
    print(("  [ok ] " if ok else "  [FAIL] ") + f"{name:<62} {str(got)[:22]:>22}  vs {str(want):>22}")
    if not ok: FAIL.append(name)

def cpar(p):
    return (p + 1) // 6 if p % 6 == 5 else (p - 1) // 6

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fast", action="store_true")
    ap.add_argument("--force-fail", action="store_true")
    a = ap.parse_args()
    ROW = 20000 if not a.fast else 6000
    PR  = 3000 if not a.fast else 800

    rows = [n for n in range(1, ROW) if isprime(6*n - 1) and isprime(6*n + 1)]
    R = set(rows)

    print("\n--- [I, 3.5]: the exact phase set of a twin row ---")
    bad = 0
    for p in primerange(5, PR):
        c = cpar(p)
        for m in range(0, 6):
            n = c + m*p
            want = p*(6*m + 1)
            got = 6*n - 1 if p % 6 == 5 else 6*n + 1
            if got != want: bad += 1
        for m in range(1, 6):
            n = m*p - c
            want = p*(6*m - 1)
            got = 6*n + 1 if p % 6 == 5 else 6*n - 1
            if got != want: bad += 1
    check("1. u = +1 gives p(6m+1) and u = -1 gives p(6m-1)", bad, 0)

    bad_plus = bad_minus = tested = 0
    for p in primerange(5, PR):
        c = cpar(p); ci = pow(c, -1, p); tested += 1
        ones = [n for n in rows if (n*ci) % p == 1]
        if ones != ([c] if c in R else []): bad_plus += 1
        if any((n*ci) % p == p - 1 for n in rows): bad_minus += 1
    check("2. primes tested", tested, len(list(primerange(5, PR))))
    check("3. phase +1 among twin rows is {c} if c is a row, else empty", bad_plus, 0)
    check("4. phase -1 never occurs among twin rows", bad_minus, 0)

    print("\n--- [I, 3.6]: the centre of a diamond and its four generators ---")
    bad = 0; pairs = 0
    sub = rows[:80]
    for x in sub:
        for y in sub:
            if x == y: continue
            K = 36*x*y; pairs += 1
            for p in (6*x - 1, 6*x + 1, 6*y - 1, 6*y + 1):
                if (K - 1) % p == 0 or (K + 1) % p == 0: bad += 1
    check("5. ordered pairs tested", pairs, len(sub)*(len(sub) - 1))
    check("6. generator strikes on the centre", bad, 0)
    check("7. self-diamond closes itself: 36a^2-1 = (6a-1)(6a+1)",
          all(36*n*n - 1 == (6*n - 1)*(6*n + 1) for n in range(1, 200)), True)

    bad = 0
    for p in primerange(5, 200):
        c = cpar(p); ci = pow(c, -1, p)
        for x in range(1, 60):
            for y in range(1, 60):
                u = (x*ci) % p; v = (y*ci) % p
                if ((36*x*y - 1) % p == 0) != (u*v % p == 1): bad += 1
                if ((36*x*y + 1) % p == 0) != (u*v % p == p - 1): bad += 1
    check("8. phase law  p | 36ab-1 <=> uv=1,  p | 36ab+1 <=> uv=-1", bad, 0)

    bad = 0; pairs = 0
    sub = rows[:150]
    for i, x in enumerate(sub):
        for y in sub[i+1:]:
            K = 36*x*y; pairs += 1
            survives = (K - 1) % 5 != 0 and (K + 1) % 5 != 0
            pred = (x % 5 == 0 or y % 5 == 0 or x == 1 or y == 1)
            if survives != pred: bad += 1
    check("9. unordered pairs tested for the 5-law", pairs, len(sub)*(len(sub) - 1)//2)
    check("10. corrected 5-law (5 | ab, or a = 1, or b = 1)", bad, 0)

    print("\n--- [II, 3]: the line-3 channel in the refined generating function ---")
    u, v, w = symbols("u v w")
    from collections import Counter
    sets = [[5, 7], [5, 7, 11]] + ([] if a.fast else [[5, 7, 11, 13]])
    for lines in sets:
        Q = 1
        for p in lines: Q *= p
        cen = Counter()
        for j in range(Q):
            L = sum(1 for p in lines if (6*j - 1) % p == 0)
            Rr = sum(1 for p in lines if (6*j + 1) % p == 0)
            T = sum(1 for p in lines if (6*j + 3) % p == 0)
            cen[(L, Rr, T)] += 1
        g = 1
        for p in lines: g *= (p - 3) + u + v + w
        g = expand(g)
        bad = 0
        for (L, Rr, T), n in cen.items():
            coef = g.subs({u: 0, v: 0, w: 0}) if L == Rr == T == 0 \
                   else g.coeff(u, L).coeff(v, Rr).coeff(w, T)
            if int(coef) != n: bad += 1
        check(f"11. prod((p-3)+u+v+w) reproduces the census for {lines}", bad, 0)

    cen = Counter()
    for j in range(35):
        L = sum(1 for p in (5, 7) if (6*j - 1) % p == 0)
        Rr = sum(1 for p in (5, 7) if (6*j + 1) % p == 0)
        T = sum(1 for p in (5, 7) if (6*j + 3) % p == 0)
        cen[(L, Rr, T)] += 1
    check("12. the 15 open cells split 8 + 6 + 1 by the line-3 channel",
          [cen[(0, 0, k)] for k in (0, 1, 2)], [8, 6, 1])

    print("\n--- [II, 4]: the pair count for a diamond centre ---")
    for p in (5, 7, 11, 13, 17, 19):
        S = [x for x in range(p) if x % p not in (1, p - 1)]
        cnt = sum(1 for x in S for y in S if (x*y) % p not in (1, p - 1))
        check(f"13. open phase pairs at p = {p}", cnt, (p - 3)**2 + 1)

    print("\n--- the line-3 channel carries no primality information ---")
    Z = [5, 7, 11, 13, 17, 19]
    tot = Counter(); tw = Counter()
    for j in range(1, 200000):
        L, Rr = 6*j - 1, 6*j + 1
        if any(L % p == 0 or Rr % p == 0 for p in Z): continue
        k = sum(1 for p in Z if (6*j + 3) % p == 0)
        tot[k] += 1
        if isprime(L) and isprime(Rr): tw[k] += 1
    base = sum(tw.values())/sum(tot.values())
    devs = []
    for k in sorted(tot):
        if tot[k] < 300: continue
        devs.append(round(tw[k]/tot[k]/base, 3))
    print(f"     twin rate by number of strikes spent on the line-3 slot, relative to base: {devs}")
    check("14. every ratio within 3% of one", all(abs(d - 1) <= 0.03 for d in devs), True)

    print("\n--- [I, 3.6]: the gap around a k-line coincidence ---")
    bad = 0; tested = 0
    for lines in ([5,7],[5,7,11],[5,11,13],[7,11,13,17]):
        P = 1
        for q in lines: P *= q
        for x in range(0, 40*P, 6):
            if all(x % q in (1, q-1) for q in lines):
                d = x - 3*P; tested += 1
                if d != 0 and abs(d)**2 < P + 1: bad += 1
    check("15. images tested around a coincidence", tested > 0, True)
    check("16. every image at distance >= sqrt(P+1)", bad, 0)

    print("\n--- [IV, 3.10]: the balanced window is one word and a rotation ---")
    from collections import Counter
    pp, qq, rr = 1009, 1013, 52
    check("17. the bundle condition 52*1013 < 53*1009", 52*1013 < 53*1009, True)
    SM = (3, 5, 7)
    words = []
    for t in range(12):
        A = pp*qq*(2*t + 1)
        words.append(tuple(tuple(x for x in SM if (A + 2*j*pp) % x == 0)
                           for j in range(-rr, rr + 1)))
    keys = [(), (3,), (5,), (7,), (3,5), (3,7), (5,7), (3,5,7)]
    cens = {tuple(Counter(w).get(k, 0) for k in keys) for w in words}
    check("18. the incidence census is the same in every window", len(cens), 1)
    check("19. and equals the 3-5-7 fingerprint", list(cens)[0], (48,24,12,8,6,4,2,1))
    n = len(words[0])
    rot = {words[0][k:] + words[0][:k] for k in range(n)}
    check("20. every window's word is a rotation of the first",
          all(w in rot for w in words), True)

    print("\n--- [IV, 3.10]: ownership and the cofactor ---")
    from sympy import factorint
    check("21. 10387 = 13*17*47 inside [101^2,103^2)",
          (dict(factorint(10387)), 101**2 <= 10387 < 103**2),
          ({13:1, 17:1, 47:1}, True))
    check("22. 1009091 = 97*101*103 inside [997^2,1009^2)",
          (dict(factorint(1009091)), 997**2 <= 1009091 < 1009**2),
          ({97:1, 101:1, 103:1}, True))
    bad = 0
    for P2, Q2 in ((101, 103), (499, 503)):
        for x in primerange(5, P2 + 1):
            if x**3 < Q2*Q2: continue
            for m in range(max(2, P2*P2//x), Q2*Q2//x + 1):
                N = x*m
                if N < P2*P2 or N >= Q2*Q2 or min(factorint(N)) != x: continue
                if not isprime(m): bad += 1
    check("23. clean owner: p^3 >= Q^2 forces a prime cofactor", bad, 0)

    print("\n--- [V, 6.1-6.2]: the cubic cut, the monotone deficit, the counterexample ---")
    import numpy as np
    NN = 4_100_000 if a.fast else 20_000_000
    sv = np.ones(NN + 1, dtype=bool); sv[:2] = False
    for i in range(2, int(NN**0.5) + 1):
        if sv[i]: sv[i*i::i] = False
    allp = [int(x) for x in np.flatnonzero(sv) if x < 8000]

    def counts(P, Q, z):
        lo, hi = P*P, Q*Q
        j = np.arange((lo + 5)//6, (hi - 1)//6 + 1)
        L, R2 = 6*j - 1, 6*j + 1
        m = (L > lo) & (R2 < hi); L, R2 = L[m], R2[m]
        for q in allp:
            if q > z: break
            k = (L % q != 0) & (R2 % q != 0); L, R2 = L[k], R2[k]
        pl, pr = sv[L], sv[R2]
        return len(L), int((~pl).sum() + (~pr).sum()), int(((~pl) & (~pr)).sum()), int((pl & pr).sum())

    C0, R0, S0, T0 = counts(29, 31, 31**(2/3))
    check("24. the counterexample 29^2->31^2: C, R, S, T", (C0, R0, S0, T0), (8, 8, 2, 2))
    check("25. there R = C although 2h < 1", R0 == C0, True)
    check("26. and the identity T = C - R + S still holds", C0 - R0 + S0, T0)

    cases = [(1009, 1013, (146, 110, 18, 54))]
    if not a.fast: cases.append((2003, 2011, (512, 396, 89, 205)))
    for P, Q, want in cases:
        check(f"27. cubic cut at {P}: C, R, S, T", counts(P, Q, Q**(2/3)), want)

    P, Q = 1009, 1013
    lo, hi = P*P, Q*Q
    j = np.arange((lo + 5)//6, (hi - 1)//6 + 1)
    L, R2 = 6*j - 1, 6*j + 1
    m = (L > lo) & (R2 < hi); L, R2 = L[m], R2[m]
    alive = np.ones(len(L), bool)
    lines = [q for q in allp if q <= P]
    D = []
    for z in lines:
        alive &= (L % z != 0) & (R2 % z != 0)
        Cc = int(alive.sum())
        Rr = sum(int(((L % q == 0) & alive).sum() + ((R2 % q == 0) & alive).sum())
                 for q in lines if q > z)
        D.append(Rr - Cc)
    check("28. the deficit R-C is non-increasing at every cut", all(D[i+1] <= D[i] for i in range(len(D)-1)), True)
    Tw = int((sv[L] & sv[R2] & alive).sum())
    check("29. at the final cut the deficit equals -T", D[-1], -Tw)

    if a.force_fail: FAIL.append("forced")
    print("\n" + "=" * 62)
    if FAIL:
        print("FAILED:", ", ".join(FAIL)); return 1
    print("all checks passed"); return 0

if __name__ == "__main__":
    sys.exit(main())
