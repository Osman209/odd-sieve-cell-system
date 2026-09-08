#!/usr/bin/env python3
"""
verify_window_transfer.py

COVERS = ["[P2, S4.3]", "[P4, S2.1]", "[P4, S3.4]", "[P4, S3.5]", "[P6, S2.1]"]

Closes five measured tables that had no generator.

The moving-depth objects of [P4] are defined here as the paper's own numbers
require, which took four passes to pin and is worth stating once:

    u runs over the integers = 5 (mod 6);  v = u + 2, which is then also coprime
    to 6;  the window is (u^2, v^2) in cell coordinates;  it is sieved by every
    line q <= u;  a survivor is a CELL with both members surviving;  and
    P(u) = prod_{5<=q<=u} (1 - 2/q) as in [P4, Thm 3], C(u) the cell count.

    T(U) = sum_{u<=U} survivors,   M(U) = sum_{u<=U} C(u) P(u).

Note what that makes T: since every odd composite below v^2 has a prime factor
at most u, sieving to u leaves exactly the twin pairs, so T is a twin count and
not an estimate of one.

NOT reproduced: the binned row of [P4, S3.2].  The cumulative pair (T, M) at
U = 1019 and 2039 is reproduced here to 0.07 per cent and the deficit T - M to
one part in ten thousand, but neither a per-bin nor a cumulative reading of the
row itself comes out.  The row is left resting on its original run.

Modes:  --fast (seconds)   default (minutes)   --full (U = 2039)
"""
import sys, math
from sympy import primerange
import numpy as np

COVERS = ["[P2, S4.3]", "[P4, S2.1]", "[P4, S3.4]", "[P4, S3.5]", "[P6, S2.1]"]
FAST = "--fast" in sys.argv
FULL = "--full" in sys.argv
fails = 0
def check(name, ok, detail=""):
    global fails
    print(("  PASS  " if ok else "  FAIL  ") + name + ("   " + detail if detail else ""))
    if not ok: fails += 1
print("verify_window_transfer.py   mode:", "fast" if FAST else ("full" if FULL else "default"))
C2 = 0.6601618158468695

def sieve_cells(lo, hi, upto, primes):
    """cells strictly inside (lo, hi); returns (cell count, survivors of lines <= upto)"""
    b0 = lo//6 + 1; b1 = (hi - 1)//6
    if b1 < b0: return 0, 0
    b = np.arange(b0, b1 + 1, dtype=np.int64)
    keep = (6*b - 1 > lo) & (6*b + 1 < hi)
    C = int(keep.sum())
    for q in primes:
        if q > upto: break
        c = pow(6, -1, q)
        keep &= (b % q != c % q) & (b % q != (-c) % q)
    return C, int(keep.sum())

# ------------------------------------------------------------- [P2, S4.3]
print("\n1. [P2, S4.3]: the split at l = N")
PS = list(primerange(5, 20000))
rows = {3: (11, 2, 8, 4, 1, 2), 17: (67, 16, 60, 9, 0, 7), 167: (667, 119, 629, 47, 7, 31)}
if not FAST: rows[1667] = (6667, 857, 6500, 370, 20, 147)
ok = True; got = {}
for a, exp in rows.items():
    N = 4*a - 1; c0 = 6*a*a - 2*a + 1
    cells = np.arange(c0, c0 + N, dtype=np.int64)
    L = [q for q in primerange(5, 6*a + 2)]
    sm = np.zeros(N, dtype=bool); lg = np.zeros(N, dtype=bool)
    for q in L:
        c = pow(6, -1, q)
        hit = (cells % q == c % q) | (cells % q == (-c) % q)
        if q < N: sm |= hit
        else: lg |= hit
    got[a] = (N, sum(1 for q in L if q < N), int(sm.sum()),
              sum(1 for q in L if q >= N), int((lg & ~sm).sum()), int((~sm & ~lg).sum()))
    ok = ok and got[a] == exp
check("every row of the small-line / large-line split", ok, "a = 3 -> %s" % (got[3],))
check("the two groups and the twins exhaust the window",
      all(v[2] + v[4] + v[5] == v[0] for v in got.values()))

# ------------------------------------------------------------- [P4, S2.1]
print("\n2. [P4, S2.1]: the strip of L_7 cut by the squares")
exp = {(49,81): ([1,2], 2), (81,121): ([3,4,5], 3), (121,169): ([6,7,8], 3),
       (169,225): (list(range(9,13)), 4), (225,289): (list(range(13,18)), 5),
       (289,361): (list(range(18,23)), 5), (361,441): (list(range(23,29)), 6)}
ok = True
for (lo, hi), (ks, H) in exp.items():
    got_k = [k for k in range(0, 40) if lo < 7*(7 + 2*k) <= hi]
    ok = ok and got_k == ks and len(got_k) == H
check("the seven rows of the strip table", ok)

# ------------------------------------------------------------- [P4, S3.5]
print("\n3. [P4, S3.5]: the state space is the cycle")
exp = {13: (5, 15015), 31: (10, None), 59: (16, None), 101: (25, None)}
ok = True; det = []
for z, (nl, st) in exp.items():
    L = list(primerange(3, z + 1)); prod = math.prod(L)
    ok = ok and len(L) == nl and (st is None or prod == st)
    det.append("z=%d: %d lines, %.1e states" % (z, len(L), prod))
check("lines and states at the four cutoffs", ok, "; ".join(det))
check("the survivor count in one period is prod (q-2)",
      math.prod(q - 2 for q in primerange(5, 14)) == 3*5*9*11)

# ------------------------------------------------------------- [P6, S2.1]
print("\n4. [P6, S2.1]: C_M against Hardy-Littlewood and the sieve product")
rows = {1005: (2016, 87, 83.6, 104.7), 5001: (10008, 281, 273.2, 343.4)}
if not FAST: rows[10005] = (20016, 504, 467.3, 587.8)
if FULL: rows.update({20001: (40008, 796, 807.9, 1017.6), 50001: (100008, 1679, 1691.9, 2131.8)})
ok = True; det = []
for M, (cells, CM, hl, sp) in rows.items():
    C, s = sieve_cells(M*M, (M+6)**2, M, PS + list(primerange(20000, M+1)))
    W = 12*M + 36
    HL = 2*C2*W/math.log(M*M)**2
    SP = C*math.prod(1 - 2.0/q for q in primerange(5, M+1))
    ok = ok and C == cells and s == CM and abs(HL-hl) < 0.1 and abs(SP-sp) < 0.1
    det.append("M=%d: %d/%d/%.1f/%.1f" % (M, C, s, HL, SP))
check("every row of the C_M table", ok, "; ".join(det))

# ------------------------------------------------------------- [P4, S3.4]
print("\n5. [P4, S3.4]: T and M at moving depth, and Theorem 3's telescoping")
U = 199 if FAST else (2039 if FULL else 1019)
PP = list(primerange(5, U + 2))
T = 0; M = 0.0; P = 1.0; k = 0
for n in range(2, U + 1):
    while k < len(PP) and PP[k] <= n: P *= (1 - 2.0/PP[k]); k += 1
    if n % 6 != 5: continue
    C, s = sieve_cells(n*n, (n+2)**2, n, PP)
    T += s; M += C*P
print("     U = %d :  T = %.1f   M = %.1f   T - M = %.1f   T/M = %.4f" % (U, T, M, T-M, T/M))
if U == 1019:
    check("T and M at U = 1019 match the printed 2920.0 and 3535.3 to 0.1%",
          abs(T-2920)/2920 < 1e-3 and abs(M-3535.3)/3535.3 < 1e-3, "T = %d, M = %.1f" % (T, M))
if U == 2039:
    check("T - M at U = 2039 matches the printed -2143.2 to 0.1%",
          abs((T-M) + 2143.2)/2143.2 < 1e-3, "T - M = %.1f" % (T-M))
check("T/M sits near 0.80", 0.78 < T/M < 0.84, "%.4f" % (T/M))
from sympy import isprime as _isp
check("sieving to u leaves exactly the twin pairs of the window",
      all(sieve_cells(u*u, (u+2)**2, u, PP)[1] ==
          sum(1 for b in range(u*u//6 + 1, ((u+2)**2 - 1)//6 + 1)
              if 6*b-1 > u*u and 6*b+1 < (u+2)**2 and _isp(6*b-1) and _isp(6*b+1))
          for u in (5, 11, 17, 23, 29, 35, 41)),
      "so T is a twin count, not an estimate")
print("     for reference: (e^gamma/2)^2 = %.6f" % ((math.exp(0.5772156649015329)/2)**2))

print("\n%d of the checks failed." % fails)
sys.exit(0 if fails == 0 else 1)
