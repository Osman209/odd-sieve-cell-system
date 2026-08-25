# Where the Framework Stops

## V. The measurements, the two test cases, and the exact form of the obstruction

---

### Abstract

Paper IV collects what the cell coordinates prove about twin pairs. This paper reports what they fail to prove, how far the failure is from success, and — the point of the whole exercise — the exact form the obstruction takes when it is derived from inside the construction rather than quoted from sieve theory.

Three criteria are examined and each is shown to fall short: capacity, resonance and parity taken separately (§2); the closing budget $\tau$ against the survivor count $S$, whose deviation is decomposed into internal quantities and compared, under a stated heuristic, at a margin of $0.73$% in the wrong direction (§3); and a deterministic local constraint that is real but not binding (§4). Across the *sequence* of sectors, the three exact inheritance laws of [IV, §6] are shown to be absorbed: the constraint they impose binds one line at a time and dissolves in aggregate, the later lines outnumbering what it requires by a factor of six and erasing the survivor classes at a rate indistinguishable from independent chance (§5).

§6 is the substance. Cutting the sieve at depth $z$ with $z^3$ above the window makes every surviving endpoint either prime or a product of exactly two primes, each with a **unique** responsible line. Writing $C$ for the surviving cells, $R$ for the composite endpoints inside them and $S$ for the cells with both endpoints composite, the twin count of the window is exactly $T = C - R + S$, and therefore
$$2(R-C)  =  \sum (-1)^{\Omega(n)}$$
over the endpoints of the surviving cells. The inequality one wants, $R \lt  C$, is precisely the statement that a **Liouville sum over the sifted set is negative**. We then show that the classical Buchstab upper bound for the composite part equals *exactly twice* the corresponding lower-bound sieve function on the whole relevant range, so any purely sieve-theoretic attempt loses a clean factor of two uniformly in every parameter; and that the two natural constraints on the cut are incompatible, $R\lt C$ requiring the sieve variable below $2e^{\gamma} = 3.5621$ while a positive lower bound in dimension two requires it above $\beta_2 = 4.2664$.

A closing subsection (§6.8) records the shape of the fallacy that the identity is written to avoid: rewriting the total correlation as a sum over shifts and declaring the ratio of one shift to another to be a constant. That step is not merely unproved — the inequality is false as a general statement, and we give the counterexample.

Two test cases, chosen because their answers are known independently — Jacobsthal's function and almost-primes between squares — are used to check that the framework reproduces the right shape and supplies no bound (§7).

**The parity problem is not an obstacle imported from sieve theory; it is what the construction reduces to on its own.** No progress toward the twin-prime conjecture is claimed, and no new bound.

**Keywords:** parity obstruction, Buchstab function, Liouville function, Jacobsthal's function, almost-primes between squares.

**MSC 2020:** 11N35, 11N05, 11N36.

---

## 1. Setting

We use Papers 0–IV as follows and import nothing else.

- **[0]** supplies the window combinatorics: the increments $W_j$ of $\lfloor 2j^2/p\rfloor$, their uniform bound and their exact histogram.
- **[I]** supplies the coordinates: the line $L_p(k) = p(p+2k)$ beginning at $p^2$, the grid $L_3$, the cells $C_b = (6b-1,6b+1)$.
- **[II]** supplies the exact cycle laws: the four-state census and its refinement by inheritance depth.
- **[III]** supplies the passage to a short window, and the measurement $T/M \approx 0.80$ at moving depth.
- **[IV]** supplies everything this paper tests: the gap alphabet, the six exception positions, the closing budget, the clocks, and the sector inheritance laws.

Throughout, a statement labelled *measured* is a numerical finding with its controls; it is not a theorem and not an asymptotic claim.

---

## 2. Why capacity, resonance and parity separately do not suffice


**(a) Capacity.** The old lines *are* able to cover a window longer than the square window: at $p=71$ a fully closed run of 67 cells exists elsewhere, against a window of 47. **The argument "the lines are too few" is therefore dead; only the phase at $p^2$ can protect a twin.**

**(b) Budget.** The per-line cap $2W/p$ is correct, but $\sum_p 2/p$ exceeds $1$ by the fourth line: for $W=100$, $40+29+18+15 = 102$. (The double-counting responsible is removed by the layering of [II, §5.1], and [II, §5.2] shows that the repaired sum returns the sieve product exactly — the bound stops diverging but does not improve.) The simple summation spends the entire budget on the small lines, long before reaching the large lines for which the cap is a single position. Solving the head exactly repairs this only partially: an exhaustive scan of all $5005$ offsets and all lengths for the core $\lbrace 5,7,11,13\rbrace$ gives the uniform lemma
$$\left| R_0(I) - \tfrac{27}{91} |I| \right| \le \tfrac{98}{13},$$
with both extrema attained exactly (at $|I| = 868$, offset $2069$, and at $|I| = 4137$, offset $2937$) — **a constant error, independent of $|I|$**. This moves the bottleneck from the fourth line to roughly the fifteenth, but the guaranteed minimum still falls to zero: for a **fixed** window of $100$ cells it reaches $0$ at depth $101$. With the window scaled as the sector, $W = z^2/6$, the minimum instead grows and the ratio min/mean stabilises at $0.82$–$0.85$ across five doublings of $z$. **The failure is therefore of the fixed window, not of the capacity argument.**

**(c) Resonance alone.** No correlation was measured between boundary resonance ($r \mid q^2-p^2$) and survival.

**(d) Parity.** The sieve counts *rough* integers and does not separate a prime from a semiprime. We measured this directly on the relevant quantity: after conditioning on the size of the rough part in bins of width $0.02$ in $\log$, with permutation performed within bins, the slope of $\mathbf{P}(\Omega_{\gt P} \text{ odd})$ against $\Omega_{\le P}$ is $-0.0013$ against a null of s.d. $0.0012$, i.e. $z = -1.11$. Over $1.5\times10^6$ samples we therefore detect **no statistically significant dependence** between the two axes under this control.

---



## 3. The closing budget, and how far it misses

### 3.1 $\Delta_q$: the Buchstab factor [5] decomposed into internal quantities

Periodically a line should delete the fraction $2/q$ of the surviving pairs. Write the actual deletion as
$$E_q = \frac{2}{q}T_{q^-} + \Delta_q, \qquad\text{so}\qquad T_q = \Big(1-\frac2q\Big)T_{q^-} - \Delta_q, \qquad\text{(4.1)}$$
and iterating from a core at $13$,
$$T_P = T_{13}\prod_{13\lt q\le P}\Big(1-\frac2q\Big)  -  \sum_{13\lt r\le P}\Delta_r \prod_{r\lt q\le P}\Big(1-\frac2q\Big). \qquad\text{(4.2)}$$

**Measured at $P = 499$**, ratio of actual to periodic deletion, binned by $q/P$:

| $q/P$ | 0.0–0.1 | 0.1–0.2 | 0.2–0.3 | 0.3–0.4 | 0.4–0.5 | 0.5–0.6 | 0.6–0.7 | 0.7–0.8 | 0.8–0.9 | 0.9–1.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| actual/periodic | **1.0012** | 0.9699 | 0.9638 | 1.0622 | 1.1578 | 1.2152 | 1.2779 | 1.3575 | 1.4074 | **1.4706** |

Individually, $q = 5, 7, 11$ give exactly $1.0000$; $q = 101$ gives $0.9519$; $q = 499$ gives $1.5263$.

**At $P=499$, the smallest tested lines are essentially periodic while many larger lines over-delete, by as much as $47$%.** A structural interpretation is that a small line traverses the window many times and sees it as a full cycle, whereas a large line traverses it few times, and the position of its strikes relative to a window bounded by two squares is not random.

The measurements therefore suggest an internal way to read the correction factor
$$\frac{16 C_2 e^{-\gamma}}{32 C_2 e^{-2\gamma}} = \frac{e^{\gamma}}{2} = 0.8905362 = \frac{\omega(2)}{e^{-\gamma}}:$$
as an accumulated effect of the $\Delta_q$, negligible for the smallest lines and positive for many lines near $P$. This is an interpretation of the measured profile, not a derivation of the limiting constant.

*Independent numerical check.* $T(P)\log^2 P/P^2$ measures $6.01865,\ 5.97181,\ \mathbf{5.93072},\ 5.90936$ at $P=1999, 4999, 9973, 19997$, passing near $16C_2e^{-\gamma}=5.9304658$ around $P\approx10^4$. These finite values favour the local $5.93$ scale over the full-cycle $6.66$ scale on the tested range; they do not by themselves establish a limiting constant.

*Turning point.* The change of behaviour occurs at $q/P \approx 0.3$, which is exactly where the cofactor at the window's lower edge, $P^2/q$, equals $3P$ — the window's upper root.

### 3.2 A conditional asymptotic comparison: the $0.73$% margin

The available future deletions are the surviving semiprimes
$$S_P=\sum_{P\lt q\lt 3P}\big[\pi(9P^2/q)-\pi(q-1)\big],$$
each counted once by its least factor. The prime number theorem gives the formal main term
$$S_P \sim \Big(\int_1^3 \big(\tfrac{9}{t}-t\big) dt\Big)\frac{P^2}{\log^2 P}=\big(9\log3-4\big)\frac{P^2}{\log^2P},\qquad 9\log3-4=5.8875106.$$

For the cover side, the data of §3.1 suggest the local scale
$$\tau \approx 5.9304658 \frac{P^2}{\log^2P}.$$
**If** that measured local scale is the true asymptotic main term (and if the lower-order $U,Q$ terms remain negligible), then the predicted ratio is
$$\boxed{ \frac{\tau}{S} \approx \frac{5.9304658}{5.8875106}=1.0072960,\qquad\text{a predicted surplus of }0.73\text{ per cent}. }$$

**Measured at finite $P$**, the ratio is larger and decreases in the direction of the conditional prediction:

| $P$ | $\tau$ | $S$ | $\tau/S$ |
|---|---|---|---|
| 101 | 2,283 | 1,867 | 1.2228 |
| 499 | 32,550 | 28,186 | 1.1548 |
| 997 | 107,439 | 95,613 | 1.1237 |
| 1,999 | 359,498 | 326,120 | 1.1024 |

**Why this is not a theorem.** The cover criterion itself is exact: if the available deletions are fewer than the minimum vertex cover, an edge survives. What is not proved is the required asymptotic lower bound for $\tau$ in this short window. The coefficient $5.9304658$ is imported into the comparison from the measured local scale of §3.1, precisely at the difficult $s\approx2$ regime. Thus the $0.73$% number is a conditional target margin, not a proved surplus.

**As a diagnostic, this number explains the numerical difficulty.** If the predicted asymptotics are correct, any proof losing appreciably more than $0.73$% cannot close this budget. It also explains why the two measured sides track one another so closely.

**A caution, and a correction we record.** One is tempted to derive $\tau$'s constant from the full-cycle density $32C_2e^{-2\gamma} = 6.6594325$, which would give a surplus of $13.1$% instead. That is wrong: sieving to depth $P$ integers of size $P^2$ places one exactly at $u = 2$, where the Buchstab correction is not negligible, and the measurements of §3.1 favour the $5.93$ local scale on the tested range. This error was made and corrected in the course of the work; it is recorded in Appendix B.

**The measured inheritance profile is not the dominant distortion at $P=1999$.** The ratios of window to global values for $V/W$, $T/V$, $U/T$ and $Q/U$ are $0.9534,\ 0.9531,\ 0.9532,\ 0.9533$. Their agreement to four decimals suggests a nearly uniform scale factor across these observables. This supports, but does not prove asymptotically, the use of a common local correction in the budget comparison.

### 3.3 Why $K \lt  G$ does not close

For each survivor $v$ let $\deg_6(v) \in \lbrace 0,1,2\rbrace$, let $\mathcal{C}$ be the set of survivors the future lines will remove, and put $K = \sum_{v\in\mathcal{C}}\deg_6(v)$. If $K \lt  G$ then some gap-$6$ pair has neither endpoint touched — i.e. a prime pair $(p,p+6)$, by the caution at the head of §4.

Defining the concentration factor $c_p = (K/S) \div (2G/V)$:

| $p$ | 101 | 199 | 499 | 997 | 1,999 | 4,999 |
|---|---|---|---|---|---|---|
| $c_p$ | 1.0074 | 1.0143 | 1.0035 | 1.0094 | 1.0105 | 1.0057 |
| required bound | 2.54 | 2.89 | 3.05 | 3.23 | 3.44 | 3.74 |

$c_p$ is flat at $1.01$ across five doublings while the required bound widens; three independent checks (the identity $\sum\deg_6 = 2G$; a random control sample of equal size giving $c = 1.0195, 1.0043, 1.0071, 0.99966$; and a breakdown by killing line) show that the observed $1$% effect is comparable to the random controls and is not resolved as a structural signal by these tests.

**The criterion nonetheless fails, and for a reason that recurs.** It needs an **upper** bound on $K$ — available, since Selberg's upper-bound sieve has no parity obstruction — and a **lower** bound on $G$, which is not. Inside $(P^2, 9P^2)$ sieved to depth $P$, the sieve variable is
$$s = \frac{\log(8P^2)}{\log P} = 2.451,\ 2.301,\ 2.226,\ 2.151 \quad\text{at } P = 101,\ 997,\ 9973,\ 10^6,$$
i.e. always $\approx 2$ and falling toward it, whereas a lower bound in dimension $2$ requires $s \gt  \beta_2 = 4.2664$, the sifting limit of the Diamond–Halberstam–Richert sieve [8] (the $\Lambda^2\Lambda^-$ sieve gives $4.516$ and the Rosser–Iwaniec $\beta$-sieve $4.85$; see Franze [11] for the table and [12, §11.19]). Sieve methods have of course gone a long way at bounded gaps — Zhang [30], Maynard [22] and Polymath [25] — but Polymath's §8 shows that $6$ is the floor obtainable from purely sieve-theoretic considerations, by adapting Selberg's parity argument [28]; the present framework sits inside that same family. **The route inherits the barrier rather than avoiding it — and the irony is that the crude part ($K$) is available while the part one expects to know ($G$) is not.**



## 4. A deterministic local constraint, and its weakness

> **Proposition 1.** In any contiguous block of length $H$, each residue of a period-$q$ ruler occurs $\lfloor H/q\rfloor$ or $\lceil H/q\rceil$ times. Hence one old line's deviation from its cyclic mean is $\lt 1$ for a single mark and $\lt r$ for a run of $r$ marks.

This is a pigeonhole statement, not a statistical one, and it is the only non-probabilistic constraint the framework produces. *Zero violations over $q \in \lbrace 5,7,11,13\rbrace$, $H \le 40$, every starting position.*

**It is nevertheless useless at the scale required.** Summing over lines gives $2\pi(p)$: that is $46$ at $p=101$, $330$ at $p=997$, and $2{,}454$ at $p=10{,}007$, against a block of length $\approx 4$. Meanwhile the actual deviation is at or below noise level:

| block $H$ | measured s.d. | pure noise | ratio |
|---|---|---|---|
| 4 | 0.169574 | 0.159424 | 1.064 |
| 64 | 0.033494 | 0.039856 | 0.840 |
| 1,024 | 0.005987 | 0.009964 | 0.601 |

The provable bound and the truth differ by two to three orders of magnitude. **The failure occurs at the summation over lines**, which is precisely where the union bound and the budget argument also fail.

---



## 5. Why the three laws do not close the problem

They give a supply-and-demand comparison, and the comparison goes the wrong way. Take the fixed set $\lbrace 5,7,11\rbrace$, so $Q = 385$, $S = 135$, and consider the sector at $M = 2319$: $4{,}644$ cells, of which the tail of $4{,}620$ carries exactly $1{,}620$ cells open after $5, 7, 11$ — [IV, Thm 13] confirmed.

[IV, Thm 14] says no single later line can close more than two of any family's twelve copies, so **at least six distinct lines** must cooperate to erase one family. But the lines are not scarce:

| | |
|---|---|
| open cells to be closed | $1{,}620$ |
| later lines able to reach the sector | $339$ |
| total available strikes, $\sum_q 2\cdot(12Q)/q$ | $9{,}650$ |
| **oversupply** | $\mathbf{6.0\times}$ |

Running the lines in order leaves $157$ of the $1{,}620$ open, and those $157$ are exactly the twin pairs of the sector. So the local constraint is real and is simply absorbed by the number of lines.

**And no family is protected.** Distributing the $157$ survivors over the $135$ families gives $38$ families wiped out entirely, $51$ with one survivor, $37$ with two, $5$ with three, $3$ with four and $1$ with five — never more than five of twelve. Against a null in which the twelve copies of each family survive independently with probability $p = 157/1620$, the binomial prediction is $39.7,\ 51.2,\ 30.2,\ 10.8,\ 2.6,\ 0.4$. A second sector ($M = 4629$, $125$ survivors) gives observed $54,\ 47,\ 25,\ 8,\ 1$ against predicted $51.5,\ 51.7,\ 23.8,\ 6.6,\ 1.2$.

> **The constraint binds one line at a time and dissolves in aggregate.** Each line is restricted to one copy per family beyond the finite exceptional set, yet three hundred such lines erase the families at a rate indistinguishable from independent chance. This is the pattern of §7.5 again, met in the sharpest local form the framework has produced: an exact per-gap restriction, and no aggregate consequence.

---


---

## 6. The obstruction, derived from inside

Sections 2–5 each end the same way: an exact local statement that is absorbed in aggregate. This section explains why, by cutting the sieve at a depth that removes every complication except one, and then showing what that one is.

### 6.1 The depth cut

Fix a window $W \subset (1,U)$ and a cut $z$ with
$$z^3  \gt   U. \qquad\text{(6.1)}$$

> **Theorem 1 (depth cut).** After every line up to $z$ has been switched on, each surviving endpoint $n \in W$ is either prime or a product of exactly two primes, both exceeding $z$.

*Proof.* Every prime factor of a survivor exceeds $z$, or a line below $z$ would have closed it. Three such factors would give $n \gt  z^3 \gt  U$, which is impossible. $\blacksquare$

> **Theorem 2 (unique owner).** If $n = qr$ with $q \lt  r$ both prime, then $n$ lies on $L_q$ and not on $L_r$. Hence every surviving composite endpoint has exactly one line responsible for it: its smaller factor.

*Proof.* $qr \ge q^2$, so $n \in L_q$. And $qr \lt  r^2$, so $L_r$ has not yet begun at $n$. $\blacksquare$

Together these remove, at one stroke, everything the earlier sections had to track: the multiplicative depth beyond two, and the overlap of several lines on one endpoint. **After the cut there is exactly one kind of composite left, and exactly one line responsible for each.**

### 6.2 The exact twin count

Write, for the window after the cut,

| | |
|---|---|
| $C$ | surviving cells (both members surviving) |
| $R$ | composite endpoints inside those cells — a cell with both members composite is counted **twice** |
| $S$ | cells with both endpoints composite |
| $T$ | cells with both endpoints prime, i.e. twin pairs |

> **Theorem 3.** $T  =  C - R + S.$

*Proof.* Classify the surviving cells by state: $C = T + (\text{one member composite}) + S$, while $R = (\text{one member composite}) + 2S$. Subtracting eliminates the middle class. $\blacksquare$

*Verification.* Exact on every window tested. At $M = 999$ with the core taken to $P = (M+6)^{2/3} \approx 100$: $C = 234$, $R = 175$, $S = 34$, and $C-R+S = 93$, which is the true number of twin pairs in $(999^2, 1005^2)$. Over a sweep of $56$ windows with $M$ prime between $101$ and $2500$ and $h \in \lbrace M/2, M\rbrace$, the identity held without exception, with $R/C \in [0.711,\ 0.785]$ and $T/C \in [0.370,\ 0.410]$.

### 6.3 The parity identity

By Theorem 1 every surviving endpoint has $\Omega(n) \in \lbrace 1,2\rbrace$, so $(-1)^{\Omega(n)}$ is $-1$ on the primes and $+1$ on the semiprimes. Writing $P$ for the number of prime endpoints, one has $P + R = 2C$ and hence $P = 2C-R$, so

$$\sum_{\text{endpoints of surviving cells}} (-1)^{\Omega(n)}  =  R - P  =  2(R-C).$$

> **Theorem 4.** With the cut (6.1) in force,
> $$\boxed{ 2 (R-C)  =  \sum_{\text{endpoints of surviving cells}} (-1)^{\Omega(n)} }$$
> and consequently
> $$R \lt  C \quad\Longleftrightarrow\quad \sum (-1)^{\Omega(n)} \lt  0 .$$

**This is the point of the paper.** The inequality $R\lt C$ is what every criterion in Paper IV eventually reduces to. Theorem 4 says it is *identical* to the statement that a Liouville sum over the sifted set is negative. The parity problem is therefore not an external obstacle that the framework happens to run into; **it is what the framework reduces to.**

Two remarks make the shape of this clearer.

- **$R\lt C$ is stronger than what is needed.** Since $C - R = T - S$, the inequality asks for $T \gt  S$: more twins than double-semiprime cells, not merely $T\gt 0$. The natural weaker requirement is that the number of cells with at least one composite endpoint, namely $R-S$, be less than $C$; measured, this holds comfortably even at cuts where $R\gt C$. But using it requires a *lower* bound on $S$ — the count of cells with both endpoints semiprime — which is itself parity-sensitive.
- **The identity is indifferent to the window.** Nothing in Theorems 1–4 refers to the length or the position of $W$. Lengthening the window from squares to cubes, or to $[x,2x]$, changes $C$, $R$ and $S$ and leaves the identity untouched. That is the structural reason none of the geometric variations in Papers I and IV can help.

### 6.4 The classical loss is exactly a factor of two

One might hope the sieve could deliver $R\lt C$ directly: bound $C$ from below and $R$ from above. It cannot, and the loss is a clean constant.

Set the problem in the standard normalisation. Let the sequence be sifted to depth $z$ with level of distribution $D = x^{\theta}$, so the sieve variable is $s = \log D/\log z$, and let $f_1, F_1$ be the linear-sieve functions, the solutions of
$$(sF)' = f(s-1), \qquad (sf)' = F(s-1), \qquad sF(s) = 2e^{\gamma} \ \ (1\le s\le 3), \qquad f(s) = \tfrac{2e^{\gamma}\log(s-1)}{s} \ \ (2\le s\le 4).$$
The lower bound for the survivor count carries $f_1(s)$; the Buchstab upper bound for the composite part is, after the substitution that removes both $\theta$ and the depth,
$$I(s)  =  \int_1^{s-1} \frac{F_1(v)}{s-v} dv .$$

> **Theorem 5.** $I(s) = 2 f_1(s)$ for $2 \le s \le 4$.
>
> *(Beyond $s = 4$ the equality fails and the excess is in our favour, but we do not prove that: computed from the delay system, $I(s)/2f_1(s) = 1.011,\ 1.044,\ 1.076,\ 1.079$ at $s = 5, 6, 8, 12$. **Measured, not proved**, and nothing below uses it.)*

*Proof for the whole range $2\le s\le4$.* The linear sieve upper function satisfies $vF_1(v) = 2e^{\gamma}$ throughout $1 \le v \le 3$, and for $s \le 4$ the integration variable runs over $v \in [1,s-1] \subseteq [1,3]$, so $F_1(v) = 2e^{\gamma}/v$ on the whole range of integration. Partial fractions then give
$$I(s) = \frac{2e^{\gamma}}{s}\int_1^{s-1}\Big(\frac1v+\frac1{s-v}\Big)dv = \frac{4e^{\gamma}}{s}\log(s-1),$$
while $f_1(s) = 2e^{\gamma}\log(s-1)/s$ on $2 \le s \le 4$. Hence $I(s) = 2f_1(s)$ there. $\blacksquare$

*(An earlier draft proved this only on $[2,3]$ and verified $[3,4]$ numerically. The restriction was unnecessary: the initial range of $F_1$ already covers $v \le 3$, which is all $s \le 4$ requires.)*

*Verification.* Computed from the delay system: $I(s)/2f_1(s) = 1.00000$ at $s = 2.2, 2.5, 3.0, 3.5, 4.0$, confirming the theorem on its whole range. Checks on the functions themselves: $f_1(3) = 0.82303 = 2e^{\gamma}\log 2/3$, $F_1(2) = 1.781072 = e^{\gamma}$, $F_1(3) = 1.187382 = 2e^{\gamma}/3$.

> **Corollary 1.** On $2 \le s \le 4$ the naive balance is $f_1(s) - I(s) = -f_1(s)$, identically. The deficit is a **factor of two, uniform on that range and independent of $\theta$ and of the window** — and $[2,4]$ is the whole of the sieve-usable region for this problem, since a lower bound in dimension two needs $s \gt  \beta_2 = 4.2664$ (§6.5).

That uniformity is the reason no choice of cut, level or geometry has ever improved matters in this framework: the parameters cancel out of the comparison before the comparison is made. It is Selberg's parity factor in its most explicit form, reached here from inside the construction.

### 6.5 The two constraints on the cut are incompatible

The heuristic version of $R\lt C$ is also instructive, because it fails by a small and identifiable amount.

Among the $z$-rough numbers below $x$, the proportion that are prime is $1/(u \omega(u))$ with $u = \log x/\log z$ and $\omega$ Buchstab's function; hence
$$\frac RC  =  2\Big(1-\frac{1}{u \omega(u)}\Big), \qquad\text{so}\qquad R\lt C \iff u \omega(u) \lt  2 .$$
Since $\omega(u) \to e^{-\gamma}$ rapidly, the numerical threshold is $u^{*} \approx 3.5658$, close to the limiting proxy $2e^{\gamma} \approx 3.56215$; the two are near but not equal, and we use $u^{*}$ where the numerics require it and $2e^{\gamma}$ only as the limiting value. Equivalently: **$R\lt C$ asks that more than half the rough numbers be prime.**

*At the natural cut the threshold is closed-form, and needs no delay system.* The cut (6.1) is $z^3 \gt  U$, i.e. $u = 3$, and there $\omega(u) = (1+\log(u-1))/u$ still holds, so
$$u \omega(u)\big|_{u=3}  =  1+\log 2, \qquad \frac RC  \longrightarrow  2\Big(1-\frac{1}{1+\log 2}\Big)  =  0.818768 .$$
The same number arrives without Buchstab at all: a $z$-rough $n \le x$ with $z = x^{1/3}$ is prime or a product of two primes $x^{\alpha}, x^{1-\alpha}$ with $\alpha \in (1/3,1/2)$, and counting the latter gives $\frac{x}{\log x}\int_{1/3}^{1/2}\frac{\mathrm{d}\alpha}{\alpha(1-\alpha)} = \frac{x}{\log x}\log 2$, so $\Phi(x,x^{1/3}) \sim (1+\log 2) x/\log x$ and the prime proportion tends to $1/(1+\log 2) = 0.590616$. **So at the cut this paper actually uses, the heuristic of this subsection is a consequence of the prime number theorem and not of any sieve estimate.**

*Measured*, at $M = h = 1009$ with the cut at $U^{\alpha}$:

| $\alpha$ | 0.20 | 0.25 | 0.28 | $1/3$ | 0.38 | 0.42 |
|---|---|---|---|---|---|---|
| $u$ | 5.08 | 4.02 | 3.58 | 3.00 | 2.63 | 2.38 |
| $R/C$ measured | 1.2025 | 1.0369 | 0.9453 | 0.7559 | 0.5806 | 0.4003 |
| $2(1-1/u\omega(u))$ | 1.2988 | 1.1139 | 1.0040 | 0.8188 | 0.6564 | 0.4872 |

*(The prediction row is now complete and recomputed at the same $u$ from the delay system; the $\alpha = 0.25$ entry was printed as $1.110$ in an earlier version and is $1.1139$.)*

*The prediction sits systematically above the measurement, and the gap is a finite-size effect that closes exactly.* Taking the global window — every cell $6n\pm1 \le X$, cut at $z = X^{1/3}$, so $u = 3$ throughout — and classifying each surviving endpoint by Theorem 1:

| $X$ | $10^6$ | $10^7$ | $10^8$ | $10^9$ | $4\times10^9$ | limit |
|---|---|---|---|---|---|---|
| $C$ | 19,303 | 142,921 | 1,096,286 | 8,775,268 | 30,857,268 | — |
| $T$ | 8,168 | 58,979 | 440,311 | 3,424,505 | 11,944,437 | — |
| $R/C$ | 0.7038 | 0.7208 | 0.7355 | 0.7527 | 0.7575 | **0.8188** |
| $T/C$ | 0.4231 | 0.4127 | 0.4016 | 0.3902 | 0.3871 | **0.3488** |
| $\Phi(x,x^{1/3})\log x/x$ | 1.6683 | 1.6753 | 1.6783 | 1.6893 | — | $1+\log2 = 1.6931$ |

The prime proportion among surviving endpoints is the quotient of two finite-size quantities, $\big[\pi(x)\log x/x\big]\big/\big[\Phi(x,x^{1/3})\log x/x\big]$; at $X = 10^9$ that reads $1.0537/1.6893 = 0.6237$ against the directly measured $0.6237$. **The whole distance from the prediction is the secondary term of the prime number theorem, and the numerator is what carries it.** The limiting value of $T/C$ shown above is $1/(1+\log 2)^2 = 0.3488$, i.e. the two endpoints treated as independent; the measured departure from independence, $\big(T\cdot S\big)/\big(\text{one-composite halves}\big)$, reads $1.0633,\ 1.0694,\ 1.0354,\ 1.0237,\ 1.0203$ across the same five heights — decreasing, consistent with independence, and **not established by it**, since that residual is the only place a twin excess could live.

On the other side, a positive lower bound for $C$ is a sieve lower bound in **dimension two**, and therefore requires $s \gt  \beta_2 = 4.2664$.

$$\boxed{ u \lt  2e^{\gamma} = 3.5621 \quad\text{and}\quad s \gt  \beta_2 = 4.2664 \quad\text{cannot both hold.} }$$

The window is empty, and it stays empty under the dimension-versus-level trade: taking $\kappa = 1$ with $\theta = 1/2$ (Chen's setting) requires $u \gt  \beta_1/\theta = 4$, exactly what $\kappa=2$ with $\theta=1$ requires. **The trade between dimension and level of distribution is neutral for this problem.**

*A caution about the last paragraph.* This comparison uses only leading-order densities; it ignores the sieve efficiency factors $f_{\kappa}$, which vanish as $s \to \beta_{\kappa}$, and $F_{\kappa} \gt  1$ in the upper bound. Including them makes the requirement strictly harder — the tell is that the row $\kappa=1$, $\theta=1$ (Elliott–Halberstam) gives $u\gt 2$, which lies inside the window, and Elliott–Halberstam is known not to give twin primes. The comparison above is therefore a diagnostic, not a criterion, and Theorem 5 is the criterion.

### 6.6 Why switching cannot repair it

Chen's switching principle bridges exactly the region where the upper-bound sieve is vacuous, that is where $D/(q_1q_2\cdots) \lt  z$. Its reach can be located precisely in the present normalisation.

For the target $\Omega \le 2$ the quantity to subtract is the double Buchstab integral, and the balance $f_1(s) - I_2$ is **positive** on the sieve-usable region: computed at $\theta = 1/2$, it is $+0.823$, $+0.789$, $+0.583$ and $+0.128$ at $u = 6, 7, 8, 10$, going negative just afterwards. Chen's own choice is $z = x^{1/10}$, i.e. $u = 10$, where the balance is $+0.128$ — thin and positive, which is a strong check that the normalisation is right.

For the target $\Omega \le 1$, by contrast, Corollary 1 gives $-f_1(s)$ on the sieve-usable region, **before the vacuous region is considered at all.**

> **The switching principle is not too weak for the twin problem; it is aimed at the wrong region.** For $\Omega\le2$ the usable region is already positive and switching need only show the vacuous region is small — which Chen proves. For $\Omega\le1$ the usable region is itself short by a factor of two, and switching has nothing to repair.


---

### 6.7 Five routes through the line geometry, closed by measurement

Sections 6.1–6.6 argue that the obstruction is the distinction between $\Omega=1$ and $\Omega=2$ inside the sifted set. That argument is analytic. This section reports what happens when one instead asks the line geometry itself for the missing information, in a single explicit window, and follows each of the five natural routes to the point where it stops. Every number below is **measured**, not proved.

**The window.** We take the phase of the surviving configuration of [IV, §3.8],
$$M_0 = 448{,}353, \qquad X = (M_0+210)^2 = 201{,}208{,}764{,}969,$$
which carries $N = 31{,}392{,}060$ cells. The cut is the largest prime with $z^3 \lt  X$, namely $z = 5857$, since $5857^3 = 200{,}921{,}157{,}793$ and $5861^3 = 201{,}333{,}092{,}381$. After sieving to $z$, Theorem 1 applies and each surviving endpoint is $P$ or $P_2$. Writing the four states of a surviving cell by the status of its two endpoints:
$$R = 1{,}049{,}024, \quad H = 857{,}695, \quad C_{\square} = 174{,}791, \quad T = 366{,}120,$$
where $R$ is the surviving cells, $H$ the $P_2$ endpoints among them (a cell with both endpoints composite contributing two), $C_{\square}$ the cells with both endpoints $P_2$, and $T$ the twins. These are the $C$, $R$, $S$, $T$ of Theorem 3 in the letters this section uses, and $T = R - H + C_{\square}$ holds exactly.

Two side measurements fix the scale. The prime share among the $2R$ endpoints is $1{,}240{,}353/2{,}098{,}048 = 0.591196$ against the limit $1/(1+\log 2) = 0.590616$ of §6.5 — agreement to four decimals, because a short window at height $Y$ carries no secondary term in the prime count, which is the reading §6.5 gives of its own global table. And the survivors of **all** lines up to $M_0$ number $366{,}130$, that is $T$ plus ten composite cells whose two factors both exceed $M_0$; the same measurement at $M_0 + 510{,}510$ and $M_0 + 1{,}021{,}020$ gives $699{,}747 = 699{,}726 + 21$ and $1{,}010{,}762 = 1{,}010{,}734 + 28$. **The survivor count of a square window is the twin count plus a two-digit remainder.**

**Route 1: prime gaps.** Each $P_2$ endpoint has a unique smallest factor $q \in (z, \sqrt{X}]$. Classify $q$ by its gap to the next prime and compare the observed count in each class against the count predicted by the cofactor interval $L/q$ and the prime density at $X/q$. Over twenty-nine gap classes from $2$ to $60$ the ratio is flat at $0.171$ to $0.176$, and the largest standardised residual anywhere is $1.59$ — smaller than one expects by chance from twenty-nine classes. A control is required here and it passes: the mean gap rises from $10.16$ to $12.92$ across octiles of $q$, so gap classes are confounded with $q$, and the same ratio binned by $q$ instead is flat to four decimals ($1.0004$, $0.9995$, $1.0021$, $0.9969$, $0.9926$, $1.0052$, $1.0059$, $0.9943$). The gap after $q$ is a function of the small factor alone, and the count of endpoints it owns is a prime count in the interval $(\mathrm{lo}/q, \mathrm{hi}/q)$; nothing links the two.

**Route 2: line capacity.** The $36{,}824$ lines in $(z, \sqrt{X}]$ have $25{,}353{,}670$ raw strikes available inside the window, against the ceiling $R - 1 = 1{,}049{,}023$ that a single twin needs — larger by a factor of $24.2$, the usual outcome. Restricting the count to strikes that land on an endpoint of one of the $R$ rough cells gives $857{,}712$, against $H = 857{,}695$: a difference of **seventeen**, the endpoints whose two prime factors both lie below $\sqrt{X}$ and which are therefore counted twice. So the restricted capacity is not an upper bound on the output; it **equals** the output. That is Theorem 2 read as a statement about capacity — a surviving composite has exactly one responsible line, so there is no slack between what the lines can do and what they do.

Two further quantities locate why no upper bound is available here. First, the cofactor interval $L/q$ equals the sieving depth $z$ at $q = L/z = 32{,}159$; above that point the interval to be sifted is shorter than the sieve limit and no sieve estimate applies at all. Of the $36{,}824$ lines, $34{,}145$ lie above it, and they own $509{,}602$ of the $P_2$ endpoints — $59.4$ per cent of $H$. This is the vacuous region of §6.6, and the measurement supplies the number that section states qualitatively: for $\Omega \le 2$ Chen's switching principle need only show the vacuous region is small, and here it is not small, it is the majority. Second, dropping the partner condition — counting rough $P_2$ endpoints without requiring the other member of the cell to be rough — raises the count from $857{,}695$ to $4{,}997{,}471$, which is $4.76$ times the ceiling. The partner condition supplies a factor $0.1716$ and it is the whole of the margin; any bound that does not see both members of the cell at once fails by a factor of five before the sieve constant is reached. A Brun–Titchmarsh bound on the cofactor, which does not see it, gives $24{,}119{,}320$.

**Route 3: the two endpoints.** Under independence one would predict $C_{\square} = R \cdot h_L h_R$ with $h_L, h_R$ the two $P_2$ shares. Measured against that prediction, over the same three windows, $C_{\square}$ gives $0.99701$, $0.99847$, $1.00125$ and $T$ gives $0.99857$, $0.99927$, $1.00060$. **The deviation from independence is under three parts in a thousand and changes sign between windows.** The shares themselves are stable at $0.4086$ to $0.4093$, against $1 - 1/(1+\log 2) = 0.40938$.

This also settles the status of the weaker requirement recorded in §6.3. In the letters above it reads $H - C_{\square} \lt  R$; but $H - C_{\square} = R - T$ identically, so the requirement is $T \gt  0$ — it is not a weaker route to the conclusion, it is the conclusion. What $C_{\square}$ does buy is quantitative and worth recording: discarding it via $C_{\square} \ge 0$ leaves an upper bound on $H$ a tolerance of $(R-1)/H = 1.2231$, while keeping it raises the tolerance to $1.4269$ — measured as $1.2231, 1.2230, 1.2225$ and $1.4269, 1.4271, 1.4273$ across the three windows. Roughly half the available margin sits in $C_{\square}$, and a lower bound on it is a lower bound on pairs $(n, n+2)$ with all four prime factors above $X^{1/3}$, which is the same dimension and the same sieve variable as $T$.

**Route 4: the two small factors.** Each of the $174{,}791$ cells of type $P_2P_2$ carries a factorisation of both members,
$$6j-1 = pq, \qquad 6j+1 = rs,$$
with $p, r$ the smaller factors. The only constraint between them is $p \ne r$, which holds in all $174{,}791$ and follows in a line: a prime dividing $6j-1$ leaves remainder $2$ in $6j+1$. Beyond it the pair behaves as two independent draws from the marginal law $\propto 1/(p\log(X/p))$ that the line count itself produces. The correlation of $\log p$ with $\log r$ is $-0.00062$ against a permutation null of mean $0.00009$ and standard deviation $0.00274$, that is $z = -0.26$; a chi-square on an $8\times8$ grid of quantiles gives $56.3$ on $49$ degrees of freedom, with largest standardised residual $2.47$ in sixty-four cells; the share with $r/p$ in $(0.952, 1.05)$ is $0.02264$ against a shuffled $0.02188$, in $(0.833, 1.2)$ it is $0.08262$ against $0.08309$, and in $(0.5, 2)$ it is $0.29293$ against $0.29270$; the median of $|r-p|$ is $73{,}880$ against $74{,}042$. The phase inside the sector is equally flat: correlations $0.00223$ and $-0.00035$ with $\log p$ and $\log r$, and the ten deciles of the sector hold $17{,}523$, $17{,}728$, $17{,}247$, $17{,}534$, $17{,}323$, $17{,}386$, $17{,}552$, $17{,}416$, $17{,}667$, $17{,}415$ cells against a flat $17{,}479$.

**Route 5: the determinant-one relation.** The same cells carry an exact Bézout relation. From $rs - pq = 2$, writing $r - p = 2a$ and $q - s = 2b$,
$$as - pb = 1, \qquad\text{equivalently}\qquad \left\lvert \frac{a}{p} - \frac{b}{s} \right\rvert = \frac{1}{ps},$$
so every $P_2P_2$ cell is a Farey pair, and $a \equiv s^{-1} \pmod p$. Verified on all $174{,}791$. A genuine finiteness statement follows: the two congruences $6j \equiv 1 \pmod p$ and $6j \equiv -1 \pmod r$ fix $j$ modulo $pr \ge 5861^2 = 34{,}351{,}321 \gt  N$, so **no pair $(p,r)$ can occur twice in the window** — and indeed the $174{,}791$ cells carry $174{,}791$ distinct pairs.

The relation is nevertheless local. Ordering the cells by $j$, the natural composition law would make consecutive cells Farey neighbours, $\lvert a_i p_{i+1} - a_{i+1} p_i \rvert = 1$. **That holds for none of the $174{,}790$ consecutive pairs**; the median of that quantity is $2.3\times10^9$ and its minimum anywhere in the window is $4604$. Nor does anything telescope: $\sum a_i/p_i = 2.6170\times10^5$ with total variation $5.1593\times10^5$, against the $1.181$ that a boundary term would leave, and the same failure by five orders of magnitude for $b/s$ and for $1/(ps)$. Reordering the cells at random gives the same zero, so the ordering by $j$ contributes nothing. As a bipartite graph on $(p, r)$ the configuration is likewise generic: $16{,}289$ four-cycles against $15{,}830 \pm 195$ from a degree-preserving shuffle, a ratio of $1.029$.

*A methodological note, because this measurement was got wrong twice before it was got right.* The shuffle must be constrained to simple graphs. A closed-form configuration estimate gave $64$, reading the data as a $255$-fold excess; an unconstrained shuffle created $115$ to $156$ multi-edges and gave $20{,}360$, reading the same data as a $20$ per cent deficit. Only when the shuffle respects the constraint $pr \gt  N$ that the geometry itself imposes — the constraint proved two paragraphs above — does the null become $15{,}830$ and the answer $1.029$. **The correct null was derivable from the object under study, and neither wrong null was distinguishable from a signal by inspection.**

**What the five have in common.** Each route asks the line geometry for a quantity that would separate $\Omega = 1$ from $\Omega = 2$, and each returns a quantity that is either identically the output, or independent of it to the precision available. The framework describes the one-sided structure exactly — the marginal law of the small factor, the capacity of every line, the position of every strike — and describes the two-sided structure by independence. The twin conjecture is the assertion that the two-sided structure is *not* exactly independent, by an amount far below anything measurable here. That is §8.2 in the vocabulary of the lines rather than of the sieve, and it is the reason the account stops where it does.


---

### 6.8 The trap this section exists to avoid

Theorem 4 is worth restating as a discipline rather than only as a result. The identity
$$2(R-C)  =  \sum (-1)^{\Omega(n)}$$
says that the inequality one wants is *equivalent* to a statement nobody knows how to prove. It would have been easy, and would have looked like progress, to write the same content in a form that hides this.

The characteristic way of hiding it is to introduce a ratio and assume it bounded. Suppose one writes the total correlation over all shifts as a sum of the individual shift correlations,
$$\sum_{n \lt  m \le x} f(n)f(m)  =  \sum_{l \ge 1} \sum_{n \le x} f(n)f(n+l),$$
an identity — both sides count the ordered pairs $n\lt m$ — and then bounds each term by a multiple of the one term of interest,
$$\sum_{n\le x} f(n)f(n+l)  \le  C \sum_{n\le x} f(n)f(n+l_0),$$
with $C$ declared to be a constant. Inverting gives a lower bound for the shift-$l_0$ correlation in terms of the total, and for $f = \vartheta$, $l_0 = 2$ the total is $\sim x^2/2$ by the prime number theorem alone, so a positive lower bound for the twin correlation appears to follow.

**It does not, and the reason is instructive.** The quantity declared constant is
$$C  =  \max_{l \le x}\ \frac{\sum_n f(n)f(n+l)}{\sum_n f(n)f(n+l_0)},$$
whose denominator is the very quantity being bounded. Assuming $C$ bounded independently of $x$ is assuming that the shift-$l_0$ correlation is not asymptotically smaller than every other shift correlation — which for $l_0 = 2$ and $f = \vartheta$ is the twin prime conjecture.

**The step is not merely unproved; the inequality is false as a general statement about $f$.** Take $f$ to be the indicator of the multiples of $3$ together with the two extra points $5$ and $7$. The shift-$2$ correlation is then the three pairs $(3,5)$, $(5,7)$, $(7,9)$ and is **equal to $3$ for every $x$**, while the double sum divided by $x$ grows like $x/18$:

| $x$ | $10^2$ | $10^3$ | $10^4$ | $10^5$ |
|---|---|---|---|---|
| shift-$2$ correlation | 3 | 3 | 3 | 3 |
| (double sum)$/x$ | 6.0 | 55.9 | 555.9 | 5555.9 |
| ratio required of $C$ | 2.0 | 18.6 | 185.3 | 1852.0 |

No fixed $C$ exists.

We record this because the shape of the fallacy is exactly the shape of the correct statement. Every criterion in Paper IV and every measurement in §§2–5 above reduces, on inspection, to a ratio that would have to stay bounded; §6 is written to name that ratio rather than to assume it. **The discipline the whole framework has tried to keep is this: when a construction reduces to an unknown quantity, the useful thing to do is to identify the quantity, not to give it a name and a positive sign.**

## 7. Scope: two test cases

The examples above suggest a useful organising pattern, which we state explicitly as a summary of the tested cases rather than as a universal classification.

### 7.1 The pattern seen in the test cases

$$\begin{array}{lll}
\textbf{periodic statement / zero prime input} & \text{decided internally in these examples} & \text{gap 2} \cr 
\textbf{one prime in a progression} & \text{Dirichlet supplies the missing input here} & \text{gap 4} \cr 
\textbf{two simultaneous primes} & \textbf{not decided by the present framework} & \text{gap 6 / twins}
\end{array}$$

This table summarises the examples studied in this paper; it is not asserted as a theorem classifying every prime problem. The framework describes the periodic divisibility pattern exactly, while simultaneous primality requires information not contained in those periodic counts alone.

### 7.2 A test case: Jacobsthal's function

Jacobsthal's function $j(n)$ [17] — the maximal gap between integers coprime to $n$ — is such a statement: no primality enters, only the pattern modulo a primorial. Computing directly from the pattern, $j(P_k) = 2, 4, 6, 10, 14, 22, 26$ for $k = 1,\dots,7$ (OEIS A048670 [23]) over cycles $2, 6, 30, 210, 2310, 30030, 510510$.

The literature states these bounds in the **sieving bound** $y$ rather than in $k = \pi(y)$, and the translation costs a factor of $\log$, so we give both columns. Write $P(y)$ for the product of the primes up to $y$, and $\log_2, \log_3$ for iterated logarithms.

| | in $y$ | in $k$, via $y \approx k\log k$ |
|---|---|---|
| upper bound (Iwaniec [15], via the linear-sieve error term [14]) | $j(P(y)) \ll y^2$ | $\ll (k\log k)^2$ |
| lower bound (Ford–Green–Konyagin–Maynard–Tao [10]) | $j(P(y)) \gg y\log y \log_3 y/\log_2 y$ | $\gg k\log^2 k \log_3 k/\log_2 k$ |
| conjecture (Maier–Pomerance [21]) | $j(P(y)) \ll y(\log y)^{2+o(1)}$ | $\ll k(\log k)^{3+o(1)}$ |

Measured against the two shapes, from the tabulated values [23] for $k \le 64$: $j/(k\log^2 k) = 1.081,\ 0.868,\ 0.969,\ 0.951,\ 0.988,\ 0.996$ at $k = 5,10,20,30,40,50$ — flat at $1$; while $j/(k\log k)^2 = 0.216,\ 0.087,\ 0.048,\ 0.032,\ 0.025,\ 0.020$ — falling, and falling *exactly* like $1/k$, which is the ratio of the two shapes.

**Two readings have to be kept apart, and we separate them because it is easy not to.** (i) The data sit at $k\log^2 k$, that is, at the FGKMT lower bound up to the factor $\log_3 k/\log_2 k$, and about a factor $\log k$ *below* the Maier–Pomerance conjecture. So the numbers do not confirm that conjecture; they merely fail to contradict it. (ii) The proved upper bound is away from the data by a factor of order $k$, not of order $\log^2 k$ — which is exactly what the clean $1/k$ decay of the second row records.

### 7.3 Proposition 2 (saturation of extremal runs)

Applying the framework to the *structure* rather than the *size* of an extremal configuration reveals a clean measured pattern.

> **Proposition 2 (measured).** In the maximal closed run of length $L$ for the first $k$ primes, every line $p$ covers exactly $\lceil L/p \rceil$ positions, with the single exception of the largest line, which covers exactly one.

| primes | $L$ | measured coverage | ceilings $\lceil L/p\rceil$ |
|---|---|---|---|
| $\lbrace 2,3\rbrace$ | 3 | 2, 1 | 2, 1 |
| $\lbrace 2,3,5\rbrace$ | 5 | 3, 2, 1 | 3, 2, 1 |
| $\lbrace 2,3,5,7\rbrace$ | 9 | 5, 3, 2, **1** | 5, 3, 2, **2** |
| $\lbrace 2,3,5,7,11\rbrace$ | 13 | 7, 5, 3, 2, **1** | 7, 5, 3, 2, **2** |
| $\lbrace 2,3,5,7,11,13\rbrace$ | 21 | 11, 7, 5, 3, 2, **1** | 11, 7, 5, 3, 2, **2** |

**In every displayed extremal run, no line wastes a strike relative to the stated ceiling pattern.** The proportion of *critical* positions — those covered by exactly one line — rises steadily: $3/3$, $4/5$, $7/9$, $10/13$, $16/21$.

### 7.4 And why it yields no bound

The counting condition that saturation feeds is $\sum_p \lceil L/p\rceil \ge L$. Because $\sum_p 1/p$ diverges, this is satisfied for $L$ into the tens of thousands from $k=3$ onward:

| $k$ | 3 | 5 | 10 |
|---|---|---|---|
| true $j(P_k)-1$ | 5 | 13 | 45 |
| counting bound | $\gt 2\times10^4$ | $\gt 2\times10^4$ | $\gt 2\times10^4$ |

The bound exceeds the truth by factors of $400$ to $4000$ already at small $k$. **This is the same failure recorded in §4 and §2(b): the framework's local statements are exact, and its summation over lines destroys them.**

### 7.5 The pattern of the whole work

$$\boxed{ \text{Across the tested routes, the local laws are much sharper than the available summed bounds.} }$$

The routes examined here exhibit this repeatedly: the pigeonhole constraint (§4), the deletion budget (§2(b)), the criterion $K\lt G$ (§3.3), the collective cancellation [III, §4], and the covering condition for Jacobsthal (§7.4). In each case a sharp local law is followed by a summation — or, equivalently, a passage from cycle to short window — whose loss exceeds the margin available. **[II, §5.2] isolates why with unusual clarity: making the layers disjoint removes the double-counting entirely, so the summed bound stops diverging and stays below $1$ for every depth — yet it then returns exactly $\prod(1-1/q)$. The interference was never in the intersections; it lives in the size of each layer, which already contains the product of all the layers before it.** **We therefore treat this as the recurring limitation revealed by the present tests, rather than as a theorem excluding every possible summation method.**



### 7.6 A second test case: almost-primes between squares

The pattern in §7.1 suggests a second family of test problems, structurally closer than Jacobsthal: statements of the form *every interval $(n^2,(n+1)^2)$ contains an integer with $\Omega(m) \le k$*. These are natural here because **$\Omega$ is precisely inheritance depth**: a point of multiplicative depth $k$ is a point at which $k$ layers of inheritance met.

**The literature.** Brun [4] obtained $k = 11$ for large $n$; Chen [7] later obtained $k = 2$ for sufficiently large $n$. Explicit statements valid for *every* $n$ are much harder: Dudek and Johnston [9] reached $k = 4$ using Kuhn's weights [20], and Campbell [6] reached $k = 3$, combining a finite verification for $n^2 \le 10^{31}$ with Richert's logarithmic weights [26] and the explicit linear sieve of Bordignon, Johnston and Starichkova [1]. Between consecutive **cubes**, Johnston, Sorenson, Thomas and Webster [18] obtain $k = 2$ for all $n$. Legendre's conjecture, $k=1$, remains open even under the Riemann hypothesis [24].

**The framework reproduces the exponent-level squares-versus-cubes contrast.** A survivor of sieving to depth $x^{\theta}$ near $x$ has $\Omega \le \lfloor1/\theta\rfloor$, while the window enters through the sieve variable $s=\alpha/\theta$ when its length is $x^{\alpha}$:

| window | $\theta = 1/4$ | $\theta = 1/3$ | $\theta = 1/2$ |
|---|---|---|---|
| squares, $\alpha = 1/2$ | 2.000 | 1.500 | **1.000** |
| cubes, $\alpha = 2/3$ | 2.667 | 2.000 | **1.333** |

At the depth required for $\Omega \le 2$ the cube window gives a sieve variable larger by exactly the exponent gap $2/3 - 1/2 = 1/6$, i.e. by $33$%. **This exponent gap is one structural reason the cube problem gives more sieve room than the square problem; it is not, by itself, a proof of the published distinction.** (Measured, the distinction is about provability and not truth: the minimum of $\Omega$ over the window is $1$ for both squares and cubes at $x = 10^6, 10^8, 10^{10}$.)

**Where the framework stops, and where it does not.** For $k=3$ the sieve variable is $s = 1.500$, and for $k=2$ it is $s = 1.000$ — both far below the linear sieve's lower-bound threshold $s\gt 2$. The published proofs bridge the gap with **weights**. Paper II shows that the framework carries those weights exactly on the cycle, including Richert's once the generating function is refined by the size of the line [II, Cor 2]; Paper III finds that weights of that soft shape transfer very accurately on the tested windows [III, Prop 1]. **Thus the experiments do not identify the algebraic representation of the weight as the bottleneck; the required rigorous lower-bound argument remains external.**

**How much is lost in that transfer, measured.** The statement just made is qualitative, and it can be replaced by numbers. Compare the cycle law of [II, Thm 2] against a direct census over consecutive square windows $[M^2,(M+2)^2]$ near $X$, sieving at depth $z = X^{1/u}$, and separate the comparison into three layers.

*Layer 1 — the mean is exact.* The mean inheritance depth is $\sum_{q\le z} 2/q$, and each line strikes exactly $2/q$ of the cells of any interval up to a bounded edge term; measured, the window/cycle ratio is $1.0000$ at $u = 2, 3, 4$. There is no transfer problem at this level.

*Layer 2 — the state totals move by a known constant.* At $u = 2$ the $NN$ total in the window, divided by its cycle value, converges to the two-dimensional Buchstab factor $e^{2\gamma}/4 = 0.793055$ already met in Appendix B:

| $X$ | $10^6$ | $10^7$ | $10^8$ | $10^9$ | $10^{10}$ |
|---|---|---|---|---|---|
| $NN$ window / $NN$ cycle | $1.0113$ | $0.9814$ | $0.8653$ | $0.8071$ | $\mathbf{0.7953}$ |
| distance to $e^{2\gamma}/4$ | $+0.218$ | $+0.188$ | $+0.072$ | $+0.014$ | $\mathbf{+0.002}$ |

Three decimal places at $X = 10^{10}$. So this layer is not a free parameter: it is a constant the framework already computes.

*Layer 3 — the shape of the depth distribution carries a residual that does not decay.* Within the state $OO$, the conditional mean depth in the window is below its cycle value by $+0.18\text{ per cent},\ -0.24\text{ per cent},\ -1.51\text{ per cent},\ -1.89\text{ per cent},\ -1.78$% at the same five heights, and the total-variation distance of the conditional law is $0.012,\ 0.028,\ 0.042,\ 0.046,\ 0.045$. **Both saturate; neither is a finite-size effect.** Rescaling each state to its measured total removes almost none of it ($0.0770 \to 0.0755$ at $X = 10^8$), so the correction is not a single multiplicative constant. Across $u$ the residual is signed: negative on $(2, 2.7)$ with a minimum near $u = 2.2$, positive on $(2.7, 3.3)$, and indistinguishable from zero for $u \ge 3.5$ — a shape consistent with a Buchstab-type delay structure in the depth variable, though we do not identify it.

**And the quantity the proofs actually use transfers far better than the law it is computed from.** Taking Richert's weight itself, with the sifting range and the weight range both scaled with $X$ ($z = X^{1/4}$, $y = X^{1/2}$), and comparing the cycle prediction with the direct window census:

| $X$ | $z$ | $y$ | mean $w$, window / cycle | $\sum\max(0,w)$, window / cycle |
|---|---|---|---|---|
| $10^{8}$ | $100$ | $10^{4}$ | $0.99860$ | $0.99610$ |
| $10^{9}$ | $177$ | $3.2\times10^{4}$ | $0.99886$ | $0.99628$ |
| $10^{10}$ | $316$ | $10^{5}$ | $0.99892$ | $\mathbf{0.99638}$ |

The truncated sum — the quantity a weighted sieve argument evaluates — transfers with a **relative error of $0.36$%, stable across three decades**; the linear part is off by $0.11$%, and the truncation triples the discrepancy, as one expects of a nonlinear functional. This is five times smaller than the $1.8$% distortion of the depth law from which the weight is computed, and it is the same phenomenon as [III, Prop 1]: soft weights transfer, sharp indicators do not, and $OO$ is a sharp condition while $w$ is a soft one.

**What this does and does not settle.** A weighted-sieve argument needs the *sign* of the truncated sum, not its value to four figures; an error of a third of a percent cannot change a sign. **So the computational side of the weight is not the obstruction, by a wide margin — and that is now a measured statement rather than an impression.** What is missing is not a better computation but a *proof*: a rigorous upper bound for $\bigl|\sum_{\text{window}}\max(0,w) - \sum_{\text{cycle}}\max(0,w)\bigr|$, valid for all $X$ rather than observed over three decades. That is the distribution of a weighted $\Omega$ in a short interval, and it is the external ingredient of §8.1 in its most concrete form the present work can give it.

**A sharper localisation of what is missing, obtained inside the framework.** The bound above ($s = 1.500$ for $k=3$) describes the sieve at the depth that makes survivors $P_3$ directly. One may instead sieve *less* deeply and let the almost-prime bound come from the size of the window. Write $Y = \sqrt{n+1}$ and sieve $(n^2,(n+1)^2)$ only to depth $Y/2$. Every prime factor of a survivor then exceeds $Y/2$ while the survivor itself is below $Y^4$, and $(Y/2)^5 \gt  Y^4$ as soon as $Y \gt  32$; hence

$$\Omega(x) \le 4 \quad\text{for every survivor, once } Y \gt  32,$$

so the *only* obstruction to $\Omega \le 3$ in the window is a survivor with exactly four prime factors. Such a survivor is severely constrained. Writing $x = pqrs$ with $p \le q \le r \le s$:

- **the fourth factor is forced.** Given $p,q,r$, the admissible $s$ lies in a window of width $(2n+1)/pqr \lt  2Y^2/(Y/2)^3 = 16/Y$, which is below $1$ once $Y \gt  16$: there is at most one candidate;
- **the first two are confined to about four positions.** Given $r,s$, the product $pq$ lies in a window of width $(2n+1)/rs \lt  2Y^2/(Y/2)^2 = 8$;
- **the factorisation always straddles $n$:** $pq \le n \lt  rs$ in every case examined ($78$ of $78$ at $Y = 29, 53, 101, 199, 293, 401$).

| $Y$ | $29$ | $53$ | $101$ | $199$ | $293$ | $401$ |
|---|---|---|---|---|---|---|
| survivors | $321$ | $922$ | $2{,}840$ | $9{,}535$ | $19{,}093$ | $33{,}379$ |
| with $\Omega = 4$ | $1$ | $3$ | $6$ | $15$ | $25$ | $28$ |
| fraction with $\Omega \le 3$ | $0.99688$ | $0.99675$ | $0.99789$ | $0.99843$ | $0.99869$ | $\mathbf{0.99916}$ |
| bound $16/Y$ (widest $s$-window) | $0.552$ | $0.302$ | $0.158$ | $0.080$ | $0.055$ | $0.040$ |
| widest $s$-window measured | $0.245$ | $0.202$ | $0.083$ | $0.040$ | $0.036$ | $0.023$ |

**And this is what makes the localisation informative rather than encouraging.** Since the exceptional set is so rigidly determined, it is natural to look for an injection sending each $\Omega = 4$ survivor to a nearby $\Omega \le 3$ one; four constructions were tried (sliding the large half, reflection in the window, replacing the least factor by a neighbouring prime, and perturbing the difference-of-squares representation), and the best succeeded on $12$ of $61$ exceptional survivors — none is close to the required $100$%. The measurement above explains why an injection was the wrong instrument: **the exceptional set is not the difficulty.** At $Y = 401$ it is $0.08$% of the survivors and falling, so essentially the entire content of the statement is a positive *lower bound* on the number of survivors of sieving to depth $Y/2$ in a window of length $2n+1$. That is a dimension-one sieve question with sieve variable

$$s  =  \frac{\log(2Y^2)}{\log(Y/2)}  \longrightarrow  2 ,$$

i.e. the critical point once more. **The reduction is genuine and sharp — it removes every degree of freedom but one — and the one it leaves is exactly the lower bound the framework cannot supply, at exactly the value of $s$ at which it never can.** This is §7.1's pattern in its most compressed form: the framework can localise the difficulty to a set of density $10^{-3}$ and still not cross it.

### 7.7 The correlation of the survivor count, and the order of its sum

**The variance of the survivor count, and where that question already stands.** The measurements above concern the mean; one may also ask for the second moment of $B(a)$, the number of cells of $(a^2,(a+2)^2)$ surviving all lines $p \le a/2$. Expanding the square introduces the correlation of the survivor indicator at cell-distance $h$, and **that correlation is already transported exactly by [II, Thm 4]**; nothing new is needed here beyond a change of coordinates, which we record because the resulting form is the one the present section uses.

Paper II indexes gap-$2$ pairs by $x$, so that consecutive indices differ by $2$ in the integer, and obtains the ladder $K_q(h_{\mathrm{II}}) = q-2, q-3, q-4$ according as $h_{\mathrm{II}} \equiv 0$, $\pm1$, or otherwise modulo $q$. Cells are spaced $6$ apart, so a cell-distance $h$ is $h_{\mathrm{II}} = 3h$; substituting, $h_{\mathrm{II}} \equiv 0$ becomes $p \mid h$ for $p\gt 3$, and $h_{\mathrm{II}} \equiv \pm1$ becomes $3h \equiv \pm1$, i.e. $p \mid 9h^2-1$. Writing $\nu_p(h) = p - K_p$ for the number of residues the pair of cells forbids:

$$\nu_p(h)  =  \begin{cases} 2, & p \mid h,\cr  3, & p \mid 9h^2-1,\cr  4, & \text{otherwise,}\end{cases}$$

the three cases being mutually exclusive, since $p \mid h$ forces $3h \equiv 0$. (Directly: with $c_p \equiv 6^{-1}$, the forbidden residues for $m$ are $\pm c_p$ and $-h\pm c_p$, which coincide in pairs under exactly those two conditions. Checked against a direct count with no mismatch for all $p\lt 200$, $h\lt 300$.) **[II, §6.3] already names the resulting product as the singular series of the Hardy--Littlewood $k$-tuple conjecture, "suitably normalised"; what is added below is the normalising constant, the exact mean, and the order of the error.** The series is

$$S_B(h;z) = \prod_{5\le p\le z}\frac{1-\nu_p(h)/p}{(1-2/p)^2} = G(z)\prod_{p \mid h}\frac{1-2/p}{1-4/p}\prod_{p \mid 9h^2-1}\frac{1-3/p}{1-4/p},\qquad G(z)=\prod_{5\le p\le z}\frac{1-4/p}{(1-2/p)^2},$$

with $G$ convergent ($\log$ of the factor is $\asymp -4/p^2$) and $G(\infty) = 0.39688$ to five places.

**This series is self-normalising, exactly.** Two derivations agree. Per prime, the three cases have densities $1/p$, $2/p$ and $1-3/p$, so with $q = 1/p$ the expected local factor is
$$(1-3q) + q \frac{1-2q}{1-4q} + 2q \frac{1-3q}{1-4q} = \frac{1-4q+4q^2}{1-4q} = \frac{(1-2/p)^2}{1-4/p},$$
which is the reciprocal of the corresponding factor of $G$; hence $G\prod_p E_p = 1$. Equivalently, expanding by Dirichlet convolution with $f(p) = 2/(p-4)$ and $g(p) = 1/(p-4)$, the condition $e \mid 9h^2-1$ contributes $2^{\omega(e)}$ residues and the main term is $G H \prod_p\bigl(1 + 4/(p(p-4))\bigr) = GH\prod_p (p-2)^2/(p(p-4)) = H$. This is the analogue, for the pattern $h(3h-1)(3h+1)$, of the singular-series averages of Montgomery and Soundararajan, and it identifies the object: $S_B$ is the Hardy--Littlewood series of a prime quadruple, normalised by the square of the twin constant. Writing $\mathcal H_h = \lbrace -1,1,6h-1,6h+1\rbrace$, the local factors at $2$ and $3$ are $8$ and $27/16$, and $\prod_{p\gt 3}$ of the $C_2$ factor is $\tfrac43 C_2$, so that

$$\mathfrak S(\mathcal H_h)  =  \tfrac{27}{2}\bigl(\tfrac43\bigr)^2 C_2^2  S_B(h)  =  24 C_2^2 S_B(h).$$

**The size of the error in that average is larger than a first look suggests, and we record the correction.** An earlier draft of this section fitted $\sum_{h\le H}(S_B(h)-1)$ over $H \le 4\times10^5$, obtained a coefficient near $0.85$ that drifted with the fitting range, and reported the error as $O(\log H)$. Extending the computation to $H = Q_7 = 37{,}182{,}145$ (the seventh primorial from $5$) shows that reading to be wrong: the drift was not instability in a coefficient but the curvature of a quadratic seen over too short a range. For the smoothed sum, which has far smaller fluctuation,

$$\Sigma_B(C) := \sum_{h\lt C}\Bigl(1-\frac{h}{C}\Bigr)\bigl(S_B(h)-1\bigr)  =  -0.0329 (\log C)^2  -  0.244\log C  -  0.38,$$

with root-mean-square residual $0.0018$ over nine points spanning $10^5 \le C \le 3.7\times10^7$; the linear model $a\log C + b$ has residual $0.105$ over the same points, and $a\log C\log\log C + \cdots$ has $0.0045$. The unsmoothed sum fluctuates by $O(1)$ and does not separate the models on its own, but its local slope over the upper range is near $1.5$, against the $0.85$ that the short-range fit had suggested. **We therefore state the order as $(\log C)^2$ and withdraw the earlier $O(\log H)$.** The coefficient is measured, not derived; we have no closed form for it.

**One consequence is worth stating, because it converts a measured constant into an explained one.** In the independent-window model the dispersion is
$$\frac{\mathrm{Var}(B)}{\mathbb E B}  =  1 - \rho_1 + 2\rho_1\Sigma_B(C),\qquad \rho_1(z)=\prod_{5\le p\le z}\Bigl(1-\frac2p\Bigr) \sim \frac{12C_2e^{-2\gamma}}{\log^2 z} = \frac{2.497}{\log^2 z},$$
the factor $2$ accounting for $\pm h$. Had $\Sigma_B$ been $O(\log C)$ the product $\rho_1\Sigma_B$ would vanish and the dispersion would tend to $1$; with $\Sigma_B \asymp -c(\log C)^2$ the two logarithms cancel and the leading term contributes $-2\times2.497\times0.0329 = -0.164$, a constant. **So the sub-Poisson behaviour is a genuine limit and not a slowly vanishing correction, and the quadratic order is exactly what makes it one.**

**At the scales where the dispersion was measured, however, the subleading terms of $\Sigma_B$ dominate that limit, and the model is therefore a prediction of drift rather than of a fixed number.** Evaluating the fitted $\Sigma_B$ at $z = a/2$, $C = 2a/3$:

| $a$ | $10^{4}$ | $10^{5}$ | $10^{6}$ | $10^{8}$ | $\to\infty$ |
|---|---|---|---|---|---|
| $\rho_1$ | $0.0344$ | $0.0213$ | $0.0145$ | $0.0079$ | $0$ |
| model $\mathrm{Var}/\mathbb E$ | $0.616$ | $0.674$ | $0.708$ | $0.747$ | $\mathbf{0.836}$ |
| measured | $0.685$ | $0.702$ | — | — | — |

A direct evaluation at $a = 100001$ from the exact truncated series ($C = 66{,}668$, $z = 50{,}000$, $\rho_1 = 2.13\times10^{-2}$, $\sum_{h\ne0} = -13.95$) gives $0.681$ against the measured $0.702$, a $3$% agreement with no free parameter. **The negative sign is the substance: the repulsion encoded in $\nu_p$ is what makes the count sub-Poisson.** The model runs a few percent low at these sizes, and predicts a slow rise of the dispersion toward $0.836$; the two available measurements do rise, $0.685$ at $a\sim10^4$ to $0.702$ at $a\sim10^5$, against a predicted rise of $0.616$ to $0.674$. That the increments agree better than the levels is consistent with a constant offset from the Buchstab correction, which the independence model omits; we have not isolated it, and the rise itself remains a prediction rather than a confirmed law.

**Why this is a description and not a route.** It is natural to hope that a second-moment bound of the shape $\sum_{A\lt a\le2A}(B(a)-\mu(a))^2 \ll \sum_{A\lt a\le2A}\mu(a)$ would give $B(a)\gt 0$ for almost all $a$, which is far weaker than a large-deviation estimate. But that conclusion is already known, in a much stronger form and by different means. Bazzanella [2] proves **unconditionally** that all intervals $[n^2,(n+1)^2]\subset[1,N]$ with at most $O(N^{1/4+\varepsilon})$ exceptions contain the *expected number of primes* — not merely a survivor of the small lines — with $O(f(N)\log^2 N)$ exceptions on the Riemann hypothesis, $O(N^{\varepsilon})$ under the Lindelöf or Density hypotheses [3], and none at all under a strong form of Montgomery's conjecture. The mechanism is zero-density estimates for $\zeta$ together with a fourth-power mean of $\psi$ in short intervals; the bridge to square windows is the observation that consecutive square windows are spaced further apart than the block of exceptions forced around any one of them, so their exceptional blocks are disjoint [3, Lem. 2.2]. **We record the local law above as a description of the dispersion, therefore, and not as the first step of a route: the almost-all statement it was reaching for is settled, more strongly, by analytic methods this framework does not contain.**

**A methodological caution that cost two false readings here.** The subtracted term $W(C) e_k(\lbrace \lambda_p\rbrace )$ is of size $C$, so an unclosed tail in the expectation is amplified by $C$: two computations differing only in the prime bound used for $G$ and $e_k$ disagreed by $0.1$ at $C = 1.6\times10^6$, an amount larger than several of the effects under discussion, and the disagreement was traced exactly to $4/(P\log P)$ summed over the missing primes. Any reproduction must close that tail analytically or fix the bound; the accompanying script does the former.

### 7.8 The narrowest form of the requirement, and why it is still the wall

**The narrowest the requirement gets, and what that shows.** Paper IV, §3.2, reduces a twin in a sector to a single open cell avoiding six named positions. Two further facts sharpen that as far as the construction can. First, the lines $5$ and $7$ alone cut the six to three, and no further small line lowers it — a larger line can pick a phase striking none of the six, and the Chinese remainder theorem combines that freely with the phase of $5$ and $7$ that leaves three. Second, three open positions occur **only** when $(M+2,M+4)$ is itself a twin [IV, Cor. 7], so under the negation the count is at most two. And in five residue classes,
$$M \equiv 3,\ 51,\ 141,\ 153,\ 201 \pmod{210},$$
those two lines close all six, so there **every** open cell is a twin: the requirement becomes the bare $C_M \ge 1$.

That is the weakest *numerical* requirement the twin statement takes anywhere in this work — condition (3.2) of [IV, §3.2] is weaker still, but it asks for no count at all — and three measurements say the reduction is not paid for elsewhere. Over the $713$ such sectors below $M = 30{,}000$ there are $444{,}958$ open cells and **not one fails to be a twin**, against $155$ non-twin survivors in the $428$ ordinary sectors below $M = 3000$ alone. The survivor count itself is not depressed: the density in these five classes against all others is $0.934$ up to $M = 4000$, $0.997$ up to $12000$ and $1.000$ up to $30000$ — **fixing the phases of $5$ and $7$ changes which cells die, not how many.**

That last sentence names a standard device rather than an observation of ours. Passing to a residue class modulo a primorial to remove the local bias at the small primes, at no asymptotic cost, is the **$W$-trick**, and the modulus here is $210 = 2\cdot3\cdot5\cdot7$. In the analytic literature the compensating factor $\phi(W)/W$ is inserted by hand and the absence of cost is known; here it is not assumed but measured, and the three ratios above are that measurement. The device is standard — see its use in Tao and Teräväinen [29], and in the quantitative polynomial Szemerédi work of Krause, Mousavi, Tao and Teräväinen [19] — and we record the identification because the same thing has happened repeatedly here: an object built from inside the construction turns out to have a name. And $C_M$ is nowhere near zero: its minimum over those sectors is $10$ below $M = 3000$ and $520$ for $M$ near $2\times10^4$, against $497$ in the ordinary classes.

**That calculation has been carried out, and it closes the local route.** Coupling consecutive sectors and admitting the lines $11,13,17$ bounds the exception budget over a full $210$-window by $31$ under the twinless hypothesis, and that ceiling cannot be lowered by any finite set of lines: of the $28$ maximal configurations, $27$ are killed by a fixed prime divisor once the quadratic partner conditions are included, and the survivor is admissible at every prime, so the residues can be chosen simultaneously against any finite list. The order in which the lines are born adds nothing either. The calculation, with its verifications, is [IV, §3.8]; here we record only what it means.

**The upper-bound side of the argument is therefore finished, and the whole difficulty sits in the other half.** One does not need to kill the escapee: if $\sum_{i} C_{M_i} \ge 32$ can be established, the thirty-second survivor has no room inside $E$ and is a twin. Measured, that requirement is met with enormous room — $B_k := \sum_i C_{M_i}$ is $1{,}337$ at $k=1$, $29{,}579$ at $k=100$ and $196{,}948$ at $k=1000$, with $B_k\log^2 M_0/M_0$ flat at about $139$ from $k = 20$ onward, and the minimum over a band of sixty consecutive $k$ never below $1{,}337$. **The requirement is exceeded by a factor of six thousand and rising, and remains unproved.**

**And lengthening the window does not help.** Sieving an interval of length $H$ to depth $z$ has $s = \log H/\log z$; for one sector $H \asymp 12M_0$ and for the full window $H \asymp 420M_0$, both against $z \asymp M_0$, so $s \to 1$ in each and the gain is $\Delta s = \log 35/\log M_0$ — $0.257$ at $M_0 = 10^6$, $0.129$ at $10^{12}$, vanishing. Against the two-dimensional sifting limit $\beta_2 = 4.2664$ this closes under seven per cent of the gap, and less as $M_0$ grows: **a constant multiple of the length buys nothing asymptotically, only a power of $M_0$ would.** The reorganisation is therefore a clarification and not a reduction — but it is a real one, because it closes one of the two branches permanently and by proof.

**So the requirement is now one survivor, in one arithmetic progression, for infinitely many $M$ — and it is still the same wall.** The quantity to be bounded below is the number of cells of an interval of length $\asymp 2M$ surviving every line $p \le M$: a two-dimensional sieve at $u = 2$, where the sifting limit is $\beta_2 = 4.2664$ and no positive lower bound is available. Lowering the demand from $C_M \ge 7$ to $C_M \ge 3$ to $C_M \ge 1$ does not approach that bound, because the sieve supplies none of the three. **The reduction is worth recording precisely because it is so sharp and still does not bind: it isolates what the framework can do — fix the arithmetic of the exceptional positions completely — from what it cannot, which is to produce a single guaranteed survivor.**

**A remark from the same literature, which corroborates §7.** Campbell records that reaching $\Omega \le 2$ between squares appears to lie beyond his framework precisely because it uses only Type I information, and that this is so even for very large $n$ [6]; Chen's asymptotic $k = 2$ [7] comes from a different route. The deficit named *bilinearity* in §7.1 is therefore the one the specialists name as well, in the same test problem.

**What does remain** is the numerical optimisation itself, and the fact that at $k=2$ even that is not enough: Campbell records that reaching $\Omega \le 2$ appears to lie beyond an argument using only Type I information, however large $n$ is taken. That is the fourth deficit of §7.1, met in a test problem where the first three do not bite.



## 8. Conclusion

### 8.1 What an external ingredient would have to supply

Taking §7.5 and §7.6 together, the deficits exposed by these tests can be organised into four categories, each corresponding to a standard class of tools.

| deficit | what is missing | standard remedy |
|---|---|---|
| **Summation** (§7.5) | control of the aggregate when local laws are summed over lines | large-sieve inequalities; Buchstab iteration with sign selection (Rosser–Iwaniec [16], Harman [13]) |
| **Factor size** (§7.6) | a weight sensitive to *how large* the factors are, not only to how many there are | Richert's logarithmic weights; internally, the per-bin refinement of [II, §4.3] — **carried out there, and it closes** |
| **Window transfer** ([III, §6]) | passage from a cycle statement to a short window at $s\approx2$ | Buchstab's function; the beta-sieve; Richert weights *in application* |
| **Bilinearity** ([III, §5.4], §7.2) | information about $n$ *as a product*, with independent weights on the factors | Type II sums; bilinear forms; dispersion |

**Within this analysis the four deficits are progressively stronger.** The first three concern aggregation, weighting and transfer of information already encoded by the sieve pattern. The fourth asks for bilinear information that the present framework does not generate. Papers II and III address the factor-size bookkeeping and measure the window transfer; they do not supply the missing bilinear control needed for a twin-prime conclusion.

**One deficit has been narrowed rather than removed.** We initially listed *continuity* — the absence of any measure sensitive to the factorisation beyond a count — as a flat impossibility. [II, Thm 2] disposes of the nonlinearity, and [II, §4.1] shows what is left is the dependence on factor size, together with a candidate repair. The lesson is worth stating, since it is the one place in this work where a stated obstruction proved to be partly an artefact of insufficient refinement.





---

### 8.2 Why the stopping point is the right one

Because it is where genuinely new information about the survivors would have to enter, rather than another rearrangement of the same sieve identities. In standard sieve terminology, the missing kind of input is **Type II / bilinear information**: control that sees an integer through interacting factors rather than only through membership in residue classes. The present cell framework supplies no such bilinear estimate for the twin-prime correlation, so the argument stops there.

$$\boxed{ \text{What is missing is not a cleaner formulation but an arithmetic input of a different kind.} }$$

### 8.3 This is not a new sieve

The main sieve-level objects used across the series have classical counterparts: the dimension-$2$ sifting density, the sifting limit $\beta_\kappa$, the sieve density $V(z)$ and Buchstab-type corrections. Correspondingly, the obstruction located here from several independent directions — residue classes, height, square position, cell states, $\Omega$, collective cancellation, and the interaction of the two motions — is the obstruction the literature states in one sentence: **the sieve counts rough integers and does not separate a prime from a semiprime.**

What the series adds is not a new tool but a change of type. Several quantities that are usually embedded inside sieve estimates become exact cycle identities in these coordinates. Those identities help isolate where the remaining loss enters, even though the short-window conclusions still require separate estimates. Several failures come with quantitative diagnostics: the **predicted** cover margin $1.0073$ under the local-constant hypothesis (§3.2), an effective $L^2$ exponent about $3.16$ on the tested range [III, §4], the sifting variable $s\approx2$ against $\beta_2=4.2664$ (§3.3), the Jacobsthal counting overshoot (§7.4), and the measured transfer curve from about $1.0000$ to $0.80$ [III, §6].

### 8.4 Limitations

1. **The framework is multiplicative throughout.** A line is a set of multiples, a strike is divisibility and a meeting is a common divisor. Additive prime correlations such as fixed differences are not determined by these multiplicative identities alone; an additional arithmetic input is required.
2. **Exactness on the cycle, not automatically on the window.** Paper II is exact over a cycle of length $\prod q$. Paper III shows numerically that many soft statistics transfer well, but the short-window statements are partly empirical.
3. **Section 4 is not about twins.** Its graph joins survivors at distance $6$, so its conclusion concerns prime pairs $(p, p+6)$. The caution is stated at the head of §4 and repeated here because the phrase "gap 6" carries two meanings in this subject.
4. **No explicit constants.** The framework produces exact identities and measured ratios, not explicit numerical bounds valid from a stated point onward. The published results on almost-primes between squares are explicit-constant work, and the framework has no machinery for it.
5. **Several statements are measured, not proved,** and are labelled as such: the stability of $T/M \approx 0.80$ [III, §3.2], the saturation law of §7.3, the transfer curve [III, §6], and — in §7.7 — the quadratic order of the singular-series sum together with its coefficient $0.0329$, for which we have no closed form and no proof. The exception-budget results quoted in §7.8 are of a different kind and should not be read as measurements: the ceiling of $31$, the admissibility of the surviving configuration and the emptiness of the timing table are finite exhaustive computations over stated residue classes, and each is a proof. They are carried out in [IV, §3.8]. The script `verify_exception_dichotomy.py` covers the closed forms, the $\lbrace 5,7\rbrace$ table and [IV, Cor. 7]; the sector-coupling budget, the admissibility of the escapee and the timing table are not yet in it, and until they are they should be treated as stated but unaudited.
6. **Priority is not claimed for any result in these papers.**
7. **Negative claims deserve the same suspicion as positive ones.** We recorded one impossibility claim — that the framework could not carry analytic weights — which proved to be an artefact of insufficient refinement; Paper II removes it in two stages. Appendix B lists five further withdrawn results. **The rate at which this structure produces plausible but spurious signals is itself among the findings.**

### 8.5 What this framework does not presently supply

A Type II/bilinear estimate strong enough for the twin-prime correlation. The calculations in these papers do not produce such an estimate, so further rearrangement of the same periodic identities should not be mistaken for having supplied it.

---

## References

The companion papers are cited as [0], [I], [II], [III], [IV].

1. M. Bordignon, D. R. Johnston and V. Starichkova, *An explicit version of Chen's theorem and the linear sieve*, Int. J. Number Theory **21** (2025), 2497–2572.
2. D. Bazzanella, *Primes between consecutive squares*, Arch. Math. (Basel) **75** (2000), no. 1, 29–34.
3. D. Bazzanella, *Some conditional results on primes between consecutive squares*, Funct. Approx. Comment. Math. **45** (2011), no. 2, 255–263.
4. V. Brun, *Le crible d'Ératosthène et le théorème de Goldbach*, Skrifter utgit av Videnskapsselskapet i Kristiania I, no. 3, J. Dybwad, Kristiania, 1920.
5. A. A. Buchstab, *Asymptotic estimates of a general number-theoretic function*, Mat. Sb. **44** (1937), 1239–1246.
6. P. Campbell, *On the existence of integers with at most 3 prime factors between every pair of consecutive squares*, arXiv:2603.10356 (2026).
7. J.-R. Chen, *On the distribution of almost primes in an interval*, Scientia Sinica **18** (1975), 611–627.
8. H. G. Diamond and H. Halberstam, *A higher-dimensional sieve method*, Cambridge Tracts in Mathematics **177**, Cambridge University Press, 2008.
9. A. W. Dudek and D. R. Johnston, *Almost primes between all squares*, J. Number Theory **278** (2026), 726–745.
10. K. Ford, B. Green, S. Konyagin, J. Maynard and T. Tao, *Long gaps between primes*, J. Amer. Math. Soc. **31** (2018), 65–105.
11. C. S. Franze, *Sifting limits for the $\Lambda^2\Lambda^-$ sieve*, J. Number Theory (2011); arXiv:1012.3809.
12. J. Friedlander and H. Iwaniec, *Opera de Cribro*, AMS Colloquium Publications **57**, 2010.
13. G. Harman, *Prime-Detecting Sieves*, Princeton University Press, 2007.
14. H. Iwaniec, *On the error term in the linear sieve*, Acta Arith. **19** (1971), 1–30.
15. H. Iwaniec, *On the problem of Jacobsthal*, Demonstratio Math. **11** (1978), 225–231.
16. H. Iwaniec, *Rosser's sieve*, Acta Arith. **36** (1980), 171–202.
17. E. Jacobsthal, *Über Sequenzen ganzer Zahlen von denen keine zu $n$ teilerfremd ist*, I–III, Norske Vid. Selsk. Forh. Trondheim **33** (1960), 117–139.
18. D. R. Johnston, J. P. Sorenson, S. N. Thomas and J. E. Webster, *Primes and almost primes between cubes*, arXiv:2601.15564 (2026).
19. B. Krause, H. Mousavi, T. Tao and J. Teräväinen, *Quantitative bounds for sets lacking polynomial progressions with shifted prime difference*, arXiv:2608.19525 (2026).

20. P. Kuhn, *Neue Abschätzungen auf Grund der Viggo Brunschen Siebmethode*, Proc. 12th Scandinavian Math. Congress (Lund, 1953), 160–168, 1954.
21. H. Maier and C. Pomerance, *Unusually large gaps between consecutive primes*, Trans. Amer. Math. Soc. **322** (1990), 201–237.
22. J. Maynard, *Small gaps between primes*, Ann. of Math. **181** (2015), 383–413.
23. OEIS Foundation, sequence A048670 (Jacobsthal's function at the primorials).
24. J. Pintz, *Landau's problems on primes*, J. Théor. Nombres Bordeaux **21** (2009), 357–404.
25. D. H. J. Polymath, *Variants of the Selberg sieve, and bounded intervals containing many primes*, Res. Math. Sci. **1** (2014), Art. 12.
26. H.-E. Richert, *Selberg's sieve with weights*, Mathematika **16** (1969), 1–22.
27. A. Schinzel and W. Sierpiński, *Sur certaines hypothèses concernant les nombres premiers*, Acta Arith. **4** (1958), 185–208; erratum, ibid. **5** (1959), 259.

28. A. Selberg, *On elementary methods in prime number theory and their limitations*, Proc. 11th Scandinavian Math. Congress, Trondheim (1949), 13–22.
29. T. Tao and J. Teräväinen, *Quantitative bounds for Gowers uniformity of the Möbius and von Mangoldt functions*, J. Eur. Math. Soc. **27** (2025), 1321–1384.

30. Y. Zhang, *Bounded gaps between primes*, Ann. of Math. **179** (2014), 1121–1174.



## Appendix A — Deviation tables

$T/M$ at moving depth: see [III, §3.2].

Contribution of lines to $\sum B_r$:

| $U$ | negative | sum | positive | sum |
|---|---|---|---|---|
| 1,019 | 136 | $-708.3$ | 33 | $+93.1$ |
| 2,039 | 271 | $-2306.2$ | 36 | $+162.9$ |

$\mu_r$: prediction against measurement over 1,400 sectors:

| $r$ | 5 | 7 | 11 | 17 | 23 | 101 |
|---|---|---|---|---|---|---|
| predicted | 0.200000 | $-0.114286$ | 0.041558 | $-0.022566$ | $-0.013013$ | 0.001415 |
| measured | 0.200286 | $-0.113959$ | 0.027162 | 0.010435 | $-0.093274$ | $-0.037823$ |
| $z$ | 0.04 | 0.01 | $-0.44$ | 0.49 | $-1.03$ | $-0.80$ |



## Appendix B — Note on method

A single rule was followed: **every deviation was measured against an explicit baseline before being interpreted.** Several apparent results were withdrawn under it, and they are recorded here because the rate at which this structure generates spurious signals is part of the finding.

- An apparent $50$% excess of gap-6 pairs in the square window proved to be a baseline error: for a pair $(n, n+6)$ the line $3$ forbids one class, not two, since $6 \equiv 0 \pmod 3$. With the correct baseline the window is slightly *poorer* than the naive periodic average, consistent with the Buchstab-type short-window correction discussed in Paper III.
- An apparent concentration of future composites at the endpoints of gap-6 pairs proved to arise from a wrong definition of degree; with the correct definition the concentration factor is $1.007$–$1.015$, indistinguishable from a random control sample of the same size.
- A statistically significant slope ($z = 9.10$) linking small-factor and large-factor parity proved to be an artefact of an insufficient control: a cubic polynomial failed to absorb the size dependence. With bins of width $0.02$ in $\log$ and permutation within bins, the same data give $z = -1.11$.
- An apparent square-window bias of $1.5$% in the $e$-strip proved to be a statistic artefact: averaging per-sector *ratios* rather than pooling, with only 2–4 samples per sector.
- The asymptotic constant for $\tau$ was first derived from the full-cycle density $32C_2e^{-2\gamma} = 6.6594325$, giving an apparent surplus of $13.1$%. This was wrong: sieving to depth $P$ integers of size $P^2$ places one exactly at $u = 2$, where the Buchstab correction is not negligible. The candidate local scale is $16C_2e^{-\gamma}=5.9304658$, differing from the full-cycle scale by $e^{\gamma}/2=\omega(2)/e^{-\gamma}$. The measurement $T(P)\log^2P/P^2=5.93072$ at $P=9973$ strongly favours this scale on the tested range, but does not establish the asymptotic constant. **Accordingly the $0.73$% surplus is a conditional prediction, not a theorem.**
- A candidate zero-crossing near $2/3$ for the deviation profile is numerically close to $\sqrt{1-e^{-\gamma}}=0.6622239$, which the present data favour among the tested fits; and a candidate amplitude $e^{2\gamma}/4 = 0.7930547$ must **not** be treated as independent evidence, since the profile and the final deficit are linked by the exact identity of [III, identity B] and are therefore the same measurement seen twice.

- **The same constant was later reached a third time, by a third route, and it is again not independent.** Writing $\delta_p$ for the fraction of the cells still surviving that line $L_p$ closes, the survival product $R(P) = R_0\prod_{5\le p\le P}(1-\delta_p)$ is an exact identity, and $\prod(1-\delta_p)/\prod(1-2/p)$ was measured at $0.9436,\ 0.9221,\ 0.8996,\ 0.8840$ for $X = 10^6 \dots 10^9$, apparently approaching $e^{2\gamma}/4$. It is the same quantity as above: $\delta_p$ is computed *from the survivors*, so the product contains the twin count by construction, and substituting the Hardy–Littlewood count in integral form reproduces the whole column to four decimals ($0.8842$ against $0.8840$ at $X=10^9$). **The one thing in that experiment which is not a restatement is where the deviation lives:** $\delta_p = 2/p$ to within $10^{-3}$ for every $p \le X^{1/4}$ — measured ratio $1.0000$ for $u \ge 5$ — with the entire departure confined to $u \in (2,4)$, and the partial products agreeing with $\big(e^{\gamma}\omega(u)\big)^2$ there. That is the fundamental lemma of the sieve stated in the vocabulary of §3.1, and it is the reason no redistribution of effort among the lines changes anything: below $X^{1/4}$ there is nothing to redistribute.

- **A stated obstruction proved to be an artefact.** We first concluded that the framework could not carry analytic weights, since all its objects are binary or counts and a weight would require an infinite state space. Refining the four-state law by *inheritance depth* — a quantity that changes by exactly one under a strike — makes the state space finite and the law exact ([II, Thm 2]), and arbitrary weights follow. **The negative control matters here: binning by weight *value* does not close (error up to $24$%), so the refinement had to be by depth and not by weight.** The general lesson is that an impossibility claim in this setting should be tested against at least one refinement before being recorded.

Any subsequent work in this structure should begin with the baseline, not with the deviation — and should treat its own negative claims with the same suspicion as its positive ones.
