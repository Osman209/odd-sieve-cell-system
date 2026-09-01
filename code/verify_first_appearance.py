#!/usr/bin/env python3
"""
verify_first_appearance.py

A sieve cutoff z and a window length L are fixed.  Each integer m determines a
phase vector

    v_z(m) = ( m^2 mod p )_{5 <= p <= z},

because the sector at m begins at cell (m^2+3)/6 and a line p closes the two
cell classes n = +- 6^{-1} (mod p), so all the line sees of the sector is
m^2 mod p.  Only quadratic residues occur, so the reachable phase vectors are a
proper subset of the full CRT product.

Call a phase vector bad when it leaves the fewest cells open.  For each z this
script sweeps every reachable vector, i.e. every m = 3 (mod 6) modulo 6 Q_z with
Q_z = prod_{5 <= p <= z} p, and reports two things: the density of bad vectors,
and the least positive m realising one.

The quantity of interest is their product.  A random set of the same density
would have its least element at about 1 / density; the measured ratio is a small
constant, so nothing arithmetic delays the first appearance.

    python3 verify_first_appearance.py            # z = 13, 17, 19
    python3 verify_first_appearance.py --fast     # z = 13, 17
    python3 verify_first_appearance.py --self-test

Exits non-zero if any self-test fails.  Standard library plus numpy.
z = 19 sweeps 1,616,615 residues and takes a couple of minutes.
"""

import argparse
import sys

try:
    import numpy as np
except ImportError:
    sys.exit("this script needs numpy:  pip install numpy")


def primes_upto(n):
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


def cover_table(p, L):
    """For each s = m^2 mod p, the bitmask of window cells the line p closes.

    Cell j of the window holds the pair (m^2+6j+2, m^2+6j+4), so p closes it
    when 6j = -(s+2) or -(s+4) modulo p.
    """
    inv6 = pow(6, -1, p)
    table = np.zeros(p, dtype=np.uint64)
    for s in range(p):
        mask = 0
        for c in (2, 4):
            r = (-(s + c) * inv6) % p
            for j in range(r, L, p):
                mask |= 1 << j
        table[s] = np.uint64(mask)
    return table


def popcount(a):
    a = a.copy()
    out = np.zeros(a.shape, dtype=np.uint8)
    for _ in range(64):
        out += (a & np.uint64(1)).astype(np.uint8)
        a >>= np.uint64(1)
    return out


def sweep(z, L):
    """Survivor count for every m = 3 (mod 6) modulo 6*Q_z."""
    if L > 63:
        raise ValueError("window longer than a 64-bit mask")
    P = [p for p in primes_upto(z) if p >= 5]
    Q = 1
    for p in P:
        Q *= p
    m = np.arange(3, 6 * Q, 6, dtype=np.int64)
    acc = np.full(m.shape, (1 << L) - 1, dtype=np.uint64)
    for p in P:
        acc &= ~cover_table(p, L)[(m % p) * (m % p) % p]
    return m, popcount(acc), Q


def report(z, L):
    m, counts, Q = sweep(z, L)
    best = int(counts.min())
    hit = counts == best
    n_bad = int(hit.sum())
    total = len(m)
    least = int(m[hit].min())
    density = n_bad / total
    print(f"{z:5d} {L:5d} {best:9d} {n_bad:10d} {total:11d} "
          f"{1 / density:14.1f} {least:13,d} {least * density:9.2f}")
    return best, least, density


# ------------------------------------------------------------- self-tests ---

def self_test():
    ok = True

    def check(name, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print(f"  [{'ok ' if good else 'FAIL'}] {name:<56} {got!r:>20} vs {want!r}")

    print("--- the cover table is the sieve, checked against direct arithmetic ---")
    bad = 0
    for p in (5, 7, 11, 13):
        T = cover_table(p, 24)
        for mm in range(3, 400, 6):
            s = (mm * mm) % p
            direct = 0
            for j in range(24):
                lo, hi = mm * mm + 6 * j + 2, mm * mm + 6 * j + 4
                if lo % p == 0 or hi % p == 0:
                    direct |= 1 << j
            if int(T[s]) != direct:
                bad += 1
    check("mask disagreements with direct divisibility", bad, 0)

    print("--- the sweep agrees with a direct sieve of the actual sector ---")
    bad = 0
    for z, L in ((13, 24), (13, 36)):
        m, counts, Q = sweep(z, L)
        P = [p for p in primes_upto(z) if p >= 5]
        for mm in (3, 9, 15, 21, 39, 105, 501, 1005):
            idx = ((mm - 3) // 6) % (Q)
            direct = 0
            for j in range(L):
                lo, hi = mm * mm + 6 * j + 2, mm * mm + 6 * j + 4
                if all(lo % p and hi % p for p in P):
                    direct += 1
            if int(counts[idx]) != direct:
                bad += 1
    check("sweep vs direct sieve, 16 cases", bad, 0)

    print("--- reference values ---")
    b, least, dens = report_quiet(13, 36)
    check("z = 13: optimum, least m, bad count", (b, least), (8, 171))
    check("z = 13: bad residues out of 5005", round(1 / dens), 104)
    b, least, dens = report_quiet(17, 48)
    check("z = 17: optimum, least m", (b, least), (8, 8517))
    return ok


def report_quiet(z, L):
    m, counts, Q = sweep(z, L)
    best = int(counts.min())
    hit = counts == best
    return best, int(m[hit].min()), int(hit.sum()) / len(m)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fast", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    print("verify_first_appearance.py  --  bad square-phase vectors and when they first occur")
    print()
    if not self_test():
        print("\nSELF-TEST FAILED")
        return 1
    print("\nall self-tests passed\n")
    if args.self_test:
        return 0

    cases = [(13, 36), (17, 48)] if args.fast else [(13, 36), (17, 48), (19, 48)]
    print(f"{'z':>5} {'L':>5} {'optimum':>9} {'bad vectors':>10} {'residues':>11} "
          f"{'1 / density':>14} {'least m':>13} {'ratio':>9}")
    for z, L in cases:
        report(z, L)
    print()
    print("The last column is (least m) x density.  A random set of the same")
    print("density would give about 1.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
