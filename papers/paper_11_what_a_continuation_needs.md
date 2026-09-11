# What a Continuation Would Have to Supply

## Paper 11. The external ingredient, the limitations, and the routes already tried

---

### Abstract

The closing part of the set. It states what an external ingredient would have to supply for the identity of [P9] to become a theorem, why the stopping point is the right one rather than an accident of effort, what the work is not — in particular that it is not a new sieve — and where each route would have to be resumed. An appendix records the routes that were tried and closed, with the measurement that closed each, so that they are not retried. **No progress toward the twin-prime conjecture is claimed.**

**Numbering.** This paper is one part of a set that was written as a single document and is now published in parts. Each part numbers its own results from one and is self-contained: a reference of the form [Pn, Thm 1] means Theorem 1 of Paper n, and an unqualified "Theorem 1" always means this paper's own. Result numbers therefore differ from those of the earlier seven-document releases, where the whole set shared the numbering of the single document.

**How to read the claims in this paper.** Statements set as Theorems, Propositions and Corollaries are proved, and the proofs are given. Anything described as *measured* is a computation over a stated finite range and is labelled as such where it occurs.

**Keywords:** twin primes, parity obstruction, level of distribution, cell coordinates.

**MSC 2020:** 11N35, 11N05, 11A41.

---

## Summary of the results in this part

**§2 — Conclusion**

| Result | What it says | Section |
|------------------|-----------------------------------------------|---------|
| ***What is required*** | What an external ingredient would have to supply; why this stopping point is the right one; that this is not a new sieve; the limitations; and what the framework does not presently supply. | §2 |
| **Proposition 1** | In any contiguous block of length $H$, each residue of a period-$q$ ruler occurs $\lfloor H/q\rfloor$ or $\lceil H/q\rceil$ times — the only non-probabilistic constraint the framework produces, and useless at the scale required. | App. B.2.2 |

---

## 1. Setting

[P1] to [P8] supply the framework, [P9] the exact form of the obstruction, and [P10] the four tests whose deficits are classified here. Nothing else is imported.

- **[P1]** supplies the window combinatorics: the increments $W_j$ of $\lfloor 2j^2/p\rfloor$, their uniform bound and their exact histogram.
- **[P2]** supplies the coordinates: the line $L_p(k) = p(p+2k)$ beginning at $p^2$, the grid $L_3$, the cells $C_b = (6b-1,6b+1)$.
- **[P3]** supplies the exact cycle laws: the four-state census and its refinement by inheritance depth.
- **[P4]** supplies the passage to a short window, and the measurement $T/M \approx 0.80$ at moving depth.
- **[P5]–[P8]** supplies everything this paper tests: the gap alphabet, the six exception positions, the closing budget, the clocks, and the sector inheritance laws.

**The three words used constantly below**, all as defined in [P2]: a **line** $L_p$ is the odd multiples of $p$ from $p^2$ onward; a **cell** is a pair $C_b = (6b-1,\ 6b+1)$, and it is **open**, or **survives** a set of lines, when neither member lies on any of them; the **window** is the interval between two consecutive odd squares, which in cell coordinates is a block of consecutive indices. A twin pair is an open cell whose two members are both prime, and inside $(u^2,v^2)$ sieved by every line up to $u$ the two notions coincide [P6, §2.1].

**How this paper is organised.** It is the conclusion of the set and it answers four questions in order: what has been established, where it stops, what kind of external information a continuation would have to supply, and why none of the routes already tried supplies it. §2 does the first three; Appendix B carries the routes in full, so that a route closed by measurement or by proof is written down rather than left to be attempted again. Throughout, a statement labelled *measured* is a numerical finding with its controls; it is not a theorem and not an asymptotic claim.

---

## 2. Conclusion

### 2.1 What an external ingredient would have to supply

Taking [P10, §2.5] and [P10, §2.15] together, the deficits exposed by these tests can be organised into four categories, each corresponding to a standard class of tools.

| deficit | what is missing | standard remedy |
|--------------|--------------------------|--------------------------------------|
| **Summation** ([P10, §2.15]) | control of the aggregate when local laws are summed over lines | large-sieve inequalities; Buchstab iteration with sign selection (Rosser–Iwaniec [5], Harman [4]) |
| **Factor size** ([P10, §2.5]) | a weight sensitive to *how large* the factors are, not only to how many there are | Richert's logarithmic weights; internally, the per-bin refinement of [P3, §4.3] — **carried out there, and it closes** |
| **Window transfer** ([P4, §6]) | passage from a cycle statement to a short window at $s\approx2$ | Buchstab's function; the beta-sieve; Richert weights *in application* |
| **Bilinearity** ([P4, §5.4], [P10, §2.2]) | information about $n$ *as a product*, with independent weights on the factors | Type II sums; bilinear forms; dispersion |

**One measure of the distance, from outside the framework.** The same window is reached unconditionally by a classical dimension-two sieve with Richert weights: [P12, Thm 1] gives a pair $(a,a+2)$ with $\Omega \le 5$ on each member in every sufficiently large window between consecutive squares, and [P12, Thm 2] gives $\Omega \le 4$ on each member once the interval is lengthened to $X^{0.52}$. What this framework has not supplied is therefore an addition to a known tool, not a first approach to an unreached target.

**Within this analysis the four deficits are progressively stronger.** The first three concern aggregation, weighting and transfer of information already encoded by the sieve pattern. The fourth asks for bilinear information that the present framework does not generate. [P3] and [P4] address the factor-size bookkeeping and measure the window transfer; they do not supply the missing bilinear control needed for a twin-prime conclusion.

**One deficit has been narrowed rather than removed.** We initially listed *continuity* — the absence of any measure sensitive to the factorisation beyond a count — as a flat impossibility. [P3, Thm 2] disposes of the nonlinearity, and [P3, §4.1] shows what is left is the dependence on factor size, together with a candidate repair. The lesson is worth stating, since it is the one place in this work where a stated obstruction proved to be partly an artefact of insufficient refinement.


---

### 2.2 Why the stopping point is the right one

Because it is where genuinely new information about the survivors would have to enter, rather than another rearrangement of the same sieve identities. In standard sieve terminology, the missing kind of input is **Type II / bilinear information**: control that sees an integer through interacting factors rather than only through membership in residue classes. The present cell framework supplies no such bilinear estimate for the twin-prime correlation, so the argument stops there.

$$\boxed{ \text{What is missing is not a cleaner formulation but an arithmetic input of a different kind.} }$$

### 2.3 This is not a new sieve

The main sieve-level objects used across the series have classical counterparts: the dimension-$2$ sifting density, the sifting limit $\beta_\kappa$, the sieve density $V(z)$ and Buchstab-type corrections. Correspondingly, the obstruction located here from several independent directions — residue classes, height, square position, cell states, $\Omega$, collective cancellation, and the interaction of the two motions — is the obstruction the literature states in one sentence: **the sieve counts rough integers and does not separate a prime from a semiprime.**

What the series adds is not a new tool but a change of type. Several quantities that are usually embedded inside sieve estimates become exact cycle identities in these coordinates. Those identities help isolate where the remaining loss enters, even though the short-window conclusions still require separate estimates. Several failures come with quantitative diagnostics: the **predicted** cover margin $1.0073$ under the local-constant hypothesis (App. B.2.1.2), the flat $L^2$ ratio of [P4, §5.3] once the normalisation is corrected, the sifting variable $s\approx2$ against $\beta_2=4.2664$ (App. B.2.1.3), the Jacobsthal counting overshoot ([P10, §2.4]), and the measured transfer curve from about $1.0000$ to $0.80$ [P4, §6].

**A quantitative form of the same sentence, and it names the exchange rate.** [P9, Thm 1] and [P12] are the same sieve at two settings of one dial, the cut $z$. Cutting deep, with $z^3$ above the window as in [P9, Thm 1], makes every surviving endpoint prime or a product of exactly two primes — a factor bound of $\Omega \le 2$ on both members, obtained for nothing. But that cut puts the sifting variable at $s \approx 1.5$, and the lower bound sieve returns zero below $\beta_2 = 4.2664$, so the count of such cells is not bounded below at all. Cutting shallow, at $z = U^{1/16}$ as in [P12], puts the variable at $s = 8$, where the lower bound is available and the count is of order $m(\log m)^{-2}$ — and there the factor bound has to be bought back by Richert's weights, which reach five per member in the square window [P12, Thm 1]. The two parts are not two tools to be combined; they are one tool at two settings, and the coefficient of [P12, §5] is the exchange rate between them.

**Even the hypothetical next rung would not be a twin.** A pair with $\Omega \le 2$ on both members leaves $(1,1)$, $(1,2)$, $(2,1)$ and $(2,2)$, and separating the first requires the parity of $\Omega$ — which is exactly what [P9, Thm 6] writes as an identity, and exactly what the sieve does not see. A bound on how many prime factors there are says nothing about whether that number is even or odd.

### 2.4 Limitations

1. **The framework is multiplicative throughout.** A line is a set of multiples, a strike is divisibility and a meeting is a common divisor. Additive prime correlations such as fixed differences are not determined by these multiplicative identities alone; an additional arithmetic input is required.
2. **Exactness on the cycle, not automatically on the window.** Paper 3 is exact over a cycle of length $\prod q$. Paper 4 shows numerically that many soft statistics transfer well, but the short-window statements are partly empirical.
3. **The closing budget is not about twins.** The graph of [P7, App. A] joins survivors at distance $6$, so its conclusion concerns prime pairs $(p, p+6)$. The caution is stated at the head of that appendix and repeated here because the phrase "gap 6" carries two meanings in this subject.
4. **No explicit constants.** The framework produces exact identities and measured ratios, not explicit numerical bounds valid from a stated point onward. The published results on almost-primes between squares are explicit-constant work, and the framework has no machinery for it.
5. **Several statements are measured, not proved,** and are labelled as such: the stability of $T/M \approx 0.80$ [P4, §3.2], the saturation law of [P10, §2.3], the transfer curve [P4, §6], and — in [P10, §2.6] — the quadratic order of the singular-series sum together with its coefficient $0.0329$, for which we have no closed form and no proof. The exception-budget results quoted in [P10, §2.7] are of a different kind and should not be read as measurements: the ceiling of $31$, the admissibility of the surviving configuration and the emptiness of the timing table are finite exhaustive computations over stated residue classes, and each is a proof. They are carried out in [P6, §2.3]. Two scripts cover them. `verify_exception_dichotomy.py` carries the closed forms and the $\lbrace 5,7\rbrace$ table, [P6, Cor. 1], the per-phase caps and their sum before the coupling (checks 21 and 22), the budget after the coupling across sector joins (check 23), the ceiling of $31$ over all $2{,}431$ alignments and the nine that attain it (checks 24 and 25), and the alignment of the escapee at $448{,}353$ among them (check 27). `verify_exception_certificate.py` carries the part the first one stops short of: the $28$ maximal configurations, every prime that eliminates each of the $27$, and the $59$ polynomials of the survivor together with an admissible residue at every prime — the degree being $90$, only $q \le 90$ has to be examined and the script examines every prime to $200$. No table in this set is printed without a script that regenerates it.
6. **Priority is not claimed for any result in these papers.**
7. **Negative claims deserve the same suspicion as positive ones.** We recorded one impossibility claim — that the framework could not carry analytic weights — which proved to be an artefact of insufficient refinement; Paper 3 removes it in two stages. Appendix A lists the further withdrawn results. **The rate at which this structure produces plausible but spurious signals is itself among the findings.**

### 2.5 What a continuation would have to supply, route by route

Each route in this work stops at a definite quantity, and in most cases the shortfall has been measured. We list them so that a reader who wants to continue knows where the road ends rather than only that it does.

**The identity of [P9, §2.3] needs a sign, not a bound — and here is exactly what the sign is.** $R \lt  C$ is the statement that a Liouville sum over the sifted set is negative. Write $A$ and $B$ for the numbers of primes and of products of two primes among the $z$-rough integers to $x$ at $z = x^{1/3}$, so that $B/A \to \log 2$; and let $\alpha$ and $\beta$ be the proportions of each kind whose neighbour $n \pm 2$ is also $z$-rough. The prime endpoints of the open cells number $2A\alpha$ and the composite ones $2B\beta$, so the mean of $(-1)^{\Omega}$ over the endpoints of open cells is $(B\beta - A\alpha)/(A\alpha + B\beta)$ — exactly $(D - T)/H$, where $D$ counts the cells with two composite members — and it is negative if and only if
$$\frac{\beta}{\alpha} \ \lt \ \frac{A}{B} \ \longrightarrow\ \frac{1}{\log 2} = 1.4427 .$$
The two rails must both be counted: a negative mean on one rail alone is consistent with every open cell being prime–composite and no twin at all. So what the twin problem needs, in one line, is that **the neighbour condition may favour the composites over the primes by at most $44$%**, together with the existence of open cells. Measured, the ratio $\beta/\alpha$ is $1.0008$, $1.0085$, $0.9990$, $1.0005$ at $x = 10^5, 10^6, 10^7, 10^8$: the condition treats the two kinds alike to the third decimal, against an allowance of $44$%.

*What is proved.* If the neighbour is sifted only to a fixed $y$, then $\alpha_y$ and $\beta_y$ both tend to $\prod_{3 \le r \le y}(r-2)/(r-1)$, so their ratio tends to $1$, since primes are equidistributed over the admissible classes modulo each $r$ and so are the rough semiprimes, by fixing the smaller factor and applying the prime number theorem in progressions to the larger; with Siegel–Walfisz uniformity this extends to $y = c\log\log x$. That preserves the mean at $-0.1812$. **Negativity alone goes much further, under one stated assumption.** Sifting the neighbour to $y = x^{a}$ at level of distribution $x^{1/2}$ gives the linear sieve at $s = 1/(2a)$ on the same local densities for both kinds, hence
$$\frac{\beta}{\alpha} \ \le\ \frac{F(s)}{f(s)} + o(1),$$
with the linear sieve functions in their standard ranges,
$$F(s) = \frac{2e^{\gamma}}{s} \quad (1 \le s \le 3), \qquad f(s) = \frac{2e^{\gamma}\log(s-1)}{s} \quad (2 \le s \le 4),$$
and $F$ continued above $s = 3$ by its own delay equation $sF(s) = 2e^{\gamma} + \int_3^s f(t-1)\ dt$. **The level of distribution is the assumption here, and it is not the same on the two rails.** For the prime rail it is Bombieri–Vinogradov. For the rail of $z$-rough products of two primes we assume the corresponding Bombieri–Vinogradov estimate for that sequence, with the weights and the constraints on the two factors used above; the standard convolution form makes it plausible, but we have not found it stated for this sequence and do not prove it here. So what follows is proved on the prime rail and conditional on that estimate for the other,
and at $s = 3$ the ratio is $1/\log 2$ **exactly** — the threshold itself. For $s \gt  3$ it falls below it, so the conditional mean is provably negative whenever $a \lt  1/6$: at $y = x^{1/7}$, for instance, $F(3.5)/f(3.5) = 1.1422$ and the mean is at most $-0.116$. (The continued branch is what is used: $F(3.5) = 1.0652$ and $f(3.5) = 0.9326$. The closed form $2e^{\gamma}/s$ is not valid at $3.5$ and would give $1.0914$ instead.) The coincidence at $s = 3$ is structural: $f(s)/F(s) = \log(s-1)$ on $[2,3]$ while $B/A = \log(u-1)$ for integers rough to $x^{1/u}$, so the condition is simply **$s \gt  u$** — the neighbour's sieve parameter must exceed the number's own — and with the level halved by Bombieri–Vinogradov that is $1/(2a) \gt  3$, i.e. $a \lt  1/6 = \tfrac13 \cdot \tfrac12$. Under a level-one distribution hypothesis of Elliott–Halberstam type **on both rails** — the same assumption again, raised from level $1/2$ to level $1$ — the computation gives $a \lt  1/3$ with **zero margin at $1/3$ itself**: it lands exactly on the threshold and does not cross it, which is a second reading of why it does not yield twins. Nothing here suggests that Elliott–Halberstam alone removes the parity barrier for twins.

*What is not.* Negativity at neighbour depth $x^{1/6-\varepsilon}$ produces no twin, because the neighbour may still carry a prime factor between $x^{1/6}$ and $x^{1/3}$ and [P9, Thm 6] needs both members sifted to the same depth. So the gap this route leaves is precisely stated: raise the neighbour's depth from below $1/6$ to $1/3$ while keeping the sign, which by the reading above is the gap between level of distribution $1/2$ and level $1$ — and even level $1$ arrives with no margin. A further measurement closes one tempting shortcut: adding the line $43$ to the neighbour's sieve at $x = 10^5$ moves the mean from $-0.3519$ to $-0.3484$, so it is not the case that each added line makes the mean more negative, and no line-by-line accumulation argument is available. No sieve-shaped object supplies the sign in any case. *The four measured ratios, the values of $F$ and $f$ from their own delay equation, the exact coincidence with $1/\log 2$ at $s = 3$, and the line-$43$ measurement are regenerated by `code/verify_parity_rails.py`.* The point is not that survival fails to determine $\Omega$ — sifting to $\sqrt{x}$ determines primality exactly — but that at the depth this identity requires the sieve delivers no positive lower bound at all, so there is nothing on which to read a sign; the fixed-$z$ case, where both means vanish by periodicity, carries no information about finite $u$.

**The sieve lower bound needs the parameter to move by a factor of four.** A dimension-two lower bound is available only for $s = \log X/\log z \gt \beta_2 = 4.2664$. The twin criterion, in any window whose length is comparable to its square root, sits at $s \approx 1$. This is the reason the argument of [P9, §3.2] cannot be repaired by sharper constants: **the gap is a factor of four in a parameter, not a factor in a constant.** A construction that claims a positive lower bound at $s \approx 1$ is claiming something that would also prove Legendre's conjecture, and should be checked against that first.

**Even Elliott–Halberstam in full leaves the survivors less than half prime.** At level of distribution $\theta$, the deepest provable sieve is $z = X^{\theta/\beta_2}$; the prime share of survivors there is $0.209$ at $\theta = 1/2$ and $0.417$ at $\theta = 1$. So a continuation through the level of distribution alone cannot reach a set of survivors that is mostly prime.

**An argument that sees only sizes and counts cannot work.** The control of [P9, §3.5] gives the same lines the same number of residue classes, chosen freely, and they cover the window completely — zero survivors against $8$ to $995$ for the true classes. So a proof of non-covering that uses only the number of lines, the number of classes each removes and the length of the window would apply verbatim to the greedy allocation, where the covering succeeds; no argument of that form can work, in these windows or in any window where the greedy allocation covers. **Any continuation must therefore use the arithmetic of the forced classes $\pm 6^{-1}$ and not their number.** Stated at that width and no wider: the control is finite, so it bounds no asymptotic statement about capacities; it leaves open any argument using a further property of the true classes — their distribution, their correlations between lines, their behaviour under translation — which the greedy allocation does not have; and it says nothing about switching or about an exchange of masses, which do not proceed by counting resources at all.

**The smoothed criterion is Jacobsthal's function.** Applying the double Fejér window to the whole survivor mask and asking for a positive smoothed count at every centre is equivalent to bounding the largest gap in the coprime set — the least admissible $H$ equals half that gap to within one in every case tested. A continuation there is a bound on $h(k)$ polynomial in $P$, which is a known hard problem and not a weaker one.

**And the criterion itself is exact, not a reduction.** $C_M$ exceeds the twin count of the sector by at most six, so any lower bound on $C_M$ is a lower bound on twins. That is what makes the framework's statements sharp and also what prevents them from being a route: **there is no slack in the criterion to be exploited.**

**What is missing, in one sentence.** A Type II or bilinear estimate strong enough for the twin correlation, or a parity-breaking input of the kind Chen's switching principle supplies for $P_2$. Further rearrangement of the same periodic identities will not produce either; every rearrangement we tried is recorded above or in Appendix B, together with the number at which it stopped.
---

## Appendix A — Note on method

A single rule was followed: **every deviation was measured against an explicit baseline before being interpreted.** Several apparent results were withdrawn under it, and they are recorded here because the rate at which this structure generates spurious signals is part of the finding.

- An apparent $50$% excess of gap-6 pairs in the square window proved to be a baseline error: for a pair $(n, n+6)$ the line $3$ forbids one class, not two, since $6 \equiv 0 \pmod 3$. With the correct baseline the window is slightly *poorer* than the naive periodic average, consistent with the Buchstab-type short-window correction discussed in Paper 4.
- An apparent concentration of future composites at the endpoints of gap-6 pairs proved to arise from a wrong definition of degree; with the correct definition the concentration factor is $1.007\text{--}1.015$, indistinguishable from a random control sample of the same size.
- A statistically significant slope ($z = 9.10$) linking small-factor and large-factor parity proved to be an artefact of an insufficient control: a cubic polynomial failed to absorb the size dependence. With bins of width $0.02$ in $\log$ and permutation within bins, the same data give $z = -1.11$.
- An apparent square-window bias of $1.5$% in the $e$-strip proved to be a statistic artefact: averaging per-sector *ratios* rather than pooling, with only 2–4 samples per sector.
- The asymptotic constant for $\tau$ was first derived from the full-cycle density $32C_2e^{-2\gamma} = 6.6594325$, giving an apparent surplus of $13.1$%. This was wrong: sieving to depth $P$ integers of size $P^2$ places one exactly at $u = 2$, where the Buchstab correction is not negligible. The candidate local scale is $16C_2e^{-\gamma}=5.9304658$, differing from the full-cycle scale by $e^{\gamma}/2=\omega(2)/e^{-\gamma}$. The measurement $T(P)\log^2P/P^2=5.93072$ at $P=9973$ strongly favours this scale on the tested range, but does not establish the asymptotic constant. **Accordingly the $0.73$% surplus is a conditional prediction, not a theorem.**
- A candidate zero-crossing near $2/3$ for the deviation profile is numerically close to $\sqrt{1-e^{-\gamma}}=0.6622239$, which the present data favour among the tested fits; and a candidate amplitude $e^{2\gamma}/4 = 0.7930547$ must **not** be treated as independent evidence, since the profile and the final deficit are linked by the exact identity of [P4, §4.2] and are therefore the same measurement seen twice.

- **The same constant was later reached a third time, by a third route, and it is again not independent.** Writing $\delta_p$ for the fraction of the cells still surviving that line $L_p$ closes, the survival product $R(P) = R_0\prod_{5\le p\le P}(1-\delta_p)$ is an exact identity, and $\prod(1-\delta_p)/\prod(1-2/p)$ was measured at $0.9436,\ 0.9221,\ 0.8996,\ 0.8840$ for $X = 10^6 \dots 10^9$, apparently approaching $e^{2\gamma}/4$. It is the same quantity as above: $\delta_p$ is computed *from the survivors*, so the product contains the twin count by construction, and substituting the Hardy–Littlewood count in integral form reproduces the whole column to four decimals ($0.8842$ against $0.8840$ at $X=10^9$). **The one thing in that experiment which is not a restatement is where the deviation lives:** $\delta_p = 2/p$ to within $10^{-3}$ for every $p \le X^{1/4}$ — measured ratio $1.0000$ for $u \ge 5$ — with the entire departure confined to $u \in (2,4)$, and the partial products agreeing with $\big(e^{\gamma}\omega(u)\big)^2$ there. That is the fundamental lemma of the sieve stated in the vocabulary of App. B.2.1.1, and it is the reason no redistribution of effort among the lines changes anything: below $X^{1/4}$ there is nothing to redistribute.

- **A stated obstruction proved to be an artefact.** We first concluded that the framework could not carry analytic weights, since all its objects are binary or counts and a weight would require an infinite state space. Refining the four-state law by *inheritance depth* — a quantity that changes by exactly one under a strike — makes the state space finite and the law exact ([P3, Thm 2]), and arbitrary weights follow. **The negative control matters here: binning by weight *value* does not close (error up to $24$%), so the refinement had to be by depth and not by weight.** The general lesson is that an impossibility claim in this setting should be tested against at least one refinement before being recorded.

Any subsequent work in this structure should begin with the baseline, not with the deviation — and should treat its own negative claims with the same suspicion as its positive ones.

---

## Appendix B — Routes that were tried and closed

The two accounts below were in the body in an earlier version. They are collected here so that the body reads as one argument — the obstruction, then why no ordinary sieve crosses it — and kept in full because a route closed by measurement seems to us worth more written down than left to be attempted again. Each has a stub in the body stating its conclusion.

### B.1 Five routes through the line geometry, closed by measurement

[P9, §§2–3] argues that the obstruction is the distinction between $\Omega=1$ and $\Omega=2$ inside the sifted set. That argument is analytic. This section reports what happens when one instead asks the line geometry itself for the missing information, in a single explicit window, and follows each of the five natural routes to the point where it stops. Every number below is **measured**, not proved.

**The window.** We take the phase of the surviving configuration of [P6, §2.3],
$$M_0 = 448{,}353, \qquad X = (M_0+210)^2 = 201{,}208{,}764{,}969,$$
which carries $N = 31{,}392{,}060$ cells. The cut is $z = 5857$, the largest prime with $z^3 \lt  X$. [P9, Thm 1] is applied in the form its proof gives: every prime factor of a survivor is at least the **next** prime, $5861$, and $5861^3 = 201{,}333{,}092{,}381 \gt  X$, so three of them are impossible and each surviving endpoint is $P$ or $P_2$. (Read with $z$ itself the hypothesis $z^3 \gt  X$ would fail here, since $5857^3 = 200{,}921{,}157{,}793 \lt  X$.) Writing the four states of a surviving cell by the status of its two endpoints:
$$C = 1{,}049{,}024, \quad R = 857{,}695, \quad S = 174{,}791, \quad T = 366{,}120,$$
in the letters of [P9, Thm 4]: $C$ the surviving cells, $R$ the $P_2$ endpoints among them (a cell with both endpoints composite contributing two), $S$ the cells with both endpoints $P_2$, and $T$ the twins. The identity $T = C - R + S$ holds exactly.

Two side measurements fix the scale. The prime share among the $2C$ endpoints of the surviving cells is $1{,}240{,}353/2{,}098{,}048 = 0.591196$ against the limit $1/(1+\log 2) = 0.590616$ of [P9, §3.2] — agreement to four decimals, because a short window at height $Y$ carries no secondary term in the prime count, which is the reading [P9, §3.2] gives of its own global table. And the survivors of **all** lines up to $M_0$ number $366{,}130$, that is $T$ plus ten composite cells whose two factors both exceed $M_0$; the same measurement at $M_0 + 510{,}510$ and $M_0 + 1{,}021{,}020$ gives $699{,}747 = 699{,}726 + 21$ and $1{,}010{,}762 = 1{,}010{,}734 + 28$. **The survivor count of a square window is the twin count plus a two-digit remainder.**

**Route 1: prime gaps.** Each $P_2$ endpoint has a unique smallest factor $q \in (z, \sqrt{X}]$. Classify $q$ by its gap to the next prime and compare the observed count in each class against the count predicted by the cofactor interval $L/q$ and the prime density at $X/q$. Over twenty-nine gap classes from $2$ to $60$ the ratio is flat at $0.171$ to $0.176$, and the largest standardised residual anywhere is $1.59$ — smaller than one expects by chance from twenty-nine classes. A control is required here and it passes: the mean gap rises from $10.16$ to $12.92$ across octiles of $q$, so gap classes are confounded with $q$, and the same ratio binned by $q$ instead is flat to four decimals ($1.0004$, $0.9995$, $1.0021$, $0.9969$, $0.9926$, $1.0052$, $1.0059$, $0.9943$). The gap after $q$ is a function of the small factor alone, and the count of endpoints it owns is a prime count in the interval $(\mathrm{lo}/q, \mathrm{hi}/q)$; nothing links the two.

**Route 2: line capacity.** The $36{,}824$ lines in $(z, \sqrt{X}]$ have $25{,}353{,}670$ raw strikes available inside the window, against the ceiling $C - 1 = 1{,}049{,}023$ that a single twin needs — larger by a factor of $24.2$, the usual outcome. Restricting the count to lines that **divide** an endpoint of one of the surviving cells gives $857{,}712$, against $R = 857{,}695$: a difference of **seventeen**, the endpoints both of whose prime factors lie below $\sqrt{X}$ and which are therefore counted twice. The difference is a reminder that divisibility and a strike are not the same relation — a line reaches a position only from its own square onward — and it is the strike count, not the divisor count, that Theorem 2 makes equal to $R$. So the restricted capacity is not an upper bound on the output; it **equals** the output. That is [P9, Thm 2] read as a statement about capacity — a surviving composite has exactly one responsible line, so there is no slack between what the lines can do and what they do.

Two further quantities locate why no upper bound is available here. First, the cofactor interval $L/q$ equals the sieving depth $z$ at $q = L/z = 32{,}159$; above that point the interval to be sifted is shorter than the sieve limit and no sieve estimate applies at all. Of the $36{,}824$ lines, $34{,}145$ lie above it, and they own $509{,}602$ of the $P_2$ endpoints — $59.4$ per cent of $H$. This is the vacuous region of [P9, §3.3], and the measurement supplies the number that section states qualitatively: for $\Omega \le 2$ Chen's switching principle need only show the vacuous region is small, and here it is not small, it is the majority. Second, dropping the partner condition — counting rough $P_2$ endpoints without requiring the other member of the cell to be rough — raises the count from $857{,}695$ to $4{,}997{,}471$, which is $4.76$ times the ceiling. The partner condition supplies a factor $0.1716$ and it is the whole of the margin; any bound that does not see both members of the cell at once fails by a factor of five before the sieve constant is reached. A Brun–Titchmarsh bound on the cofactor, which does not see it, gives $24{,}119{,}320$.

**Route 3: the two endpoints.** Under independence one would predict $S = C \cdot h_L h_R$ with $h_L, h_R$ the two $P_2$ shares. Measured against that prediction, over the same three windows, $S$ gives $0.99701$, $0.99847$, $1.00125$ and $T$ gives $0.99857$, $0.99927$, $1.00060$. **The deviation from independence is under three parts in a thousand and changes sign between windows.** The shares themselves are stable at $0.4086$ to $0.4093$, against $1 - 1/(1+\log 2) = 0.40938$.

This also settles the status of the weaker requirement recorded in [P9, §2.3]. In these letters it reads $R - S \lt  C$; but $R - S = C - T$ identically, so the requirement is $T \gt  0$ — it is not a weaker route to the conclusion, it is the conclusion. What $S$ does buy is quantitative and worth recording: discarding it via $S \ge 0$ leaves an upper bound on $R$ a tolerance of $(C-1)/R = 1.2231$, while keeping it raises the tolerance to $1.4269$ — measured as $1.2231, 1.2230, 1.2225$ and $1.4269, 1.4271, 1.4273$ across the three windows. Roughly half the available margin sits in $S$, and a lower bound on it is a lower bound on pairs $(n, n+2)$ with all four prime factors above $X^{1/3}$, which is the same dimension and the same sieve variable as $T$.

**Route 4: the two small factors.** Each of the $174{,}791$ cells of type $P_2P_2$ carries a factorisation of both members,
$$6j-1 = pq, \qquad 6j+1 = rs,$$
with $p, r$ the smaller factors. The only constraint between them is $p \ne r$, which holds in all $174{,}791$ and follows in a line: a prime dividing $6j-1$ leaves remainder $2$ in $6j+1$. Beyond it the pair behaves as two independent draws from the marginal law $\propto 1/(p\log(X/p))$ that the line count itself produces. The correlation of $\log p$ with $\log r$ is $-0.00062$ against a permutation null of mean $0.00009$ and standard deviation $0.00274$, that is $z = -0.26$; a chi-square on an $8\times8$ grid of quantiles gives $56.3$ on $49$ degrees of freedom, with largest standardised residual $2.47$ in sixty-four cells; the share with $r/p$ in $(0.952, 1.05)$ is $0.02264$ against a shuffled $0.02188$, in $(0.833, 1.2)$ it is $0.08262$ against $0.08309$, and in $(0.5, 2)$ it is $0.29293$ against $0.29270$; the median of $|r-p|$ is $73{,}880$ against $74{,}042$. The phase inside the sector is equally flat: correlations $0.00223$ and $-0.00035$ with $\log p$ and $\log r$, and the ten deciles of the sector hold $17{,}523$, $17{,}728$, $17{,}247$, $17{,}534$, $17{,}323$, $17{,}386$, $17{,}552$, $17{,}416$, $17{,}667$, $17{,}415$ cells against a flat $17{,}479$.

**Route 5: the determinant-one relation.** The same cells carry an exact Bézout relation. From $rs - pq = 2$, writing $r - p = 2a$ and $q - s = 2b$,
$$as - pb = 1, \qquad\text{equivalently}\qquad \left\lvert \frac{a}{p} - \frac{b}{s} \right\rvert = \frac{1}{ps},$$
so every $P_2P_2$ cell is a Farey pair, and $a \equiv s^{-1} \pmod p$. Verified on all $174{,}791$. A genuine finiteness statement follows: the two congruences $6j \equiv 1 \pmod p$ and $6j \equiv -1 \pmod r$ fix $j$ modulo $pr \ge 5861^2 = 34{,}351{,}321 \gt  N$, so **no pair $(p,r)$ can occur twice in the window** — and indeed the $174{,}791$ cells carry $174{,}791$ distinct pairs.

The relation is nevertheless local. Ordering the cells by $j$, the natural composition law would make consecutive cells Farey neighbours, $\lvert a_i p_{i+1} - a_{i+1} p_i \rvert = 1$. **That holds for none of the $174{,}790$ consecutive pairs**; the median of that quantity is $2.3\times10^9$ and its minimum anywhere in the window is $4604$. Nor does anything telescope: $\sum a_i/p_i = 2.6170\times10^5$ with total variation $5.1593\times10^5$, against the $1.181$ that a boundary term would leave, and the same failure by five orders of magnitude for $b/s$ and for $1/(ps)$. Reordering the cells at random gives the same zero, so the ordering by $j$ contributes nothing. As a bipartite graph on $(p, r)$ the configuration is likewise generic: $16{,}289$ four-cycles against $15{,}830 \pm 195$ from a degree-preserving shuffle, a ratio of $1.029$.

*A methodological note, because this measurement was got wrong twice before it was got right.* The shuffle must be constrained to simple graphs. A closed-form configuration estimate gave $64$, reading the data as a $255$-fold excess; an unconstrained shuffle created $115$ to $156$ multi-edges and gave $20{,}360$, reading the same data as a $20$ per cent deficit. Only when the shuffle respects the constraint $pr \gt  N$ that the geometry itself imposes — the constraint proved two paragraphs above — does the null become $15{,}830$ and the answer $1.029$. **The correct null was derivable from the object under study, and neither wrong null was distinguishable from a signal by inspection.**

**What the five have in common.** Each route asks the line geometry for a quantity that would separate $\Omega = 1$ from $\Omega = 2$, and each returns a quantity that is either identically the output, or independent of it to the precision available. The framework describes the one-sided structure exactly — the marginal law of the small factor, the capacity of every line, the position of every strike — and describes the two-sided structure by independence. Independence with the measured marginals would itself predict twins in abundance; what the twin conjecture needs is not a departure from independence but a *lower* bound on the two-sided count, and the framework supplies neither the bound nor a reason the independence it measures should persist. That is [P9, §3.2] in the vocabulary of the lines rather than of the sieve, and it is the reason the account stops where it does.


---

### B.2 The routes tried before the identity was written

*This appendix reports the routes this framework produced before [P9, §2] was written; each of them stops at the identity of [P9, §2.3]. They are kept, in the order they were tried, because a route closed by measurement seems to us worth more written down than left to be attempted again — with the caveat that a measurement closes a route only on the range measured, and what is offered with each is our reading of why it fails. The four items below are the short ones; the three that fail in an instructive way are taken up in full afterwards — the deletion budget in B.2.1, the pigeonhole constraint in B.2.2, and the inheritance laws in B.2.3.*


**(a) Capacity.** The old lines *are* able to cover a window longer than the square window: at $p=71$ a fully closed run of 67 cells exists elsewhere, against a window of 47. **The argument "the lines are too few" is therefore dead; only the phase at $p^2$ can protect a twin.**

**(b) Budget.** The per-line cap $2W/p$ is correct, but $\sum_p 2/p$ exceeds $1$ by the fourth line: for $W=100$, $40+29+18+15 = 102$. (The double-counting responsible is removed by the layering of [P3, §5.1], and [P3, §5.2] shows that the repaired sum returns the sieve product exactly — the bound stops diverging but does not improve.) The simple summation spends the entire budget on the small lines, long before reaching the large lines for which the cap is a single position. Solving the head exactly repairs this only partially: an exhaustive scan of all $5005$ offsets and all lengths for the core $\lbrace 5,7,11,13\rbrace$ gives the uniform lemma
$$\left| R_0(I) - \tfrac{27}{91} |I| \right| \le \tfrac{98}{13},$$
with both extrema attained exactly (at $|I| = 868$, offset $2069$, and at $|I| = 4137$, offset $2937$) — **a constant error, independent of $|I|$**. This moves the bottleneck from the fourth line to roughly the fifteenth, but the guaranteed minimum still falls to zero: for a **fixed** window of $100$ cells it reaches $0$ at depth $101$. With the window scaled as the sector, $W = z^2/6$, the minimum instead grows and the ratio min/mean stabilises at $0.82\text{--}0.85$ across five doublings of $z$. **The failure is therefore of the fixed window, not of the capacity argument.**

**(c) Resonance alone.** No correlation was measured between boundary resonance ($r \mid q^2-p^2$) and survival.

**(d) Parity.** The sieve counts *rough* integers and does not separate a prime from a semiprime. We measured this directly on the relevant quantity: after conditioning on the size of the rough part in bins of width $0.02$ in $\log$, with permutation performed within bins, the slope of $\mathbf{P}(\Omega_{\gt P} \text{ odd})$ against $\Omega_{\le P}$ is $-0.0013$ against a null of s.d. $0.0012$, i.e. $z = -1.11$. Over $1.5\times10^6$ samples we therefore detect **no statistically significant dependence** between the two axes under this control.

---

#### B.2.1 The closing budget, and how far it misses

##### B.2.1.1 $\Delta_q$: the Buchstab factor decomposed into internal quantities

Periodically a line should delete the fraction $2/q$ of the surviving pairs. Write the actual deletion as
$$E_q = \frac{2}{q}T_{q^-} + \Delta_q, \qquad\text{so}\qquad T_q = \Big(1-\frac2q\Big)T_{q^-} - \Delta_q,$$
and iterating from a core at $13$,
$$T_P = T_{13}\prod_{13\lt q\le P}\Big(1-\frac2q\Big)  -  \sum_{13\lt r\le P}\Delta_r \prod_{r\lt q\le P}\Big(1-\frac2q\Big).$$

**Measured at $P = 499$**, ratio of actual to periodic deletion, binned by $q/P$:

| $q/P$ | 0.0–0.1 | 0.1–0.2 | 0.2–0.3 | 0.3–0.4 | 0.4–0.5 | 0.5–0.6 | 0.6–0.7 | 0.7–0.8 | 0.8–0.9 | 0.9–1.0 |
|-----------------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
| actual/periodic | **1.0012** | 0.9699 | 0.9638 | 1.0622 | 1.1578 | 1.2152 | 1.2779 | 1.3575 | 1.4074 | **1.4706** |

Individually, $q = 5, 7, 11$ give exactly $1.0000$; $q = 101$ gives $0.9519$; $q = 499$ gives $1.5263$.

**At $P=499$, the smallest tested lines are essentially periodic while many larger lines over-delete, by as much as $47$%.** A structural interpretation is that a small line traverses the window many times and sees it as a full cycle, whereas a large line traverses it few times, and the position of its strikes relative to a window bounded by two squares is not random.

The measurements therefore suggest an internal way to read the correction factor
$$\frac{16 C_2 e^{-\gamma}}{32 C_2 e^{-2\gamma}} = \frac{e^{\gamma}}{2} = 0.8905362 = \frac{\omega(2)}{e^{-\gamma}}:$$
as an accumulated effect of the $\Delta_q$, negligible for the smallest lines and positive for many lines near $P$. This is an interpretation of the measured profile, not a derivation of the limiting constant.

*Independent numerical check.* $T(P)\log^2 P/P^2$ measures $6.01865,\ 5.97181,\ \mathbf{5.93072},\ 5.90936$ at $P=1999, 4999, 9973, 19997$, passing near $16C_2e^{-\gamma}=5.9304658$ around $P\approx10^4$. These finite values favour the local $5.93$ scale over the full-cycle $6.66$ scale on the tested range; they do not by themselves establish a limiting constant.

*Turning point.* The change of behaviour occurs at $q/P \approx 0.3$, which is exactly where the cofactor at the window's lower edge, $P^2/q$, equals $3P$ — the window's upper root.

##### B.2.1.2 A conditional asymptotic comparison: the $0.73$% margin

The available future deletions are the surviving semiprimes
$$S_P=\sum_{P\lt q\lt 3P}\big[\pi(9P^2/q)-\pi(q-1)\big],$$
each counted once by its least factor. The prime number theorem gives the formal main term
$$S_P \sim \Big(\int_1^3 \big(\tfrac{9}{t}-t\big) dt\Big)\frac{P^2}{\log^2 P}=\big(9\log3-4\big)\frac{P^2}{\log^2P},\qquad 9\log3-4=5.8875106.$$

For the cover side, the data of B.2.1.1 suggest the local scale
$$\tau \approx 5.9304658 \frac{P^2}{\log^2P}.$$
**If** that measured local scale is the true asymptotic main term (and if the lower-order $U,Q$ terms remain negligible), then the predicted ratio is
$$\boxed{ \frac{\tau}{S} \approx \frac{5.9304658}{5.8875106}=1.0072960,\qquad\text{a predicted surplus of }0.73\text{ per cent}. }$$

**Measured at finite $P$**, the ratio is larger and decreases in the direction of the conditional prediction:

| $P$ | $\tau$ | $S$ | $\tau/S$ |
|-------|---------|---------|--------|
| 101 | 2,283 | 1,867 | 1.2228 |
| 499 | 32,550 | 28,186 | 1.1548 |
| 997 | 107,439 | 95,613 | 1.1237 |
| 1,999 | 359,498 | 326,120 | 1.1024 |

**Why this is not a theorem.** The cover criterion itself is exact: if the available deletions are fewer than the minimum vertex cover, an edge survives. What is not proved is the required asymptotic lower bound for $\tau$ in this short window. The coefficient $5.9304658$ is imported into the comparison from the measured local scale of App. B.2.1.1, precisely at the difficult $s\approx2$ regime. Thus the $0.73$% number is a conditional target margin, not a proved surplus.

**As a diagnostic, this number explains the numerical difficulty.** If the predicted asymptotics are correct, any proof losing appreciably more than $0.73$% cannot close this budget. It also explains why the two measured sides track one another so closely.

**A caution, and a correction we record.** One is tempted to derive $\tau$'s constant from the full-cycle density $32C_2e^{-2\gamma} = 6.6594325$, which would give a surplus of $13.1$% instead. That is wrong: sieving to depth $P$ integers of size $P^2$ places one exactly at $u = 2$, where the Buchstab correction is not negligible, and the measurements of App. B.2.1.1 favour the $5.93$ local scale on the tested range. This error was made and corrected in the course of the work; it is recorded in Appendix A.

**The measured inheritance profile is not the dominant distortion at $P=1999$, on the range tested.** The ratios of window to global values for $V/W$, $T/V$, $U/T$ and $Q/U$ are $0.9534,\ 0.9531,\ 0.9532,\ 0.9533$. Their agreement to four decimals suggests a nearly uniform scale factor across these observables. This supports, but does not prove asymptotically, the use of a common local correction in the budget comparison.

##### B.2.1.3 Why $K \lt  G$ does not close

For each survivor $v$ let $\deg_6(v) \in \lbrace 0,1,2\rbrace$, let $\mathcal{C}$ be the set of survivors the future lines will remove, and put $K = \sum_{v\in\mathcal{C}}\deg_6(v)$. If $K \lt  G$ then some gap-$6$ pair has neither endpoint touched — i.e. a prime pair $(p,p+6)$, by the caution at the head of [P7, App. A].

Defining the concentration factor $c_p = (K/S) \div (2G/V)$:

| $p$ | 101 | 199 | 499 | 997 | 1,999 | 4,999 |
|----------------|--------|--------|--------|--------|--------|--------|
| $c_p$ | 1.0074 | 1.0143 | 1.0035 | 1.0094 | 1.0105 | 1.0057 |
| required bound | 2.54 | 2.89 | 3.05 | 3.23 | 3.44 | 3.74 |

$c_p$ is flat at $1.01$ across five doublings while the required bound widens; three independent checks (the identity $\sum\deg_6 = 2G$; a random control sample of equal size giving $c = 1.0195, 1.0043, 1.0071, 0.99966$; and a breakdown by killing line) show that the observed $1$% effect is comparable to the random controls and is not resolved as a structural signal by these tests.

**The criterion nonetheless fails, and for a reason that recurs.** It needs an **upper** bound on $K$ — available, since Selberg's upper-bound sieve has no parity obstruction — and a **lower** bound on $G$, which is not. Inside $(P^2, 9P^2)$ sieved to depth $P$, the sieve variable is
$$s = \frac{\log(8P^2)}{\log P} = 2.451,\ 2.301,\ 2.226,\ 2.151 \quad\text{at } P = 101,\ 997,\ 9973,\ 10^6,$$
i.e. always $\approx 2$ and falling toward it, whereas a lower bound in dimension $2$ requires $s \gt  \beta_2 = 4.2664$, the sifting limit of the Diamond–Halberstam–Richert sieve [1] (the $\Lambda^2\Lambda^-$ sieve gives $4.516$ and the Rosser–Iwaniec $\beta$-sieve $4.85$; see Franze [2] for the table and [3, §11.19]). Sieve methods have of course gone a long way at bounded gaps — Zhang [9], Maynard [6] and Polymath [7] — but Polymath's §2 shows that $6$ is the floor obtainable from purely sieve-theoretic considerations, by adapting Selberg's parity argument [8]; the present framework sits inside that same family. **The route inherits the barrier rather than avoiding it — and the irony is that the crude part ($K$) is available while the part one expects to know ($G$) is not.**

---

#### B.2.2 A deterministic local constraint, and its weakness

> **Proposition 1.** In any contiguous block of length $H$, each residue of a period-$q$ ruler occurs $\lfloor H/q\rfloor$ or $\lceil H/q\rceil$ times. Hence one old line's deviation from its cyclic mean is $\lt 1$ for a single mark and $\lt r$ for a run of $r$ marks.

This is a pigeonhole statement, not a statistical one, and it is the only non-probabilistic constraint the framework produces. *Zero violations over $q \in \lbrace 5,7,11,13\rbrace$, $H \le 40$, every starting position.*

**It is nevertheless useless at the scale required.** Summing over the lines above $3$ gives $2(\pi(p)-3)$: that is $46$ at $p=101$, $330$ at $p=997$, and $2{,}454$ at $p=10{,}007$, against a block of length $\approx 4$. Meanwhile the actual deviation is at or below noise level:

| block $H$ | measured s.d. | pure noise | ratio |
|------------|---------------|------------|-------|
| 4 | 0.169574 | 0.159424 | 1.064 |
| 64 | 0.033494 | 0.039856 | 0.840 |
| 1,024 | 0.005987 | 0.009964 | 0.601 |

The provable bound and the truth differ by two to three orders of magnitude. **The failure occurs at the summation over lines**, which is precisely where the union bound and the budget argument also fail.

---

#### B.2.3 Why the three laws do not close the problem

They give a supply-and-demand comparison, and the comparison goes the wrong way. Take the fixed set $\lbrace 5,7,11\rbrace$, so $Q = 385$, $S = 135$, and consider the sector at $M = 2319$: $4{,}644$ cells, of which the tail of $4{,}620$ carries exactly $1{,}620$ cells open after $5, 7, 11$ — [P7, Thm 4] confirmed.

[P7, Thm 5] says no single later line can close more than two of any family's twelve copies, so **at least six distinct lines** must cooperate to erase one family. But the lines are not scarce:

| | |
|--------------------------------------------------------------------|------|
| open cells to be closed | $1{,}620$ |
| later lines able to reach the sector | $339$ |
| total available strikes, $\sum_q 2\cdot(12Q)/q$ | $9{,}650$ |
| **oversupply** | $\mathbf{6.0\times}$ |

Running the lines in order leaves $157$ of the $1{,}620$ open, and those $157$ are exactly the twin pairs of the sector. So the local constraint is real and is simply absorbed by the number of lines.

**And no family is protected.** Distributing the $157$ survivors over the $135$ families gives $38$ families wiped out entirely, $51$ with one survivor, $37$ with two, $5$ with three, $3$ with four and $1$ with five — never more than five of twelve. Against a null in which the twelve copies of each family survive independently with probability $p = 157/1620$, the binomial prediction is $39.7,\ 51.2,\ 30.2,\ 10.8,\ 2.6,\ 0.4$. A second sector ($M = 4629$, $125$ survivors) gives observed $54,\ 47,\ 25,\ 8,\ 1$ against predicted $51.5,\ 51.7,\ 23.8,\ 6.6,\ 1.2$.

> **The constraint binds one line at a time and dissolves in aggregate.** Each line is restricted to one copy per family beyond the finite exceptional set, yet three hundred such lines erase the families at a rate indistinguishable from independent chance. This is the pattern of [P10, §2.15] again, met in the sharpest local form the framework has produced: an exact per-gap restriction, and no aggregate consequence.

---

**No progress toward the twin-prime conjecture is claimed, and no new bound.** Priority is not claimed for any result.


---

*The computations and much of the prose in this paper were prepared with AI assistance (ChatGPT, OpenAI; Claude, Anthropic), used for algebraic derivation, for drafting and rewriting code and text, for running the computations, and for auditing the papers against their own scripts. All statements were checked by the author, who is responsible for them; the repository README sets out the division of labour in full.*
---

## References

The companion papers of this set are cited as [P1] to [P12], and the numbered entries below are the external works. The two kinds never share a number: a bracket with a P is a companion paper, a bare number is a reference in the list below. This paper imports only the definitions and statements of the companion papers, never their proofs.

1. H. G. Diamond and H. Halberstam, *A higher-dimensional sieve method*, Cambridge Tracts in Mathematics **177**, Cambridge University Press, 2008.
2. C. S. Franze, *Sifting limits for the $\Lambda^2\Lambda^-$ sieve*, J. Number Theory (2011); arXiv:1012.3809.
3. J. Friedlander and H. Iwaniec, *Opera de Cribro*, AMS Colloquium Publications **57**, 2010.
4. G. Harman, *Prime-Detecting Sieves*, Princeton University Press, 2007.
5. H. Iwaniec, *Rosser's sieve*, Acta Arith. **36** (1980), 171–202.
6. J. Maynard, *Small gaps between primes*, Ann. of Math. **181** (2015), 383–413.
7. D. H. J. Polymath, *Variants of the Selberg sieve, and bounded intervals containing many primes*, Res. Math. Sci. **1** (2014), Art. 12.
8. A. Selberg, *On elementary methods in prime number theory and their limitations*, Proc. 11th Scandinavian Math. Congress, Trondheim (1949), 13–22.
9. Y. Zhang, *Bounded gaps between primes*, Ann. of Math. **179** (2014), 1121–1174.
