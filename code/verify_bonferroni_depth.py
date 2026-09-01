#!/usr/bin/env python3
"""
verify_bonferroni_depth.py

Odd integers are written as cells C_n = (6n-1, 6n+1).  For M = 3 (mod 6) the
sector (M^2, (M+6)^2) is exactly the block of cell indices [a_r, a_{r+1}) with

    M = 6r+3,   a_r = 6r(r+1)+2,   length L_r = 12(r+1),

and a_{r+1} - a_r = L_r exactly, so consecutive sectors tile one fixed strip.
A line p closes exactly the two cell classes n = +- 6^{-1} (mod p), fixed once
and for all, so no sector carries a phase of its own.

Let m(d) be the number of lines p <= M striking cell d, and

    S_i = sum_d binom(m(d), i).

The odd Bonferroni truncations L_k = S_0 - S_1 + ... - S_k are lower bounds for
the survivor count C_M, and the alternating sum is EXACT as soon as
k >= max_d m(d), since a cell struck by m lines contributes the complete
alternating binomial sum (1-1)^m = 0.

This script checks that, checks the geometry, checks that an open cell outside
the six positions E_M is a twin pair, and tabulates max_d m(d) and the least
sufficient odd order against M.

    python3 verify_bonferroni_depth.py            # full table, to M = 10^6
    python3 verify_bonferroni_depth.py --fast     # short run
    python3 verify_bonferroni_depth.py --M 50001  # one sector
    python3 verify_bonferroni_depth.py --self-test

Exits non-zero if any self-test fails.  Standard library plus numpy.
"""

import argparse
import sys
from math import comb

try:
    import numpy as np
except ImportError:
    sys.exit("this script needs numpy:  pip install numpy")


# ----------------------------------------------------------------- primes ---

def primes_upto(n):
    """Primes <= n by a plain sieve."""
    if n < 2:
        return []
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    i = 2
    while i * i <= n:
        if s[i]:
            s[i * i::i] = bytearray(len(range(i * i, n + 1, i)))
        i += 1
    return [i for i in range(2, n + 1) if s[i]]


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            return False
        f += 2
    return True


# --------------------------------------------------------------- geometry ---

def sector(M):
    """First cell index and length of the sector (M^2, (M+6)^2)."""
    if M % 6 != 3:
        raise ValueError("M must be 3 (mod 6)")
    r = (M - 3) // 6
    return 6 * r * (r + 1) + 2, 12 * (r + 1)


def multiplicities(M, primes=None):
    """m(d) for every cell d of the sector: how many lines p <= M strike it."""
    a, L = sector(M)
    m = np.zeros(L, dtype=np.int32)
    for p in (primes if primes is not None else primes_upto(M)):
        if p < 5:
            continue
        if p > M:
            break
        inv6 = pow(6, -1, p)
        for c in (inv6 % p, (-inv6) % p):
            m[(c - a) % p::p] += 1
    return m, L


def bonferroni(m, L, orders):
    """L_k = S_0 - S_1 + ... - S_k, evaluated by the multiplicity form."""
    top = int(m.max())
    counts = np.bincount(m, minlength=top + 1)
    out = {}
    for k in orders:
        total = L
        for i in range(1, k + 1):
            S_i = sum(int(counts[x]) * comb(x, i) for x in range(i, top + 1))
            total += (-1) ** i * S_i
        out[k] = total
    return out


def least_sufficient_order(m, L):
    """Smallest odd k with L_k > 0, or None."""
    top = int(m.max())
    for k in range(1, top + 2, 2):
        if bonferroni(m, L, [k])[k] > 0:
            return k
    return None


# ------------------------------------------------------------- self-tests ---

def self_test():
    ok = True

    def check(name, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print(f"  [{'ok ' if good else 'FAIL'}] {name:<58} {got!r:>22} vs {want!r}")

    print("--- geometry ---")
    check("a_r = 6r(r+1)+2 at M = 9", sector(9)[0], 14)
    check("length 12(r+1) at M = 9", sector(9)[1], 24)
    check("sectors tile: a_{r+1} - a_r = L_r, r < 500",
          all(sector(6 * (r + 1) + 3)[0] - sector(6 * r + 3)[0] == sector(6 * r + 3)[1]
              for r in range(500)), True)

    print("--- Theorem 4: an open cell outside E_M is a twin pair ---")
    # The sector spans a gap of 6, so M+2 and M+4 are not switched on and an
    # open cell may still be composite.  E_M is the set of positions where that
    # can happen: the six products of M+2 and M+4 that fall inside the sector.
    def exception_positions(M):
        E = set()
        if is_prime(M + 2):
            E |= {2 * M // 3, M + 1, (5 * M) // 3 + 2, 2 * M + 3}
        if is_prime(M + 4):
            E |= {(4 * M) // 3 + 2, 2 * M + 5}
        return E

    bad = 0
    tested = 0
    for M in range(9, 2500, 6):
        m, L = multiplicities(M)
        a, _ = sector(M)
        E = exception_positions(M)
        for j in np.flatnonzero(m == 0):
            tested += 1
            n = a + int(j)
            lo, hi = 6 * n - 1, 6 * n + 1
            if is_prime(lo) and is_prime(hi):
                continue
            if int(j) not in E:          # composite and NOT a listed exception
                bad += 1
    check("open cells outside E_M that are not twins, M < 2500", bad, 0)
    check("open cells examined", tested > 5000, True)

    print("--- Bonferroni ---")
    bad = 0
    for M in (9, 21, 51, 105, 201, 381, 753, 1005):
        m, L = multiplicities(M)
        top = int(m.max())
        if bonferroni(m, L, [top])[top] != int((m == 0).sum()):
            bad += 1
    check("alternating sum at order max m(d) equals C_M", bad, 0)

    bad = 0
    for M in (105, 201, 381, 501, 753, 1005):
        m, L = multiplicities(M)
        C = int((m == 0).sum())
        for k in (1, 3, 5, 7):
            if k <= int(m.max()) and bonferroni(m, L, [k])[k] > C:
                bad += 1
    check("odd truncations never exceed C_M", bad, 0)

    print("--- reference values ---")
    m, L = multiplicities(21)
    check("M = 21: L_3 = C_M = 7", (bonferroni(m, L, [3])[3], int((m == 0).sum())), (7, 7))
    m, L = multiplicities(381)
    check("M = 381: L_7 = C_M = 47", (bonferroni(m, L, [7])[7], int((m == 0).sum())), (47, 47))
    m, L = multiplicities(1005)
    check("M = 1005: max m(d) = 9, least odd order = 7",
          (int(m.max()), least_sufficient_order(m, L)), (9, 7))
    return ok


# ------------------------------------------------------------------ table ---

def table(Ms):
    print(f"{'M':>9} {'cells':>9} {'C_M':>8} {'max m(d)':>9} {'least odd k':>12} "
          f"{'L_3':>12} {'L_5':>12} {'L_7':>12} {'L_9':>12}")
    for M in Ms:
        m, L = multiplicities(M)
        b = bonferroni(m, L, [3, 5, 7, 9])
        print(f"{M:9d} {L:9d} {int((m == 0).sum()):8d} {int(m.max()):9d} "
              f"{str(least_sufficient_order(m, L)):>12} "
              f"{b[3]:12d} {b[5]:12d} {b[7]:12d} {b[9]:12d}", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fast", action="store_true")
    ap.add_argument("--M", type=int, default=None)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    print("verify_bonferroni_depth.py  --  cell coordinates, sector (M^2,(M+6)^2)")
    print()
    if not self_test():
        print("\nSELF-TEST FAILED")
        return 1
    print("\nall self-tests passed\n")
    if args.self_test:
        return 0

    if args.M is not None:
        Ms = [args.M]
    elif args.fast:
        Ms = [1005, 5001, 10005]
    else:
        Ms = [1005, 5001, 10005, 50001, 100005, 200001, 500001, 1000005]
    table(Ms)
    return 0


if __name__ == "__main__":
    sys.exit(main())
