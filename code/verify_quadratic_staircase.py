#!/usr/bin/env python3
"""
verify_quadratic_staircase.py  --  generator for Paper 1,
"An Exact Histogram for a Quadratic Staircase".

W_j = floor(2(j+1)^2/n) - floor(2j^2/n),  r_j = 2j^2 mod n,  A = floor((n+7)/8).

Covers Theorem 1, the symmetries (2.1), Theorem 2 with its sample table, the
probabilistic model, the carry-count identity of Sec. 3.1, Theorem 2b with the
mirror, Theorems 3 and 4 with their tables, identity (5.1), the Lemma of
Sec. 5.5, and Theorem 5 with its five exceptions.

Section 8 holds what the current revision added or sharpened: the model sum
evaluated exactly, the agreement of the strict and the weak reading of a
maximum from n = 11 on, the exhaustive pass over odd 3 <= n <= 49 that carries
the exception list of Theorem 5, the range of a_x in the Lemma and the closed
form of the four values, and the cancellation at n = 17, 25 that makes the two
exception lists differ.

Modes:  --fast (seconds)   default (minutes)   --full (wider ranges)

Note on ranges.  Theorem 5 is checked here to 20,001 by default and 100,001
under --full.  The paper states it exhaustively to 200,001; that run is
O(sum n) and was not repeated here, so the 200,001 in the paper rests on the
original computation, not on this script.
"""

COVERS = ["[P1, all sections]"]

import sys, math
import numpy as np

FAST = "--fast" in sys.argv
FULL = "--full" in sys.argv
def rng(fast, default, full): return fast if FAST else (full if FULL else default)

fails = 0
def check(name, ok, detail=""):
    global fails
    print(("  PASS  " if ok else "  FAIL  ") + name + ("   " + detail if detail else ""))
    if not ok: fails += 1

def Wvec(n):
    j = np.arange(n + 1, dtype=np.int64)
    F = (2 * j * j) // n
    return np.diff(F)                     # W_0 .. W_{n-1}

def A_of(n): return (n + 7) // 8
def odds(a, b): return range(a | 1, b + 1, 2)

print("verify_quadratic_staircase.py  (Paper 1)   mode:",
      "fast" if FAST else ("full" if FULL else "default"))

# ------------------------------------------------------------ Theorem 1 + (2.1)
N1 = rng(2001, 20001, 20001)
print("\n1. Theorem 1 and the symmetries (2.1),  odd n <= %d" % N1)
bad = sym = 0
for n in odds(3, N1):
    W = Wvec(n)
    if W.min() < 0 or W.max() > 4: bad += 1
    if not (np.all(W + W[::-1] == 4) and W[(n - 1) // 2] == 2): sym += 1
check("W_j lies in {0,1,2,3,4} for every odd n and every j <= n-1", bad == 0)
check("W_j + W_{n-1-j} = 4 and W_{(n-1)/2} = 2", sym == 0)

# ------------------------------------------------------------------ Theorem 2
N2 = rng(2001, 200001, 200001)
print("\n2. Theorem 2: the exact multiplicities,  odd n <= %d" % N2)
bad = 0
for n in odds(3, N2):
    A = A_of(n); H2 = (n + 1) // 2
    c = np.bincount(Wvec(n), minlength=5)
    if not (c[0] == c[4] == A and c[2] == 2 * A - 1 and c[1] == c[3] == H2 - 2 * A): bad += 1
check("the five multiplicities are exactly as stated", bad == 0,
      "%d odd n tested" % len(list(odds(3, N2))))
rows = {11: (2,2,3,2,2), 101: (13,25,25,25,13), 1009: (127,251,253,251,127),
        19997: (2500,4999,4999,4999,2500)}
ok = all(tuple(np.bincount(Wvec(n), minlength=5)) == r for n, r in rows.items())
check("the four sample rows of the table are reproduced", ok,
      "n = 101 gives %s, A = %d" % (tuple(np.bincount(Wvec(101), minlength=5)), A_of(101)))

dev = 0.0
for n in odds(3, rng(2001, 20001, 20001)):
    est = sum((n - 4 * j - 2) / n for j in range((n - 2) // 4 + (1 if (n - 2) % 4 else 0)))
    dev = max(dev, abs(est - A_of(n)))
check("the probabilistic model never deviates from N_0 by more than 0.889",
      dev < 0.889 + 1e-9, "largest deviation %.4f" % dev)

# ------------------------------------------------ Sec. 3.1: the carry identity
print("\n3. Sec. 3.1: the carry-count identity, general k")
def carry_ok(k, n):
    j = np.arange(n + 1, dtype=np.int64)
    W = np.diff((k * j * j) // n)
    N = np.bincount(W, minlength=2 * k + 1)
    prev = 0
    for q in range(2 * k):
        a = -((-(q * n - k)) // (2 * k))
        b = -((-((q + 1) * n - k)) // (2 * k)) - 1
        L = b - a + 1
        C = 0 if L <= 0 else (k * (b + 1) ** 2) // n - (k * a * a) // n - q * L
        if L < 0: L = 0
        if N[q] != L - C + prev: return False
        prev = C
    return N[2 * k] == prev
pairs = 0
bad = 0
for k in range(2, 11):
    for n in odds(3, rng(399, 3999, 3999)):
        pairs += 1
        if not carry_ok(k, n): bad += 1
check("carry identity holds on every (k,n) pair, k = 2..10, n odd", bad == 0,
      "%d pairs" % pairs)
pe = be = 0
for k in range(2, 11):
    for n in range(4, rng(400, 890, 890), 2):
        pe += 1
        if not carry_ok(k, n): be += 1
check("it also holds for even n, which Theorem 2 excludes", be == 0, "%d pairs" % pe)
bl = 0
for k in (50, 100, 200, 400):
    for n in odds(3, 401):
        if not carry_ok(k, n): bl += 1
check("and for k up to 400 on a shorter n range", bl == 0)

# ----------------------------------------------------------------- Theorem 2b
def alpha_beta(n, m):
    S = n * n - 8 * n * (m - 1)
    x = int((n - math.isqrt(S)) // 4)
    while 4 * (x + 1) <= n and (n - 4 * (x + 1)) ** 2 >= S: x += 1
    while x > 0 and not (n - 4 * x >= 0 and (n - 4 * x) ** 2 >= S): x -= 1
    y = int((n + math.isqrt(S)) // 4)
    while not (4 * y - n >= 0 and (4 * y - n) ** 2 >= S): y += 1
    while 4 * (y - 1) - n >= 0 and (4 * (y - 1) - n) ** 2 >= S: y -= 1
    return x, y - 1

N2b = rng(2001, 20001, 20001)
print("\n4. Theorem 2b: where the increments are,  odd n <= %d" % N2b)
bad = badmax = 0; cnt = 0
for n in odds(3, N2b):
    A = A_of(n); H = (n - 1) // 2; W = Wvec(n)
    al = set(); be = set()
    for m in range(1, A + 1):
        a, b = alpha_beta(n, m)
        al.add(a)
        if m >= 2: be.add(b)
    for j in range(H):
        want = 0 if j in al else (2 if j in be else 1)
        if W[j] != want: bad += 1; break
    D = np.arange(n + 1, dtype=np.int64) - (2 * np.arange(n + 1, dtype=np.int64) ** 2) // n
    if D.max() != A or len(al) != A: badmax += 1
    cnt += 1
check("W = 0 exactly at the alpha_m and W = 2 exactly at the beta_m", bad == 0,
      "%d odd n" % cnt)
check("max_j D_j = A and |{alpha_m}| = A recovers N_0 = A", badmax == 0)
bad = 0
for n in odds(3, rng(399, 3999, 3999)):
    A = A_of(n)
    for m in range(1, A + 1):
        a, b = alpha_beta(n, m)
        if not (a < n / 4 and (m < 2 or b + 1 > n / 4)): bad += 1
check("the two families are separated by the peak at n/4", bad == 0)
bad = 0; mp = 0
for n in odds(3, rng(299, 1499, 1499)):
    A = A_of(n); H = (n - 1) // 2
    for m in range(1, A + 1):
        a, b = alpha_beta(n, m)
        S = n * n - 8 * n * (m - 1)
        eps = 0 if ((n - math.sqrt(S)) / 4) % 1 < 0.5 else 1
        mp += 1
        if b != H - a - eps: bad += 1
check("the mirror beta_m = H - alpha_m - eps_m", bad == 0, "%d pairs (n,m)" % mp)

# ------------------------------------------------------------ Theorems 3 and 4
print("\n5. Theorems 3 and 4: the symmetric pairs")
def d_n(n, R): return (n + (R + 2) ** 2) // (2 * n) - (n + R * R) // (2 * n)
bad = 0
for n in odds(3, rng(199, 599, 599)):
    W = Wvec(n)
    for R in range(1, n - 1, 2):
        d = d_n(n, R)
        jR = (n + R) // 2; jL = n - 1 - jR
        if d not in (0, 1, 2) or W[jR] != 2 + d or W[jL] != 2 - d: bad += 1; break
check("d_n(R) in {0,1,2} and (W_L, W_R) = (2-d, 2+d)", bad == 0)
bad = 0
for n in odds(3, rng(499, 1999, 1999)):
    c = np.bincount([d_n(n, R) for R in range(1, n - 1, 2)], minlength=3)
    if c[2] != c[0] + 1: bad += 1
check("Theorem 4: P_2 = P_0 + 1", bad == 0)
t4 = {11: (1,2,2), 13: (1,3,2), 31: (3,8,4), 101: (12,25,13), 499: (62,124,63)}
ok = all(tuple(np.bincount([d_n(n, R) for R in range(1, n - 1, 2)], minlength=3)) == r
         for n, r in t4.items())
check("the five sample rows of the Theorem 4 table", ok)

# ------------------------------------------------------- identity (5.1), Lemma
print("\n6. Identity (5.1) and the Lemma of Sec. 5.5")
def Phi(n, x): return (2 * x * x) // n + (2 * (x - 1) ** 2) // n
def mixed_direct(n):
    j = np.arange(n + 1, dtype=np.int64)
    r = (2 * j * j) % n
    eps = (r[1:] < r[:-1]).astype(np.int8)      # eps_0 .. eps_{n-1}
    H = (n - 1) // 2
    return int(np.sum(eps[0:H] != eps[1:H + 1]))
def mixed_formula(n):
    H = (n - 1) // 2
    l1 = -((-n) // 8); b1 = -((-(n - 2)) // 4); l2 = -((-n) // 4)
    b2 = -((-(n + 2)) // 4); l3 = -((-3 * n) // 8)
    S = 2 * (b1 - l1) - (l2 - b1) + 3 * (b2 - l2) - 2 * (l3 - b2) + 4 * (H - l3) - 3
    return 2 * (Phi(n, l1) - Phi(n, b1) + Phi(n, l2) - Phi(n, b2) + Phi(n, l3) - Phi(n, H)) \
           + Phi(n, H + 1) + S
bad = 0
for n in odds(9, rng(2001, 20001, 20001)):
    if mixed_formula(n) != mixed_direct(n): bad += 1
check("identity (5.1) matches the direct mixed count", bad == 0)
K = {1: 13, 3: 7, 5: 25, 7: 19}
exc = []
for n in odds(3, rng(20001, 300001, 300001)):
    r = n % 8
    if Phi(n, -((-n) // 8)) + Phi(n, -((-3 * n) // 8)) != (5 * n - K[r]) // 8: exc.append(n)
check("the Lemma holds apart from n = 3,5,7,9,17,25,49", exc == [3,5,7,9,17,25,49],
      "exceptions found: %s" % exc)

# ------------------------------------------------------------------ Theorem 5
N5 = rng(2001, 20001, 100001)
print("\n7. Theorem 5: exactly 2A interior local maxima of 2j^2 mod n,  odd n <= %d" % N5)
exc = []
for n in odds(3, N5):
    j = np.arange(n, dtype=np.int64)
    r = (2 * j * j) % n
    lm = int(np.sum((r[1:-1] > r[:-2]) & (r[1:-1] > r[2:])))
    if lm != 2 * A_of(n): exc.append(n)
check("the only exceptions are n = 3, 5, 7, 9, 49", exc == [3, 5, 7, 9, 49],
      "exceptions found: %s" % exc)
check("and the count equals the mixed count of Step 2 for n >= 51",
      all(mixed_direct(n) == 2 * A_of(n) for n in odds(51, min(N5, 4001))))


# ------------------------------------------- 8. what the current revision added
print("\n8. The statements added or sharpened in the current revision")

# 8.1  the model sum, evaluated exactly rather than bounded ------------------
from fractions import Fraction
bad = big = 0; worst = (0.0, 0)
for n in odds(3, rng(2001, 20001, 20001)):
    m = (n + 1) // 4
    terms = (n - 2) // 4 + (1 if (n - 2) % 4 else 0)
    # sum_{j<m} (n-4j-2)/n = (m*n - 2m^2)/n, and that is (n^2-1)/(8n)
    if terms != m or 8 * (m * n - 2 * m * m) != n * n - 1: bad += 1
    d = 8 * n * A_of(n) - (n * n - 1)          # n * (A - model) * 8
    if not (0 <= d < 8 * n): big += 1
    if d / (8.0 * n) > worst[0]: worst = (d / (8.0 * n), n)
check("the model's sum is exactly (n^2-1)/(8n) = m - 2m^2/n", bad == 0)
check("A - model lies in [0,1) for every odd n", big == 0,
      "largest %.4f at n = %d" % worst)
lit = sum(Fraction(n - 4 * j - 2, n) for n in [9] for j in range(2))
check("at n = 9 the model gives 10/9 against a true count of 2",
      lit == Fraction(10, 9) and A_of(9) == 2)
bad = 0
for n in odds(3, rng(199, 999, 999)):
    m = (n + 1) // 4
    if sum(Fraction(n - 4 * j - 2, n) for j in range(m)) != Fraction(n * n - 1, 8 * n): bad += 1
check("the literal sum agrees with the closed form (small range, exact rationals)", bad == 0)

# 8.2  the two readings of a maximum ----------------------------------------
def strict_lm(n):
    j = np.arange(n, dtype=np.int64); r = (2 * j * j) % n
    return int(np.sum((r[1:-1] > r[:-2]) & (r[1:-1] > r[2:])))
def weak_lm(n):
    j = np.arange(n, dtype=np.int64); r = (2 * j * j) % n
    eps = (r[1:] < r[:-1]).astype(np.int8)          # eps_0 .. eps_{n-2}
    return int(np.sum((eps[:-1] == 0) & (eps[1:] == 1)))
diff = [n for n in odds(3, rng(2001, 20001, 20001)) if strict_lm(n) != weak_lm(n)]
check("the strict and the weak reading agree for every odd n >= 11",
      diff == [5, 7, 9], "they differ exactly at %s" % diff)

bad = 0
for n in odds(3, rng(999, 4001, 4001)):
    j = np.arange(n, dtype=np.int64); r = (2 * j * j) % n
    H = (n - 1) // 2
    ties = [i for i in range(1, n) if r[i] == r[i - 1]]
    if ties != [H + 1] or r[H] != (n + 1) // 2: bad += 1
    if n > 9 and r[H - 1] != (n + 9) // 2: bad += 1
check("the only tie is at j = H+1, with r_H = (n+1)/2 and r_{H-1} = (n+9)/2 for n > 9",
      bad == 0)
j1 = [n for n in odds(3, rng(999, 4001, 4001))
      if (2 * 1 * 1) % n > 0 and (2 * 1 * 1) % n > (2 * 4) % n]
check("j = 1 is a strict maximum only at n = 7", j1 == [7], "found %s" % j1)

# 8.3  Theorem 5: the finite part of the proof -------------------------------
finite = [n for n in odds(3, 49) if strict_lm(n) != 2 * A_of(n)]
check("odd 3 <= n <= 49 exhaustively: the failures are 3, 5, 7, 9, 49",
      finite == [3, 5, 7, 9, 49] and len(list(odds(3, 49))) == 24,
      "twenty-four values, failures %s" % finite)

# 8.4  Step 4, and identity (5.1) at n = 49 ----------------------------------
def order_ok(n):
    H = (n - 1) // 2
    l1 = -((-n) // 8); b1 = -((-(n - 2)) // 4); l2 = -((-n) // 4)
    b2 = -((-(n + 2)) // 4); l3 = -((-3 * n) // 8)
    return 1 < l1 <= b1 <= l2 <= b2 < l3 < H
check("the Step-4 ordering holds exactly from n = 13 on",
      [n for n in odds(3, 999) if not order_ok(n)] == [3, 5, 7, 9, 11])
check("identity (5.1) holds at n = 49, where Theorem 5 fails",
      mixed_formula(49) == mixed_direct(49) == 16 == 2 * A_of(49) + 2)

# 8.5  the Lemma: the range of a_x and its closed form -----------------------
def e_data(n):
    t, r = n // 8, n % 8
    m = -((-3 * r) // 8)
    return [t, t + 1, 3 * t + m - 1, 3 * t + m], [-r, 8 - r, 8 * m - 8 - 3 * r, 8 * m - 3 * r], r
bad_e = bad_a = 0
for n in odds(51, rng(2001, 20001, 60001)):
    xs, es, r = e_data(n)
    if any((8 * x - e) % n for x, e in zip(xs, es)) or sorted(abs(e) for e in es) != [1, 3, 5, 7]:
        bad_e += 1; continue
    a = [(32 * ((2 * x * x) % n) - e * e) // n for x, e in zip(xs, es)]
    if (any(not (1 <= v < 32) for v in a) or sorted(a) != sorted([8 - r, 16 - r, 24 - r, 32 - r])
            or sum(a) != 80 - 4 * r):
        bad_a += 1
check("8x = e_x mod n with |e_x| a permutation of 1,3,5,7   (n >= 51)", bad_e == 0)
check("a_x lies in [1,32) and the four are {8-r, 16-r, 24-r, 32-r}, summing to 80-4r",
      bad_a == 0)
check("the squares of 1,3,5,7 are the four classes = 1 mod 8 inside mod 32",
      sorted((x * x) % 32 for x in (1, 3, 5, 7)) == [1, 9, 17, 25])

def lemma_gap(n):
    K2 = {1: 13, 3: 7, 5: 25, 7: 19}
    return Phi(n, -((-n) // 8)) + Phi(n, -((-3 * n) // 8)) - (5 * n - K2[n % 8]) // 8
def linear_gap(n):
    t, r = n // 8, n % 8
    c = {1: 3, 3: -1, 5: 1, 7: -3}[r]
    b1 = -((-(n - 2)) // 4); l2 = -((-n) // 4); b2 = -((-(n + 2)) // 4)
    return (-Phi(n, b1) + Phi(n, l2) - Phi(n, b2)) - (-2 * t + c)
bad = 0
for n in (9, 17, 25, 49):
    xs, es, r = e_data(n)
    a = [(32 * ((2 * x * x) % n) - e * e) // n for x, e in zip(xs, es)]
    if not (any(e * e >= n for e in es) and sum(a) == 80 - 4 * r - 32 and lemma_gap(n) == 1):
        bad += 1
check("at 9, 17, 25, 49 some e_x^2 >= n, sum a_x is short by 32, the Lemma by 1", bad == 0)
check("17 and 25: the Lemma is +1 and the linear part -1, so they cancel",
      all(lemma_gap(n) == 1 and linear_gap(n) == -1 for n in (17, 25)))
check("49: the Lemma is +1 and the linear part 0, so the count is 2A+2",
      lemma_gap(49) == 1 and linear_gap(49) == 0)

# 8.6  the abstract's two corrected descriptions -----------------------------
bad = 0
for n in odds(3, rng(299, 2001, 2001)):
    for j in range(n):
        if j - (2 * j * j) // n != -((-(j * (n - 2 * j))) // n): bad += 1; break
check("D_j = j - floor(2j^2/n) = ceil(j(n-2j)/n), the object Theorem 2b quantises",
      bad == 0)
nc = [n for n in odds(3, 299) if bool(np.any(np.diff(Wvec(n)) < 0))]
check("floor(2j^2/n) is not convex, so the abstract says 'non-decreasing' instead",
      len(nc) > 100, "%d of %d odd n < 300" % (len(nc), len(list(odds(3, 299)))))

# 8.7  the sample data of Appendix A -----------------------------------------
H101 = 50
l1 = -((-101) // 8); b1 = -((-99) // 4); l2 = -((-101) // 4)
b2 = -((-103) // 4); l3 = -((-303) // 8)
bnds = [1, l1, b1, l2, b2, l3, H101, H101 + 1]
check("n = 101: six of the seven intervals carry indices",
      sum(1 for a, b in zip(bnds[:-1], bnds[1:]) if b > a) == 6, "boundaries %s" % bnds)
check("n = 17: six interior maxima and 2A = 6", strict_lm(17) == 2 * A_of(17) == 6)

print("\n%d of the checks failed." % fails)
sys.exit(0 if fails == 0 else 1)
