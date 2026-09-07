# Review before push — what changed, 2026-09-04

Reviewed all fourteen modified files against the pushed `origin/main`
(`9534136`, "Consistency pass across the seven documents").

## Checks that passed, unchanged

- Statement numbering contiguous and in order of appearance in all seven documents.
- No duplicate or orphaned equation tag; every remaining tag is cited.
- Every internal, cross-paper and prose reference resolves; every reference in each
  list is cited at least once.
- Every table has a header separator and a consistent column count.
- Bold and math delimiters balance on every line.
- `node code/check_github_math.js` — 0 problems.
- All nine verification scripts exit 0.
- Independently re-derived: the carry-count identity of [0, §3.1] (0 mismatches over
  16,731 pairs with odd n and 7,722 with even n); the proof of [I, Prop 1]; the depth
  capacity table of [IV, §7.1] at M = 499.

## Six corrections made

1. **[IV, §3.2] Corollary 2b — the printed proof was not a proof.** The claim is true
   (0 violations over 3,802 twin sectors below M = 400,000, ten times the stated range),
   but the argument given — that the pairwise differences are bounded by 31 — is false
   as written: B − A = 2(M+2). Replaced with a complete proof: closures through the
   composite member force r | M+8 or r | M+10; the fifteen partner pairs are settled by
   substituting the congruence back into one partner, nine reducing to r | 2, 3, p or q
   and the other six to r | 1, 5, 7 or 14; the mixed case r | M+10 with Q_A gives r | 62.
   Added a sharpness note: r = 31 does close A and E together, in 128 twin sectors below
   M = 400,000, the first at M = 1695. Verification range widened to match.

2. **[V, §6.5] — the sign is needed at u ≤ 3, not u ≤ 3.566.** The threshold u* = 3.5658
   is derived correctly in §3.2 and is where the prime share of rough numbers falls to
   one half. But Theorem 6 holds only under the cut (2.1), i.e. u ≤ 3, so the sentence
   in §6.5 was outside the identity's own range. Scoped to u ≤ 3.

3. **[V, §5.5] — the almost-prime table mixed two window conventions.** At m = 101 the
   Ω ≤ 2 entry counted pairs strictly inside (m², (m+2)²) while the Ω ≤ 3 and Ω ≤ 8
   entries also counted the pair ending at (m+2)². Recomputed throughout on the strict
   convention, with the convention now stated: 138/202 at m = 101, 1,998 at m = 1,001,
   9,982, 19,954, 39,880; decade minima 353/1,087/1,998 and 2,415/8,700/19,952.
   The overview entry updated to match.

4. **[V, §5.5] — "close to half the odd integers of the window" was wrong.** 19,954 of
   20,002 odd integers is close to all of them, i.e. half the window. Reworded.

5. **[IV, §7.2] Proposition 4c — the stated reason for the width bound was not the
   reason.** The width is less than 2 because numerator minus twice denominator is
   −2(M − p)², with p ≤ M − 2; "since p + 2 ≤ M" does not give it.

6. Typography: a missing space after a bold lead-in at [IV, §7.2]; four pairs of
   consecutive horizontal rules in each of Papers IV and V.

## Added after the review, 2026-09-05

7. **[V, §2.2] a counting caveat after Theorem 4.** The paper was checked against a claim
   that it confuses composite endpoints with strikes; it does not — Theorems 1 and 2 put
   endpoints, responsible lines and strikes in bijection under the cut (2.1), so R is
   unambiguous there. The new paragraph says so explicitly, gives the worked witness
   (2717, 2719) in (51^2, 53^2) with 2717 = 11*13*19 — one composite endpoint, three
   strikes, owner 11 — notes that divisibility alone is not a strike since L_p begins at
   p^2, and states that no argument below trades an overlap gain against a cost counted
   in owners. Verified here: the arithmetic, the identity T = C - E + D cell by cell, and
   the related inequality T >= C - R* + (2/3)A + (1/9)B over all 16 cases with l, r <= 3
   (it fails at l or r = 4, so that cap is necessary, not cosmetic).

8. **[IV, §3.2] Corollary 2a, the k-ladder.** New result, from a document of his, checked
   before writing. In the wider window (M^2,(M+6k)^2) under M > (6k)^2, every composite
   endpoint of an open cell is (M+a)(M+b) with a, b even, prime to 3, and a+b <= 12k;
   there are exactly K_k = 2k(2k+1) such positions (6, 20, 42, 72, 110, ... — verified to
   k = 8), and no open cell has two composite endpoints, so every exception is a P_2 next
   to a genuine prime and T = C - X with X <= 2k(2k+1). At k = 1 this reproduces E_M
   exactly. Verified over 689 windows at k <= 5. Two things added that the source did not
   state: the hypothesis M > 36k^2 is load-bearing — dropping it produces both
   composite-composite cells and description failures, counted in the paper — and
   **widening the window makes the margin worse**, since the ceiling grows like 4k^2 while
   the open cells grow like 2kM/log^2 M, so k = 1 is optimal and the ladder completes the
   description without advancing the proof. Paper IV is now 53 pages.

9. **[IV, §3.2] Corollaries 2d and 2e — the square-endpoint sharpening.** Cells with a
   perfect-square endpoint carry no twin and there are at most two of them per sector
   ((M+2)^2 and (M+4)^2). Discarding them and using the line 5 alone: at most ONE of
   B, D, E, F is open when the root pair is not a twin (D and E can never be open
   together, since D needs M+2 = 2 mod 5 and then 5 | M+10 closes E); none at all when
   M = 21 mod 30, unconditionally; only B when M = 27 mod 30. Verified over the same
   3,332 sectors. Stated plainly in the paper that this is a change of bookkeeping and
   not of strength — C° >= C - 2, so it still amounts to Corollary 2's T >= C - 2 — with
   the gain confined to the two residue classes, which cover two fifths of all sectors.
   Corollary 2e then records that the four non-square positions are sifted in **dimension
   three**, not two: each composite member is a product of two linear forms (two residues
   always) and each partner an irreducible quadratic (two or none), giving mean 3 —
   extending Appendix C.1, which had A, C at dimension 2 and D, E, F at 3, to B. Exact
   inclusion-exclusion densities are tabulated to y = 19,997; U(y)(log y)^2 falls
   throughout while U(y)(log y)^3 steadies near 9. The vanishing-density statement is
   proved in the correct order of limits (fix y, let X go first, then y), which yields
   o(X) with no rate. **An earlier draft of this passage claimed dimension two, a rate
   2/log^2 M, and a shared singular series with the twins; all three were wrong and are
   not in the paper.** Paper IV is now 55 pages.

10. **[IV, §3.2] the exception census extended to M = 10^9.** Corollary 2a makes the
    openness test purely a matter of primality — no two of the six differ by 2, so a
    partner is rough exactly when prime and a composite (M+a)(M+b) exactly when both
    factors are prime — which takes the census from 3,332 sectors to 166,666,665, run
    segmented in four chunks. Every proved statement holds throughout: D and E never open
    together, never more than one open non-square position in a twinless sector, none at
    all for M = 21 mod 30, only B for M = 27 mod 30. The decade table now measures the
    sifting dimensions directly: square density x log^2 M settles near 9.7, non-square
    density x log^3 M near 24.2, and their ratio x log M is 2.49 across four consecutive
    decades to within half a per cent. Also recorded: F is 2.09 times as common as B
    despite the same linear condition, the difference being the partner quadratics
    (M+3)^2+1 versus (M+6)^2-2. Paper IV is now 56 pages.

11. **[IV, §3.2] a remark on the partner quadratics.** From a literature review he brought.
    With M = 6t+3 the six partners become 36t^2+60t+23, +72t+37, +84t+47, +96t+53,
    +108t+67, +108t+79, with discriminants 288, -144, 288, 1584, 2016, 288 — all verified
    here, none a perfect square, so all six are irreducible; and none has a fixed prime
    divisor (checked for every prime to 73; gcd of the first sixty values is 1 in each
    row). Iwaniec (Invent. Math. 47, 1978) then gives infinitely many values with at most
    two prime factors, and Lemke Oliver (Acta Arith. 151, 2012) the square-free form.
    **Attribution corrected against the source document, which credited the whole result
    to Lemke Oliver: the theorem is Iwaniec's; Lemke Oliver adds square-freeness and the
    higher-degree generalisation.** Written in with its three limits stated — each partner
    separately and not simultaneously, no separation of prime from P_2, and nothing about
    the composite member — so it reads as a correct application of a published theorem and
    not as progress on twins. References 11 and 12 added; the count in the reference
    preamble updated from ten to twelve.

12. **Final ordering and consistency pass on [IV, §3.2]**, after all of the above.
    Three things were out of order and are now fixed: **Corollary 2a appeared before
    Corollary 2** — the k-ladder block has been moved to sit after the dichotomy and its
    five residue classes, so the section now reads Theorem 4, the criterion, Corollary 2,
    2a, 2b, 2c, 2d with the 10^9 census, 2e, and the partner remark last; the summary
    table at the front had the same inversion and its two rows were swapped to match;
    and the **partner-quadratic remark was splitting the rarity discussion** in two, so it
    has been moved to the end, after Corollary 2e. Also: the |E_M| table rows now run in
    ascending order 0, 2, 4, 6 rather than 0, 4, 2, 6, and one verification block that
    repeated "the 3,332 sectors M = 9, ..., 19,999" now says "the same 3,332 sectors" like
    the two before it. Every reference to Corollary 2a is now a backward reference.
    Re-checked afterwards: structural audit clean, KaTeX checker 0 problems, all nine
    verification scripts exit 0, every table has a separator row and consistent columns,
    and the only forward references left are the deliberate ones in the section overview
    announcing Propositions 7 to 9. Page counts unchanged: IV 56, V 39, I 21, II 12,
    III 12, 0 11, overview 15.

13. **[V, §2.2] the pair-overlap threshold, recomputed properly.** The paragraph after
    Theorem 5 estimated the effective cut exponent from ratios read at three scattered
    values of alpha and gave "about 0.54". It is now derived rather than estimated.
    **One definition had to be fixed first: l counts the lines that have BEGUN at n, i.e.
    primes q | n with q^2 <= n (Theorem 2), so l = 0 at a prime, 1 at a P_2 — the larger
    line has not started — and 3 at a P_3.** Counting all prime factors instead gives
    E[l] ~ 1.5 and a bound near -1.05, which is wrong. A second point follows from the
    first: above alpha = 1/2 the value l = 2 is impossible, since the two smaller factors
    of a P_3 already exceed X^alpha > X^{1/2}; measured at 0.0005.
    The shares s_k then come from the standard simplex integrals I_1 = 1,
    I_2 = log((1-b)/b), I_3 = double integral, with b = alpha/2 and no k >= 4 term while
    alpha > 1/2, and the bound crosses zero at **alpha = 0.5385** (bisected, integrals by
    adaptive quadrature).
    **A finite-height measurement alone would have given the wrong number, and did.** The
    crossing measured in a dyadic band is 0.52291 at X = 2e8, 0.52621 at 2e9 and 0.52915
    at 2e10 (the last from 1.6e8 open cells, run in three chunks); the deficits against
    0.5385 are 0.01557, 0.01227, 0.00932, falling by a factor near 0.77 per decade, which
    is the expected O(1/log X). A naive linear fit in 1/log X extrapolates to 0.555 and
    overshoots, because the correction is not linear at this range. So the intermediate
    figure 0.5262, taken from X = 2e9 alone, was too low, and the paper's original "about
    0.54" was closer to the truth than that measurement.
    Independence, which the B/C term assumes, was audited and holds: E[l r] against
    E[l] E[r] lies in 0.9992-1.0000 at every cut and every height, and conditioning l on
    the partner being rough changes its mean only in the fourth decimal. Paper V is now
    40 pages.

14. **Final pass across all seven documents, for the push.** The overview was carrying two
    stale figures and is now in step with Paper IV: the Theorem 4 entry says the census
    covers the 166,666,665 sectors below 10^9 rather than 3,332, and the Theorem 5 entry
    gives the threshold 0.5385 with the three measured heights instead of "near 0.54".
    A new overview entry was added for Corollaries 2d and 2e. **COMMIT_MESSAGE.txt has
    been rewritten**: the DO-NOT-PUSH lines are gone, Corollary 2b now reads 3,802 sectors
    below M = 400,000 with the sharpness of the constant 31, the §6.5 sentence reads
    u <= 3 rather than u <= 3.566, the almost-prime count reads 19,954, a new section
    covers everything added after the review, and the closing page counts read IV 56 and
    V 40. Re-checked: structural audit clean, KaTeX 0 problems, all nine verification
    scripts exit 0, all seven PDFs rebuilt from the corrected sources.
    `.zenodo.json` and `CITATION.cff` already read 1.7.0; the tag v1.7.0 still does not
    exist, and no release is being cut.

15. **[IV, §3.2] after Theorem 4: "Why six".** From his own observation about the steps of
    line 3. A line is dormant from 3p to p^2 — (p-3)/2 steps, each owned by a smaller line —
    then walks in steps of 2p, landing on upper member / L_3 / lower member in turn since
    p^2 = 1 mod 6. Only M+2 and M+4 are born in the sector; walked from their births they
    make 5 and 3 steps before (M+6)^2, lose one each to L_3, and the remaining 4 + 2 are
    exactly A,B,D,E and C,F. Verified over 4,999 sectors with zero mismatches. The same
    walk reproduces Corollary 2a's rows 4k, 4k-2, ..., 2 and the total 2k(2k+1) with 2k^2
    steps lost to L_3 — checked on 24 windows for k <= 6. Written explicitly as a second
    proof that explains the number, not as a new result. Paper IV is now 57 pages;
    COMMIT_MESSAGE.txt updated to match.

16. **[V, §6.5] the sign paragraph rewritten around alpha/beta.** From two documents of his
    over 2026-09-06. The needed statement is now one inequality, beta/alpha < A/B -> 1/log 2,
    with both rails counted (one rail alone allows all cells prime-composite and no twin —
    his correction of my earlier one-rail wording). Measured beta/alpha ~ 1.00 at
    10^5..10^8 against an allowance of 1.44. **Proved part, in two tiers:** the mean itself is
    preserved for neighbour depth up to c loglog x (equidistribution in progressions,
    Siegel-Walfisz); negativity alone is proved to neighbour depth x^(1/6-eps) by the
    linear sieve at s = 1/(2a) against the BV level, since beta/alpha <= F(s)/f(s) and
    F(3)/f(3) = 1/log 2 exactly. Verified here: F(3.5)/f(3.5) = 1.1422, bound -0.116 at
    y = x^(1/7), zero margin at s = 3. Structural reading added: f/F = log(s-1) and
    B/A = log(u-1), so the condition is s > u; with the level halved that is a < 1/6; under
    EH it is a < 1/3 with zero margin at 1/3. Gap stated: raise the neighbour's depth from
    1/6 to 1/3 keeping the sign — the level-1/2-to-level-1 gap. Also recorded: adding line
    43 at 10^5 makes the mean less negative, so no line-by-line argument. **Dropped: the
    attribution of the fixed-z case to Tao's theorem** — that case is trivial by
    periodicity (both means vanish) and carries no information about finite u. Paper V
    is now 41 pages; COMMIT_MESSAGE.txt updated.

17. **[V, §3.3] Li and Liu added.** arXiv:2606.05224 (1 June 2026, Shandong): Proposition
    (1-a) interpolates Chen's theorem (a = 2) and the twin conjecture (a = 1) by requiring
    p+2 = rq with r <= q^(a-1); (1-1.75) unconditional, (1-1.4) under a weighted EH, plus
    (1+1.9) and (1+1.4) for Goldbach. First movement in that gap in six decades, though
    the preprint is unrefereed and is cited as such. Their weight is built from P^-(n) and
    Omega(n) — this framework's two quantities — and **the correspondence with the cut is
    exact: tau = (a-1)/a, so the depth 1/3 of Theorem 1 is a = 3/2, and they independently
    record that their combinatorics changes character below 1.5.** A tempting false
    inference is recorded and refuted in the paper: their conditional (1-1.4) has every
    non-twin solution closed at the cut, but combining that with the existence of open
    cells proves nothing, since both are "infinitely many" statements over possibly
    disjoint sets — that shape of argument would give EH implies twins. Reference 32.
    Paper V is still 41 pages.

18. **[V, §5.8] a third test case, rewritten twice and now in its strongest form.** His
    idea, then his two corrections to it. **Theorem 8:** if p < q are odd primes, a >= q,
    and pa, qa lie in one window between consecutive odd squares, then q = p+2. One-line
    proof from sqrt(qa) - sqrt(pa) = (q-p)sqrt(a)/(sqrt q + sqrt p) < 2. **Neither
    primitivity nor primality of a is needed** — the earlier draft assumed both, which he
    caught; the inherited witness 31^2 < 29*35 < 31*35 < 33^2 works with a = 35 composite.
    Verified: 5,593 sharing pairs over odd k < 1000, 4,764 with composite cofactor, zero
    with q - p != 2. **Converse, unconditional:** a = p+6 always works, since
    p(p+6) = (p+2)^2 + 2p - 4 and (p+2)(p+6) = (p+4)^2 - 4 — no third prime, no congruence.
    This supersedes the mod-4 rule of the previous draft (which was correct but needlessly
    narrow, requiring a prime). **Theorem 9** records the equivalence. Horizon corrected:
    k < 2p, not the 1.707p of an earlier proposal — measured 1.824p, 1.901p, 1.944p at
    p = 17, 71, 269, approaching 2 from below. **Why it closes the route** is now stated
    from the proof itself: primality enters at exactly one point, to make q-p even, and
    23^2 < 21*27 < 23*27 < 25^2 shows the geometry holds for adjacent odd numbers with 21
    composite. Contrast with Theorem 4 kept explicit: its hypothesis is one open cell, a
    statement about survival, which a sieve can in principle deliver. Paper V is 44 pages.

19. **[V, §5.8] the cofactor intervals and the explicit construction.** From a further
    document of his, both parts verified at much larger scale than he ran. **The
    localisation:** C_p is an interval of length (4k+4)/p, two meet only if
    q/p < (1+2/k)^2, so all sharing lives in k/2 < p < q <= k — which also makes Theorem
    8's hypothesis a >= q automatic (a > k^2/q > k >= q), so it is now flagged as
    non-restrictive. The overlap length ((4k+4)p - 2k^2)/(p(p+2)) is a function of p/k
    alone (0.17, 1.12, 1.88, 2.00 at 0.51k, 0.6k, 0.8k, k) and never exceeds 2, hence
    **at most one shared odd cofactor, and it is the first of the smaller line and the
    last of the larger** — checked over 2,604,125 pairs in windows with odd root below
    501: 12,019 sharings, zero violations of either the ends rule or the range.
    **The construction:** with k = p+2t, a = p+4t+2 gives pa = k^2+2p-4t^2 and
    (p+2)a = (k+2)^2-4t^2, so both strikes are inside whenever 2t^2 < p — 44,551 identity
    checks and 3,168 inclusion checks, zero failures. So sharing near the root is forced,
    not merely frequent; 92.5% of adjacent odd pairs above k/2 share, stable at
    k = 10^3, 10^4, 10^5. **And his k = 23 example is the sharpest picture of the wall in
    the paper:** the construction forces 19,21 to share 29 and 21,23 to share 27, all four
    strikes in (529,625), but the shared line 21 is composite and the two prime lines use
    different cofactors. At k = 10^5, 23,069 of 25,001 adjacent pairs share and 519 are
    prime pairs. Paper V is now 43 pages.

20. **[V] three loose statements about the sieve corrected, at his insistence and rightly.**
    The text said in two places that "the sieve sees survival and does not see Omega". That
    is wrong: **primality is itself a survival statement** — N < x is prime exactly when it
    survives every line below sqrt(N) — so no criterion in this work ever left the sieve's
    language, and the "different toolbox" framing of the previous draft was mistaken. What
    actually differs between criteria is one number: the ratio s at which the existence of
    a survivor is being asked for. Dimension two needs s > 4.2664; Theorem 4's sector
    criterion asks at s = 1, the sharing criterion at s = 2, and below the threshold the
    sieve returns zero rather than a small bound. The closing paragraph of §5.8 now says
    this, and states that an equivalence helps only when it raises s — this one raises it
    from 1 to 2, the largest gain in the work and still short by more than it gained. The
    two sentences in §2.3 and §6.5 were reworded accordingly. Paper V is 44 pages.

21. **[V, §5.8] the movement law of the cofactor runs.** His law, with one correction of
    mine. The list F_p(k) is an unbroken run of h_p odd numbers, 2 <= h_p <= 4 (40,191
    lines: 15,414 / 18,707 / 6,070), the runs slide left with p, and sharing is exactly
    A_p = B_q, i.e. A_p - A_q = 2(h_q - 1) — 2,666,595 pairs, zero violations. The
    transition law A_p(k+2) = B_p(k) + 2 held only 99.4% of the time; **I called the
    failures rounding, which was wrong. He identified the true cause: a strike landing on
    the shared boundary belongs to neither open window and is skipped**, giving the exact
    law with the indicator 2*[p | (k+2)^2] — 79,790 pairs, 1,398 firings, zero mismatches.
    **And the indicator never fires on a prime line of the strip**, by his short argument
    (p | k+2 forces k+2 >= 3p against p > k/2); verified on 77,427 prime lines, and all
    128 in-strip occurrences are composite lines. So the movement is an exact equality in
    the prime system: steps of 4, 6 or 8, and D(k+2) = D(k) + 2(h_p - h_q) changing by
    0 or +-2 or +-4, sharing when D reaches 2(h_q - 1). Recorded with it: the boundary
    indicator is the first quantity in this work that separates prime from composite
    lines outright, but in the wrong direction — it says which lines break the law, not
    which lines share. Paper V is now 45 pages.

22. **[V, §5.8] the closed form, and the sharpest statement of the obstruction in the work.**
    The sharing criterion reduces to **(2n^2 mod p) >= 4n^2/(p+2)** — 101,015 checks, zero
    mismatches — and n = 1 always satisfies it, recovering the a = p+6 witness. Under
    equidistribution the rate averages to exactly **2/3**, which is the 0.6654 / 0.6662
    measured earlier for prime and non-prime pairs; **so the criterion reads the
    distribution of 2n^2 mod p, not its structure, and the distribution is prime-blind.**
    The structure that does differ is identified: n -> n^2 mod p is injective on
    [1,(p-1)/2] **iff p is prime**, sole exception p = 9 (76/76 primes, 1/122 composites).
    But the deviation of the sharing count does not see it — |dev|/sqrt(p) is 0.270,
    0.260, 0.222, 0.203 for primes, composites with lpf >= 11, multiples of 3, multiples
    of 5 — the same order, and *smaller* for small-factor composites, the opposite of what
    I predicted. Reason: the sum runs over single n with a moving threshold, and averages
    the local structure away. **The section now closes on this: every criterion in the
    paper is a one-parameter sum over n, hence sees only the distribution, whereas
    primality shows up as the absence of collisions — a statement about pairs. That is
    the Bilinearity deficit of §6.1, arrived at from the framework's own coordinates.**
    Section order fixed so the summary paragraph ends the section, and the cross-reference
    repointed from §3.1 to §6.1. Paper V is now 45 pages.

23. **[V, §5.9] NEW SECTION — collisions inside the sharing set; overview updated.** The
    long thread of 2026-09-07, written as its own section rather than folded into §5.8.
    **Theorem 10** (E_p = 0 iff p+2 prime), **Theorem 11** (the belt
    sqrt(p+2) < v <= (p+11)/6 for odd p > 121, eight exceptions), **Theorem 12** (a slice
    of width < sqrt(N/3) at the top collapses to divisibility by 3, via the identity
    N(v-u-3k) = 3[(N/6-u)^2 - (N/6-v)^2]). All five proof steps of Theorem 10 and every
    numeric claim were verified independently here.
    **Placement stated plainly in the text: the equivalence itself is the classical
    difference-of-squares criterion (Fermat); what is proved is that the witness always
    lies inside S_p.**
    **The closure is the sharpest obstruction in the work:** E_p vanishes exactly on twins
    and is integer-valued, so for any non-negative weights sum w E < sum w already
    requires a twin in the support — every weighted first-moment argument assumes its
    conclusion. Four relaxation families were measured and all widen the zero set faster
    than they lower the mean.
    **Three of my own claims were withdrawn during the thread and are not in the text:**
    that |S_p| is always 2/3 of the range (it is an asymptotic average); that the
    (1-theta)^2 law for the mean is a law (it is an empirical fit — 12 predicted against
    6.2 measured at theta = 0.9); and that any relaxation reaching mean < 1 collapses to a
    detector of 3 (his counterexample p = 64373, N = 625*103, u = 10522, v = 10728,
    k = 68, factor 103). The last is recorded in the paper as the inhabited gap between
    sqrt(N/3) and sqrt(2p/3).
    Paper V is now 47 pages, the overview 16.

24. **[V, §5.9] Theorem 13 — the staging law.** His result, and it widens Theorem 12.
    d and k share parity since N is odd, so d - 3k = 2t; then 2tN = d(N-3s), and the
    slice's lower edge gives 0 <= t <= floor(3(L-3/2)^2/(2N)), generally
    t <= floor((N-6H_0+6L)^2/(24N)). The maximisation needs no hypothesis on d because
    d(2L-3-d) = (L-3/2)^2 - (d-L+3/2)^2. Stages open one at a time: t=0 at L>=3
    (Theorem 12's pair), t=1 at L >= 3/2+sqrt(2N/3), t=2 at 3/2+sqrt(4N/3) — **so the
    collapse of Theorem 12 holds up to width 3/2+sqrt(2N/3), a factor sqrt2 wider than
    before.** Parity and identity verified on 276,412 collisions, zero exceptions.
    **A measurement error of mine was caught here:** I used the integer part of H both as
    the slice top and as the reference point, which shifted the slice and produced five
    apparent violations (p = 173, 389, 443, 1559). With the exact rational H = (p+11)/6
    there are none, and the two cases he checked hit the bound with equality. I also
    wrongly objected that the maximisation needs d free — the identity above disposes of
    that. **No extra hypothesis and no small-p exceptions are needed.** Census in the last
    2% of the belt below 1.2e5: 5,560 at t=0, 1,027 at t=1, none above. The earlier
    counterexample p = 64373 is now explained: t = 1, needs L = 208.6667 against the
    stage-one threshold 208.6634, clearing it by 0.0033. Paper V is now 48 pages; the
    overview entry extended.

25. **Final pass over all seven documents after the §5.9 work — two real defects found.**
    (a) **§5.8 closed with "the contrast with Theorem 4", which reads inside Paper V as its
    own Theorem 4 (the exact twin count T = C - R + S).** The intended reference is the
    sector criterion of Paper IV; both occurrences now say [IV, Thm 4].
    (b) **The cofactor list F_p(k) was floating free of the rest of the series.** It is the
    strike set of L_p read on the cofactor axis rather than the cell axis, where
    [I, Cor 4] already gives it as two interleaved progressions of step p — on the cofactor
    axis those merge into a single run, which is exactly why the run is unbroken and why
    sharing can only happen at the two ends. The text now makes that link.
    Also: the overview entry updated from "Thms 8-12" to "Thms 8-13". Re-checked
    everything — structural audit clean, KaTeX 0, all nine verification scripts exit 0,
    all seven PDFs rebuilt. Page counts: overview 16, Paper 0 11, I 21, II 12, III 12,
    IV 57, V 48. **The two standing audit notes turned out to be checker bugs, not paper
    defects, and I should have looked at them earlier instead of calling them
    informational.** (i) The §11.19 "reference" is inside the citation [12, §11.19] — a
    section of Friedlander–Iwaniec, *Opera de Cribro* — and the checker was reading § inside
    numeric citation brackets as an internal reference. (ii) The Paper IV gap at 14 is not a
    gap: the slot is **Verified Law 14**, a convention the paper states twice, and the
    checker counted only headings labelled "Theorem". Both were fixed in `audit.py`
    (numeric citation brackets stripped; the Theorem sequence counts both labels) and the
    fixes were tested against injected defects — a renumbered theorem and a bad internal
    reference — which still fire. **The audit now reports no problems at all**, which is
    what makes it useful again: a checker with two permanent items to ignore is a checker
    whose next real item gets ignored too. The fixed `audit.py` is in the working copy
    only, not in the repo.

26. **[V] §5.8 and §5.9 split one idea per subsection, at his instruction.** They had grown
    to hold four or five separate results each. Now:
    5.8 the shared-cofactor criterion (Thms 8, 9) — 5.9 the geometry of sharing (intervals,
    the ends rule, the explicit construction, the movement law, the k = 23 window, the
    closed form) — 5.10 why that equivalence closes the route — 5.11 the collision
    criterion (Thm 10) — 5.12 where the collision must sit (Thms 11, 12, 13) — 5.13 why the
    collision criterion yields no twins — 5.14 the pattern of the whole work (twice
    renumbered, was 5.9 then 5.10). Section lead-ins rewritten so none opens on a bold
    run-in left over from when it was a paragraph; summary-table pointers and the two
    §6.1 cross-references updated; the overview entry now cites §§5.8–5.13. Paper V is
    still 48 pages — the split cost nothing.

27. **Papers IV and V split into seven parts, and the whole set renumbered 1 to 11.** Two
    changes in one pass, both at his instruction.
    **The split:** IV and V were 57 and 48 pages with four or five independent threads each.
    Now 5 Gap Alphabet (4pp), 6 Twin Criterion (33pp), 7 Clocks and Inheritance (10pp),
    8 Belts and Short Windows (15pp), 9 The Exact Form of the Obstruction (17pp), 10 Four
    Test Cases (19pp), 11 What a Continuation Would Have to Supply (15pp). Each has its own
    title, abstract, setting, summary table and reference list.
    **The renumbering:** the roman numerals and "Paper 0" are gone; the set is 1 to 11 in
    reading order, files `paper_01_...` to `paper_11_...`, and each title says what the
    paper contains. Sections restart at 1 in every paper. **Result numbers deliberately kept
    from the parent set** — a part can open at Theorem 4 or Proposition 6 — because
    renumbering them would break every cross-reference and every external citation, while
    renumbering sections costs nothing outside the file. Each paper carries a Numbering note
    saying so.
    All cross-references rewired: [IV, Thm 4] -> [6, Thm 4], [V, §5.7] -> [10, §2.7], and a
    bare reference to a whole former paper becomes a range [5]–[8] or [9]–[11]. The
    paper-number line is now `## Paper N. <subtitle>` so the audit does not read it as a
    section heading.
    **Four defects repaired along the way:** two references pointed at Paper V sections
    renumbered in an earlier revision; two were damaged by an intermediate pass of my own
    splitting script, which wrapped a section number already inside a bracket. Six summary
    rows for Theorems 8–13 were in part 9 and belong to part 10.
    README, site registry, two verification-script headers, the overview's companion map,
    `.zenodo.json` and `CITATION.cff` all follow the new names and the count of eleven.
    `audit.py` globs papers/ instead of a fixed list, accepts numeric labels in citation
    brackets, and skips the numbering-gap check where continued numbering is declared.
    **This is a v2.0-shaped change:** the DOI for v1.6.0 describes a seven-document set.

28. **[10, §2.14] Theorem 14 — counting the witnesses.** His result, verified at his own
    scale and to his own numbers. With Delta = (N-6v)^2 + 48t and X = N-6u, the identity
    X^2 - Delta = 24tp gives: **inside one list Delta determines the collision** — subtract
    two copies, get (X1-X2)(X1+X2) = 24p(t1-t2) with both factors below p, so the difference
    vanishes; then u, t and v follow, the alternative v1+v2 = N/3 being excluded by
    3 not dividing N. **267,575 collisions on 1,121 prime lines below 2e4, no Delta repeats.**
    Consequence he states and I confirm: the number of collisions equals the number of
    distinct Delta, so **recoding by Delta is not a relaxation** — which closes a route I had
    not yet ruled out.
    Constructive bound: Delta = 1 mod 24 and never a square, so admissible values begin
    73, 97, 145, 193, 217, 241 (squares 1, 25, 49, 121, 169 excluded), and inside a slice
    beginning at U, Delta <= (N-6U)^2 - 24p. Checked on 786 slices, no case exceeds it. His
    four-row table reproduced exactly.
    **The first row is the limit of the whole approach and is written into the paper:** at
    p = 131 the slice is provably empty while N = 133 = 7*19 is composite — the witness
    u = 6, v = 13 sits just below the slice. So any relaxation must retain a witness for
    every composite p+2, and this bound does not. Same conclusion as §2.13 reaches through
    means and weights, here by construction. Paper 10 is now 20 pages; the overview entry
    extended to Theorems 8-14.

29. **AI disclosure: one short paragraph in each paper, the long account in the README only.**
    He asked for the papers to keep the compact note they had, so each paper carries a single
    italic paragraph naming **ChatGPT (OpenAI)** and **Claude (Anthropic)**, saying what they
    were used for, and pointing at the README. The README section carries the full division
    of labour: the questions, objects and direction are his; ChatGPT for algebraic derivation
    and independent checking, with the errors it caught named (a wrong hypothesis in a
    theorem, a mistaken diagnosis of a numerical discrepancy, a measurement whose definition
    did not match the text); Claude for the numerical work, review and most of the prose;
    where the two disagreed, computation settled it and the text records the resolution.
    Closing line: no statement rests on the assertion of a model.
    Two stale copies of the older one-line credit, left in papers 6 and 11 by the split, were
    removed in the same pass.
    Also cleaned in this pass: the last prose mentions of the old labels — "Paper 0" ->
    "Paper 1", "Paper I" -> "Paper 2", "Paper IV" -> "Papers 5 to 8", "Paper V" ->
    "Papers 9 to 11" — across ten files.

## Post-split audit — 7 September 2026

Item 27 above records that the split to eleven papers rewired all cross-references
and that README, the overview, Zenodo and the CFF followed the new names. The packaged
version did not match that record. What was actually still in it, and what was done:

30. **A bracket meant two different works.** Companion papers were cited [1] to [11]
    and external references were numbered in the same notation, so in nine of the twelve
    documents a number was ambiguous — "[9]" in Paper 10 was Paper 9 and Dudek–Johnston,
    "[2]" in Paper 6 was Paper 2 and Coppola–Laporta. Companions are now **[P1] to [P11]**,
    bare numbers are references, and every paper states the convention above its list.
    This is the defect that would have survived fixing all the broken references, and it
    was not on the earlier list.

31. **Thirty-two broken section references**, all old parent numbering: Paper 6 eight,
    Paper 8 four, Paper 9 one, Paper 10 eight, Paper 11 ten, the overview one. Three of
    them had the wrong *paper*, not the wrong section — Paper 6's three references to
    "[7, §4.5]" are equation (4.4), which lives in Paper 2. Nine `]]` and two `§[` left by
    the splitting script are gone.

32. **Two summary tables listed other papers' results.** Paper 9's carried four rows for
    Appendix C.2 and Proposition 2, which are in Paper 11; Paper 8's carried rows for
    Paper 6's Appendix A and Paper 7's Appendix B. Same class as the "six summary rows in
    part 9 belonging to part 10" already fixed in item 27, and missed for the same reason.

33. **Two overview citations named the wrong paper**: [9, Thm 5, Cor 2] is [P6, Thm 5,
    Cor 3], and [10, Thms 11, 12, Cor 6] is [P7, ...]. Both are symptoms of a mechanical
    label remap rather than a look at where the result went.

34. **Reference lists rebuilt.** Each is now numbered 1..k contiguously; they had been
    fragments of the two parents' lists (Paper 9's ran 5, 23, 32, 32). **Two works shared
    the number 32** — Zhang and Li–Liu, in both Papers 9 and 11 — and the body meant Li–Liu
    in one and Zhang in the other; the entry uncited in each paper was dropped. **Two
    citations had no entry**: [30] twice in Paper 9 (Tao's 254A notes) and [12] in Paper 11
    (Friedlander–Iwaniec). Both added.

35. **[P11, §2.5] — the one mathematical correction, and it came from an outside review.**
    The linear sieve functions were printed with the single range $2 \le s \le 3$ and then
    used at $s = 3.5$. The ranges differ: $F$'s closed form holds to $s=3$, $f$'s to $s=4$,
    and above $3$ the $F$ used must be the continued branch $sF(s) = 2e^\gamma +
    \int_3^s f(t-1)\,dt$. **The arithmetic was already right** — verified here: $F(3.5) =
    1.06519$, $f(3.5) = 0.93256$, ratio $1.142225$, which is the printed $1.1422$; the closed
    form would have given $1.09136$, and the chain's $-0.116$ confirms which was used. So only
    the definition needed extending, and the numbers are now printed with it. The claim of a
    Bombieri–Vinogradov level for shifted rough semiprimes is now stated as an **assumption**
    rather than as available, with the conclusion proved on the prime rail and conditional on
    the other. And `α_y = β_y ∼ … exactly` is split into an equality and an asymptotic.

36. **Papers 9, 10 and 11 were opening with the structure of a document that no longer
    exists** — "§§4–7 then give", and in Papers 10 and 11 a verbatim copy of Paper 9's
    paragraph. Paper 10's §2 was headed "two test cases" while running four, its table row
    read "§2.5–5.6", and its abstract said "Each is exact" although Proposition 1 is labelled
    measured. Papers 10 and 11 declared they imported nothing beyond Papers 1–8 while citing
    9, 10 and 11 from their first pages. All rewritten.

37. **Paper 6 restructured.** A numbered §3 was sitting after the appendices; it now precedes
    them. Corollaries 2a–2e, the census to $10^9$ and the partner-quadratic remark move into
    **Appendix A.3** with a stub in §2.2 — the pattern the paper already uses in §§2.4, 2.7,
    2.8 and 2.11 — so §2.2 reads as Theorem 4, the criterion and the dichotomy. Appendix C
    renamed B, so the appendices run A, B. "Section 3.3" ×2 → §2.3.

38. **Paper 5 kept as a standalone note**, against the option of folding it into Paper 6.
    Three reasons: Paper 7's Theorem B1 proof runs through [P5, Thm 3] and the cap at four is
    what makes that identity hold, so the merge would make Paper 7 cite the twin-criterion
    paper for a fact unrelated to it; Paper 6 is already 33 pages against Paper 5's four, so
    the merge worsens the imbalance the split existed to fix; and the objects differ — Paper 5
    is global (gaps along the whole odd line), Paper 6 local (one sector, six named places).
    What was wrong with Paper 5 was not its length but its Setting, which declared four
    sources and used one. Fixed, and the "gap 6" terminology warning moved into it from
    Paper 7's appendix, where it did not belong.

39. **The Numbering note did not describe what happens.** It said the sequence "begins where
    the previous part left off"; in fact a part may open well above one and skip numbers
    belonging to a sibling. Reworded in all seven parts.

40. **A stale honesty claim, in the wrong direction.** [P11, §2.4] said the sector-coupling
    budget, the admissibility of the escapee and the timing table were "not yet" in a script
    and should be treated as unaudited — contradicting the README's "no table without a
    script". They are in `verify_exception_dichotomy.py` as checks 21–25 and 27. The sentence
    was stale; it now names the checks, and the README standard stands unweakened.

41. **One title changed: Paper 10 → *Four Tests of the Cell System*** (`paper_10_four_tests.md`).
    Every other title kept: within the set they build a vocabulary, and renaming for
    descriptiveness costs more than it buys. The explanation belongs in the series name, the
    overview and the first lines of each abstract, not in eleven titles.

42. **README, overview, site builder, CITATION.cff, .zenodo.json and the backlink** all still
    described the seven-document roman-numeral set. The overview announced "six short papers"
    and carried the 0/I/II/III/IV/V dependency table while its body already used the new
    numbers; it now maps the eleven in three movements. The count is stated identically
    everywhere: eleven papers, one overview, nine verification scripts. The broken sentence in
    README's Status is repaired, "Paper V §9.1" → Paper 11 §2.1, and the instruction that the
    rendering checker "should report exactly one problem" is corrected — it reports none.
    Six verification scripts carried old labels in their comments; updated.

43. **`audit.py` rewritten, because it was the reason none of this was caught.** It reported
    "no problems found" on a version with thirty-two broken cross-references: its cross-paper
    check was keyed to the roman labels and the pre-split filenames, so it never ran, and its
    root path was hard-coded to a directory that no longer exists. It now reads the papers from
    the filesystem and adds: every `[Pn, ...]` resolved against the target's own headings and
    declarations; `]]` and `§[` rejected; any surviving roman-numeral label rejected; numbered
    sections required to precede appendices; each reference list required contiguous with no
    number used twice; a paper citing itself by label flagged; and the counts in README,
    CITATION.cff, .zenodo.json and `build_site.py` checked against what is on disk. **The new
    checks were tested against injected defects and fire**; the audit exits non-zero now, so it
    can gate a push.

44. **Version 2.0.0, not 1.7.0.** Every filename and every citation form changed, so the DOI
    for 1.6.0 describes a different object. Item 27 already called this "a v2.0-shaped change";
    the metadata now says so.

**Verified after all of the above:** `audit.py` clean and exiting 0; `check_github_math` 0
problems; all nine verification scripts exit 0; every cross-paper and internal reference
resolves; every reference entry cited and every citation declared. Independently re-verified
here, from scratch: [P10, Thm 10] with no failure for odd $9 \le p < 3000$; [P10, Thm 11] with
exception set exactly $\lbrace 23, 31, 47, 49, 67, 85, 119, 121 \rbrace$; [P10, Thm 14] over
233,455 collisions with the identity holding and no value of $\Delta$ repeating.

45. **Every paper now numbers its own results from one.** He asked for this explicitly, so that a
    single paper can be forwarded to someone or continued by someone without carrying the set with it.
    What was there before was neither per-paper nor global but **six inherited sequences**: Papers 1,
    2, 3 and 4 each had their own; Papers 5 to 8 shared one running Theorem 1 to 16 (5 held 1–3, 6 held
    4–7, 7 held 8–12, 8 held 13–16); Papers 9 to 11 shared another running Theorem 1 to 14. So Paper 6
    opened at Theorem 4, Paper 8 at Theorem 13, and "Theorem 1" named a different result in six
    different papers — safe only because every citation carried a [Pn] label.
    Now: Paper 6's Theorem 4 → 1, Paper 8's Theorem 13 → 1 and its Verified Law 14 → Verified Law 2,
    Paper 10's Theorem 8 → 1, Paper 11's Proposition 2 → 1, and so on. Letter-suffixed variants follow
    their base (Paper 6's Corollaries 2a–2e → 1a–1e), and **Corollary 6b of Paper 8 becomes plain
    Corollary 1**, since its base lived in Paper 7 and it is independent content, not a variant. The
    appendix-labelled B1–B3 of Paper 7 keep their labels. Every cross-reference was remapped through the
    target paper's map and every unqualified reference through the paper's own, and the Numbering note
    in each part now says the numbering restarts and that it differs from releases before 2.0.0.
    **`audit.py` no longer exempts a part from the contiguity check**: each sequence must start at one,
    be in order, and have no gap — and it does, in all eleven.
    **The cost, stated so it is not discovered later:** any letter or post already sent that names a
    result by number now points at a different result. Section references are unaffected.

## Second full review before the push — 7 September 2026

A further pass, prompted by an outside review of the packaged v2.0.0. **The mechanical checks were
already clean, and the defects found were of a kind no checker catches: references that resolve but
point at the wrong result.**

46. **Semantic cross-references in the overview — the important find.** `audit.py` reported no
    problems because every `[Pn, Thm k]` existed. But a whole block of the overview was pointing at
    the wrong paper, a residue of the original split script mapping the two parents' labels
    wholesale. Twelve entries corrected: the gap alphabet, the ladder and the runs were cited to
    [P9] and are [P5]; the six exception positions were cited to [P9, Thm 4] and are [P6, Thm 1];
    the row/originality theorem was cited to [P10] and is [P7, Thm 3]; the bridge and the square law
    were cited to [P9, Thms 6, 7] and are [P6, Thms 3, 4]; the synchronised window was cited to
    [P11] and is [P7, Prop 1]. **[P9, Thm 1] exists — it is the depth cut — which is exactly why the
    checker was happy.**
    Also in the overview: three bare `(Thm 13)`, `(Thm 15)`, `(Thm 16)` from the old numbering, a
    malformed `[[P8], Verified Law 14`, and a legacy `(V, Theorem 6.)`. **Every reference in the
    overview is now qualified as [Pn, ...]** — it declares no results of its own, so an unqualified
    one is always an error, and nine such were found and fixed, three of which carried stale numbers
    ([P3, Cor 3] had been written "Cor 1", [P6, Prop 2] "Proposition 1", [P6, Thm 1] "Theorem 4").
    The closing entry still described "two test cases"; it now names four.

47. **Paper 2 was still carrying the six-paper map.** Its §0 opened "This is one of six papers" with
    the full 0/I/II/III/IV/V dependency table, then mixed old and new labels in the paragraph below
    it. Replaced by two sentences saying it is the second of eleven and pointing at the overview for
    the map — repeating the map inside a paper is what let it go stale in the first place.

48. **Paper 6 contradicted itself two lines apart.** One paragraph listed what
    `verify_exception_dichotomy.py` covers, including the sector-coupling budget and the ceiling of
    31; the next said those were "not yet in a script". The script does cover them (checks 21–25 and
    27), so the second paragraph is deleted. Its closing sentence also still said "the two test
    cases"; now four.

49. **[P11, §2.5], two further corrections.** "$\alpha_y = \beta_y$ exactly" overstated what the
    argument gives: the prime-number-theorem-in-progressions route gives each of them the same limit,
    not equality at finite $x$. Restated as both tending to the same product, so the ratio tends to
    one. And the sentence "Under Elliott–Halberstam the same computation gives $a < 1/3$" was
    claiming standard EH on both rails two lines after saying that even level $1/2$ on the
    rough-semiprime rail is an assumption. Now scoped to a level-one hypothesis **of
    Elliott–Halberstam type on both rails**, with a closing sentence saying that nothing here
    suggests EH alone removes the parity barrier.

50. **Two summary tables were incomplete**: Paper 7's did not list its Appendix B results
    (Theorems B1–B3, Corollary B1) and Paper 11's did not list its Proposition 1. Rows added.

51. **`code/build_site.py` still had `DATE = "2026-09-01"`**, so every page of the site carried a
    date two releases old while CITATION.cff read 2026-09-07. Corrected and the site rebuilt.

52. **Two soft claims tightened.** [P1] said sums of this shape "normally carry an error of size
    $\sqrt n \log n$ or $n^{1/3}$" in its abstract-level sentence — a wide comparison with no
    theorem attached; it now says distributional estimates of this shape normally carry a non-zero
    error term, and the body keeps the two named comparison classes. [P4]'s "Every application needs
    a window of length $\asymp z^2$" is now "Every application considered here".

53. **`audit.py` extended again, with the checks this pass would have needed.** It now rejects the
    stale phrases that mark split residue — "one of six/seven papers", "six/seven papers", "two test
    cases", `[[P`, and a legacy paren citation `(V, Theorem …)` — and **requires every statement
    reference in a document that declares no results of its own (the overview) to be written as
    [Pn, …]**. That last check is the one that would have caught item 46's stale bare numbers, and
    it fires on injected defects. Semantic validation of which paper a reference names is still
    human work; the checks narrow it.

**Proofs spot-checked independently this pass, from scratch, none using the repository's own code:**
[P5, Cor 1] $G_k = \prod(q-k)$ reproduced exactly for the line sets $\lbrace5\rbrace$,
$\lbrace5,7\rbrace$, $\lbrace5,7,11\rbrace$ at $k = 1..5$; [P6, Thm 1] over every sector to
$M = 2000$, 121 non-twin open cells and every one at one of the six named positions; **[P6, Cor 1b]
over 809 twin sectors below $M = 60{,}000$ and 226,704 line/sector pairs — 577 multiple closures by
a line above 31, every one of them $\lbrace D,F\rbrace$, zero violations**; [P7, Thm 1] the shift
law over every odd $p < 3000$ and every $q < 200$, zero violations; [P8, Thm 1] belt sizes over 427
consecutive prime pairs, zero mismatches; [P9, Thm 4] the identity $T = C-R+S$ cell by cell at
$(P,z) = (101,10), (1009,31), (2003,43)$, exact in all three; [P2, Thm 5] the midpoint identity to
$n = 8001$.

**One methodological note, since it cost a round.** A first attempt at [P6, Cor 1b] appeared to show
hundreds of violations; the test was wrong, not the paper — it tested divisibility of the composite
member's neighbours rather than of the partner given by the corollary's own formulas $Q_A,\dots,Q_F$.
Written down because the failure mode is worth remembering: **when a check contradicts a proof, the
check is the more likely suspect, and the paper's own definitions are the ones to test against.**

**Verified after this pass:** `audit.py` clean and exiting 0, with the new checks tested against
injected defects; `check_github_math` 0 problems; all nine verification scripts exit 0; every
statement reference in every document qualified and resolving; every reference list contiguous, fully
cited, with no number used twice; no stale phrase anywhere in the repository. Site and PDFs rebuilt.

## Third review — 7 September 2026, and it found a mathematical error

54. **[P6, §2.1] asserted $C_M = T_M$, and that is false. This is the first defect in this whole
    series of passes that is mathematics rather than bookkeeping.** The lemma above it is right:
    between the squares of consecutive integers coprime to six with no prime between them, a
    surviving cell *is* a twin pair. The paper then carried that across to the six-step sector
    $(M^2,(M+6)^2)$ and wrote "$C_M$ *is* the twin count of the sector", twice. It is not: the sector
    contains the births of $M+2$ and $M+4$, whose strikes are precisely the six exception positions
    the very next theorem names. **The paper's own published table contains the counterexample.** At
    $M = 10{,}005$ it prints $C_M = 504$; the true twin count is $503$, the extra cell being
    $(100{,}180{,}079,\ 100{,}180{,}081)$ whose upper member is $(M+4)^2 = 10{,}009^2$ — position $C$.
    Verified here directly at all four table rows computed from scratch: $X_M = 0, 0, 1, 0$ at
    $M = 1005, 5001, 10005, 20001$.
    §2.1 now states $C_M = T_M + X_M$ with $0 \le X_M \le 6$ as equation (3.4), says that the six named
    positions are the only way a sector's survivor count can move away from its twin count, and keeps
    the Hardy–Littlewood comparison as a diagnostic valid up to that explicit $O(1)$. The section
    title changes from "A surviving cell is a twin pair" to "When a surviving cell is automatically a
    twin pair", and the sentence "$C_M$ is the twin count itself, so it cannot differ from it" becomes
    the correct version. **Measured and written into the paper: over the 49,999 sectors below
    $M = 3\cdot10^5$, $X_M$ is $0$ in 45,439, $1$ in 4,369, $2$ in 186 and $3$ in five — never more,
    so the bound of six is not attained on that range.**
    The paper already knew the right statement in two other places ("$C_M$ exceeds the twin count of
    the sector by at most six", in [P6, A.3] and [P11, §2.4]); §2.1 simply contradicted them.

55. **The overview's *In brief* made the same conflation in one sentence**, putting the six exception
    positions inside "such an interval", meaning the prime-square belt. They are not there: the belt
    has no newborn line, the six-step sector has two. The two windows are now stated separately.

56. **Three more references that resolve and are wrong.** [P2, §5.3] cited [P9, Thm 4] — the identity
    $T = C-R+S$ — for the six exception positions, which are [P6, Thm 1]; and [P10, §2.10] cited the
    same theorem twice as "the sector criterion", now [P6, §2.2].

57. **[P6, §3] was the largest surviving block of pre-split numbering.** It listed the shift law as
    "Theorems 8, 9, 10, Corollaries 4, 5", the sector laws as "Theorems 11, 12", the tracks as
    "Theorems 15, 16", the shell as "Propositions 4b, 4c, 4d ... §3.1–7.2", and the reach as
    "[10, VL 14]" — which after the reference renumbering pointed at Schinzel–Sierpiński. The section
    is rewritten and split in two: **Proved in this paper**, listing only Paper 6's own results, and
    **Exact results in the companion construction papers**, every entry labelled [P5], [P7] or [P8].
    That division is also the honest one: a conclusion section listing four papers' results under
    "Proved here" was a leftover of the parent document.

58. **One roman numeral had escaped every sweep**: [P9, §2.3] said "geometric variations in Papers 2
    and IV". The audit's legacy check only matched a label directly after the word "Papers", not one
    after "and". Pattern widened, and the sentence now reads [P2] and [P6]–[P8].

59. **Two gaps in `audit.py` closed by this pass.** It was reading equation tags only from `\tag{}`
    and standalone lines, so the inline form `\text{(3.2)}` used throughout these papers was invisible
    — which is how a duplicate tag (3.2) survived my own edit, and how an uncited (A.1) had sat there
    unnoticed. Both now caught; the duplicate is renumbered (3.4) and the uncited tag on a defining
    equation is removed. Legacy-label matching widened as in item 58. Both new checks were confirmed
    to fire.

**Verified after this pass:** `audit.py` clean and exiting 0; `check_github_math` 0 problems; site and
PDFs rebuilt. The $C_M = T_M + X_M$ correction was arrived at from the paper's own table, and the
counterexample it contains is now printed in the paper rather than sitting silently in a row of it.

## README pass — 7 September 2026

60. **The README was written for the maintainer, not the reader.** Its `Contents` section listed the
    eleven papers and then three build recipes — how to regenerate the site, how to regenerate the
    PDFs, and how to run the rendering checker — thirty lines of instructions that only the author
    ever uses, sitting before the reader reaches Status. Worse, **"How the citations work" was buried
    between two of them**, though it is the one thing a reader needs early to make sense of
    `[P6, Thm 1]`.
    The three build sections are **deleted, not moved**. All three scripts already document
    themselves at the top — `build_pdfs.sh` even carries the warning about running the checker
    first — so the README was pure duplication, and duplication is what went stale everywhere else
    in this repository. `check_github_math.js` had a stale header naming itself "check.js"; it now
    carries its own usage line, including `npm install katex`, and the description of what it looks
    for.

61. **A section the README was missing, and it mattered more than the ones removed.** The opening
    claims "runnable code for every number printed" and "every script exits non-zero when its claim
    fails", and then never said how to run one. A short **Checking a claim** section now gives the
    three commands: one script, all nine, and `audit.py` for the structure.

62. **Two sections cut to what a reader needs.** The AI-assistance section went from 32 lines to 9:
    the division of labour and the closing standard stay, the catalogue of which model caught which
    error goes — that is a diary entry, and it is recorded in full in these notes. The three method
    rules went from 29 lines to 13 and moved after Status, so that nothing instructional stands
    between the reader and what the work claims.
    Kept deliberately: the fifteen-row table mapping each headline result to where it already lives
    in the literature — it is the most important thing in the file — and the Status paragraph with
    the open question and the invitation to send corrections.

    README: 265 lines to 212, and no shell command appears before the reader has passed the papers.

63. **`audit.py` crashed on Windows.** It opened the papers without naming an encoding, so Python
    used the system default (cp1252 there) and died on the first non-ASCII character — the en dash in
    a table. It had never shown up because every run until then was on Linux, where the default is
    UTF-8. Both `open()` calls now pass `encoding="utf-8"`. Worth recording as the same lesson as the
    rendering checker: **a check that has only ever run in one environment has only been tested in
    one environment.**

## Rendering failures found on the published page — 7 September 2026

64. **The rendering checker had never run.** `check_github_math.js` takes its files from
    `process.argv.slice(2)`; every time it was invoked in this work it was invoked as
    `node code/check_github_math.js` with no arguments, so it looped over an empty list and printed
    `TOTAL problems: 0`. The correct invocation is in the README and was not used. Run properly,
    against the version that had just been pushed, it reported **45 problems**. The checker now
    **refuses to run with no files and exits 2**, because a run that silently passes is worse than
    no check.

65. **The mechanism was the one the README already describes: GitHub strips the backslash from
    escaped ASCII punctuation inside math.** Fifty-one sites, five kinds, all fixed:
    `\,` (29) became a literal comma — this is why `$H\,w_H$` rendered as "H,w_H" on the page, which
    is what identified the mechanism from the screenshots; replaced by `\ `, whose space is outside
    the stripped range. `\%` (14) became `%`, which opens a KaTeX comment and swallows the rest of
    the formula; the percent sign now sits outside the math. `\#` (3) became `#`, a reserved
    character — the "macro parameter character #" error visible on two pages; the cardinality is now
    `\lvert\lbrace…\rbrace\rvert` and the primorial is written in words. `\\[2pt]` inside `cases`
    became `\[2pt]`, an undefined control sequence; replaced by `\cr`. `\!` (2) removed, and one raw
    `<` replaced by `\lt`.

66. **A second mode the checker did not know about: display math inside a blockquote.** Theorem 1 of
    Paper 6 rendered as raw source with its subscript underscores eaten and the middle italicised —
    markdown emphasis had claimed the `_` of `}_{`, which means GitHub never treated the block as
    math. **All 62 `> $$…$$` sites in the set are converted to inline `$\displaystyle …$`**, which
    every screenshot confirms renders reliably inside a blockquote.

67. **A third mode: two math spans separated by a single punctuation character merge into one.**
    `$10^4$–$10^5$` in a table cell rendered as a broken half-cell. Eleven sites, now single spans
    with `\text{--}` inside.

68. **Unbraced fraction arguments braced.** `\tfrac n8` and `\tfrac{a+b}2` were the three remaining
    checker warnings; an unbraced argument is exactly the shape that breaks when a brace vanishes, so
    they are now `\tfrac{n}{8}` and `\tfrac{a+b}{2}`.

    **The checker now carries three new checks** — display math in a blockquote, adjacent spans, and
    a space before a closing `$` — and all three were confirmed to fire against injected defects.
    Full run: **0 problems** across all twelve documents and the README.

    **The lesson is the third method rule in the README, and it applied to me.** "A check that has
    never failed has not been tested." This one had never failed because it had never run, and the
    only thing that caught it was opening the published page and reading it.

## Still to do on your machine

- **Rebuild the PDFs**: `sh code/build_pdfs.sh`. The PDFs in `docs/papers/` were rebuilt from
  the corrected sources, but on a machine without `lmodern`, so they were produced with a
  substitute font and the pagination differs slightly from what your build gives. Everything
  else in `docs/` is final.
- `.zenodo.json` and `CITATION.cff` read 2.0.0; the tag `v2.0.0` does not exist yet.
- `COMMIT_MESSAGE.txt` is final and carries no hold.
