# The Exact Form of the Obstruction

## Paper 9. An identity for the twin count with no error term, and why an ordinary sieve cannot cross it

---

### Abstract

Cutting the sieve at depth $z$ with $z^3$ above the window makes every surviving endpoint either prime or a product of exactly two primes, and in that regime the twin count satisfies $T = C - R + S$ with **no error term**: $C$ the surviving cells, $R$ the semiprime endpoints among them, $S$ the cells with both endpoints composite. The identity turns the twin problem into a comparison of two counts, and its parity form shows what the comparison needs — a sign, not a bound. The paper then measures why an ordinary sieve cannot supply it: the classical loss is exactly a factor of two, the two constraints on the cut are incompatible, switching is aimed at the wrong region, and five routes through the line geometry are closed by measurement rather than by assertion. **No progress toward the twin-prime conjecture is claimed.**

**Numbering.** This paper is one part of a set that was written as a single document and is now published in parts. Each part numbers its own results from one and is self-contained: a reference of the form [Pn, Thm 1] means Theorem 1 of Paper n, and an unqualified "Theorem 1" always means this paper's own. Result numbers therefore differ from those of the earlier seven-document releases, where the whole set shared the numbering of the single document.

**How to read the claims in this paper.** Statements set as Theorems, Propositions and Corollaries are proved, and the proofs are given. Anything described as *measured* is a computation over a stated finite range and is labelled as such where it occurs.

**Keywords:** twin primes, parity obstruction, sieve cycles, cell coordinates, Liouville function.

**MSC 2020:** 11N35, 11N05, 11A41.

---

## Summary of the results in this part

**§2 — The obstruction, derived from inside — the core of the paper**

| Result | What it says | Section |
|---------------------|--------------------------------------------|---------|
| **Theorem 1** | **The depth cut.** With $z^3$ above the window, every surviving endpoint is prime or a product of exactly two primes above $z$. | §2.1 |
| **Theorem 2** | **Unique owner.** A surviving composite lies on the line of its smaller factor only, so it is owed exactly one strike. | §2.1 |
| **Theorem 3** | **Monotone deficit.** Advancing the cut changes $R-C$ by $-\sum(k-1)$, so it never rises and a crossing never reverses. At the final cut $R-C = -T$ — hence the crossing is *equivalent* to a twin existing, and only the non-reversal is new. | §2.1 |
| **Theorem 4** | **The exact twin count** $T = C - R + S$, with no error term. | §2.2 |
| **Theorem 5** | **The pair-overlap bound** $T \ge C - R + \tfrac23 A + \tfrac19 B$, both coefficients extremal. The one place in this work where overlap is a *resource* and the estimates run the other way; evaluated on the true factor distribution, it stays positive down to a cut exponent $0.5385$. | §2.2 |
| **Theorem 6** | **The parity identity** $2(R-C) = \sum (-1)^{\Omega(n)}$ over the surviving endpoints. The inequality $R \lt C$ *is* the statement that a Liouville sum over the sifted set is negative. | §2.3 |
| ***The covariance form*** | The same content as $T/C = (1-u)(1-v) + \kappa$ with $\kappa$ the covariance of the two composite indicators; twins vanish exactly at maximal anti-correlation, and $\kappa$ is measured at $+0.00005$ of the Frechet floor over 793 sectors. | §2.3 |

**§3 — Why an ordinary sieve cannot cross it**

| Result | What it says | Section |
|---------------|-------------------------------------------------|----------|
| **Theorem 7** | The classical Buchstab upper bound for the composite part is **exactly twice** the corresponding lower bound: $I(s) = 2f_1(s)$ on $2 \le s \le 4$. | §3.1 |
| *Closed form* | Sharing reduces to $(2n^2 \bmod p) \ge 4n^2/(p+2)$, which explains the measured rate $2/3$ and its blindness to primality. | [P10, §2.9] |
| **Corollary 1** | Hence the naive balance is $-f_1(s)$ identically: the loss is a factor of two, not a discrepancy to be tightened away. | §3.1 |
| ***Closed routes*** | The two constraints on the cut are incompatible (§3.2); switching the cut cannot repair it (§3.3); five routes through the line geometry, each closed by measurement in one explicit window (§3.4, and [P11, App. B.1]); a control showing the resources are ample, so only the forced residues obstruct (§3.5); and the trap the section exists to avoid, with its counterexample (§3.6). | §3.2–3.6 |

**§4 — The routes that reach the same wall** *(in outline; the full accounts are in [P11, App. B.2], which also states its Proposition 1)*

| Result | What it says | Section |
|---------------|--------------------------------------------------|---------|
| ***Discussion*** | Capacity, resonance and parity each fail on their own. | §4, and [P11, App. B.2] |
| ***Discussion*** | The closing budget is decomposed into internal quantities and misses by a conditional $0.73$%. | [P11, App. B.2.1] |
| ***Discussion*** | A deterministic local constraint on how many lines must cooperate, and its weakness — stated as Proposition 1 of [P11]. | [P11, App. B.2.2] |
| ***Discussion*** | Why the three inheritance laws together still do not close the problem. | [P11, App. B.2.3] |

---

## 1. Setting

We use Papers [P1] to [P8] as follows and import nothing else.

- **[P1]** supplies the window combinatorics: the increments $W_j$ of $\lfloor 2j^2/p\rfloor$, their uniform bound and their exact histogram.
- **[P2]** supplies the coordinates: the line $L_p(k) = p(p+2k)$ beginning at $p^2$, the grid $L_3$, the cells $C_b = (6b-1,6b+1)$.
- **[P3]** supplies the exact cycle laws: the four-state census and its refinement by inheritance depth.
- **[P4]** supplies the passage to a short window, and the measurement $T/M \approx 0.80$ at moving depth.
- **[P5]–[P8]** supplies everything this paper tests: the gap alphabet, the six exception positions, the closing budget, the clocks, and the sector inheritance laws.

**The three words used constantly below**, all as defined in [P2]: a **line** $L_p$ is the odd multiples of $p$ from $p^2$ onward; a **cell** is a pair $C_b = (6b-1,\ 6b+1)$, and it is **open**, or **survives** a set of lines, when neither member lies on any of them; the **window** is the interval between two consecutive odd squares, which in cell coordinates is a block of consecutive indices. A twin pair is an open cell whose two members are both prime, and inside $(u^2,v^2)$ sieved by every line up to $u$ the two notions coincide [P6, §2.1].

**The order of this paper is not the order in which it was found.** §2 states the obstruction and §3 shows that no ordinary sieve crosses it; §4 then summarises the routes that were tried first, each of which arrives at the same place, with the full accounts in [P11, App. B]. Throughout, a statement labelled *measured* is a numerical finding with its controls; it is not a theorem and not an asymptotic claim.

---

## 2. The obstruction, derived from inside

This section states the obstruction first, because everything else in this paper is an instance of it. Cutting the sieve at a depth that removes every complication except one leaves a single distinction standing, and §3 shows that no purely sieve-theoretic tool crosses it. §4 then takes the routes the framework itself suggested and shows each of them arriving at exactly this point — they are the anatomy of the wall, not a sequence of separate failures, and a reader who takes the identity of §2.3 on trust may stop at the end of §3.

### 2.1 The depth cut

Fix a window $W \subset (1,U)$ and a cut $z$ with
$$z^3  \gt   U. \qquad\text{(2.1)}$$

> **Theorem 1 (depth cut).** After every line up to $z$ has been switched on, each surviving endpoint $n \in W$ is either prime or a product of exactly two primes, both exceeding $z$.

*Proof.* Every prime factor of a survivor exceeds $z$, or a line below $z$ would have closed it. Three such factors would give $n \gt  z^3 \gt  U$, which is impossible. $\blacksquare$

> **Theorem 2 (unique owner).** If $n = qr$ with $q \lt  r$ both prime, then $n$ lies on $L_q$ and not on $L_r$. Hence every surviving composite endpoint has exactly one line responsible for it: its smaller factor.

*Proof.* $qr \ge q^2$, so $n \in L_q$. And $qr \lt  r^2$, so $L_r$ has not yet begun at $n$. $\blacksquare$

Together these remove, at one stroke, the two things a sieve at ordinary depth has to track: the multiplicative depth beyond two, and the overlap of several lines on one endpoint. **After the cut there is exactly one kind of composite left, and exactly one line responsible for each.**


**Moving the cut, and why the crossing never reverses.** Write $D(z) = R(z) - C(z)$ for the deficit at cut $z$, where $C(z)$ counts surviving cells and $R(z)$ the composite endpoints inside them, equivalently the strikes still owed by the lines above $z$. Advance the cut to the next prime $r$, and let $A_r$ be the surviving cells that $r$ closes; for $X \in A_r$ let $k(X) \ge 1$ be the number of lines in $(z, P]$ that would have struck it, $r$ included.

> **Theorem 3 (monotone deficit).** $D(r)  =  D(z)  -  \sum_{X \in A_r}\bigl(k(X)-1\bigr) \ \le\ D(z).$

*Proof.* A surviving cell outside $A_r$ is by definition not struck by $r$, so it loses none of its owed strikes; hence $R(z)-R(r) = \sum_{X \in A_r} k(X)$, while $C(z)-C(r) = |A_r|$. Subtracting gives the identity, and $k \ge 1$ gives the inequality. $\blacksquare$

*Verification.* Non-increasing at every one of the $169$ successive cuts for the sector of $P = 1009$ and every one of the $304$ for $P = 2003$, with no exception.

*What drives it down.* A cell whose only future striker is $r$ contributes $k-1 = 0$ and moves $D$ not at all; cells carrying two or more owed strikes are the whole of the decrease. So here — unlike everywhere else in this work — the piling of several lines on one cell pushes the inequality in the direction one wants, because closing such a cell discards more owed strikes than it discards cells.

**And the reading that must go with it.** Take the cut to its end, $z = P$. No lines remain above it, so $R(P) = 0$, and every surviving cell is a twin, so $C(P) = T$. Hence
$$D(P)  =  -T,$$
verified exactly: at $P = 1009$ the last cut gives $C = 54$, $R = 0$, $D = -54$ against $54$ twins; at $P = 2003$ it gives $D = -205$ against $205$. Since $D$ is non-increasing and ends at $-T$, the existence of a cut with $R \lt  C$ is **equivalent** to $T \gt  0$. The crossing is therefore not evidence for a twin: it is the same statement in another coordinate. What Theorem 3 does buy is that the crossing cannot reverse, so it suffices to establish $R \lt  C$ at a single convenient cut rather than at all of them.

### 2.2 The exact twin count

Write, for the window after the cut,

| | |
|------|--------------------------------------------------------------------|
| $C$ | surviving cells (both members surviving) |
| $R$ | composite endpoints inside those cells — a cell with both members composite is counted **twice** |
| $S$ | cells with both endpoints composite |
| $T$ | cells with both endpoints prime, i.e. twin pairs |

> **Theorem 4.** $T  =  C - R + S.$

*Proof.* Classify the surviving cells by state: $C = T + (\text{one member composite}) + S$, while $R = (\text{one member composite}) + 2S$. Subtracting eliminates the middle class. $\blacksquare$

*Verification.* Exact on every window tested. At $M = 999$ with the core taken to $P = (M+6)^{2/3} \approx 100$: $C = 234$, $R = 175$, $S = 34$, and $C-R+S = 93$, which is the true number of twin pairs in $(999^2, 1005^2)$. Over a sweep of $56$ windows with $M$ prime between $101$ and $2500$ and $h \in \lbrace M/2, M\rbrace$, the identity held without exception, with $R/C \in [0.711,\ 0.785]$ and $T/C \in [0.370,\ 0.410]$.

*Which count $R$ is, and why the two available counts agree only here.* Under the cut (2.1) the composite endpoints, the responsible lines and the strikes landing on them are in bijection, by Theorems 1 and 2, so $R$ may be read either as a count of endpoints or as a count of strikes without ambiguity. That coincidence is a consequence of the cut and not a general fact. Relax it, and a surviving endpoint may carry three or more prime factors and be struck by several lines at once: in $(51^2, 53^2)$ the cell $(2717, 2719)$ has $2719$ prime and $2717 = 11\cdot 13\cdot 19$, so it contributes one composite endpoint but three strikes, its owner being $11$ alone. (Divisibility is not enough for a line to strike: $L_p$ begins at $p^2$, so $7$ divides $35$ without striking it.) Any later argument that trades a gain from lines piling on one cell against a cost counted in owners rather than in strikes therefore manufactures a surplus that is not there, and no such argument is used below.


**A quantitative model for the three counts, and the step it does not license.** Take the cut at the boundary of (2.1), $z = Q^{2/3}$ in a sector $(P^2,Q^2)$, and put
$$h  =  \sum_{z \lt  q \le P}\frac1q  \longrightarrow  \log\tfrac32  =  0.405465\ldots,$$
the limit because $\log P/\log z \to 3/2$. If the owed strikes fell on the surviving cells independently, one would get
$$\frac{R}{C} \to 2h = 0.810930, \qquad \frac{S}{C} \to h^2 = 0.164402, \qquad \frac{T}{C} \to (1-h)^2 = 0.353472 .$$
**That is a first-order model and not the limit, and its closeness is a coincidence.** The true limit is $R/C \to 0.818768$, derived from the prime number theorem in §3.2: the composite share is $\int_{1/3}^{1/2}\mathrm{d}\alpha/(\alpha(1-\alpha))$ normalised by $1+\int$, that is $\log 2/(1+\log 2)$, whereas $h$ is $\int_{1/3}^{1/2}\mathrm{d}\alpha/\alpha = \log(3/2)$. The model drops the cofactor weight $1/(1-\alpha)$, which raises the numerator by $71$%, and omits the normalisation, which raises the denominator by $69$%; the two nearly cancel, and the model lands within one per cent of the truth for that reason and not from accuracy. Everything below uses $0.818768$.

*Measured* over the 816 sectors with $5 \le P \lt  6300$: mean $R/C = 0.797$, rising toward $0.818768$ with $P$ ($0.748, 0.786, 0.798, 0.805$ by range), and $T/C \approx 0.35$ throughout. Sample sectors: $1009\to1013$ gives $C=146$, $R=110$, $S=18$, $T=54$; $2003\to2011$ gives $512, 396, 89, 205$; $6229\to6247$ gives $2729, 2229, 454, 954$.

**The model is good and the inference from it is invalid, which is the point of recording it.** The temptation is to argue that $2h \lt  1$ forces $R \lt  C$. It does not: $2h$ is an average over a long range, while a sector is a short interval, and the two are not interchangeable. The counterexample is small and explicit. In the sector $29^2 \to 31^2$ the cut is $z = 31^{2/3} = 9.87$ and $2h = 0.7145 \lt  1$, yet
$$C = 8, \qquad R = 8, \qquad S = 2, \qquad T = 2,$$
so $R = C$ exactly, with Theorem 4 still holding as $8 - 8 + 2 = 2$. Over $5 \le P \lt  6300$ it is the only sector with $R \ge C$.

*And the margin is not generous.* Writing the requirement as $R - 2hC \lt  (1-2h)C \approx 0.189 C$, the fraction of that margin actually consumed has mean $0.064$ and median $0.069$, but reaches $1.000$ at $P=29$, $0.873$ at $P=809$, $0.782$ at $P=599$, $0.723$ at $P=1487$ and $0.564$ at $P=3539$. The worst case falls with $P$, slowly. Equivalently, since $R = 2C(1-\rho)$ with $\rho$ the proportion of surviving endpoints that are prime, the inequality $R \lt  C$ **is** $\rho \gt  1/2$: what would suffice is that more than half of the endpoints of the *surviving cells* of $(P^2,Q^2)$ are prime, for infinitely many $P$. Two cautions belong with that sentence. It is a statement about the endpoints of surviving cells, a conditioned set, not about all $z$-rough numbers of the window; and it is sufficient, not necessary — $R \lt  C$ is $T \gt  S$, which is stronger than $T \gt  0$, and the sector $29 \to 31$ below has $R = C$ with $T = 2$.

**The overlap as a resource, and a lower bound that does not need the model at all.** Everything above tries to force $R \lt  C$. There is a better use of the same data. For a surviving cell write $\ell$ and $r$ for the number of lines above the cut that strike its left and its right member. Under (2.1) — indeed under the weaker $z \ge Q^{1/2}$ — no member carries four such factors, since their product would exceed $z^4 \ge Q^2$, so $\ell, r \le 3$. Put
$$A = \sum \Bigl[\binom{\ell}{2}+\binom{r}{2}\Bigr], \qquad B = \sum \ell r,$$
the pairs of lines piling on one member and the pairs splitting across the two.

> **Theorem 5 (pair-overlap bound).** Write $R_{\mathrm{hit}} = \sum(\ell+r)$ for the number of owed **strikes** — equal to $R$ under the cut (2.1), where every composite endpoint has $\ell = 1$, but larger under the weaker cut $z \ge Q^{1/2}$ used below. For all integers $0 \le \ell, r \le 3$,
> $\displaystyle \mathbf 1_{\lbrace \ell = r = 0\rbrace} \ \ge\ 1 - \ell - r + \tfrac23\Bigl[\binom{\ell}{2}+\binom{r}{2}\Bigr] + \tfrac19 \ell r,$
> and therefore, summing over the surviving cells,
> $\displaystyle T \ \ge\ C - R_{\mathrm{hit}} + \tfrac23 A + \tfrac19 B .$

*Proof.* Sixteen cases, checked directly; equality holds at $(0,0)$, $(0,1)$, $(1,0)$, $(0,3)$, $(3,0)$ and $(3,3)$. $\blacksquare$

*The coefficients cannot be improved in this shape.* Seeking $T \ge C - R_{\mathrm{hit}} + aA + bB$, the case $(3,0)$ gives $1-3+3a \le 0$, so $a \le 2/3$; taking $a = 2/3$, the case $(3,3)$ gives $1-6+4+9b \le 0$, so $b \le 1/9$.

*What changes, and it is the only place in this work where it changes.* The bound uses the overlap as a **resource**: the more the lines pile up, the larger $A$ and $B$, and the better the bound. Consequently the estimates one needs run in the opposite direction from everywhere else — an upper bound for $R$ and lower bounds for $A$ and $B$. In the free model $R/C \sim 2h$ and $A/C \sim B/C \sim h^2$ give $T/C \gtrsim 1 - 2h + \tfrac79 h^2$, whose root is $h_c = (9-3\sqrt2)/7 = 0.679623$, i.e. a cut exponent $\alpha_c = e^{-h_c} = 0.50681$ against $0.60653$ for $R \lt  C$ alone.

*And the model overstates both terms, by different amounts.* Under the cut, a line $L_q$ strikes $n$ only once it has begun, that is when $q^2 \le n$ [Theorem 2], so $\ell$ counts the distinct prime factors $q \mid n$ with $q^2 \le n$: it is $0$ at a prime, $1$ at a product of two primes — the larger line has not started — and $3$ at a product of three, since the two smaller factors already exceed $P^{\alpha}$ with $\alpha \gt  1/2$, so the largest lies below the square root of the product. The value $\ell = 2$ therefore requires a repeated prime factor — $175 = 5^2\cdot7$ carries two distinct lines and both have begun — so it is confined to the squarefull survivors and is measured at $0.0005$; it is rare, not impossible. Writing $s_k$ for the share of rough numbers with $k$ prime factors, the bound becomes
$$T/C \ \ge\ 1 - 2\ \mathbf{E}[\ell] + \tfrac43\ \mathbf{E}\left[\tbinom{\ell}{2}\right] + \tfrac19\ \mathbf{E}[\ell]^2, \qquad \mathbf{E}[\ell] = s_2 + 3s_3, \quad \mathbf{E}\left[\tbinom{\ell}{2}\right] = 3s_3,$$
where the last term uses the independence of the two rails, measured below. The shares follow from the standard density of an integer with $k$ prime factors $X^{a_1} \le \cdots \le X^{a_k}$: with $\beta = \alpha/2$,
$$s_k \propto I_k(\beta), \qquad I_1 = 1, \quad I_2 = \int_{\beta}^{1/2}\frac{da}{a(1-a)} = \log\frac{1-\beta}{\beta}, \quad I_3 = \iint \frac{da_1\ da_2}{a_1a_2a_3}$$
over $\beta \le a_1 \le a_2 \le a_3$ with $a_3 = 1-a_1-a_2$; no $k \ge 4$ term contributes while $\alpha \gt  1/2$.

| $\alpha$ | $0.60$ | $0.58$ | $0.56$ | $0.55$ | $0.54$ | $0.53$ | $0.52$ |
|---|---|---|---|---|---|---|---|
| $s_3$ | $0.0121$ | $0.0199$ | $0.0293$ | $0.0345$ | $0.0401$ | $0.0460$ | $0.0523$ |
| $\mathbf{E}[\ell]$ | $0.4895$ | $0.5227$ | $0.5594$ | $0.5789$ | $0.5990$ | $0.6199$ | $0.6413$ |
| bound | $+0.0962$ | $+0.0645$ | $+0.0332$ | $+0.0177$ | $+0.0023$ | $-0.0129$ | $-0.0279$ |

**The bound stays positive down to $\alpha = 0.5385$**, against $0.50681$ for the free model. The two overstatements pull opposite ways. The pair term is the badly modelled one: $\mathbf{E}[\binom{\ell}{2}]$ against the model's $h^2/2$ is $0.10$ at $\alpha = 0.62$, $0.32$ at $0.58$, $0.53$ at $0.54$ and $0.87$ at $0.35$ — a large shortfall at a shallow cut, closing only as the cut deepens, because two begun lines on the *same* member is a tail event. The strike term is overstated too, but by a constant: $\mathbf{E}[\ell]$ against $h$ is $0.93$ at every cut from $0.62$ down to $0.30$. Since $A$ is added and $R$ subtracted, the first loss and the second gain partly offset, and $0.5385$ is where they balance.

*The finite-height check.* Measuring $\ell$ directly in a dyadic band gives a crossing at $0.52291$ at $X = 2\cdot10^8$, $0.52621$ at $2\cdot10^9$ and $0.52915$ at $2\cdot10^{10}$ — the last from $1.6\cdot10^8$ open cells. The deficits against $0.5385$ are $0.01557$, $0.01227$, $0.00932$, falling by a factor near $0.77$ per decade, so the approach is the expected $O(1/\log X)$ and a naive linear fit in $1/\log X$ overshoots. **The finite measurements are therefore below the asymptotic value, not above it, and a single height understates the threshold by about $0.012$ at $10^9$.** The independence used above holds throughout: the ratio of $\mathbf{E}[\ell r]$ to $\mathbf{E}[\ell]\mathbf{E}[r]$ lies between $0.9992$ and $1.0000$ at every cut and every height, and conditioning $\ell$ on the partner also being rough changes its mean in the fourth decimal.

*The quantity to press on is therefore $A$*, and it is the first in this work with a classical shape of its own: it counts semiprimes $q_1q_2$ with both factors above $z$ inside a short interval. A lower bound for $A$, together with an upper bound for $R$, would close the inequality at a fixed exponent — and neither is supplied here.

### 2.3 The parity identity

By Theorem 1 every surviving endpoint has $\Omega(n) \in \lbrace 1,2\rbrace$, so $(-1)^{\Omega(n)}$ is $-1$ on the primes and $+1$ on the semiprimes. Writing $P$ for the number of prime endpoints, one has $P + R = 2C$ and hence $P = 2C-R$, so

$$\sum_{\text{endpoints of surviving cells}} (-1)^{\Omega(n)}  =  R - P  =  2(R-C).$$

> **Theorem 6.** With the cut (2.1) in force,
> $\displaystyle \boxed{ 2 (R-C)  =  \sum_{\text{endpoints of surviving cells}} (-1)^{\Omega(n)} }$
> and consequently
> $\displaystyle R \lt  C \quad\Longleftrightarrow\quad \sum (-1)^{\Omega(n)} \lt  0 .$

**This is the point of the paper.** The inequality $R\lt C$ is what every criterion in Papers 5 to 8 eventually reduces to. Theorem 6 says it is *identical* to the statement that a Liouville sum over the sifted set is negative. The parity problem is therefore not an external obstacle that the framework happens to run into; **it is what the framework reduces to.**

**And this is the mechanism the literature names.** Tao's account of the parity problem states the sharp version of the obstruction in exactly these terms: a naive parity argument gives weak bounds, and the sharpening comes from *a more careful counting of various sums involving the Liouville function* [4, Supplement 5]. Theorem 6 is that sum, written exactly, in a coordinate system where the counting is an identity rather than an estimate. So the identity does not evade the obstruction and does not restate it loosely — it says which Liouville sum the twin problem is, over which set, with no error term. What it does not supply, and what the same source says is missing, is any control on the sign of that sum.

*A related statement, and the difference.* For a sieve removing two residue classes per prime, the same notes record that any sieve-theoretic bound is off from the truth by a factor of at least four [4, Notes 4, Exercise 49]. Theorem 7 below concerns a different quantity — the ratio between the Buchstab upper bound for the composite part and the corresponding lower-bound sieve function — and gives a factor of exactly two for it. The two statements are consistent and should not be conflated: one is a limit on what a sieve bound can achieve against the truth, the other an exact relation between two sieve functions.

**The one place a twin surplus could have hidden, measured.** The identity leaves open a possibility that would be enough on its own: that conditioning a surviving endpoint on its *partner* also surviving should tilt it towards being prime. If it did, the pair condition would carry parity information that the single-endpoint count does not, and $R \lt C$ would follow from the pairing rather than from any sieve. It does not.

Over a stretch of $4\times10^7$ integers at $10^{8}$, with the cut at $u = 3$:

| set | size | mean of $(-1)^{\Omega}$ |
|--------------------------------|-------------|-------------------|
| $z$-rough $n$ | $3{,}637{,}619$ | $-0.182713 \pm 0.000515$ |
| $z$-rough $n$ with $n+2$ also rough | $436{,}828$ | $-0.183596 \pm 0.001487$ |

The predicted value for the first row, from the prime share $1/(u\omega(u))$ at $u = 3$, is $1 - 2/(1+\log 2) = -0.181232$, which the measurement meets within three standard errors. **The difference between the two rows is $-0.000883 \pm 0.001574$, that is $0.56$ standard errors — indistinguishable from zero.**

So the partner condition changes *which* cells are counted and not the parity of their factorisations. That is the parity obstruction in its most concrete numerical form here: a condition imposed through survival to depth $z$ carries no information about $\Omega$ beyond $z$, since the two are independent once the small factors are fixed. **On this reading the pairing supplies nothing, and the sign of the Liouville sum has to come from outside the construction.**

Two remarks make the shape of this clearer.

- **$R\lt C$ is stronger than what is needed.** Since $C - R = T - S$, the inequality asks for $T \gt  S$: more twins than double-semiprime cells, not merely $T\gt 0$. The natural weaker requirement is that the number of cells with at least one composite endpoint, namely $R-S$, be less than $C$; measured, this holds comfortably even at cuts where $R\gt C$. But using it requires a *lower* bound on $S$ — the count of cells with both endpoints semiprime — which is itself parity-sensitive.
- **The identity is indifferent to the window.** Nothing in Theorems 1–4 refers to the length or the position of $W$. Lengthening the window from squares to cubes, or to $[x,2x]$, changes $C$, $R$ and $S$ and leaves the identity untouched. That is the structural reason none of the geometric variations of [P2] and [P6]–[P8] can help.


**The same content as a covariance, which is the sharpest form we can give it.** Under the cut, classify a surviving cell by the two indicators $C_L, C_R \in \lbrace 0,1\rbrace$ recording whether its left and right endpoints are composite, and set $u = \mathbb E C_L$, $v = \mathbb E C_R$, $\kappa = \mathbb E(C_LC_R) - uv$. A four-state tally of the cells — both prime, one composite either way, both composite — together with $R/C = u+v$ gives immediately
$$\boxed{\ \frac{T}{C}  =  (1-u)(1-v) + \kappa .\ }$$
The independent part and the correlation, and nothing else. The Frechet inequality $\mathbb E(C_LC_R) \ge \max(0, u+v-1)$ then places a floor under $\kappa$, namely $\kappa \ge \max(0,u+v-1) - uv$, and
$$T = 0 \quad\Longleftrightarrow\quad \kappa = -(1-u)(1-v).$$
**The two agree only when $u+v \ge 1$.** Below that the floor is $-uv$, and $T/C \ge 1-u-v \gt  0$ whatever the correlation: with the composite rates measured at $u \approx v \approx 0.409$ the floor is $-0.167$ against $-(1-u)(1-v) = -0.350$, and no correlation between the rails can empty the window. So the vanishing state is not reached by moving $\kappa$ alone — the marginals have to move too, which is what the exchange of masses below does.

*The barrier realised on this surface.* At the cut $z = Q^{2/3}$ the sifting parameter is $u_B = 3$, where Buchstab's function [1] gives the primes a share $r = 1/(1+\log 2) = 0.59062$ of the rough endpoints and the semiprimes $s = \log 2/(1+\log 2) = 0.40938$. Independence then predicts $R/C = 2s = 0.81877$ and $T/C = r^2 = 0.34883$. Exchanging the two masses — which is precisely the ambiguity Selberg's parity example exploits — and then forcing maximal anti-correlation gives the state $(0,\ s,\ s,\ 1-2s)$, whence $R/C = 2r = 1.18123$, $\kappa$ at its floor, and $T = 0$ exactly. The displacement splits as $\Delta(R/C) = 0.36246$ against $\Delta\kappa$-carrier $= 0.01364$, and $-0.36246 + 0.01364 = -0.34883 = -r^2$: the small quantity is not a shortfall to be closed but the exact overlap movement that lands the configuration on zero.

*Measured.* Over the $793$ sectors with $101 \le P \lt  6300$ at this cut, the weighted mean of $\kappa$ is $+0.000048$, i.e. $+0.00005$ of the Frechet floor, and by range it reads $-0.0041$, $+0.0021$, $+0.0002$, $-0.0001$ — collapsing by an order of magnitude per range and symmetric about zero. Individual sectors scatter between $-0.32$ and $+0.27$ of the floor. At $P = 6229$: $u = 0.3983$, $v = 0.4185$, $\kappa = -0.00032$, $(1-u)(1-v) = 0.3499$ against $T/C = 0.3496$.

*So the wall has a name and a number.* Twins are plentiful for one reason, that $\kappa$ sits at zero; and the parity obstruction is exactly that nothing here forbids the pair $(u+v, \kappa)$ from reaching the vanishing state — which needs the composite share above one half **and** the correlation at its floor, the two together. The missing statement is about the **joint law of the two rails**, not about a density alone and not about a sieve — which is why sieve tools were always going to arrive at this point and stop.

---

## 3. Why an ordinary sieve cannot cross it

### 3.1 The classical loss is exactly a factor of two

One might hope the sieve could deliver $R\lt C$ directly: bound $C$ from below and $R$ from above. It cannot, and the loss is a clean constant.

Set the problem in the standard normalisation. Let the sequence be sifted to depth $z$ with level of distribution $D = x^{\theta}$, so the sieve variable is $s = \log D/\log z$, and let $f_1, F_1$ be the linear-sieve functions, the solutions of
$$(sF)' = f(s-1), \qquad (sf)' = F(s-1), \qquad sF(s) = 2e^{\gamma} \ \ (1\le s\le 3), \qquad f(s) = \tfrac{2e^{\gamma}\log(s-1)}{s} \ \ (2\le s\le 4).$$
The lower bound for the survivor count carries $f_1(s)$; the Buchstab upper bound for the composite part is, after the substitution that removes both $\theta$ and the depth,
$$I(s)  =  \int_1^{s-1} \frac{F_1(v)}{s-v} dv .$$

> **Theorem 7.** $I(s) = 2 f_1(s)$ for $2 \le s \le 4$.
>
> *(Beyond $s = 4$ the equality fails and the excess is in our favour, but we do not prove that: computed from the delay system, $I(s)/2f_1(s) = 1.011,\ 1.044,\ 1.076,\ 1.079$ at $s = 5, 6, 8, 12$. **Measured, not proved**, and nothing below uses it.)*

*Proof for the whole range $2\le s\le4$.* The linear sieve upper function satisfies $vF_1(v) = 2e^{\gamma}$ throughout $1 \le v \le 3$, and for $s \le 4$ the integration variable runs over $v \in [1,s-1] \subseteq [1, 3]$, so $F_1(v) = 2e^{\gamma}/v$ on the whole range of integration. Partial fractions then give
$$I(s) = \frac{2e^{\gamma}}{s}\int_1^{s-1}\Big(\frac1v+\frac1{s-v}\Big)dv = \frac{4e^{\gamma}}{s}\log(s-1),$$
while $f_1(s) = 2e^{\gamma}\log(s-1)/s$ on $2 \le s \le 4$. Hence $I(s) = 2f_1(s)$ there. $\blacksquare$

*(An earlier draft proved this only on $[2, 3]$ and verified $[3, 4]$ numerically. The restriction was unnecessary: the initial range of $F_1$ already covers $v \le 3$, which is all $s \le 4$ requires.)*

*Verification.* Computed from the delay system: $I(s)/2f_1(s) = 1.00000$ at $s = 2.2, 2.5, 3.0, 3.5, 4.0$, confirming the theorem on its whole range. Checks on the functions themselves: $f_1(3) = 0.82303 = 2e^{\gamma}\log 2/3$, $F_1(2) = 1.781072 = e^{\gamma}$, $F_1(3) = 1.187382 = 2e^{\gamma}/3$.

> **Corollary 1.** On $2 \le s \le 4$ the naive balance is $f_1(s) - I(s) = -f_1(s)$, identically. The deficit is a **factor of two, uniform on that range and independent of $\theta$ and of the window** — and $[2, 4]$ is the whole of the sieve-usable region for this problem, since a lower bound in dimension two needs $s \gt  \beta_2 = 4.2664$ (§3.2).

That uniformity is the reason no choice of cut, level or geometry has ever improved matters in this framework: the parameters cancel out of the comparison before the comparison is made. It is Selberg's parity factor in its most explicit form, reached here from inside the construction.

### 3.2 The two constraints on the cut are incompatible

The heuristic version of $R\lt C$ is also instructive, because it fails by a small and identifiable amount.

Among the $z$-rough numbers below $x$, the proportion that are prime is $1/(u \omega(u))$ with $u = \log x/\log z$ and $\omega$ Buchstab's function; hence
$$\frac{R}{C}  =  2\Big(1-\frac{1}{u \omega(u)}\Big), \qquad\text{so}\qquad R\lt C \iff u \omega(u) \lt  2 .$$
Since $\omega(u) \to e^{-\gamma}$ rapidly, the numerical threshold is $u^{*} \approx 3.5658$, close to the limiting proxy $2e^{\gamma} \approx 3.56215$; the two are near but not equal, and we use $u^{*}$ where the numerics require it and $2e^{\gamma}$ only as the limiting value. Equivalently: **$R\lt C$ asks that more than half the rough numbers be prime.**

*At the natural cut the threshold is closed-form, and needs no delay system.* The cut (2.1) is $z^3 \gt  U$, i.e. $u = 3$, and there $\omega(u) = (1+\log(u-1))/u$ still holds, so
$$u \omega(u)\big|_{u=3}  =  1+\log 2, \qquad \frac{R}{C}  \longrightarrow  2\Big(1-\frac{1}{1+\log 2}\Big)  =  0.818768 .$$
The same number arrives without Buchstab at all: a $z$-rough $n \le x$ with $z = x^{1/3}$ is prime or a product of two primes $x^{\alpha}, x^{1-\alpha}$ with $\alpha \in (1/3,1/2)$, and counting the latter gives $\frac{x}{\log x}\int_{1/3}^{1/2}\frac{\mathrm{d}\alpha}{\alpha(1-\alpha)} = \frac{x}{\log x}\log 2$, so $\Phi(x,x^{1/3}) \sim (1+\log 2) x/\log x$ and the prime proportion tends to $1/(1+\log 2) = 0.590616$. **So at the cut this paper actually uses, the heuristic of this subsection is a consequence of the prime number theorem and not of any sieve estimate.**

*Measured*, at $M = h = 1009$ with the cut at $U^{\alpha}$; the predicted row is $2(1-1/u\omega(u))$:

| $\alpha$ | 0.20 | 0.25 | 0.28 | $1/3$ | 0.38 | 0.42 |
|-----------------|--------|--------|--------|--------|--------|--------|
| $u$ | 5.08 | 4.02 | 3.58 | 3.00 | 2.63 | 2.38 |
| $R/C$, measured | 1.2025 | 1.0369 | 0.9453 | 0.7559 | 0.5806 | 0.4003 |
| $R/C$, predicted | 1.2988 | 1.1139 | 1.0040 | 0.8188 | 0.6564 | 0.4872 |

*(The prediction row is now complete and recomputed at the same $u$ from the delay system; the $\alpha = 0.25$ entry was printed as $1.110$ in an earlier version and is $1.1139$.)*

*The prediction sits systematically above the measurement, and the gap is a finite-size effect that closes exactly.* Taking the global window — every cell $6n\pm1 \le X$, cut at $z = X^{1/3}$, so $u = 3$ throughout — and classifying each surviving endpoint by Theorem 1, with $\Phi$ written for $\Phi(x,x^{1/3})$ in the last row:

| $X$ | $10^6$ | $10^7$ | $10^8$ | $10^9$ | $4\times10^9$ | limit |
|------|--------|---------|-----------|-----------|------------|--------|
| $C$ | 19,303 | 142,921 | 1,096,286 | 8,775,268 | 30,857,268 | — |
| $T$ | 8,168 | 58,979 | 440,311 | 3,424,505 | 11,944,437 | — |
| $R/C$ | 0.7038 | 0.7208 | 0.7355 | 0.7527 | 0.7575 | **0.8188** |
| $T/C$ | 0.4231 | 0.4127 | 0.4016 | 0.3902 | 0.3871 | **0.3488** |
| $\Phi\log x/x$ | 1.6683 | 1.6753 | 1.6783 | 1.6893 | — | $1+\log2 = 1.6931$ |

The prime proportion among surviving endpoints is the quotient of two finite-size quantities, $\big[\pi(x)\log x/x\big]\big/\big[\Phi(x,x^{1/3})\log x/x\big]$; at $X = 10^9$ that reads $1.0537/1.6893 = 0.6237$ against the directly measured $0.6237$. **The whole distance from the prediction is the secondary term of the prime number theorem, and the numerator is what carries it.** The limiting value of $T/C$ shown above is $1/(1+\log 2)^2 = 0.3488$, i.e. the two endpoints treated as independent; the measured departure from independence, $\big(T\cdot S\big)/\big(\text{one-composite halves}\big)$, reads $1.0633,\ 1.0694,\ 1.0354,\ 1.0237,\ 1.0203$ across the same five heights — decreasing, consistent with independence, and **not established by it**, since that residual is the only place a twin excess could live.

On the other side, a positive lower bound for $C$ is a sieve lower bound in **dimension two**, and therefore requires $s \gt  \beta_2 = 4.2664$.

$$\boxed{ \text{At level of distribution } \theta = 1, \text{ where } s = u: \quad u \lt  2e^{\gamma} = 3.5621 \quad\text{and}\quad u \gt  \beta_2 = 4.2664 \quad\text{cannot both hold.} }$$

(The two variables are different — $u = \log x/\log z$ and $s = \log D/\log z$ with $D = x^{\theta}$ — and coincide only at $\theta = 1$, which is why the level enters the statement; the numerical threshold is $u^{*} \approx 3.5658$, with $2e^{\gamma}$ its limiting value.)

The window is empty, and it stays empty under the dimension-versus-level trade: taking $\kappa = 1$ with $\theta = 1/2$ (Chen's setting) requires $u \gt  \beta_1/\theta = 4$, exactly what $\kappa=2$ with $\theta=1$ requires. **The trade between dimension and level of distribution is neutral for this problem.**

*A caution about the last paragraph.* This comparison uses only leading-order densities; it ignores the sieve efficiency factors $f_{\kappa}$, which vanish as $s \to \beta_{\kappa}$, and $F_{\kappa} \gt  1$ in the upper bound. Including them makes the requirement strictly harder — the tell is that the row $\kappa=1$, $\theta=1$ (Elliott–Halberstam) gives $u\gt 2$, which lies inside the window, and Elliott–Halberstam is known not to give twin primes. The comparison above is therefore a diagnostic, not a criterion, and Theorem 7 is the criterion.

### 3.3 Why switching cannot repair it

Chen's switching principle bridges exactly the region where the upper-bound sieve is vacuous, that is where $D/(q_1q_2\cdots) \lt  z$. Its reach can be located precisely in the present normalisation.

For the target $\Omega \le 2$ the quantity to subtract is the double Buchstab integral, and the balance $f_1(s) - I_2$ is **positive** on the sieve-usable region: computed at $\theta = 1/2$, it is $+0.823$, $+0.789$, $+0.583$ and $+0.128$ at $u = 6, 7, 8, 10$, going negative just afterwards. Chen's own choice is $z = x^{1/10}$, i.e. $u = 10$, where the balance is $+0.128$ — thin and positive, which is a strong check that the normalisation is right.

For the target $\Omega \le 1$, by contrast, Corollary 1 gives $-f_1(s)$ on the sieve-usable region, **before the vacuous region is considered at all.**

> **The switching principle is not too weak for the twin problem; it is aimed at the wrong region.** For $\Omega\le2$ the usable region is already positive and switching need only show the vacuous region is small — which Chen proves. For $\Omega\le1$ the usable region is itself short by a factor of two, and switching has nothing to repair.



**The gap between $(1+2)$ and $(1+1)$ has begun to move, and the cut depth of (2.1) has a name on the new scale.** Li and Liu [2] interpolate between Chen's theorem and the binary conjectures by a parameter: Proposition $(1-a)$ asserts infinitely many primes $p$ with $p+2 = rq$, $r$ prime or $1$ and $r \le q^{a-1}$, so that $a = 2$ is Chen's theorem for twins and $a = 1$ is the twin conjecture itself. They prove $(1-1.75)$ unconditionally and $(1-1.4)$ under a weighted Elliott–Halberstam hypothesis, with the companion results $(1+1.9)$ and $(1+1.4)$ for Goldbach. Their weight is built from the same two quantities used throughout this work, $P^{-}(n)$ and $\Omega(n)$, and the case analysis behind it is the cell-state table of §2.2 in another notation.

The correspondence with the present cut is exact. Their surviving composite has its smaller factor below $x^{\tau}$ with $\tau = (a-1)/a$, so $\tau = 1/3$ — the depth at which Theorem 1 puts a survivor at $\Omega \le 2$ — is $a = 3/2$; and they record independently that the combinatorics of their weighted inequality changes character below $a = 1.5$. The depth this framework stops at is therefore the same depth their method changes shape at, reached from an unrelated direction.

*What this does not give.* It is tempting to combine their conditional $(1-1.4)$, in which every non-twin solution has a factor below $x^{2/7} \lt  x^{1/3}$ and hence a **closed** cell at the cut, with the existence of open cells, and conclude that the two sets meet only at twins. They need not meet: both statements are of the form "infinitely many", over sets that may be disjoint. An argument of that shape would prove that Elliott–Halberstam implies the twin conjecture, which it does not.

---

### 3.4 Five routes through the line geometry, closed by measurement

The identity of §2.2 says what must be shown; the line geometry offers five ways of trying to show it, and all five were followed in one explicit window and closed there. They are, in order: **prime gaps** (each $P_2$ endpoint has a unique smallest factor, so the deficit is a statement about gaps between those factors); **line capacity** (the later lines have far more raw strikes available than a single twin needs); **the two endpoints** (whether the two members of a cell behave independently); **the two small factors** (whether the pair of factors of a $P_2P_2$ cell carries usable structure); and **the partner condition** (what the requirement that both members survive is worth).

The measurements are consistent with one another and with §3.2. The deviation from independence across the window is under three parts in a thousand and changes sign; the partner condition supplies a factor of about $0.17$ and is the whole of the margin; and a bound that does not see both members of a cell at once fails by a factor of five before the sieve constant is reached.

*The five routes, with the window they were run in and the numbers that close each, are in [P11, App. B.1].*

---

### 3.5 The resources are ample: a control that isolates the residues

The five routes above all ask whether the lines have *enough* to close a window. This subsection answers that question separately, and the answer removes the whole family of arguments at once.

**The control.** Fix a window $(m^2,(m+2)^2)$ in cell coordinates and give the lines exactly the resources they actually have: one line per prime $5 \le p \le m$, two residue classes closed per line. Now let the classes be **chosen freely** rather than forced to $\pm 6^{-1} \pmod p$ — take them greedily, each line removing as many still-open cells as it can. Everything else is identical: the same lines, the same count of classes, the same window.

| $m$ | cells | lines | left open by the true classes | left open by a greedy choice |
|--------|-------|-------|--------------------------|--------------------------|
| 101 | 68 | 24 | 8 | **0** |
| 499 | 333 | 93 | 13 | **0** |
| 1009 | 673 | 167 | 27 | **0** |
| 2001 | 1335 | 301 | 50 | **0** |
| 4001 | 2668 | 549 | 70 | **0** |
| 10007 | 6672 | 1228 | 161 | **0** |
| 20011 | 13341 | 2261 | 263 | **0** |
| 50021 | 33348 | 5132 | 571 | **0** |
| 100003 | 66669 | 9591 | 995 | **0** |

**With identical resources, freely allocated, the window is covered completely every time** — up to $9{,}591$ lines against $66{,}669$ cells, where the true classes still leave $995$ survivors.

**What this settles.** Every quantity this programme has measured on the strike side is a statement about resources: the sum $\sum 2/q$, the band decomposition of a window, the capacity of a single line, the closing budget, the layer ceilings, the six positions read as a budget. The control says that none of them can be the obstruction, because the resources are sufficient by a wide margin and the covering fails anyway. **What prevents it is only that the classes are forced to be $\pm 6^{-1} \pmod p$, and nothing else.** Any proof must therefore use the arithmetic of those specific residues; no argument about size, count, capacity, step or window length can reach the conclusion, because such an argument would prove the greedy case too, and the greedy case is false.

That is the same content as Theorem 6 approached from the covering side rather than the analytic one, and it is worth having in both forms. It is also the same lesson as the global maximum-gap criterion of [3]: a criterion that protects *every* translation is far stronger than one that protects the particular translations the construction actually produces, and it is the second, weaker statement that carries the problem.

---

### 3.6 The trap this section exists to avoid

Theorem 6 is worth restating as a discipline rather than only as a result. The identity
$$2(R-C)  =  \sum (-1)^{\Omega(n)}$$
says that the inequality one wants is *equivalent* to a statement nobody knows how to prove. It would have been easy, and would have looked like progress, to write the same content in a form that hides this.

The characteristic way of hiding it is to introduce a ratio and assume it bounded. Suppose one writes the total correlation over all shifts as a sum of the individual shift correlations,
$$\sum_{n \lt  m \le x} f(n)f(m)  =  \sum_{l \ge 1} \sum_{n \le x} f(n)f(n+l),$$
an identity — both sides count the ordered pairs $n\lt m$ — and then bounds each term by a multiple of the one term of interest,
$$\sum_{n\le x} f(n)f(n+l)  \le  C \sum_{n\le x} f(n)f(n+l_0),$$
with $C$ declared to be a constant. Inverting gives a lower bound for the shift-$l_0$ correlation in terms of the total, and for $f = \vartheta$, $l_0 = 2$ the total is $\sim x^2/2$ by the prime number theorem alone, so a positive lower bound for the twin correlation appears to follow.

**It does not, and the reason seems to us instructive.** The quantity declared constant is
$$C  =  \max_{l \le x}\ \frac{\sum_n f(n)f(n+l)}{\sum_n f(n)f(n+l_0)},$$
whose denominator is the very quantity being bounded. Assuming $C$ bounded independently of $x$ is assuming that the shift-$l_0$ correlation is not asymptotically smaller than every other shift correlation — which for $l_0 = 2$ and $f = \vartheta$ is the twin prime conjecture.

**The step is not merely unproved; the inequality is false as a general statement about $f$.** Take $f$ to be the indicator of the multiples of $3$ together with the two extra points $5$ and $7$. The shift-$2$ correlation is then the three pairs $(3,5)$, $(5,7)$, $(7,9)$ and is **equal to $3$ for every $x$**, while the double sum divided by $x$ grows like $x/18$:

| $x$ | $10^2$ | $10^3$ | $10^4$ | $10^5$ |
|------------------------|------|------|-------|--------|
| shift-$2$ correlation | 3 | 3 | 3 | 3 |
| (double sum)$/x$ | 6.0 | 55.9 | 555.9 | 5555.9 |
| ratio required of $C$ | 2.0 | 18.6 | 185.3 | 1852.0 |

No fixed $C$ exists.

We record this because the shape of the fallacy is exactly the shape of the correct statement. Every criterion in [P5]–[P8] and every measurement in §4 below reduces, on inspection, to a ratio that would have to stay bounded; §§2–3 are written to name that ratio rather than to assume it. **The discipline the whole framework has tried to keep is this: when a construction reduces to an unknown quantity, the useful thing to do is to identify the quantity, not to give it a name and a positive sign.**

---

## 4. How the earlier routes reach the same wall

Three routes were produced by the framework before the identity of §2 was written: the **closing budget**, which misses by a conditional margin of under one per cent; a **deterministic local constraint** on how many lines must cooperate to erase a family; and the three **inheritance laws** read together. Each reaches the same place, and none crosses it.

They are worth having on record because each was pursued to its end and because the way each fails is the same way: a lower bound on the survivors is available, an upper bound on the composite part is not, and the two are needed together. That is the shape of §2.3 in three different notations.

*The three routes, with their measurements and the exact point at which each stops, are in [P11, App. B.2].*

---

## Appendix A — Deviation tables

$T/M$ at moving depth: see [P4, §3.2].

Contribution of lines to $\sum B_r$, with $B_r$ as defined in [P4, Thm 3]:

| $U$ | negative | sum | positive | sum |
|-------|----------|------|----------|------|
| 1,019 | 136 | $-708.3$ | 33 | $+93.1$ |
| 2,039 | 271 | $-2306.2$ | 36 | $+162.9$ |

$\mu_r$, the mean of $\varepsilon_r$ over sectors, predicted by Verified identity A of [P4, §4.1]: prediction against measurement over 1,400 sectors:

| $r$ | 5 | 7 | 11 | 17 | 23 | 101 |
|-----------|----------|------|----------|----------|------|----------|
| predicted | 0.200000 | $-0.114286$ | 0.041558 | $-0.022566$ | $-0.013013$ | 0.001415 |
| measured | 0.200286 | $-0.113959$ | 0.027162 | 0.010435 | $-0.093274$ | $-0.037823$ |
| $z$ | 0.04 | 0.01 | $-0.44$ | 0.49 | $-1.03$ | $-0.80$ |

---

---

*The computations and much of the prose in this paper were prepared with AI assistance (ChatGPT, OpenAI; Claude, Anthropic), used for algebraic derivation, for drafting and rewriting code and text, for running the computations, and for auditing the papers against their own scripts. All statements were checked by the author, who is responsible for them; the repository README sets out the division of labour in full.*
---

## References

The eleven papers of this set are cited as [P1] to [P11], and the numbered entries below are the external works. The two kinds never share a number: a bracket with a P is a companion paper, a bare number is a reference in the list below. This paper imports only the definitions and statements of the companion papers, never their proofs.

1. A. A. Buchstab, *Asymptotic estimates of a general number-theoretic function*, Mat. Sb. **44** (1937), 1239–1246.
2. J. Li and J. Liu, *Theorem $(1+1.9)$ on the Goldbach Conjecture*, arXiv:2606.05224 (2026). — *A preprint, not yet refereed; cited for the statement of Propositions $(1\pm a)$ and the results claimed for them.*
3. T. T. K. Nguyen, *Finite-window noncovering on primorial wheels: higher-order CRT bounds and shift correlations*, Preprints.org (2026), doi:10.20944/preprints202608.1299.v1. — *A preprint, not peer reviewed; cited as contemporaneous independent work reaching the same finite-window diagnosis from the Goldbach side.*
4. T. Tao, *254A: Analytic prime number theory*, graduate lecture notes, UCLA (2015); Supplement 5 (the parity problem) and Notes 4.
