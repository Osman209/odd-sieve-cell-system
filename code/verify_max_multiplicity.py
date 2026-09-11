#!/usr/bin/env python3
"""
verify_max_multiplicity.py

COVERS = ["[P6, S2.9]"]

Regenerates the multiplicity material of [P6, S2.9] in its corrected form.

For a sector M = 3 (mod 6), M >= 9, the cells of (M^2, (M+6)^2) have indices
b = a, ..., a + N - 1 with a = (M^2+3)/6 and N = 2M+6, and

    m(b) = #{ p prime, 5 <= p <= M : p | (6b-1)(6b+1) },    m_*(M) = max_b m(b).

Both endpoints exceed M^2 >= p^2, so every such divisibility is an active strike.

Three statements are checked.

(1) The two-sided bound  K(2M+6) <= m_*(M) <= K((M+6)^4),  where K(t) is the
    largest k with p_1...p_k <= t and p_1 = 5, p_2 = 7, ...  The lower bound is
    constructive: 6b = 1 (mod Q_k) has a solution class, and any N >= Q_k
    consecutive indices contain it.  Hence m_* = Theta(log M / log log M), not
    O(log log M): the mean of m(b) is ~ 2 log log M and the maximum is not
    controlled by the mean.

(2) The exact Bonferroni remainder, for every odd j:

        C_M - L_j = sum over b with m(b) > j of binomial(m(b)-1, j),

    every summand positive, so L_j = C_M if and only if j >= m_*(M).  The
    termination order is therefore necessary as well as sufficient.

(3) The published tables of the section: the L_j rows and the max-multiplicity
    row, and the fact that the printed claim "order five is exact through
    M = 141" is contradicted by the row at M = 105 (20 against 21).

It also records the measurement that the accessible range does NOT separate the
two candidate orders: over the tabulated M both m_*/(2 log log M) and
m_*/(log M / log log M) sit between 2.0 and 2.6.  The correction rests on the
construction in (1), not on the finite data.

Modes:  --fast (tabulated M only)   default (adds M = 9, 15, ..., 999)
        --full (adds M = 1005, 5001, 10005, 50001, 100005, 200001)
"""
import sys, math
import numpy as np
from sympy import primerange

COVERS = ["[P6, S2.9]"]
FAST = "--fast" in sys.argv
FULL = "--full" in sys.argv
fails = 0


def check(name, ok, detail=""):
    global fails
    print(("  PASS  " if ok else "  FAIL  ") + name + ("   " + detail if detail else ""))
    if not ok:
        fails += 1


print("verify_max_multiplicity.py   mode:",
      "fast" if FAST else ("full" if FULL else "default"))


def mults(M):
    a, N = (M * M + 3) // 6, 2 * M + 6
    m = np.zeros(N, dtype=np.int32)
    for p in primerange(5, M + 1):
        inv6 = pow(6, -1, p)
        for t in (1, -1):
            start = ((t * inv6) % p - a) % p
            m[start::p] += 1
    return m


PRIMES = list(primerange(5, 10**6))


def K(t):
    q, k = 1, 0
    for p in PRIMES:
        if q * p > t:
            break
        q *= p
        k += 1
    return k


def Q(k):
    q = 1
    for p in PRIMES[:k]:
        q *= p
    return q


# ------------------------------------------------------------- the two-sided bound
Ms = [9, 15, 21, 51, 105, 141, 201, 381, 501, 753]
if not FAST:
    Ms = sorted(set(Ms) | set(range(9, 1000, 6)))
if FULL:
    Ms = sorted(set(Ms) | {1005, 5001, 10005, 50001, 100005, 200001})

bad_lo = bad_hi = bad_rem = 0
witness_ok = 0
for M in Ms:
    m = mults(M)
    ms = int(m.max())
    lo, hi = K(2 * M + 6), K((M + 6) ** 4)
    if ms < lo:
        bad_lo += 1
    if ms > hi:
        bad_hi += 1
    # the constructive witness of the lower bound really is struck k times
    k = lo
    if k:
        a, N = (M * M + 3) // 6, 2 * M + 6
        qk = Q(k)
        b = a + ((pow(6, -1, qk) - a) % qk)
        if b < a + N and int(m[b - a]) >= k:
            witness_ok += 1
    C = int((m == 0).sum())
    for j in (1, 3, 5, 7, 9, 11):
        Lj = int(sum(sum((-1) ** i * math.comb(int(x), i) for i in range(j + 1)) for x in m)) \
             if M <= 1005 else None
        if Lj is None:
            continue
        rem = int(sum(math.comb(int(x) - 1, j) for x in m if x > j))
        if C - Lj != rem:
            bad_rem += 1

check("m_* is at least K(2M+6) in every sector tested", bad_lo == 0, "%d sectors" % len(Ms))
check("m_* is at most K((M+6)^4) in every sector tested", bad_hi == 0)
check("the constructive witness is struck by all K(2M+6) primes",
      witness_ok == sum(1 for M in Ms if K(2 * M + 6) > 0),
      "%d witnesses" % witness_ok)
check("the exact remainder identity C_M - L_j = sum binom(m-1, j) holds at every odd j",
      bad_rem == 0)

# ---------------------------------------------------------------- published tables
paper_L = {9: (7, 10, 10, 10, 10), 15: (1, 11, 11, 11, 11), 21: (-13, 7, 7, 7, 7),
           51: (-72, 2, 10, 10, 10), 105: (-208, -27, 20, 21, 21),
           141: (-313, -76, 25, 29, 29), 201: (-501, -191, 19, 28, 28),
           381: (-1104, -492, 8, 47, 47), 501: (-1538, -839, -40, 46, 47),
           753: (-2490, -1431, -93, 74, 75)}
bad_tab = 0
for M, want in paper_L.items():
    m = mults(M)
    C = int((m == 0).sum())
    row = tuple(int(sum(sum((-1) ** i * math.comb(int(x), i) for i in range(j + 1)) for x in m))
                for j in (1, 3, 5, 7)) + (C,)
    if row != want:
        bad_tab += 1
        print("      row M = %d: %s against %s" % (M, row, want))
check("every row of the published L_j table reproduces", bad_tab == 0)

m105, m141 = mults(105), mults(141)
L5 = lambda m: int(sum(sum((-1) ** i * math.comb(int(x), i) for i in range(6)) for x in m))
check("order five is NOT exact at M = 105 (20 against 21), so the printed "
      "\"exact through M = 141\" is wrong",
      L5(m105) == 20 and int((m105 == 0).sum()) == 21
      and L5(m141) == 25 and int((m141 == 0).sum()) == 29)

if FULL:
    want = {1005: 9, 5001: 9, 10005: 10, 50001: 11, 100005: 11, 200001: 12}
    ok = all(int(mults(M).max()) == v for M, v in want.items())
    check("the published max-multiplicity row reproduces", ok)
    print("      M        m_*   m_*/(2 loglog M)   m_*/(log M/loglog M)")
    r1, r2 = [], []
    for M in sorted(want):
        ms = int(mults(M).max())
        L = math.log(M)
        a1, a2 = ms / (2 * math.log(L)), ms / (L / math.log(L))
        r1.append(a1)
        r2.append(a2)
        print("   %7d %6d %14.2f %19.2f" % (M, ms, a1, a2))
    check("the accessible range does not separate the two candidate orders: both "
          "ratios stay inside [2.0, 2.6]",
          all(2.0 <= x <= 2.6 for x in r1 + r2),
          "%.2f-%.2f and %.2f-%.2f" % (min(r1), max(r1), min(r2), max(r2)))

print("\n%d of the checks failed." % fails)
sys.exit(0 if fails == 0 else 1)
