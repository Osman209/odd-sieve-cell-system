# Paired Almost Primes in Square Windows and in Short Intervals

## Paper 12. Four prime factors on each member of a pair, in every square window, by a dimension-two sieve with an overlap weight

---

### Abstract

Let $\Omega(n)$ be the number of prime factors of $n$, counted with multiplicity. We prove that for every fixed $k \ge 1$ and every sufficiently large $m$,

$$\mathrm{card}\lbrace a : m^2 \lt a \lt a+2 \lt (m+k)^2,\ \Omega(a) \le 4,\ \Omega(a+2) \le 4 \rbrace \ \gg_k\ \frac{m}{(\log m)^2},$$

and that every interval $(X, X + X^{0.499}]$ with $X$ large contains $\gg X^{0.499}(\log X)^{-2}$ such pairs. The tool is the Diamond–Halberstam–Richert sieve in dimension two applied to $(6b-1)(6b+1)$. Richert's weight $\eta - B(a) - B(a+2)$ alone falls short of four factors in the square window; we add an overlap term $\kappa C(a)C(a+2)$, and an exact finite check shows that the new weight still rejects every pair with five factors on a member. With Richert's weight alone we also get $\Omega(a)+\Omega(a+2) \le 7$ in the same intervals, and $\Omega \le 3$ on each member in intervals of length $X^{0.78}$. Every sieve coefficient is certified by interval arithmetic. Nothing is claimed about primes.

**Numbering.** This paper is one part of a set that was written as a single document and is now published in parts. Each part numbers its own results from one and is self-contained: a reference of the form [Pn, Thm 1] means Theorem 1 of Paper n, and an unqualified "Theorem 1" always means this paper's own.

**This part uses no object from the cell system.** No line, sector, cell state or owner appears below. It is placed in the set because it concerns the same window.

**How to read the claims.** Theorems, Propositions and Lemmas are proved here. Anything called *measured* is a computation and is labelled where it occurs. The Diamond–Halberstam–Richert theorems and the values of their transition constants are external inputs, taken from [7] and [5] and not reproved.

**Keywords:** almost primes, square windows, short intervals, dimension-two sieve, Richert weights, overlap weight, interval arithmetic.

**MSC 2020:** 11N35, 11N36, 11N05.

---

## 1. Results

Throughout, $\Omega(n)$ counts prime factors with multiplicity and $\omega(n)$ counts distinct prime factors. All logarithms are natural.

> **Theorem 1 (four factors on each member).** (i) Fix $k \ge 1$. For every sufficiently large $m$,
> $\displaystyle \mathrm{card}\lbrace a : m^2 \lt a \lt a+2 \lt (m+k)^2,\ \Omega(a) \le 4,\ \Omega(a+2) \le 4 \rbrace \ \ge\ c_k \frac{m}{(\log m)^2}.$
> (ii) For every $\theta \ge 0.499$ and every sufficiently large $X$,
> $\displaystyle \mathrm{card}\lbrace a : X \lt a \lt a+2 \le X + X^\theta,\ \Omega(a) \le 4,\ \Omega(a+2) \le 4 \rbrace \ \ge\ c(\theta) \frac{X^\theta}{(\log X)^2}.$

> **Theorem 2 (a total of seven).** The two statements of Theorem 1 hold with the condition $\Omega(a) + \Omega(a+2) \le 7$ in place of $\Omega(a) \le 4,\ \Omega(a+2) \le 4$.

> **Theorem 3 (other lengths).** For every sufficiently large $X$ the interval $(X, X+X^\theta]$ contains $\gg_\theta X^\theta(\log X)^{-2}$ pairs $(a, a+2)$ with $\Omega(a) \le 5$ and $\Omega(a+2) \le 5$ if $\theta \ge 0.38$, and with $\Omega(a) \le 3$ and $\Omega(a+2) \le 3$ if $\theta \ge 0.78$.

> **Corollary 1.** For every sufficiently large $m$ the window $(m^2, (m + \lceil m^{0.56}\rceil)^2)$ contains a pair $(a, a+2)$ with $\Omega(a) \le 3$ and $\Omega(a+2) \le 3$.

Theorem 1 contains the statement with five factors on each member and a total of at most eight. Theorems 1 and 2 do not imply each other: Theorem 2 allows the splits $(6,1)$ and $(5,2)$, Theorem 1 allows $(4,4)$. No pair satisfying both is asserted.

**How the proof goes.** We sieve the values $Q(b) = (6b-1)(6b+1)$ by the primes below $z = U^{1/w}$, where $U$ is the top of the interval. Lemma 1 gives the local count with a remainder that is uniform in the position of the interval, so the level of distribution is the length of the interval itself, up to logarithms. Richert's weight

$$\eta - B(a) - B(a+2), \qquad B(n) = \sum_{\substack{z \le p \lt y \cr p \mid n}} \left(1 - u\frac{\log p}{\log U}\right),$$

turns a positive weighted sum into factor bounds through $B(n) \ge \Omega(n) - u$ (Lemma 2). This gives Theorems 2 and 3. For four factors at $\theta = 1/2$ it falls short (§8). Theorem 1 uses the weight

$$\eta - B(a) - B(a+2) + \kappa C(a) C(a+2),$$

where $C(n) \le B(n)$ is a capped version of $B(n)$ (§5). The extra term gives back part of the penalty when both members have middle prime factors. Lemma 3 checks, exactly, that it lets no member with five factors through, and Proposition 2 certifies that the weighted sum stays positive.

**What is known and what is added.** Results on this pair over the whole range carry fewer prime factors: by Chen [2] there are $\gg X(\log X)^{-2}$ integers $n \le X$ with $\Omega(n) + \Omega(n+2) \le 3$. For a single integer, every large square window contains one with $\Omega \le 2$ [10], and every square window without exception contains one with $\Omega \le 3$ [1] (earlier $\Omega \le 4$ [4]). These do not say that every square window contains a pair. That is what Theorems 1 to 3 add. The overlap weight of §5 has not been found by the author in the literature; no novelty or priority is claimed for it. In the author's reading Theorems 2 and 3 are what Richert's weights give at this level [3], [9]; they are recorded for completeness.

---

## 2. The sequence and its local count

The interval is $(X, X+X^\theta]$ with $0 \lt \theta \le 1$; the square window $(m^2, (m+k)^2)$ with $k$ fixed is the case $\theta = 1/2$, $X = m^2$. Let $U$ be the top of the interval. We use only pairs of the form $(6b-1, 6b+1)$, which is enough for existence. Put

$$\mathcal B = \lbrace b : 6b-1 \text{ and } 6b+1 \text{ lie in the interval} \rbrace, \qquad H = \mathrm{card}\ \mathcal B, \qquad Q(b) = (6b-1)(6b+1).$$

Then $H = X^\theta/6 + O(1)$, and $H = km/3 + O_k(1)$ in the square window.

> **Lemma 1.** For every squarefree $d$ coprime to $6$,
> $\displaystyle \mathrm{card}\lbrace b \in \mathcal B : d \mid Q(b) \rbrace = H g(d) + r_d, \qquad g(d) = \frac{2^{\omega(d)}}{d}, \qquad \lvert r_d \rvert \le 2^{\omega(d)}.$

*Proof.* Modulo a prime $p \ge 5$, $Q(b) \equiv 0$ has the two roots $6b \equiv \pm 1$. By the Chinese remainder theorem $d$ has $2^{\omega(d)}$ roots, and an interval of consecutive integers meets each residue class modulo $d$ in $H/d$ elements up to an error of $1$. $\blacksquare$

The estimate does not depend on where the interval lies. This is why every result below holds for **every** sufficiently large interval, with no averaging.

---

## 3. Sieve inputs

Fix parameters $w \gt u \gt 0$ and put

$$z = U^{1/w}, \qquad y = U^{1/u}, \qquad D = \frac{H}{(\log U)^{20}}, \qquad P(z) = \prod_{5 \le p \lt z} p, \qquad V(z) = \prod_{5 \le p \lt z}\left(1 - \frac{2}{p}\right).$$

The density $g(p) = 2/p$ has dimension two, and $V(z)$ is of order $(\log U)^{-2}$. We use the dimension-two bounds of Diamond, Halberstam and Richert in the form of [5, §4]: for a sequence of size $X_0$, density $g$ and remainders $r_d$, sifted by $P(z)$ at level $M \ge z$, the number of survivors lies between

$$X_0 V(z)\left\lbrace f_2(s) - o(1)\right\rbrace - R(M) \quad\text{and}\quad X_0 V(z)\left\lbrace F_2(s) + o(1)\right\rbrace + R(M), \qquad s = \frac{\log M}{\log z},$$

with $R(M) \ll \sum_{d \lt M,\ d \mid P(z)} 4^{\omega(d)} \lvert r_d \rvert$. Here $F_2$ and $f_2$ are the dimension-two sifting functions of [7, §4, Thm 2]: $F_2$ decreases to $1$, $f_2$ increases to $1$, and $f_2(s) = 0$ for $s \le \beta_2 = 4.2664\ldots$.

**Cut sequences.** For distinct primes $p, q$ in $[z, y)$, Lemma 1 extends to the subsequences

$$\mathrm{card}\lbrace b : p \mid Q(b),\ d \mid Q(b) \rbrace = \frac{2H}{p} g(d) + r, \qquad \mathrm{card}\lbrace b : p \mid 6b-1,\ q \mid 6b+1,\ d \mid Q(b) \rbrace = \frac{H}{pq} g(d) + r', \qquad\text{(3.1)}$$

with $\lvert r\rvert, \lvert r'\rvert \le 2^{\omega(d)}$, for squarefree $d \mid P(z)$. The density on the sifting primes is again $g$. The two members of a cell are coprime, so $p = q$ never occurs in the second count.

**The remainder.** Each modulus $pd$ or $pqd$ below $D$ has at most two prime factors $\ge z$, so it arises from at most two choices of the large primes. Summing over all cuts,

$$\sum 4^{\omega(d)} \lvert r \rvert \ \ll\ \sum_{n \lt D} 8^{\omega(n)} \ \ll\ D(\log D)^7 \ =\ o\left(H V(z)\right), \qquad\text{(3.2)}$$

using $8^{\omega(n)} \le \tau_8(n)$. Levels $D/p$ and $D/(pq)$ are used for the cut sequences; they stay above $z$ when $\theta - 1/u \gt 1/w$, and for the double cut only the range where $f_2 \gt 0$ matters, where $D/(pq)$ is a fixed positive power of $U$.

---

## 4. Richert's weight

For $z \le p \lt y$ put $t_p = \log p/\log U$, and

$$B(n) = \sum_{\substack{z \le p \lt y \cr p \mid n}} (1 - u t_p), \qquad \mathrm{wt}_\eta(b) = \eta - B(6b-1) - B(6b+1).$$

Since the two members are coprime, the weighted sum over sifted $b$ splits exactly into the uncut count and one cut count per prime. The lower bound of §3 on the first and the upper bound on the others give

$$\sum_{\substack{b \in \mathcal B \cr (Q(b), P(z)) = 1}} \mathrm{wt}_\eta(b) \ \ge\ H V(z) \left\lbrace C_\eta(\theta; w, u) + o(1) \right\rbrace, \qquad C_\eta(\theta; w, u) = \eta f_2(\theta w) - 2\int_{1/w}^{1/u}\left(\frac1t - u\right) F_2\left(w(\theta - t)\right) dt . \qquad\text{(4.1)}$$

The factor $2$ is the two roots of $Q$ modulo $p$.

Discard every cell with $p^2 \mid Q(b)$ for some $z \le p \lt y$. Their number is

$$E \ \le\ 2\sum_{z \le p \lt y}\left(\frac{H}{p^2} + 1\right) \ \ll\ \frac{H}{z} + y \ =\ o\left(H V(z)\right) \quad \text{when } 1/u \lt \theta. \qquad\text{(4.2)}$$

> **Lemma 2.** Let $n \le U$ be a member of a cell that survives the sieve at $z$ and the deletion above. Then $B(n) \ge \Omega(n) - u$.

*Proof.* Every prime factor of $n$ is at least $z$, and those below $y$ occur once. So $\Omega(n) - u\log n/\log U = \sum_{p \mid n} v_p(n)(1 - u t_p) \le B(n)$, since the terms with $p \ge y$ are not positive. Use $n \le U$. $\blacksquare$

Two consequences are used. If $\eta = r + 1 - u$ and $\mathrm{wt}_\eta(b) \gt 0$, then $B \lt \eta$ on each member (both values of $B$ are non-negative), so $\Omega \le r$ on each member. If $\eta = 8 - 2u$ and $\mathrm{wt}_\eta(b) \gt 0$, then $\Omega(6b-1) + \Omega(6b+1) - 2u \lt 8 - 2u$, so the total is at most $7$.

---

## 5. The overlap weight

Fix

$$w = 18.48, \qquad u = 2.7253, \qquad A = 0.422, \qquad L = 1.5972, \qquad \kappa = 0.3345, \qquad \eta = 5 - u = 2.2747,$$

and put

$$h_p = \min\lbrace 1 - u t_p,\ A + L t_p \rbrace, \qquad C(n) = \sum_{\substack{z \le p \lt y \cr p \mid n}} h_p, \qquad \mathrm{wt}^{\ast}(b) = \eta - B(6b-1) - B(6b+1) + \kappa C(6b-1) C(6b+1).$$

Then $0 \le h_p \le 1 - u t_p$, so $0 \le C(n) \le B(n)$.

> **Lemma 3.** $\mathrm{wt}^{\ast}(b) \le 0$ whenever $B(6b-1) \ge \eta$ or $B(6b+1) \ge \eta$, and $\mathrm{wt}^{\ast}(b) \le \eta$ for every $b$.

*Proof.* Let a member $n \le U$ have $j$ distinct prime factors in $[z, y)$. Each has $t_p \ge 1/w$ and their sum is at most $1$, so $j \le 18$, and $x = B(n) = j - u\sum t_p$ satisfies

$$\max(0, j - u) \le x \le j\left(1 - \frac{u}{w}\right), \qquad 0 \le C(n) \le H_j(x) := \min\left\lbrace x,\ jA + \frac{L(j - x)}{u} \right\rbrace. \qquad\text{(5.1)}$$

So the weight of a cell whose members have $(j, x)$ and $(l, x')$ is at most $\eta - x - x' + \kappa H_j(x) H_l(x')$. Each $H_j$ is affine on both sides of $x = j(uA+L)/(u+L)$; on each rectangle of pieces the bound is bilinear, so its maximum is at a corner. The corners are checked for all $j, l \le 18$ in exact rational arithmetic, with $x \ge \eta$ for the first claim (the other member is symmetric). The maximum over the bad region is exactly $0$; the largest admissible $\kappa$ is $58905625/176072763 = 0.33455\ldots$; the maximum over all corners is exactly $\eta$. $\blacksquare$

Without the integer $j$ in (5.1), $C(n)$ could be large while $B(n)$ is small, and no $\kappa$ of this size would pass.

**The weighted sum.** The overlap term is a sum over pairs $p \mid 6b-1$, $q \mid 6b+1$ of the second count in (3.1), bounded below by $f_2$ at level $D/(pq)$. With (4.1) and partial summation over $p$ and $q$,

$$\sum_{\substack{b \in \mathcal B \cr (Q(b), P(z)) = 1}} \mathrm{wt}^{\ast}(b) \ \ge\ H V(z) \left\lbrace C_{\ast} + o(1) \right\rbrace, \qquad C_{\ast} = C_{5-u}(\theta; w, u) + \kappa \int_{1/w}^{1/u}\int_{1/w}^{1/u} \frac{h(t)h(v)}{tv} f_2\left(w(\theta - t - v)\right) dt\ dv, \qquad\text{(5.2)}$$

with $h(t) = \min\lbrace 1 - ut, A + Lt \rbrace$. There is no factor $2$ in the double integral: one root is prescribed at each of $p$ and $q$.

---

## 6. Certified coefficients

> **Proposition 1.** For Richert's weight with $\eta = r + 1 - u$,
> $\displaystyle C_{6-u}(1/2; 16, 3) \ge 0.91558, \quad C_{6-u}(0.38; 23.43, 3.376) \ge 0.08793, \quad C_{5-u}(0.513; 16.42405, 2.79166) \ge 0.00621, \quad C_{4-u}(0.78; 10.028, 2.257) \ge 0.05351.$

> **Proposition 2.** For the overlap weight of §5, $C_{\ast} \ge 0.0064$ at $\theta = 1/2$ and $C_{\ast} \ge 0.0017$ at $\theta = 0.499$.

> **Proposition 3.** For Richert's weight with $\eta = 8 - 2u$, $w = 18.75$ and $u = 2.38$: $C_{8-2u} \ge 0.42$ at $\theta = 1/2$ and $C_{8-2u} \ge 0.41$ at $\theta = 0.499$.

*Method.* $F_2$ and $f_2$ are enclosed from the DHR delay equations with outward-rounded interval arithmetic: $\sigma_2$ from its explicit formulas and integral recursion, $F_2 = 1/\sigma_2$ below $\alpha_2$, and both functions above by a monotone march of the two delayed equations. The inputs taken from [7] are the system itself, the monotonicity of $F_2$ and $f_2$, and $\alpha_2 \in [5.3576, 5.3578]$, $\beta_2 \in [4.2662, 4.2665]$; the uncertainty in $\alpha_2$ is handled by the fact that $s^2 F_2(s)$ increases, so no further digit is used. The subtracted integral is bounded above by a Riemann sum on $20{,}000$ or $50{,}000$ pieces, taking $1/t - u$ at the left end and $F_2$ at the right end of each piece. The double integral in (5.2) is bounded below on an inner grid of step $0.00018$: $h(t)/t$ decreases and $f_2$ increases, so the upper corner of each square gives a lower bound. Proposition 1 uses a grid of step $0.0002$, Propositions 2 and 3 a grid of step $0.0001$.

The first and third values of Proposition 1 are no longer used in a theorem, because Theorem 1 contains what they give. They are kept as the record of what Richert's weight alone reaches (§8).

---

## 7. Proofs of the theorems

All four parameter sets used satisfy the conditions of §3 and §4:

- Theorem 1, $w = 18.48$, $u = 2.7253$: $1/u = 0.36693 \lt 0.499$, $\theta - 1/u \ge 0.13207 \gt 1/w = 0.05411$, $\theta w \ge 9.2215 \gt \beta_2$.
- Theorem 2, $w = 18.75$, $u = 2.38$: $1/u = 0.42017 \lt 0.499$, $\theta - 1/u \ge 0.07883 \gt 1/w = 0.05333$, $\theta w \ge 9.356 \gt \beta_2$.
- Theorem 3, $(w, u) = (23.43, 3.376)$ at $\theta = 0.38$ and $(10.028, 2.257)$ at $\theta = 0.78$: $1/u = 0.29621$ and $0.44306$, $\theta - 1/u = 0.08379$ and $0.33694$ against $1/w = 0.04268$ and $0.09972$, and $\theta w = 8.9034$ and $7.8218$.

*Proof of Theorems 1 to 3.* Take the weight of §5 for Theorem 1, Richert's weight with $\eta = 8 - 2u$ for Theorem 2, and with $\eta = r + 1 - u$ for Theorem 3. By (4.1) or (5.2) and Propositions 1 to 3, the weighted sum over sifted cells is at least $c HV(z)$ for some $c \gt 0$ and all large $X$; the remainders are $o(HV(z))$ by (3.2). Every weight is at most $\eta$ (Lemma 3 for the overlap weight; $B \ge 0$ otherwise), so deleting the cells of (4.2) costs at most $\eta E = o(HV(z))$, and the sum stays positive. A remaining cell with positive weight satisfies the factor bound: by Lemma 3 and Lemma 2 for Theorem 1, and by the two consequences of Lemma 2 for Theorems 2 and 3. The number of such cells is at least the weighted sum divided by $\eta$, which is of order $HV(z)$, that is $X^\theta(\log X)^{-2}$, or $m(\log m)^{-2}$ in the square window ($\theta = 1/2$). For larger $\theta$ the same parameters work: raising $\theta$ raises every $f_2$ value and lowers every $F_2$ value in (4.1) and (5.2). $\blacksquare$

*Proof of Corollary 1.* With $X = m^2$ and $k = \lceil m^{0.56}\rceil$, the window has length at least $2mk \ge 2X^{0.78}$, so it contains $(X, X + X^{0.78}]$; apply Theorem 3. $\blacksquare$

"Sufficiently large" is part of every statement: the $o(1)$ terms of the DHR theorems are not made explicit, so no threshold is computed.

---

## 8. Where Richert's weight stops (measured)

*Everything in this section is measured, from a floating-point solution of the DHR system; it is not part of any proof.*

With Richert's weight alone, four factors on each member at $\theta = 1/2$ need $C_{5-u}(1/2; w, u) \gt 0$. Optimising gives $w = 16.9155$, $u = 2.8215$ and

$$C_{5-u} = 2.176419 - 2.241279 = -0.064861,$$

the first term being $\eta f_2(\theta w)$ and the second the subtracted integral of (4.1). Since $f_2(8.45775) = 0.999045$, raising $f_2$ to its supremum $1$ would save only $0.002081$. The deficit sits in $F_2$: replacing $F_2$ by $1$ leaves $1.915523$, so the excess of $F_2$ above $1$ contributes $0.325757$, of which 59.1% comes from $s = w(1/2 - t) \ge 4.3$. An independent upper bound sieve would have to cut that excess by 19.91% over the whole range to close the gap with this weight. Proposition 1 shows the weight reaches four factors at $\theta = 0.513$.

The overlap weight of §5 closes the gap by changing the weight instead of the sifting functions. Three factors on each member at $\theta = 1/2$ are not reached by the weights tried here; this is a report of those trials, not a statement about every weight. Campbell [1] notes, for the single integer, the natural limitation of weighted sieves described by Greaves [6].

---

## 9. What is and is not established

- Theorems 1 to 3 hold for **every** sufficiently large interval, not on average. The uniformity comes from Lemma 1. No unproved hypothesis about primes is used.
- Nothing asserts that either member is prime. Published results on this pair over the whole range carry fewer prime factors (§1).
- Theorem 2 bounds the total, not each member.
- The parameter sets are not claimed optimal, and $0.499$ is not claimed to be the smallest length reached.
- §8 is measured, not proved. §3 supplies a level equal to the interval length up to logarithms and claims no impossibility for larger levels.
- The closest construction found to the overlap weight is a bivariate Richert weight for prime triples over the whole range [8]. The settings differ, and the two weights are not compared here.

---

## Reproducing

Three scripts in `code/` regenerate every number printed.

- `code/verify_paired_almost_primes.py` — interval certificate for Proposition 1. Standard library only.
- `code/verify_four_factor_weights.py` — exact check of Lemma 3, and interval certificates for Propositions 2 and 3. Standard library only.
- `code/verify_square_window_deficit.py` — the floating-point measurements of §8. Not an enclosure.

Each exits non-zero if a claim it supports fails. None of them reproves the DHR theorems.

---

*The computations and much of the prose in this paper were prepared with AI assistance (ChatGPT, OpenAI; Claude, Anthropic), used for algebraic derivation, for drafting and rewriting code and text, for running the computations, and for auditing the papers against their own scripts. All statements were checked by the author, who is responsible for them; the repository README sets out the division of labour in full.*

---

## References

The companion papers of this set are cited as [P1] to [P12], and the numbered entries below are the external works. This paper cites no companion paper.

1. P. J. Campbell, *On the existence of integers with at most 3 prime factors between every pair of consecutive squares*, arXiv:2603.10356 (2026).
2. J.-R. Chen, *On the representation of a large even integer as the sum of a prime and a product of at most two primes*, Sci. Sinica **16** (1973), 157–176.
3. H. G. Diamond and H. Halberstam, *A Higher-Dimensional Sieve Method*, Cambridge Tracts in Mathematics **177**, Cambridge University Press, 2008.
4. A. W. Dudek and D. R. Johnston, *Almost primes between all squares*, J. Number Theory **278** (2026), 726–745.
5. C. S. Franze and P.-H. Kao, *Almost-prime values of reducible polynomials at prime arguments*, arXiv:1812.11280 (2018).
6. G. Greaves, *Sieves in Number Theory*, Ergebnisse der Mathematik und ihrer Grenzgebiete (3) **43**, Springer, 2001.
7. P.-H. Kao, *Almost-prime polynomials with prime arguments*, arXiv:1606.03505 (2016).
8. M. Ratliff, *A bivariate Richert sieve for prime triples with two $P_5$-companions*, Zenodo (2026), doi:10.5281/zenodo.20292957.
9. H.-E. Richert, *Selberg's sieve with weights*, Mathematika **16** (1969), 1–22.
10. J. Wu, *Almost primes in short intervals*, Sci. China Math. **53** (2010), 2511–2524.
