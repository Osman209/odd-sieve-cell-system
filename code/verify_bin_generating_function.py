#!/usr/bin/env python3
"""
verify_bin_generating_function.py

COVERS = ["[P3, S4.3]"]

Corollary 4 of [P3]: the per-bin refinement of the generating function transports
the JOINT distribution of the per-bin strike counts on each rail, exactly.

Two things are checked, and the second is why this file exists.

  1. The two-marker form  prod_q ( (q-2) + u_b(q) + v_b(q) )  reproduces the
     direct census of the full cycle, state by state, at B = 2 and B = 3.
  2. The one-marker form  prod_q ( (q-2) + x_b(q) u + x_b(q) v ), printed in
     earlier versions, CANNOT: a left strike from bin 1 with a right strike from
     bin 2 and the reverse both give the monomial x1 x2 u v.  The script counts
     its distinct monomials and shows they are fewer than the states.

Run: python3 verify_bin_generating_function.py [--fast]
"""
COVERS = ["[P3, S4.3]"]

import sys
from collections import Counter
from sympy import symbols, expand, Poly

FAST = "--fast" in sys.argv
LINES = [5, 7, 11, 13] if FAST else [5, 7, 11, 13, 17, 19]
fails = 0
def check(name, ok, detail=""):
    global fails
    print(("  PASS  " if ok else "  FAIL  ") + name + ("   " + detail if detail else ""))
    if not ok: fails += 1

M = 1
for q in LINES: M *= q
print("verify_bin_generating_function.py   lines %s   cycle M = %d" % (LINES, M))

for B in (2, 3):
    if B > len(LINES): continue
    k = len(LINES) // B
    beta = {q: min(i // k, B - 1) for i, q in enumerate(LINES)}
    sizes = Counter(beta.values())

    census = Counter()
    for n in range(M):
        st = [[0, 0] for _ in range(B)]
        for q in LINES:
            c = pow(6, -1, q)
            if n % q == c % q:      st[beta[q]][0] += 1
            if n % q == (-c) % q:   st[beta[q]][1] += 1
        census[tuple(tuple(x) for x in st)] += 1

    us = symbols('u0:%d' % B); vs = symbols('v0:%d' % B)
    P = 1
    for q in LINES: P *= ((q - 2) + us[beta[q]] + vs[beta[q]])
    p = Poly(expand(P), *us, *vs)
    gf = Counter()
    for mono, coef in zip(p.monoms(), p.coeffs()):
        gf[tuple((mono[i], mono[B + i]) for i in range(B))] += int(coef)

    predicted = 1
    for b in range(B):
        nb = sizes[b]; predicted *= (nb + 2) * (nb + 1) // 2

    print("  B = %d   bins %s   states: census %d, generating function %d, predicted prod C(n_b+2,2) = %d"
          % (B, dict(sizes), len(census), len(gf), predicted))
    check("B = %d: the two-marker form reproduces the census in every state" % B,
          dict(census) == dict(gf))
    check("B = %d: the state count is prod_b C(n_b+2,2)" % B, len(census) == predicted)
    check("B = %d: the census totals the cycle" % B, sum(census.values()) == M)

    xs = symbols('x0:%d' % B); u, v = symbols('u v')
    P1 = 1
    for q in LINES: P1 *= ((q - 2) + xs[beta[q]] * u + xs[beta[q]] * v)
    p1 = Poly(expand(P1), *xs, u, v)
    check("B = %d: the one-marker form has fewer monomials than there are states" % B,
          len(p1.monoms()) < len(census),
          "%d against %d" % (len(p1.monoms()), len(census)))

print("\n%d of the checks failed." % fails)
sys.exit(0 if fails == 0 else 1)
