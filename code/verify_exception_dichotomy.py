#!/usr/bin/env python3
"""
verify_exception_dichotomy.py — every number in [IV, §3.2] beyond Theorem 4:
the closed forms of the six exceptional positions, the exhaustiveness of the
35-class scan, the {5,7} bound of three, the negative result that larger lines
do not lower it, Corollary 7, and the five residue classes in which the two
lines close all six.

  python3 verify_exception_dichotomy.py --fast   # M < 3,000,   ~20 s
  python3 verify_exception_dichotomy.py          # M < 20,000,  ~3 min
  python3 verify_exception_dichotomy.py --deep   # M < 30,000 for the five classes

Exits non-zero if any check fails.  --force-fail exercises the gate.
"""
import argparse
import sys
from itertools import product

import numpy as np
from sympy import isprime

KEYS = list("ABCDEF")
L = {"A", "D", "E"}          # each forces M+2 prime
R = {"C", "F"}               # each forces M+4 prime
SPECIAL = {3, 51, 141, 153, 201}      # mod 210
FAIL = []


def check(tag, got, want):
    ok = got == want
    print(f"  [{'ok ' if ok else 'FAIL'}] {tag:<62} {str(got):>12}  vs {str(want):>12}")
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


# the six positions as absolute cell indices, M = 6n+3
QUAD = {
    "A": lambda n: 6 * n * n + 10 * n + 4,
    "B": lambda n: 6 * n * n + 12 * n + 6,
    "C": lambda n: 6 * n * n + 14 * n + 8,
    "D": lambda n: 6 * n * n + 16 * n + 9,
    "E": lambda n: 6 * n * n + 18 * n + 11,
    "F": lambda n: 6 * n * n + 18 * n + 13,
}


def positions_from_definition(M):
    """E_M as offsets [IV, Thm 4], plus the sector's first cell."""
    off = (M * M + 1) // 6 + 1
    return [2 * M // 3 + off, M + 1 + off, 4 * M // 3 + 2 + off,
            5 * M // 3 + 2 + off, 2 * M + 3 + off, 2 * M + 5 + off]


def open_under(M, lines):
    """which of the six survive the given lines"""
    n = (M - 3) // 6
    out = set()
    for k in KEYS:
        m = QUAD[k](n)
        a, b = 6 * m - 1, 6 * m + 1
        if all(a % p and b % p for p in lines):
            out.add(k)
    return out


def sector_open(M, P):
    """the six that survive EVERY line p <= M, and the full survivor count"""
    n = (M - 3) // 6
    lo = (M * M + 1) // 6 + 1
    hi = ((M + 6) ** 2 - 1) // 6
    alive = np.ones(hi - lo + 1, dtype=bool)
    for p in P:
        if p > M:
            break
        if p < 5:
            continue
        r = pow(6, -1, p) % p
        alive[(r - lo) % p::p] = False
        alive[((p - r) % p - lo) % p::p] = False
    S = [lo + i for i in np.flatnonzero(alive)]
    E = {QUAD[k](n): k for k in KEYS}
    return len(S), {E[m] for m in S if m in E}, S, E


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fast", action="store_true")
    ap.add_argument("--deep", action="store_true")
    ap.add_argument("--force-fail", action="store_true")
    a = ap.parse_args()
    top = 3000 if a.fast else 20000
    spec_top = 30000 if a.deep else top

    print("--- the closed forms, and why the 35-class scan is exhaustive ---")
    bad = 0
    for n in range(1, 4000):
        M = 6 * n + 3
        if [QUAD[k](n) for k in KEYS] != positions_from_definition(M):
            bad += 1
    check("1.  six positions are the stated quadratics in n, for n < 4000", bad, 0)
    # each being a polynomial in n makes the state mod p a function of n mod p
    bad = 0
    for p in (5, 7):
        for n in range(0, 200):
            if open_under(6 * n + 3, [p]) != open_under(6 * (n + p) + 3, [p]):
                bad += 1
    check("2.  the state under a line p is periodic in n with period p", bad, 0)

    print("\n--- the {5,7} table, over all 35 classes ---")
    pats, mx = set(), 0
    zero = []
    for n in range(35):
        M = 6 * (n + 35 * 40) + 3
        o = open_under(M, [5, 7])
        mx = max(mx, len(o))
        if len(o) == 3:
            pats.add("".join(sorted(o)))
        if not o:
            zero.append(n)
    check("3.  max open after lines {5,7}", mx, 3)
    check("4.  the maximal patterns", sorted(pats), ["ABC", "AEF", "CDF", "CEF"])
    check("5.  classes closing all six (n mod 35)", sorted(zero), [0, 8, 23, 25, 33])
    check("6.  the same, as M mod 210",
          sorted({(6 * n + 3) % 210 for n in zero}), sorted(SPECIAL))

    print("\n--- larger lines do not lower the bound of three ---")
    for extra, want in ((11, 3), (13, 3)):
        lines = [5, 7] + [q for q in (11, 13) if q <= extra]
        per = 1
        for q in lines:
            per *= q
        m = max(len(open_under(6 * (n + per * 7) + 3, lines)) for n in range(per))
        check(f"7.  max open after lines {lines}", m, want)
    m5 = max(len(open_under(6 * (n + 5 * 40) + 3, [5])) for n in range(5))
    check("8.  line 5 alone leaves four", m5, 4)

    print(f"\n--- Corollary 7, over every sector M = 9 .. {top - 1} ---")
    P = primes_upto(2 * top)
    mx_tw = mx_no = 0
    n_tw = n_no = 0
    viol_force = viol_mix = viol_dicho = 0
    att3 = att2 = 0
    for M in range(9, top, 6):
        _, o, _, _ = sector_open(M, P)
        twin = isprime(M + 2) and isprime(M + 4)
        if (o & L) and not isprime(M + 2):
            viol_force += 1
        if (o & R) and not isprime(M + 4):
            viol_force += 1
        if "B" in o and not twin:
            viol_force += 1
        if twin:
            n_tw += 1
            mx_tw = max(mx_tw, len(o))
            att3 += (len(o) == 3)
        else:
            n_no += 1
            mx_no = max(mx_no, len(o))
            att2 += (len(o) == 2)
            if len(o) > 2:
                viol_dicho += 1
            if (o & L) and (o & R):
                viol_mix += 1
    check("9.  L/R forcing, violations", viol_force, 0)
    check("10. no mixing without the twin, violations", viol_mix, 0)
    check("11. max |S cap E| when (M+2,M+4) is a twin", mx_tw, 3)
    check("12. max |S cap E| when it is not", mx_no, 2)
    check("13. Corollary 7, violations", viol_dicho, 0)
    check("14. the bound three is attained", att3 > 0, True)
    check("15. the bound two is attained", att2 > 0, True)

    print(f"\n--- the five classes, M = 9 .. {spec_top - 1} ---")
    Pd = primes_upto(2 * spec_top)
    sect = cells = nontwin = 0
    minC = 10 ** 9
    nonempty = 0
    for M in range(9, spec_top, 6):
        if M % 210 not in SPECIAL:
            continue
        c, o, S, _ = sector_open(M, Pd)
        sect += 1
        cells += c
        minC = min(minC, c)
        if o:
            nonempty += 1
        nontwin += sum(1 for m in S if not (isprime(6 * m - 1) and isprime(6 * m + 1)))
    check("16. sectors in which S cap E is non-empty", nonempty, 0)
    check("17. open cells that are not twins", nontwin, 0)
    check("18. C_M is never zero", minC > 0, True)
    print(f"       ({sect} sectors, {cells} open cells, min C_M = {minC})")

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
