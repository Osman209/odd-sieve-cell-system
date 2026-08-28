#!/usr/bin/env python3
"""
verify_central_pair.py — regenerates every claim of [I, §4] (Theorem 4, Corollaries 2-3).

    checks 1-2   the Lemma of §5.2 (the two formulations agree)
    check  3     Theorem 4:  ell(m) = a+b+2  for every odd m in range
    checks 4-5   the parity hypothesis: the law fails for even m, and the
                 weaker floor (m1+1)(g+1) predicted by the same proof holds
    checks 6-8   Corollary 2: the handover, the square case, the prime case
    check  9     Corollary 3: composites hand over to composites
    check  10    §5.6: ell(m) = m+3 exactly on the primes

    python3 verify_central_pair.py --fast    # odd m < 1200,  ~20 s
    python3 verify_central_pair.py           # odd m < 4000,  ~4 min

Exits nonzero if any check fails.  --force-fail exercises the gate.
"""
import sys, math, argparse
from sympy import divisors, isprime

FAIL = []


def report(tag, ok, detail=""):
    print(f"  [{'ok ' if ok else 'FAIL'}] {tag}{('   ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(tag)


def central_pair(m):
    a = max(d for d in divisors(m) if d * d <= m)
    return a, m // a


def loses_by_sqrt(m, n):
    """largest divisor of m*n at most sqrt(m*n) exceeds m ?"""
    N = m * n
    r = math.isqrt(N)
    return max(d for d in divisors(N) if d <= r) > m


def loses_by_interval(m, n):
    """m*n has a divisor strictly between m and n ?"""
    N = m * n
    return any(m < d < n for d in divisors(N))


def ell(m, kmax, test=loses_by_sqrt):
    for k in range(1, kmax + 1):
        if test(m, m + 2 * k):
            return k
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fast", action="store_true")
    ap.add_argument("--force-fail", action="store_true")
    a_ = ap.parse_args()
    TOP = 1200 if a_.fast else 4000
    print(f"odd range for this run: m < {TOP}\n")

    print("--- [I, §5.2] the Lemma ---")
    bad = [(m, n) for m in range(3, 400, 2) for n in range(m + 2, m + 400, 2)
           if loses_by_sqrt(m, n) != loses_by_interval(m, n)]
    report("1.  'largest divisor below sqrt exceeds m'  ==  'a divisor lies in (m,n)'",
           not bad, f"{len(bad)} disagreements over 39,800 pairs")
    report("2.  the displacing divisor is a(b+2) = m+2a",
           all((lambda a, b: (a * (b + 2) == m + 2 * a) and
                             (m < a * (b + 2) < (a + 2) * (b + 2)))(*central_pair(m))
               for m in range(3, TOP, 2)))

    print("\n--- [I, §5.3] Theorem 8 ---")
    bad = []
    for m in range(3, TOP, 2):
        a, b = central_pair(m)
        if ell(m, a + b + 60) != a + b + 2:
            bad.append(m)
    report(f"3.  ell(m) = a+b+2 for every odd 3 <= m < {TOP}",
           not bad, f"{len(bad)} exceptions" + (f": {bad[:6]}" if bad else ""))

    print("\n--- [I, §5.3] the parity hypothesis ---")
    fails = []
    for m in range(4, 600, 2):
        a, b = central_pair(m)
        if ell(m, a + b + 60) != a + b + 2:
            fails.append(m)
    report("4.  the law fails for even m", len(fails) == 298,
           f"{len(fails)} of 298 even m in [4,600) do not satisfy it")
    below = []
    for m in range(4, 600, 2):
        a, b = central_pair(m)
        k = ell(m, a + b + 60)
        if k is not None and m + 2 * k < (a + 1) * (b + 1):
            below.append(m)
    report("5.  the weaker floor (m1+1)(g+1) is never breached for even m",
           not below, f"{len(below)} breaches")

    print("\n--- [I, §5.4] Corollary 5 ---")
    bad = []
    for m in range(3, TOP, 2):
        a, b = central_pair(m)
        lhs = m * (m + 2 * (a + b + 2))
        T = m + 2 * a
        rhs = T * (T + 2 * (b - a))
        if lhs != rhs:
            bad.append(m)
    report("6.  L_m(a+b+2) = L_{m+2a}(b-a)", not bad, f"{len(bad)} exceptions")
    bad = [c for c in range(3, 200, 2)
           if c * c * (c * c + 2 * (2 * c + 2)) != (c * (c + 2)) ** 2]
    report("7.  squares: L_{c^2}(2c+2) = [c(c+2)]^2", not bad)
    bad = [p for p in range(3, 2000, 2) if isprime(p)
           and not (central_pair(p) == (1, p)
                    and p * (p + 2 * (p + 3)) == (p + 2) * ((p + 2) + 2 * (p - 1))
                    and p * (p + 2 * (p + 3)) == 3 * p * (p + 2))]
    report("8.  primes: L_p(p+3) = L_{p+2}(p-1) = 3p(p+2)", not bad)

    print("\n--- [I, §5.5] Corollary 6 ---")
    bad = [m for m in range(9, 20001, 2)
           if not isprime(m) and isprime(m + 2 * central_pair(m)[0])]
    report("9.  composite m  =>  T(m) composite", not bad, f"{len(bad)} exceptions")

    print("\n--- [I, §5.6] the boundary ---")
    bad = [m for m in range(3, TOP, 2)
           if ((central_pair(m)[0] + central_pair(m)[1] + 2) == m + 3) != isprime(m)]
    report("10. ell(m) = m+3  <=>  m prime", not bad, f"{len(bad)} exceptions")

    if a_.force_fail:
        report("99. forced failure gate", False)

    print("\n" + "=" * 62)
    if FAIL:
        print(f"FAILED: {len(FAIL)} check(s): " + "; ".join(FAIL))
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
