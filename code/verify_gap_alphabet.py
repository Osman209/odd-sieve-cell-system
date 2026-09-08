#!/usr/bin/env python3
"""
verify_gap_alphabet.py   --   generator for Paper 5, "The Gap Alphabet".

Covers Theorem 1, Theorem 2, Theorem 3 and Corollary 1, and regenerates the
run-length census quoted in the Verification note of Sec. 2.3.

ON THAT CENSUS.  Releases up to v2.0.0 described it as "sieve depth 97 over
6e7 cells".  The range is wrong: the four published counts are reproduced
here exactly at 4e7, and the survivor total 14,437,300 gives a density of
0.360932 against prod_{5<=q<=97}(1-1/q) = 0.360951, which pins the range
independently of the counts.  Everything else in the note is correct.

The census convention, now made explicit because three different objects
give visibly different numbers:
  * the UPPER rail 6b+1, with b running from 0 to 4e7;
  * survivors are the members coprime to every prime from 5 to 97,
    i.e. the birth-at-p^2 rule of [P2] is NOT applied here.
The lower rail 6b-1 gives 6,448,103 / 2,403,803 / 779,340 / 210,868 instead,
and under the birth rule it carries one run of length five - which is the
exception 5, 11, 17, 23, 29 of Theorem 3.  The claim "none of length 5 or
more" is a statement about the upper rail under the stated convention.

Modes:  --fast (seconds)   default (minutes)   --full (published ranges)
"""

COVERS = ["[P5, all sections]"]

import sys, math
import numpy as np

FAST = "--fast" in sys.argv
FULL = "--full" in sys.argv
GAP_N   = 10**6 if FAST else (2*10**9 if FULL else 10**8)
CENSUS_N= 10**6 if FAST else 40_000_000
AP_N    = 20_000 if FAST else 200_000

fails = 0
def check(name, ok, detail=""):
    global fails
    print(("  PASS  " if ok else "  FAIL  ") + name + ("   " + detail if detail else ""))
    if not ok: fails += 1

def small_primes(n):
    s = np.ones(n+1, dtype=bool); s[:2] = False
    for i in range(2, int(n**0.5)+1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]

def odd_segments(limit, seg=10**8):
    """yield (lo, is_prime_array) over odd n in [lo, lo+seg), lo odd."""
    base = int(limit**0.5) + 1
    ps = small_primes(base)
    ps = ps[ps >= 3]
    lo = 3
    while lo <= limit:
        hi = min(lo + seg - 1, limit)
        arr = np.ones((hi - lo)//2 + 1, dtype=bool)
        for p in ps:
            start = max(p*p, ((lo + p - 1)//p)*p)
            if start % 2 == 0: start += p
            if start > hi: continue
            arr[(start - lo)//2::p] = False
        if lo == 3:
            pass                      # 3,5,7 correctly left prime
        yield lo, hi, arr
        lo = hi + 1
        if lo % 2 == 0: lo += 1

print("verify_gap_alphabet.py  (Paper 5)   mode:",
      "fast" if FAST else ("full" if FULL else "default"),
      "  gaps to %g, census to %g" % (GAP_N, CENSUS_N))

# ---------------------------------------------------------------- Theorem 1
print("\n1. Theorem 1: the alphabet {2,4,6}")
counts = {2:0, 4:0, 6:0}
other = []
recip = {2:0.0, 4:0.0, 6:0.0}
first6 = None
prev = None
for lo, hi, isp in odd_segments(GAP_N):
    n = lo + 2*np.nonzero(~isp)[0]
    n = n[n >= 9]
    if n.size == 0: continue
    if prev is not None:
        n = np.concatenate(([prev], n))
    g = np.diff(n)
    for h in (2, 4, 6):
        m = (g == h)
        counts[h] += int(m.sum())
        recip[h]  += float(np.sum(1.0/n[:-1][m]))
    bad = g[(g != 2) & (g != 4) & (g != 6)]
    if bad.size: other.extend(bad.tolist()[:5])
    if first6 is None:
        w = np.nonzero(g == 6)[0]
        if w.size: first6 = int(n[w[0]])
    prev = int(n[-1])
check("every gap between consecutive odd composites is 2, 4 or 6", not other,
      "%d gaps examined" % sum(counts.values()))
check("the maximum gap is 6, first attained at 9", first6 == 9, "first at %s" % first6)

# every gap-6 interval below 3e5 holds a twin pair, and there are 2,992 of them
lim = 300_000
sp = small_primes(lim + 10)
isprime = np.zeros(lim + 11, dtype=bool); isprime[sp] = True
oc = np.array([m for m in range(9, lim+1, 2) if not isprime[m]])
g6 = oc[:-1][np.diff(oc) == 6]
twins = sum(1 for a in g6 if isprime[a+2] and isprime[a+4])
check("2,992 gap-6 intervals below 3e5, every one a twin pair",
      len(g6) == 2992 and twins == len(g6), "%d intervals, %d twins" % (len(g6), twins))

# ---------------------------------------------------------------- Theorem 2
print("\n2. Theorem 2: the two elementary families")
ok = all((30*j+3) % 3 == 0 and (30*j+5) % 5 == 0 and
         not isprime[30*j+3] and not isprime[30*j+5]
         for j in range(1, 2000) if 30*j+5 <= lim)
check("30j+3 on L_3 and 30j+5 on L_5 give a gap-2 pair for every j", ok)
iso = [p for p in sp if p > 15 and p % 15 == 8]
ok = all((p-2) % 3 == 0 and (p+2) % 5 == 0 for p in iso)
check("every prime p = 8 mod 15 is an isolated survivor", ok, "%d such primes below 3e5" % len(iso))
print("     reciprocal sums by gap type (one reciprocal per gap, at its left endpoint):")
print("        N = %-12g gap2 = %.3f   gap4 = %.3f   gap6 = %.3f"
      % (GAP_N, recip[2], recip[4], recip[6]))
tgt = {10**6: (2.805, 0.887, 0.464), 10**8: (4.556, 1.127, 0.488), 2*10**9: (5.762, 1.257, 0.498)}
if GAP_N in tgt:
    a, b, c = tgt[GAP_N]
    check("reciprocal sums match the published row for N = %g" % GAP_N,
          abs(recip[2]-a) < 5e-3 and abs(recip[4]-b) < 5e-3 and abs(recip[6]-c) < 5e-3)
if FULL:
    tot = sum(counts.values())
    fr = tuple(counts[h]/tot for h in (2, 4, 6))
    print("        letter frequencies: %.5f / %.5f / %.5f" % fr)
    check("letter frequencies match 0.89816 / 0.09475 / 0.00708",
          all(abs(x-y) < 5e-5 for x, y in zip(fr, (0.89816, 0.09475, 0.00708))))

# ---------------------------------------------------------------- Theorem 3
print("\n3. Theorem 3: no five survivors above 5 in AP of step 6")
sp2 = small_primes(AP_N + 30)
S = np.zeros(AP_N + 31, dtype=bool); S[sp2] = True
starts = [int(x) for x in sp2 if x + 24 <= AP_N and all(S[x + 6*i] for i in range(1, 5))]
check("the only 5-term AP of step 6 below %g is the one at 5" % AP_N,
      starts == [5], "starts found: %s" % starts)

print("\n   run-length census: upper rail 6b+1, b = 0 .. %g, coprime to 5..97" % CENSUS_N)
PR = [p for p in range(5, 98) if all(p % q for q in range(2, int(p**0.5)+1))]
surv = np.ones(CENSUS_N + 1, dtype=bool)
for p in PR:
    surv[(-pow(6, -1, p)) % p::p] = False
x = np.concatenate(([False], surv, [False])).astype(np.int8)
d = np.diff(x)
L = np.where(d == -1)[0] - np.where(d == 1)[0]
cen = np.bincount(L, minlength=8)[1:8]
total = int(surv.sum())
V = 1.0
for p in PR: V *= (1 - 1.0/p)
print("        lengths 1..4 = %s ;  length >= 5 : %d" % ([int(v) for v in cen[:4]], int(cen[4:].sum())))
print("        survivors = %d ;  density = %.6f  against prod(1-1/q) = %.6f"
      % (total, total/CENSUS_N, V))
check("no run of length 5 or more", cen[4:].sum() == 0)
tol = 5.0/math.sqrt(CENSUS_N)
check("density agrees with the Euler product within sampling error",
      abs(total/CENSUS_N - V) < tol, "difference %.2e, tolerance %.2e" % (abs(total/CENSUS_N-V), tol))
if CENSUS_N == 40_000_000:
    check("the four published counts are reproduced exactly",
          [int(v) for v in cen[:4]] == [6448150, 2404092, 778762, 211170])
    check("the survivor total pins the range at 4e7, not 6e7", total == 14437300,
          "total = %d" % total)

# ---------------------------------------------------------------- Corollary 1
print("\n4. Corollary 1: G_k = prod (q-k)")
ok = True
for lines in ([5], [5, 7], [5, 7, 11]):
    M = math.prod(lines)
    s = np.ones(M, dtype=bool)
    for q in lines: s[(-pow(6, -1, q)) % q::q] = False
    G = [int(sum(all(s[(b+i) % M] for i in range(k)) for b in range(M))) for k in range(1, 6)]
    law = [math.prod(q - k for q in lines) for k in range(1, 6)]
    print("        lines %-12s G = %-22s product law %s" % (lines, G, law))
    ok = ok and G == law
check("the direct count equals the product law on all three line sets", ok)

print("\n%d of the checks failed." % fails)
sys.exit(0 if fails == 0 else 1)
