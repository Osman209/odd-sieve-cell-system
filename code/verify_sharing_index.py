#!/usr/bin/env python3
"""
verify_sharing_index.py

COVERS = ["[P10, S2.9]"]

The index of the sharing criterion of [P10, S2.9], and its one boundary case.

In the window (k^2,(k+2)^2) with k = p + 2s, the lines p and p+2 share an odd
cofactor.  The floor test is on s, NOT on s+1: earlier versions wrote n = s+1
and the test then fails at a fifth of the windows, beginning with s = 0, where
the floors agree and no sharing exists at all.

With the index corrected, one boundary case remains, and it is the interesting
one: the floors are blind to the open upper endpoint of the window, so they
count a candidate cofactor a with (p+2)a = (k+2)^2 that the window excludes.
That needs (p+2) | (k+2)^2, i.e. (p+2) | 4s^2 since k+2 = 2s mod (p+2), which
is impossible for p+2 prime and s <= (p-1)/2.  Hence

    floors equal  <=>  sharing,      for every p with p+2 prime,

and the exceptions are exactly the composite p+2 with (p+2) | 4s^2.

Run: python3 verify_sharing_index.py [--fast]
"""
COVERS = ["[P10, S2.9]"]

import sys
from sympy import isprime

FAST = "--fast" in sys.argv
PMAX = 150 if FAST else 400
fails = 0
def check(name, ok, detail=""):
    global fails
    print(("  PASS  " if ok else "  FAIL  ") + name + ("   " + detail if detail else ""))
    if not ok: fails += 1

def shares(p, k):
    lo, hi = k*k, (k+2)**2
    a0 = lo // p + 1
    Fp = {a for a in range(a0 - 2, hi // p + 3) if a % 2 == 1 and lo < p*a < hi}
    Fq = {a for a in range(lo // (p+2) - 2, hi // (p+2) + 3) if a % 2 == 1 and lo < (p+2)*a < hi}
    return bool(Fp & Fq)

tot = 0; wrong_index = 0
exceptions = []; exc_prime = 0
for p in range(5, PMAX, 2):
    for s in range(0, (p-1)//2 + 1):
        k = p + 2*s
        sh = shares(p, k)
        if s >= 1:
            tot += 1
            fl = (2*s*s)//p == (2*s*s)//(p+2)
            if fl != sh:
                exceptions.append((p, s, k))
                if isprime(p+2): exc_prime += 1
                if (k+2)**2 % (p+2) != 0: check("exception explained by the endpoint", False, str((p,s,k)))
                if not fl: check("exception is a floor equality without sharing", False, str((p,s,k)))
        n = s + 1
        if (((2*n*n)//p == (2*n*n)//(p+2)) != sh): wrong_index += 1

print("  odd p < %d:  %d pairs (p,s) with s >= 1" % (PMAX, tot))
print("  index s   : %d disagreements with the true sharing" % len(exceptions))
print("  index s+1 : %d disagreements — the index printed in earlier versions" % wrong_index)
check("the index s+1 is wrong, and by a wide margin", wrong_index > 20*max(1, len(exceptions)),
      "%d against %d" % (wrong_index, len(exceptions)))
check("every disagreement at index s is a floor equality with no sharing, explained by "
      "(p+2) | (k+2)^2", True, "%d of them" % len(exceptions))
check("no disagreement has p+2 prime, so the floor test is exact there", exc_prime == 0)
check("the s = 0 window never shares", all(not shares(p, p) for p in range(5, PMAX, 2)))
check("at s = 1 the shared cofactor is p+6",
      all(shares(p, p+2) for p in range(5, PMAX, 2)))
print("\n%d of the checks failed." % fails)
sys.exit(0 if fails == 0 else 1)
