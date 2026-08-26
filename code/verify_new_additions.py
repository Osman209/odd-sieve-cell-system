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

    if a.force_fail: FAIL.append("forced")
    print("\n" + "=" * 62)
    if FAIL:
        print("FAILED:", ", ".join(FAIL)); return 1
    print("all checks passed"); return 0

if __name__ == "__main__":
    sys.exit(main())
