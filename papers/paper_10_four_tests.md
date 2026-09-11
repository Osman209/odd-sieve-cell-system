# Four Tests of the Cell System

## Paper 10. Jacobsthal, almost-primes between squares, shared cofactors, and collisions

---

### Abstract

Four independent tests of the same framework, each carried to the point where it stops. Jacobsthal's function is reproduced exactly on the cycle and yields no bound. Almost-primes between consecutive squares give an asymptotic pair statement with no parity cost, and an explicit version fails at a measured log-lag wall. A shared cofactor between two lines in one window forces the lines to differ by two, and every twin produces such a sharing, so the two statements are equivalent. Collisions inside the sharing set give a criterion that reads the primality of $p+2$ rather than assuming it, with an exact belt for its witness and a collapse to divisibility by three in a narrow slice. **Each case separates its exact statements from its measured diagnostics, none of the four closes the gap, and the paper says in each case exactly why.**

**Numbering.** This paper is one part of a set that was written as a single document and is now published in parts. Each part numbers its own results from one and is self-contained: a reference of the form [Pn, Thm 1] means Theorem 1 of Paper n, and an unqualified "Theorem 1" always means this paper's own. Result numbers therefore differ from those of the earlier seven-document releases, where the whole set shared the numbering of the single document.

**How to read the claims in this paper.** Statements set as Theorems, Propositions and Corollaries are proved, and the proofs are given. Anything described as *measured* is a computation over a stated finite range and is labelled as such where it occurs.

**Keywords:** twin primes, Jacobsthal function, almost-primes, difference of squares, cell coordinates.

**MSC 2020:** 11N35, 11N05, 11A41.

---

## Summary of the results in this part

**§2 — Four tests, the narrowest form of the requirement, and the pattern of the whole**

| Result | What it says | Section |
|--------------------|--------------------------------------------|----------|
| **Proposition 1** | *Measured, not proved.* Saturation of extremal runs in the first test, Jacobsthal's function — and §2.4 explains why it yields no bound. | §2.3 |
| ***Second test*** | Almost-primes between squares, with the correlation of the survivor count and the order of its sum. | §2.5–2.6 |
| ***The narrowest form*** | The requirement reduced as far as the construction can take it — and why it is still the wall. | §2.7 |
| ***The first moment*** | Why a mean below one would suffice, and why no upper bound on it is available here. | §2.13 |
| **Theorem 1** | Two odd primes sharing a cofactor inside one window must differ by $2$ — no primitivity, no primality of $a$, and $a \ge q$ is automatic. | §2.8 |
| **Theorem 2** | The equivalence: infinitely many twins iff sharing occurs at unbounded height. The witness $a = p+6$ works for every twin. | §2.8 |
| **Theorem 3** | $E_p = 0$ iff $p+2$ is prime: the classical difference-of-squares witness always lies inside the sharing set $S_p$. | §2.11 |
| **Theorem 4** | The witness is confined to the belt $\sqrt{p+2} \lt  v \le (p+11)/6$, for every odd $p \gt  121$ with eight exceptions. | §2.12 |
| **Theorem 5** | In a slice of width below $\sqrt{N/3}$ at the top of the belt the test collapses to divisibility by $3$. | §2.12 |
| **Theorem 6** | Collisions enter the slice in stages $t = \tfrac12(d-3k)$ with $t \le \lfloor 3(L-\tfrac32)^2/2N \rfloor$, widening Theorem 5 by $\sqrt2$. | §2.12 |
| **Theorem 7** | Inside one list the value of $\Delta = (N-6v)^2+48t$ determines the collision, so counting $\Delta$ is not a relaxation. | §2.14 |

---

## 1. Setting

[P1] to [P8] supply the framework this paper tests; [P9] supplies the exact form of the obstruction that each test is measured against, and [P11] collects the routes closed elsewhere. Nothing else is imported.

- **[P1]** supplies the window combinatorics: the increments $W_j$ of $\lfloor 2j^2/p\rfloor$, their uniform bound and their exact histogram.
- **[P2]** supplies the coordinates: the line $L_p(k) = p(p+2k)$ beginning at $p^2$, the grid $L_3$, the cells $C_b = (6b-1,6b+1)$.
- **[P3]** supplies the exact cycle laws: the four-state census and its refinement by inheritance depth.
- **[P4]** supplies the passage to a short window, and the measurement $T/M \approx 0.80$ at moving depth.
- **[P5]–[P8]** supplies everything this paper tests: the gap alphabet, the six exception positions, the closing budget, the clocks, and the sector inheritance laws.

**The three words used constantly below**, all as defined in [P2]: a **line** $L_p$ is the odd multiples of $p$ from $p^2$ onward; a **cell** is a pair $C_b = (6b-1,\ 6b+1)$, and it is **open**, or **survives** a set of lines, when neither member lies on any of them; the **window** is the interval between two consecutive odd squares, which in cell coordinates is a block of consecutive indices. A twin pair is an open cell whose two members are both prime, and inside $(u^2,v^2)$ sieved by every line up to $u$ the two notions coincide [P6, §2.1].

**How this paper is organised.** §2 runs four tests of the framework against problems whose answers are known independently of it — Jacobsthal's function (§§2.2–2.4), almost-primes between consecutive squares (§§2.5–2.6), a shared cofactor between two lines (§§2.8–2.10), and collisions inside the sharing set (§§2.11–2.14) — with §2.7 stating the narrowest form the twin requirement takes and §2.15 the pattern common to all four. Throughout, a statement labelled *measured* is a numerical finding with its controls; it is not a theorem and not an asymptotic claim.

---

## 2. Four tests, the sharpest form of the requirement, and the pattern of the whole

The four cases below have one thing in common: each is a question this framework can pose in its own coordinates and whose answer is already known, or already known to be hard, by other means. That makes each of them a test of the framework rather than an application of it. §2.1 states the organising pattern they share, as a summary of the tested cases and not as a universal classification; §§2.2–2.4 and §§2.5–2.6 run the first two cases; §2.7 states the narrowest form the twin requirement takes anywhere in this work; §§2.8–2.10 and §§2.11–2.14 run the third and fourth; and §2.15 closes with the pattern common to all of them.

### 2.1 The pattern seen in the test cases

$$\begin{array}{lll}
\textbf{periodic statement / zero prime input} & \text{decided internally in these examples} & \text{gap 2} \cr 
\textbf{one prime in a progression} & \text{Dirichlet supplies the missing input here} & \text{gap 4} \cr 
\textbf{two simultaneous primes} & \textbf{not decided by the present framework} & \text{gap 6 / twins}
\end{array}$$

This table summarises the examples studied in this paper; it is not asserted as a theorem classifying every prime problem. The framework describes the periodic divisibility pattern exactly, while simultaneous primality requires information not contained in those periodic counts alone.

### 2.2 A test case: Jacobsthal's function

Jacobsthal's function $j(n)$ [11] — the maximal gap between integers coprime to $n$ — is such a statement: no primality enters, only the pattern modulo a primorial. Computing directly from the pattern, $j(P_k) = 2, 4, 6, 10, 14, 22, 26$ for $k = 1,\dots,7$ (OEIS A048670 [16]) over cycles $2, 6, 30, 210, 2310, 30030, 510510$.

The literature states these bounds in the **sieving bound** $y$ rather than in $k = \pi(y)$, and the translation costs a factor of $\log$, so we give both columns. Write $P(y)$ for the product of the primes up to $y$, and $\log_2, \log_3$ for iterated logarithms.

| | in $y$ | in $k$, via $y \approx k\log k$ |
|----------------------------------------------|---------|-------------------|
| upper bound (Iwaniec [10], via the linear-sieve error term [9]) | $j(P(y)) \ll y^2$ | $\ll (k\log k)^2$ |
| lower bound (Ford–Green–Konyagin–Maynard–Tao [8]) | $j(P(y)) \gg y\log y \log_3 y/\log_2 y$ | $\gg k\log^2 k \log_3 k/\log_2 k$ |
| conjecture (Maier–Pomerance [15]) | $j(P(y)) \ll y(\log y)^{2+o(1)}$ | $\ll k(\log k)^{3+o(1)}$ |

Measured against the two shapes, from the tabulated values [16] for $k \le 64$: $j/(k\log^2 k) = 1.081,\ 0.868,\ 0.969,\ 0.951,\ 0.988,\ 0.996$ at $k = 5,10,20,30,40,50$ — flat at $1$; while $j/(k\log k)^2 = 0.216,\ 0.087,\ 0.048,\ 0.032,\ 0.025,\ 0.020$ — falling, and falling *exactly* like $1/k$, which is the ratio of the two shapes.

**Two readings have to be kept apart, and we separate them because it is easy not to.** (i) The data sit at $k\log^2 k$, that is, at the FGKMT lower bound up to the factor $\log_3 k/\log_2 k$, and about a factor $\log k$ *below* the Maier–Pomerance conjecture. So the numbers do not confirm that conjecture; they merely fail to contradict it. (ii) The proved upper bound is away from the data by a factor of order $k$, not of order $\log^2 k$ — which is exactly what the clean $1/k$ decay of the second row records.

### 2.3 Proposition 1 (saturation of extremal runs)

Applying the framework to the *structure* rather than the *size* of an extremal configuration reveals a clean measured pattern.

> **Proposition 1 (measured).** In the maximal closed run of length $L$ for the first $k$ primes, every line $p$ covers exactly $\lceil L/p \rceil$ positions, with the single exception of the largest line, which covers exactly one.

| primes | $L$ | measured coverage | ceilings $\lceil L/p\rceil$ |
|--------|------|-------------------|-------------------|
| $\lbrace 2,3\rbrace$ | 3 | 2, 1 | 2, 1 |
| $\lbrace 2,3,5\rbrace$ | 5 | 3, 2, 1 | 3, 2, 1 |
| $\lbrace 2,3,5,7\rbrace$ | 9 | 5, 3, 2, **1** | 5, 3, 2, **2** |
| $\lbrace 2,3,5,7,11\rbrace$ | 13 | 7, 5, 3, 2, **1** | 7, 5, 3, 2, **2** |
| $\lbrace 2,3,5,7,11,13\rbrace$ | 21 | 11, 7, 5, 3, 2, **1** | 11, 7, 5, 3, 2, **2** |

**In every displayed extremal run, no line wastes a strike relative to the stated ceiling pattern.** The proportion of *critical* positions — those covered by exactly one line — rises steadily: $3/3$, $4/5$, $7/9$, $10/13$, $16/21$.

### 2.4 And why it yields no bound

The counting condition that saturation feeds is $\sum_p \lceil L/p\rceil \ge L$. Because $\sum_p 1/p$ diverges, this is satisfied for $L$ into the tens of thousands from $k=3$ onward:

| $k$ | 3 | 5 | 10 |
|----------------|------|------|------|
| true $j(P_k)-1$ | 5 | 13 | 45 |
| counting bound | $\gt 2\times10^4$ | $\gt 2\times10^4$ | $\gt 2\times10^4$ |

The bound exceeds the truth by factors of $400$ to $4000$ already at small $k$. **This is the same failure recorded in [P11, App. B.2.2] and [P11, App. B.2.1]: the framework's local statements are exact, and its summation over lines destroys them.**

### 2.5 A second test case: almost-primes between squares

The pattern in §2.1 suggests a second family of test problems, structurally closer than Jacobsthal: statements of the form *every interval $(n^2,(n+1)^2)$ contains an integer with $\Omega(m) \le k$*. These are natural here because **$\Omega$ is precisely inheritance depth**: a point of multiplicative depth $k$ is a point at which $k$ layers of inheritance met.

**The literature.** Brun [4] obtained $k = 11$ for large $n$; Chen [6] later obtained $k = 2$ for sufficiently large $n$. Explicit statements valid for *every* $n$ are much harder: Dudek and Johnston [7] reached $k = 4$ using Kuhn's weights [14], and Campbell [5] reached $k = 3$, combining a finite verification for $n^2 \le 10^{31}$ with Richert's logarithmic weights [18] and the explicit linear sieve of Bordignon, Johnston and Starichkova [3]. Between consecutive **cubes**, Johnston, Sorenson, Thomas and Webster [12] obtain $k = 2$ for all $n$. Legendre's conjecture, $k=1$, remains open even under the Riemann hypothesis [17].

**The framework reproduces the exponent-level squares-versus-cubes contrast.** A survivor of sieving to depth $x^{\theta}$ near $x$ has $\Omega \le \lfloor1/\theta\rfloor$, while the window enters through the sieve variable $s=\alpha/\theta$ when its length is $x^{\alpha}$:

| window | $\theta = 1/4$ | $\theta = 1/3$ | $\theta = 1/2$ |
|---------------|-------|-------|-------|
| squares, $\alpha = 1/2$ | 2.000 | 1.500 | **1.000** |
| cubes, $\alpha = 2/3$ | 2.667 | 2.000 | **1.333** |

At the depth required for $\Omega \le 2$ the cube window gives a sieve variable larger by exactly the exponent gap $2/3 - 1/2 = 1/6$, i.e. by $33$%. **This exponent gap is one structural reason the cube problem gives more sieve room than the square problem; it is not, by itself, a proof of the published distinction.** (Measured, the distinction is about provability and not truth: the minimum of $\Omega$ over the window is $1$ for both squares and cubes at $x = 10^6, 10^8, 10^{10}$.)

**A statement of the same shape that the framework does reach, because it asks for no primality.** The obstruction of [P9, §2] is about primes; it says nothing about pairs of almost-primes. Weakening the target from *both members prime* to *both members having few prime factors* removes the parity problem entirely, because a lower bound for $\Omega \le k$ with $k$ large enough is a dimension-two sieve problem above its threshold. That gives, for every sufficiently large $m$, a pair $(n, n+2)$ inside $(m^2, (m+2)^2)$ with $\Omega \le 8$ on each member, and a count $\gg m/\log^2 m$.

*What is proved and what is measured, kept apart.* The bound just stated is what a dimension-two sieve delivers with the losses carried honestly; **it is not what the counts actually are.** Measured over the window $(m^2,(m+2)^2)$:

| $m$ | window length | both $\Omega \le 2$ | both $\Omega \le 3$ | both $\Omega \le 8$ | $m/\log^2 m$ |
|-------|-------|-------|-------|-------|-------|
| 101 | 408 | 66 | 138 | 202 | 4.7 |
| 1,001 | 4,008 | 375 | 1,114 | 1,998 | 21.0 |
| 5,001 | 20,008 | 1,388 | 4,703 | 9,982 | 68.9 |
| 10,001 | 40,008 | 2,513 | 8,767 | 19,954 | 117.9 |
| 20,001 | 80,008 | 4,454 | 16,512 | 39,880 | 203.9 |

*(A pair is counted when both $n$ and $n+2$ lie strictly inside the window.)*

The $\Omega \le 8$ count is close to *every* odd integer of the window — about $2m$ of them, so linear in $m$, and larger than the proved lower bound by a factor near $170$ at $m = 10^4$. Taking the minimum over a decade rather than a single $m$: for $m \in [10^4, 10^4+200)$ the least counts are $2{,}415$ at $\Omega \le 2$, $8{,}700$ at $\Omega \le 3$ and $19{,}952$ at $\Omega \le 8$; at $m \in [10^3, 10^3+200)$ they are $353$, $1{,}087$ and $1{,}998$.

**So the gap here is between a theorem and a count, not between a count and the truth.** Even the far stronger statement — a pair of semiprimes at distance $2$ in every such window — appears to hold with thousands of witnesses, and its count grows like $m/\log m$; **we do not prove it, and record it as a measurement.** What the framework cannot do is push $k$ down to $1$, which is the twin statement and the wall of [P9, §2].

**Where the framework stops, and where it does not.** For $k=3$ the sieve variable is $s = 1.500$, and for $k=2$ it is $s = 1.000$ — both far below the linear sieve's lower-bound threshold $s\gt 2$. The published proofs bridge the gap with **weights**. Paper 3 shows that the framework carries those weights exactly on the cycle, including Richert's once the generating function is refined by the size of the line [P3, Cor 4]; Paper 4 finds that weights of that soft shape transfer very accurately on the tested windows [P4, Prop 1]. **Thus the experiments do not identify the algebraic representation of the weight as the bottleneck; the required rigorous lower-bound argument remains external.**

**How much is lost in that transfer, measured.** The statement just made is qualitative, and it can be replaced by numbers. Compare the cycle law of [P3, Thm 2] against a direct census over consecutive square windows $[M^2,(M+2)^2]$ near $X$, sieving at depth $z = X^{1/u}$, and separate the comparison into three layers.

*Layer 1 — the mean is exact.* The mean inheritance depth is $\sum_{q\le z} 2/q$, and each line strikes exactly $2/q$ of the cells of any interval up to a bounded edge term; measured, the window/cycle ratio is $1.0000$ at $u = 2, 3, 4$. There is no transfer problem at this level.

*Layer 2 — the state totals move by a known constant.* At $u = 2$ the $NN$ total in the window, divided by its cycle value, converges to the two-dimensional Buchstab factor $e^{2\gamma}/4 = 0.793055$ already met in [P11, App. A]:

| $X$ | $10^6$ | $10^7$ | $10^8$ | $10^9$ | $10^{10}$ |
|--------------------------------------------|------|------|------|------|------|
| $NN$ window / $NN$ cycle | $1.0113$ | $0.9814$ | $0.8653$ | $0.8071$ | $\mathbf{0.7953}$ |
| distance to $e^{2\gamma}/4$ | $+0.218$ | $+0.188$ | $+0.072$ | $+0.014$ | $\mathbf{+0.002}$ |

Three decimal places at $X = 10^{10}$. So this layer is not a free parameter: it is a constant the framework already computes.

*Layer 3 — the shape of the depth distribution carries a residual that does not decay.* Within the state $OO$, the conditional mean depth in the window is below its cycle value by $+0.18\text{ per cent},\ -0.24\text{ per cent},\ -1.51\text{ per cent},\ -1.89\text{ per cent},\ -1.78$% at the same five heights, and the total-variation distance of the conditional law is $0.012,\ 0.028,\ 0.042,\ 0.046,\ 0.045$. **Both saturate; neither is a finite-size effect.** Rescaling each state to its measured total removes almost none of it ($0.0770 \to 0.0755$ at $X = 10^8$), so the correction is not a single multiplicative constant. Across $u$ the residual is signed: negative on $(2, 2.7)$ with a minimum near $u = 2.2$, positive on $(2.7, 3.3)$, and indistinguishable from zero for $u \ge 3.5$ — a shape consistent with a Buchstab-type delay structure in the depth variable, though we do not identify it.

**And the quantity the proofs actually use transfers far better than the law it is computed from.** Taking Richert's weight itself, with the sifting range and the weight range both scaled with $X$ ($z = X^{1/4}$, $y = X^{1/2}$), and comparing the cycle prediction with the direct window census:

| $X$ | $z$ | $y$ | mean $w$, window / cycle | $\sum\max(0,w)$, window / cycle |
|------|------|------|----------------------------------|----------------------|
| $10^{8}$ | $100$ | $10^{4}$ | $0.99860$ | $0.99610$ |
| $10^{9}$ | $177$ | $3.2\times10^{4}$ | $0.99886$ | $0.99628$ |
| $10^{10}$ | $316$ | $10^{5}$ | $0.99892$ | $\mathbf{0.99638}$ |

The truncated sum — the quantity a weighted sieve argument evaluates — transfers with a **relative error of $0.36$%, stable across three decades**; the linear part is off by $0.11$%, and the truncation triples the discrepancy, as one expects of a nonlinear functional. This is five times smaller than the $1.8$% distortion of the depth law from which the weight is computed, and it is the same phenomenon as [P4, Prop 1]: soft weights transfer, sharp indicators do not, and $OO$ is a sharp condition while $w$ is a soft one.

**What this does and does not settle.** A weighted-sieve argument needs the *sign* of the truncated sum, not its value to four figures; an error of a third of a percent cannot change a sign. **So the computational side of the weight is not the obstruction, by a wide margin — and that is now a measured statement rather than an impression.** What is missing is not a better computation but a *proof*: a rigorous upper bound for $\bigl|\sum_{\text{window}}\max(0,w) - \sum_{\text{cycle}}\max(0,w)\bigr|$, valid for all $X$ rather than observed over three decades. That is the distribution of a weighted $\Omega$ in a short interval, and it is the external ingredient of [P11, §2.1] in its most concrete form the present work can give it.

**A sharper localisation of what is missing, obtained inside the framework.** The bound above ($s = 1.500$ for $k=3$) describes the sieve at the depth that makes survivors $P_3$ directly. One may instead sieve *less* deeply and let the almost-prime bound come from the size of the window. Write $Y = \sqrt{n+1}$ and sieve $(n^2,(n+1)^2)$ only to depth $Y/2$. Every prime factor of a survivor then exceeds $Y/2$ while the survivor itself is below $Y^4$, and $(Y/2)^5 \gt  Y^4$ as soon as $Y \gt  32$; hence

$$\Omega(x) \le 4 \quad\text{for every survivor, once } Y \gt  32,$$

so the *only* obstruction to $\Omega \le 3$ in the window is a survivor with exactly four prime factors. Such a survivor is severely constrained. Writing $x = pqrs$ with $p \le q \le r \le s$:

- **the fourth factor is forced.** Given $p,q,r$, the admissible $s$ lies in a window of width $(2n+1)/pqr \lt  2Y^2/(Y/2)^3 = 16/Y$, which is below $1$ once $Y \gt  16$: there is at most one candidate;
- **the first two are confined to about four positions.** Given $r,s$, the product $pq$ lies in a window of width $(2n+1)/rs \lt  2Y^2/(Y/2)^2 = 8$;
- **the factorisation always straddles $n$:** $pq \le n \lt  rs$ in every case examined ($78$ of $78$ at $Y = 29, 53, 101, 199, 293, 401$).

| $Y$ | $29$ | $53$ | $101$ | $199$ | $293$ | $401$ |
|--------------------------------------|------|------|------|------|------|------|
| survivors | $321$ | $922$ | $2{,}840$ | $9{,}535$ | $19{,}093$ | $33{,}379$ |
| with $\Omega = 4$ | $1$ | $3$ | $6$ | $15$ | $25$ | $28$ |
| fraction with $\Omega \le 3$ | $0.99688$ | $0.99675$ | $0.99789$ | $0.99843$ | $0.99869$ | $\mathbf{0.99916}$ |
| bound $16/Y$ (widest $s$-window) | $0.552$ | $0.302$ | $0.158$ | $0.080$ | $0.055$ | $0.040$ |
| widest $s$-window measured | $0.245$ | $0.202$ | $0.083$ | $0.040$ | $0.036$ | $0.023$ |

**And this is what makes the localisation informative rather than encouraging.** Since the exceptional set is so rigidly determined, it is natural to look for an injection sending each $\Omega = 4$ survivor to a nearby $\Omega \le 3$ one; four constructions were tried (sliding the large half, reflection in the window, replacing the least factor by a neighbouring prime, and perturbing the difference-of-squares representation), and the best succeeded on $12$ of $61$ exceptional survivors — none is close to the required $100$%. The measurement above explains why an injection was the wrong instrument: **the exceptional set does not appear to be the difficulty.** At $Y = 401$ it is $0.08$% of the survivors and falling, so essentially the entire content of the statement is a positive *lower bound* on the number of survivors of sieving to depth $Y/2$ in a window of length $2n+1$. That is a dimension-one sieve question with sieve variable

$$s  =  \frac{\log(2Y^2)}{\log(Y/2)}  \longrightarrow  2 ,$$

i.e. the critical point once more. **The reduction is genuine and sharp — it removes every degree of freedom but one — and the one it leaves is exactly the lower bound the framework cannot supply, at exactly the value of $s$ at which it never can.** This is §2.1's pattern in its most compressed form: the framework can localise the difficulty to a set of density $10^{-3}$ and still not cross it.

### 2.6 The correlation of the survivor count, and the order of its sum

**The variance of the survivor count, and where that question already stands.** The measurements above concern the mean; one may also ask for the second moment of $B(a)$, the number of cells of $(a^2,(a+2)^2)$ surviving all lines $p \le a/2$. Expanding the square introduces the correlation of the survivor indicator at cell-distance $h$, and **that correlation is already transported exactly by [P3, Thm 4]**; nothing new is needed here beyond a change of coordinates, which we record because the resulting form is the one the present section uses.

Paper 3 indexes gap-$2$ pairs by $x$, so that consecutive indices differ by $2$ in the integer, and obtains the ladder $K_q(h_{\mathrm{II}}) = q-2, q-3, q-4$ according as $h_{\mathrm{II}} \equiv 0$, $\pm1$, or otherwise modulo $q$. Cells are spaced $6$ apart, so a cell-distance $h$ is $h_{\mathrm{II}} = 3h$; substituting, $h_{\mathrm{II}} \equiv 0$ becomes $p \mid h$ for $p\gt 3$, and $h_{\mathrm{II}} \equiv \pm1$ becomes $3h \equiv \pm1$, i.e. $p \mid 9h^2-1$. Writing $\nu_p(h) = p - K_p$ for the number of residues the pair of cells forbids:

$$\nu_p(h)  =  \begin{cases} 2, & p \mid h,\cr  3, & p \mid 9h^2-1,\cr  4, & \text{otherwise,}\end{cases}$$

the three cases being mutually exclusive, since $p \mid h$ forces $3h \equiv 0$. (Directly: with $c_p \equiv 6^{-1}$, the forbidden residues for $m$ are $\pm c_p$ and $-h\pm c_p$, which coincide in pairs under exactly those two conditions. Checked against a direct count with no mismatch for all $p\lt 200$, $h\lt 300$.) **[P3, §6.3] already names the resulting product as the singular series of the Hardy--Littlewood $k$-tuple conjecture, "suitably normalised"; what is added below is the normalising constant, the exact mean, and the order of the error.** The series is

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
|------------|------|------|------|------|------|
| $\rho_1$ | $0.0344$ | $0.0213$ | $0.0145$ | $0.0079$ | $0$ |
| model $\mathrm{Var}/\mathbb E$ | $0.616$ | $0.674$ | $0.708$ | $0.747$ | $\mathbf{0.836}$ |
| measured | $0.685$ | $0.702$ | — | — | — |

A direct evaluation at $a = 100001$ from the exact truncated series ($C = 66{,}668$, $z = 50{,}000$, $\rho_1 = 2.13\times10^{-2}$, $\sum_{h\ne0} = -13.95$) gives $0.681$ against the measured $0.702$, a $3$% agreement with no free parameter. **The negative sign is the substance: the repulsion encoded in $\nu_p$ is what makes the count sub-Poisson.** The model runs a few percent low at these sizes, and predicts a slow rise of the dispersion toward $0.836$; the two available measurements do rise, $0.685$ at $a\sim10^4$ to $0.702$ at $a\sim10^5$, against a predicted rise of $0.616$ to $0.674$. That the increments agree better than the levels is consistent with a constant offset from the Buchstab correction, which the independence model omits; we have not isolated it, and the rise itself remains a prediction rather than a confirmed law.

**Why this is a description and not a route.** It is natural to hope that a second-moment bound of the shape $\sum_{A\lt a\le2A}(B(a)-\mu(a))^2 \ll \sum_{A\lt a\le2A}\mu(a)$ would give $B(a)\gt 0$ for almost all $a$, which is far weaker than a large-deviation estimate. But that conclusion is already known, in a much stronger form and by different means. Bazzanella [1] proves **unconditionally** that all intervals $[n^2,(n+1)^2]\subset[3,N]$ with at most $O(N^{1/4+\varepsilon})$ exceptions contain the *expected number of primes* — not merely a survivor of the small lines — with $O(f(N)\log^2 N)$ exceptions on the Riemann hypothesis, $O(N^{\varepsilon})$ under the Lindelöf or Density hypotheses [2], and none at all under a strong form of Montgomery's conjecture. The mechanism is zero-density estimates for $\zeta$ together with a fourth-power mean of $\psi$ in short intervals; the bridge to square windows is the observation that consecutive square windows are spaced further apart than the block of exceptions forced around any one of them, so their exceptional blocks are disjoint [2, Lem. 2.2]. **We record the local law above as a description of the dispersion, therefore, and not as the first step of a route: the almost-all statement it was reaching for is settled, more strongly, by analytic methods this framework does not contain.**

**A methodological caution that cost two false readings here.** The subtracted term $W(C) e_k(\lbrace \lambda_p\rbrace )$ is of size $C$, so an unclosed tail in the expectation is amplified by $C$: two computations differing only in the prime bound used for $G$ and $e_k$ disagreed by $0.1$ at $C = 1.6\times10^6$, an amount larger than several of the effects under discussion, and the disagreement was traced exactly to $4/(P\log P)$ summed over the missing primes. Any reproduction must close that tail analytically or fix the bound; the accompanying script does the former.

### 2.7 The narrowest form of the requirement, and why it is still the wall

**The narrowest the requirement gets, and what that shows.** [P6, §2.2] reduces a twin in a sector to a single open cell avoiding six named positions. Two further facts sharpen that as far as the construction can. First, the lines $5$ and $7$ alone cut the six to three, and no further small line lowers it — a larger line can pick a phase striking none of the six, and the Chinese remainder theorem combines that freely with the phase of $5$ and $7$ that leaves three. Second, three open positions occur **only** when $(M+2,M+4)$ is itself a twin [P6, Cor. 1], so under the negation the count is at most two. And in five residue classes,
$$M \equiv 3,\ 51,\ 141,\ 153,\ 201 \pmod{210},$$
those two lines close all six, so there **every** open cell is a twin: the requirement becomes the bare $C_M \ge 1$.

That is the weakest *numerical* requirement the twin statement takes anywhere in this work — condition (2.3) of [P6, §2.2] is weaker still, but it asks for no count at all — and three measurements say the reduction is not paid for elsewhere. Over the $713$ such sectors below $M = 30{,}000$ there are $444{,}958$ open cells and **not one fails to be a twin**, against $155$ non-twin survivors in the $428$ ordinary sectors below $M = 3000$ alone. The survivor count itself is not depressed: the density in these five classes against all others is $0.934$ up to $M = 4000$, $0.997$ up to $12000$ and $1.000$ up to $30000$ — **fixing the phases of $5$ and $7$ changes which cells die, not how many.**

That last sentence names a standard device rather than an observation of ours. Passing to a residue class modulo a primorial to remove the local bias at the small primes, at no asymptotic cost, is the **$W$-trick**, and the modulus here is $210 = 2\cdot3\cdot5\cdot7$. In the analytic literature the compensating factor $\phi(W)/W$ is inserted by hand and the absence of cost is known; here it is not assumed but measured, and the three ratios above are that measurement. The device is standard — see its use in Tao and Teräväinen [20], and in the quantitative polynomial Szemerédi work of Krause, Mousavi, Tao and Teräväinen [13] — and we record the identification because the same thing has happened repeatedly here: an object built from inside the construction turns out to have a name. And $C_M$ is nowhere near zero: its minimum over those sectors is $10$ below $M = 3000$ and $520$ for $M$ near $2\times10^4$, against $497$ in the ordinary classes.

**That calculation has been carried out, and on our reading it closes the local route.** Coupling consecutive sectors and admitting the lines $11,13,17$ bounds the exception budget over a full $210$-window by $31$ under the twinless hypothesis, and that ceiling cannot be lowered by any finite set of lines: of the $28$ maximal configurations, $27$ are killed by a fixed prime divisor once the quadratic partner conditions are included, and the survivor is admissible at every prime, so the residues can be chosen simultaneously against any finite list — the setting of Schinzel's Hypothesis H [19]. The order in which the lines are born adds nothing either. The calculation, with its verifications, is [P6, §2.3]; here we record only what it means.

**The upper-bound side of the argument is therefore finished, and the whole difficulty sits in the other half.** One does not need to kill the escapee: if $\sum_{i} C_{M_i} \ge 32$ can be established, the thirty-second survivor has no room inside $E$ and is a twin. Measured, that requirement is met with enormous room — $B_k := \sum_i C_{M_i}$ is $1{,}337$ at $k=1$, $29{,}579$ at $k=100$ and $196{,}948$ at $k=1000$, with $B_k\log^2 M_0/M_0$ flat at about $139$ from $k = 20$ onward, and the minimum over a band of sixty consecutive $k$ never below $1{,}337$. **The requirement is exceeded by a factor of six thousand and rising, and remains unproved.**

**And lengthening the window does not help.** Sieving an interval of length $H$ to depth $z$ has $s = \log H/\log z$; for one sector $H \asymp 12M_0$ and for the full window $H \asymp 420M_0$, both against $z \asymp M_0$, so $s \to 1$ in each and the gain is $\Delta s = \log 35/\log M_0$ — $0.257$ at $M_0 = 10^6$, $0.129$ at $10^{12}$, vanishing. Against the two-dimensional sifting limit $\beta_2 = 4.2664$ this closes under seven per cent of the gap, and less as $M_0$ grows: **a constant multiple of the length buys nothing asymptotically, only a power of $M_0$ would.** The reorganisation is therefore a clarification and not a reduction — but it is a real one, because it closes one of the two branches permanently and by proof.

**So the requirement is now one survivor, in one arithmetic progression, for infinitely many $M$ — and it is still the same wall.** The quantity to be bounded below is the number of cells of an interval of length $\asymp 2M$ surviving every line $p \le M$: a two-dimensional sieve at $u = 2$, where the sifting limit is $\beta_2 = 4.2664$ and no positive lower bound is available. Lowering the demand from $C_M \ge 7$ to $C_M \ge 3$ to $C_M \ge 1$ does not approach that bound, because the sieve supplies none of the three. **The reduction is worth recording precisely because it is so sharp and still does not bind: it isolates what the framework can do — fix the arithmetic of the exceptional positions completely — from what it cannot, which is to produce a single guaranteed survivor.**

**A remark from the same literature, which corroborates §2.** Campbell records that reaching $\Omega \le 2$ between squares appears to lie beyond his framework precisely because it uses only Type I information, and that this is so however large $n$ is taken [5]; Chen's asymptotic $k = 2$ [6] comes from a different route. So what remains on this side is the numerical optimisation itself, and at $k = 2$ even that is not enough. The deficit named *bilinearity* in [P11, §2.1] is therefore the one the specialists name as well — the fourth of the four, met in a test problem where the first three do not bite.

### 2.8 A third test case: a shared cofactor on two lines

Look at the cofactors rather than the numbers. Two lines $L_p$ and $L_q$ **share** the cofactor $a$ when $pa$ and $qa$ both lie in one window between consecutive odd squares. Only one condition on $a$ is needed, and it is the natural one: that both strikes come after both lines have begun.

> **Theorem 1.** Let $p \lt  q$ be odd primes and let $a \ge q$ satisfy $k^2 \lt  pa \lt  qa \lt  (k+2)^2$ for some odd $k$. Then $q = p+2$. (The hypothesis $a \ge q$ is not a restriction: it holds automatically whenever $q \le k$, and is what confines the sharing to the lines above $k/2$ — see below.)

*Proof.* Both $\sqrt{pa}$ and $\sqrt{qa}$ lie in $(k, k+2)$, so their difference is less than $2$. That difference is
$$\sqrt{qa}-\sqrt{pa} \ = \ \frac{(q-p)\sqrt{a}}{\sqrt q + \sqrt p} \ \gt \ \frac{(q-p)\sqrt q}{2\sqrt q} \ = \ \frac{q-p}{2},$$
using $a \ge q$ for the numerator and $p \lt  q$ for the denominator. Hence $q - p \lt  4$, and the difference of two odd primes is even, so $q-p = 2$. $\blacksquare$

Nothing here asks $a$ to be prime, and nothing asks the strikes to be **primitive** — that is, for $p$ to be the least prime factor of $pa$. An inherited strike is an equally good witness: at $k = 31$,
$$31^2 \ \lt \ 29 \cdot 35 = 1015 \ \lt \ 31 \cdot 35 = 1085 \ \lt \ 33^2,$$
and the cofactor $35$ is composite, both strikes are owned by smaller lines, and the pair $(29,31)$ is still exhibited. The distinction between primitive and inherited matters for ownership and for coverage counts, as in [P9, §2.2]; it is not needed here.

*Verification.* Over all windows with odd $k \lt  1000$: $5{,}593$ sharing pairs with $a \ge q$, of which $4{,}764$ have a composite cofactor, and **not one** has $q - p \ne 2$.

**The converse is immediate, with an explicit cofactor.** For any twin $(p, p+2)$ take $a = p+6$. Then
$$p(p+6) = (p+2)^2 + 2p - 4, \qquad (p+2)(p+6) = (p+4)^2 - 4,$$
so both strikes lie in $\big((p+2)^2, (p+4)^2\big)$ for every $p \gt  2$, whatever the factorisation of $p+6$. No third prime is required, and no congruence condition: every twin shares a cofactor, always, in a window whose root is its own upper member plus two.

> **Theorem 2.** Infinitely many twins exist if and only if two odd primes share a cofactor, in the sense of Theorem 1, in windows of unbounded height.

*The horizon.* For a fixed twin the sharing windows are finitely many. The constraints $k^2 \lt  pa$ and $(p+2)a \lt  (k+2)^2$ require $k^2/p \lt  (k+2)^2/(p+2)$, that is $(p+2)/p \lt  (1+2/k)^2$, which gives $k \lt  2p$ asymptotically. Measured: the largest window root is $1.824p$ at $p = 17$, $1.901p$ at $p=71$ and $1.944p$ at $p = 269$, approaching the bound from below.

### 2.9 The geometry of sharing: where it sits, and how it is forced

In the window $W_k = (k^2,(k+2)^2)$ the line $L_p$ has the cofactor set $C_p = \lbrace a \text{ odd} : k^2 \lt  pa \lt  (k+2)^2 \rbrace$, an interval of length $(4k+4)/p$. Two such sets meet only if $q/p \lt  (1+2/k)^2$, which for $q = p+2$ is $p \gt  k^2/(2k+2)$: **all sharing lives in the upper half $k/2 \lt  p \lt  q \le k$**, and no line below $k/2$ takes part. There the hypothesis $a \ge q$ of Theorem 1 is automatic, since $a \gt  k^2/q \gt  k \ge q$, so it may be dropped from the statement. The overlap of $C_p$ and $C_{p+2}$ has length
$$\frac{(4k+4)p - 2k^2}{p(p+2)},$$
a function of $p/k$ alone: $0.17$ at $p = 0.51k$, $1.12$ at $0.6k$, $1.88$ at $0.8k$ and exactly $2$ at $p = k$. Since the sets are intervals and the overlap never exceeds $2$, **two lines share at most one odd cofactor, and it is the first cofactor of the smaller line and the last of the larger.** In $(19^2, 21^2)$: line $11$ has $33, 35, 37, 39$, line $13$ has $29, 31, 33$, line $17$ has $23, 25$, line $19$ has $21, 23$ — and the two sharings are $33$ and $23$, each at the ends. Checked over all $2{,}604{,}125$ pairs of odd lines in windows with odd root below $501$: $12{,}019$ sharings, every one of them a single cofactor equal to the first of the smaller and the last of the larger, and every one with $k/2 \lt  p \lt  q \le k$.

The sharing can also be produced outright. Write $k = p + 2t$ with $t \ge 1$ and take
$$a = p + 4t + 2 . \qquad\text{Then}\qquad pa = k^2 + 2p - 4t^2, \qquad (p+2)a = (k+2)^2 - 4t^2,$$
so both strikes lie in $W_k$ **whenever $2t^2 \lt  p$** — that is, whenever the two lines are close enough to the root. Verified on $44{,}551$ instances of the identity and $3{,}168$ of the inclusion, without exception. So among adjacent odd lines near the root, sharing is not a tendency but a construction; measured, $92.5$% of all adjacent odd pairs above $k/2$ share, at $k = 10^3, 10^4, 10^5$ alike.

**The cofactor lists move by a law, and inside the candidate strip the law is exact.** The list $F_p(k) = \lbrace a \text{ odd} : k^2 \lt  pa \lt  (k+2)^2\rbrace$ is the strike set of $L_p$ read on the cofactor axis rather than the cell axis, where [P2, Cor 4] presents it as two interleaved progressions of step $p$; on this axis it is a single run. For a candidate line that run has $h_p(k)$ terms with $2 \le h_p \le 4$ — measured over $40{,}191$ lines, never broken and never outside that range, with $h_p = 2, 3, 4$ occurring $15{,}414$, $18{,}707$ and $6{,}070$ times. Writing $A_p$ and $B_p$ for its first and last entries, $p \lt  q$ gives $A_p \gt  A_q$ and $B_p \gt  B_q$: the runs slide left as the line grows. Since the overlap never exceeds one entry, sharing is an equality of endpoints,
$$F_p(k) \cap F_q(k) \ne \varnothing \iff A_p = B_q \iff A_p - A_q = 2\big(h_q - 1\big),$$
verified on all $2{,}666{,}595$ pairs of candidate lines with $k \lt  801$.

Passing to the next window, the line resumes where it stopped, except that a strike landing exactly on the shared boundary belongs to neither open window and is skipped:
$$A_p(k+2) = B_p(k) + 2 + 2\cdot\mathbf{1}_{\ p \ \mid\  (k+2)^2} = A_p(k) + 2h_p(k) + 2\cdot\mathbf{1}_{\ p \ \mid\  (k+2)^2},$$
exact on all $79{,}790$ line-window pairs tested, of which $1{,}398$ trigger the indicator. **And the indicator never fires on a prime line of the strip.** If $p$ is prime and $p \mid (k+2)^2$ then $p \mid k+2$; as $k+2 \gt  p$ and both are odd, $k+2 \ge 3p$, while $p \gt  k/2$ gives $3p \gt  3k/2 \gt  k+2$ for $k \ge 5$ — a contradiction. Checked: of the $77{,}427$ prime lines in the strip with $k \lt  3001$, none triggers it, and of the $128$ occurrences inside the strip below $k = 801$ every one is on a composite line.

So within the system of prime candidate lines the movement is an exact equality: each line advances by $2h_p$, which is $4$, $6$ or $8$, and for two lines the difference of the run-starts obeys
$$D_{p,q}(k+2) = D_{p,q}(k) + 2\big(h_p(k) - h_q(k)\big),$$
changing by $0$ or $\pm 2$ or $\pm 4$ at each step, with sharing occurring exactly when $D_{p,q}$ reaches $2(h_q-1)$. This is the sharpest description of the motion the framework produces, and it is worth noting what it does and does not separate: the boundary indicator is the first quantity in this work that distinguishes prime lines from composite ones outright — it fires only on composite lines. But it separates them in the wrong direction. It says which lines can break the movement law, not which lines can share; the sharing condition itself remains a statement about the runs, and the runs do not know whether their index is prime.

**The sharing condition in closed form, and why it is blind.** The quadratic walk turns the whole criterion into one inequality. In the window $k = p+2s$ with $s \ge 1$, the sharing of the lines $p$ and $p+2$ is
$$\left\lfloor \frac{2s^2}{p} \right\rfloor = \left\lfloor \frac{2s^2}{p+2} \right\rfloor \iff \big(2s^2 \bmod p\big) \ \ge\ \frac{4s^2}{p+2},$$
the second form obtained by writing $2s^2 = jp + r$ and noting that the two floors differ exactly when $r \lt  2j$. **The index is $s$ and not $s+1$**, and the window $s = 0$ carries no sharing at all: there $F_p = \lbrace p+2, p+4\rbrace$ while the cofactors of $p+2$ all lie below it. At $s = 1$ the residue is $2$ and the threshold below $1$, so sharing occurs in the first window in which it can, $\big((p+2)^2,(p+4)^2\big)$, with cofactor $p+6$ — the witness above, recovered independently.

**One boundary case separates the floor test from the sharing itself, and it is worth stating because it is where the primality enters.** The floor equality is blind to the upper endpoint of the open window: it counts a candidate cofactor $a$ with $(p+2)a = (k+2)^2$, which the window excludes. That happens exactly when $p+2$ divides $(k+2)^2$, and since $k+2 \equiv 2s \pmod{p+2}$ this is $(p+2) \mid 4s^2$ — impossible for $p+2$ prime with $s \le (p-1)/2$, and the only way the two can differ. Hence
$$\text{floors equal} \iff \text{sharing}, \qquad\text{for every } p \text{ with } p+2 \text{ prime},$$
while for composite $p+2$ the floor set can be strictly larger. Over all odd $p \lt  400$ and every $s$ there are $19{,}899$ pairs and exactly $93$ such cases, every one of them at composite $p+2$, every one of them a floor equality with no sharing. Regenerated by `code/verify_sharing_index.py`. *(So the set $S_p$ of §2.11 is defined by the floors, and is the set of sharing windows exactly in the case the criterion is applied to.)*

This closed form explains the measured rate. If $2s^2 \bmod p$ is equidistributed then sharing at $s$ has probability $1 - 4s^2/p^2$, and averaging over $s \le p/2$ gives $1 - \tfrac13 = \tfrac23$; measured, the rate is $0.6654$ over pairs of prime lines and $0.6662$ over all other adjacent odd pairs. **It also explains why the criterion cannot see primality: it depends on the distribution of $2s^2 \bmod p$ and not on its structure, and the distribution is the same for prime and composite $p$.**

That the structure differs is easy to state. The map $s \mapsto s^2 \bmod p$ is injective on the interval $[1, (p-1)/2]$ **if and only if $p$ is prime** — a collision $s_1^2 \equiv s_2^2$ needs $p \mid (s_2-s_1)(s_2+s_1)$ with both factors below $p$ — with the single exception $p = 9$, where the smallest collision falls outside the range. Checked: injective for all $76$ odd primes below $400$ and for exactly one of the $122$ odd composites. But the deviation of the sharing count from its mean does not detect it: measured as $|{\cdot}|/\sqrt{p}$ over $p \in [8000, 20000)$, it is $0.270$ for primes, $0.260$ for composites with least factor at least $11$, $0.222$ for multiples of $3$ and $0.203$ for multiples of $5$ — the same order throughout, and *smaller* for the composites with small factors, not larger. The sharing count is a sum over single values of $s$, the threshold moves with $s$, and the sum averages away any local structure in the residues.

**And that is exactly where the primality is missing.** Take $k = 23$. The cofactor lists are $13 : 41,43,45,47$; $17 : 33,35$; $19 : 29,31$; $21 : 27,29$; $23 : 25,27$. Two sharings are forced by the construction — lines $19, 21$ at the cofactor $29$, and lines $21, 23$ at the cofactor $27$ — and all four strikes lie in $(529, 625)$. But the shared line is $21$, which is composite. The two prime lines present, $19$ and $23$, use *different* cofactors in these two sharings, and the composite line between them does not merge them. Of the $25{,}001$ adjacent odd pairs above $k/2$ at $k = 10^5$, $23{,}069$ share and only $519$ consist of two primes — a ratio of $2.1$%, falling like $1/\log^2 k$.

### 2.10 Why the sharing equivalence closes the route

The proof of Theorem 1 used the primality of $p$ and $q$ at exactly one point — to say that $q-p$ is even — and used nothing else about them. Everything geometric in it holds for any two odd numbers two apart:
$$23^2 \ \lt \ 21 \cdot 27 = 567 \ \lt \ 23 \cdot 27 = 621 \ \lt \ 25^2,$$
and $21$ is not prime. So the square law forces a shared cofactor between **adjacent odd numbers**, and what is missing is precisely that infinitely many adjacent odd pairs are both prime — the conjecture itself. To prove "sharing occurs at unbounded height" one must exhibit the two primes, since sharing between primes is defined by their primality and has no formulation that avoids it.

The contrast with the sector criterion [P6, §2.2] is a matter of degree rather than of kind, and it is worth stating precisely. Primality is itself a survival statement — $N \lt  x$ is prime exactly when it survives every line below $\sqrt{N}$ — so no reformulation moves the problem out of the sieve's language, and none of the criteria in this work ever did. What changes between them is one number: the ratio $s$ of the logarithm of the range to the logarithm of the sifting depth, at which the existence of a survivor is being asked for. A dimension-two lower bound needs $s \gt  \beta_2 = 4.2664$; the sector criterion [P6, §2.2] asks at $s \approx 1$, and the sharing criterion here at $s \approx 2$, since it needs a survivor to depth $\sqrt{N}$ in a range of length $N$. Below the threshold the sieve returns not a small bound but zero, so neither is available. **What the sieve cannot do is not recognise a prime — sifting to $\sqrt{N}$ recognises it exactly — but prove that a survivor exists at these depths.** An equivalence between two criteria is useful only when it raises $s$; this one raises it from $1$ to $2$, which is the largest gain recorded in this work and still short of the threshold by more than it gained.

**This is the sharpest form the obstruction takes in this work.** A criterion built from a one-parameter sum over $n$ sees the distribution of $2n^2 \bmod p$ and nothing else, and that distribution is prime-blind; what distinguishes a prime modulus is the absence of *collisions*, a statement about **pairs** $(n_1, n_2)$. Every criterion in this paper is a one-parameter sum, which is why each of them has turned out to be equivalent to the conjecture rather than weaker than it. The requirement that the decisive input be bilinear — a statement about pairs — is the **Bilinearity** deficit of [P11, §2.1] below, reached here from the local coordinates of the framework rather than from the sieve literature.


### 2.11 A fourth test case: collisions inside the sharing set

The sharing criterion of §2.8 can be pushed one step further, and the step is worth recording because it produces a criterion that *reads* the primality of $p+2$ instead of assuming it — and then fails for a reason that is sharper than any recorded above.

Fix an odd $p$ and write $N = p+2$. Numbering the windows by $s$, so that the root is $m = p+2s$, the sharing condition of §2.9 becomes a comparison of two floors, and the set is
$$S_p \ = \ \Big\lbrace 1 \le s \le \tfrac{p-1}{2} \ : \ \Big\lfloor \tfrac{2s^2}{p} \Big\rfloor = \Big\lfloor \tfrac{2s^2}{N} \Big\rfloor \Big\rbrace \ = \ \Big\lbrace s : (2s^2 \bmod p) \ge 2\big\lfloor \tfrac{2s^2}{p} \big\rfloor \Big\rbrace ,$$
the set of sharing windows exactly when $N$ is prime, by the boundary case of §2.9.
Its size carries no information — the density is near $2/3$ whether $N$ is prime or not. What does carry information is a **collision**: a pair $u \lt  v$ in $S_p$ with $u^2 \equiv v^2 \pmod N$. Write $E_p$ for the number of such pairs. *(The letters $u, v$ here are two members of $S_p$, and are unrelated to the composite rates $u, v$ of [P9, §2.3].)*

> **Theorem 3.** For odd $p \gt  7$: $E_p = 0$ if and only if $p+2$ is prime.

One direction is immediate — if $N$ is prime it divides neither $v-u$ nor $v+u$, both being positive and below $N$. The other direction is where the work sits. That an odd composite $N = ab$ admits *some* pair $u = (b-a)/2$, $v = (b+a)/2$ with $v^2 - u^2 = N$ is the classical difference-of-squares criterion, in use since Fermat; **the content here is that the witness can always be taken inside $S_p$.** The argument runs in five steps: (i) if $v^2 - u^2 = \mu N$ and $v \in S_p$ then $u \in S_p$, by subtracting $2\mu N$ from the double inequality that defines membership, so only the larger member must be placed; (ii) with $k = \lfloor b/2a \rfloor$, $c = 2a(k+1)-b$ and $\Delta = bc - a^2$ one has the identity $2v^2 = (k+2)N - \Delta/2$, and the witness fails exactly when $0 \lt  \Delta \le 4k+8$; (iii) that forces $b \gt  3a$, since $a \lt  b \le 3a$ gives $3N - 2v^2 = (3a^2 - (b-2a)^2)/2 \ge a^2 \gt  6$ and both floors equal $2$; (iv) the split $(3a, b)$ of $3N$ then works, by $2v_3^2 = (k+4)N + R$ with $R = 4a^2 - \Delta/2$ and the bounds $0 \lt  R \lt  N - 2(k+5)$; (v) for $N = q^2$ the pair $(q, 2q)$ serves, with $v^2-u^2 = 3N$. Each step was checked exhaustively: the identity on $16{,}793$ factorisations, step (iii) on every factorisation below $p = 2\cdot10^5$, step (iv) on the $32$ failing factorisations below $3\cdot10^6$, all without exception.

### 2.12 Where the collision must sit, and what a narrow slice sees

The position of the witness is confined, and the confinement is exact.

> **Theorem 4.** Let $p \gt  121$ be odd with $p+2$ composite. Then some collision in $S_p$ has $\sqrt{p+2} \lt  v \le (p+11)/6$.

The upper bound is $6v \le N+9 \iff (a-3)(b-3) \ge 0$, which holds for every factorisation with $a \ge 3$; the rescue witness stays inside because $6v_3 \le N+9 \iff (a-3)b \ge 9(a-1)$, which follows from $b \gt  3a$ for $a \ge 7$, from $b \ge 25$ for $a=5$, and for $a=3$ from the fact that the ordinary witness then fails only at $p = 31, 49, 67, 85, 103, 121$. The lower bound is forced by $v^2 - u^2 \ge N$. **The hypothesis is that $p$ be odd, not prime**: among odd $p \gt  7$ the only exceptions are $23, 31, 47, 49, 67, 85, 119, 121$, of which the primes are $23, 31, 47, 67$. Reading the bound through $v-u = a$ and $v+u = b$ shows what the belt is: a balanced factorisation puts the collision near $\sqrt N$, a lopsided one near $N/6$, and the belt is the image of all factorisations of $N$ on the axis of window positions. Only $v$ is confined — at $p = 999{,}917 = 991\cdot1009 - 2$ the witness is $u = 9$, $v = 1000$.

**And a slice at the top of the belt collapses to a divisibility test.**

> **Theorem 5.** Let $p \gt  121$ and $H = (N+9)/6$. Inside the slice $H - L \le u \lt  v \le H$ with $3 \le L \lt  \sqrt{N/3}$, a collision exists if and only if $3 \mid N$, and then it is the single pair $u = (N-9)/6$, $v = (N+9)/6$.

This follows from the identity
$$N\ (v-u-3k) \ = \ 3\Big[ \big(\tfrac{N}{6}-u\big)^2 - \big(\tfrac{N}{6}-v\big)^2 \Big],$$
whose right side has modulus below $N$ inside the slice while the left is a multiple of $N$; hence $v-u = 3k$, then $u+v = N/3$, so $3 \mid N$, and $v \le N/6 + 3/2$ forces $k=1$. Verified over the primes in $(121, 6\cdot10^4)$: no collision at all when $3 \nmid N$, and exactly one in each of the $3{,}001$ cases with $3 \mid N$.

**Collisions enter the slice in numbered stages, and each stage has an explicit threshold.** Keep $H = (N+9)/6$ and the slice $H - L \le u \lt  v \le H$, and for a collision write $d = v-u$ and $s = u+v$, so that $v^2-u^2 = kN$ becomes $ds = kN$. Since $N$ is odd, $d$ and $k$ have the same parity, so $d - 3k$ is even; put $d - 3k = 2t$. Then
$$2tN \ = \ d\ (N - 3s),$$
and the lower edge of the slice gives $s \ge 2(H-L) + d$, whence $2tN \le 3d(2L-3-d)$. The right-hand side is $3[(L-\tfrac32)^2 - (d-L+\tfrac32)^2]$ by an identity, so the bound holds for every $d$ with no further hypothesis:

> **Theorem 6.** For $p \gt  121$ and $L \ge 3$, every collision inside the slice satisfies
> $\displaystyle 0 \ \le \ t \ \le \ \Big\lfloor \frac{3\ (L - \tfrac32)^2}{2N} \Big\rfloor, \qquad t = \tfrac{1}{2}(d - 3k).$
> More generally, for a slice with top $H_0$ the bound reads $t \le \lfloor (N - 6H_0 + 6L)^2/(24N) \rfloor$.

So the stages open one at a time as the slice widens: $t = 0$ needs only $L \ge 3$ and is the pair of Theorem 5; $t = 1$ needs $L \ge \tfrac32 + \sqrt{2N/3}$; $t = 2$ needs $L \ge \tfrac32 + \sqrt{4N/3}$. **This widens Theorem 5 by a factor $\sqrt2$:**
$$3 \le L \ \lt \ \tfrac32 + \sqrt{2N/3} \quad\Longrightarrow\quad \text{the slice detects divisibility by } 3 \text{ and nothing else.}$$
The parity law and the identity were checked on $276{,}412$ collisions without exception, and the bound on every slice tested once the top of the slice and the reference point use the same $H$ — the exact rational $(p+11)/6$, not its integer part, a distinction that matters at small $p$ and produced spurious violations before it was fixed. The census bears out the staging: in the last $2$% of the belt below $p = 1.2\cdot10^5$ there are $5{,}560$ collisions at $t = 0$, $1{,}027$ at $t = 1$, and none above.

The earlier counterexample is now explained rather than merely recorded. At $N = 64{,}375$ the pair $u = 10{,}522$, $v = 10{,}728$ has $d = 206$, $k = 68$, hence $t = 1$; the narrowest slice containing it has $L = H - u = 208.6667$, while the stage-one threshold is $\tfrac32 + \sqrt{2N/3} = 208.6634$. It clears the threshold by $0.0033$.

*What the staging does not give.* A slice narrow enough to sit below the stage-one threshold sees only the divisibility by $3$; a vanishing count there says nothing about the primality of $p+2$, since the witness for a different factor lives in the part that was cut away. The staging law explains the mechanism of every relaxation tried above — it says exactly which factors can reach which depth — without turning any of them into a criterion.

### 2.13 What a first moment on the collision count would need

$E_p$ is integer-valued and vanishes exactly on twins, so $E_p \ge \mathbf 1_{\lbrace p+2 \text{ composite}\rbrace}$ pointwise, and for *any* non-negative weights $w$,
$$\sum_p w(p) E_p \ \ge\ \sum_p w(p) - \sum_{p \text{ twin}} w(p).$$
So $\sum w E \lt  \sum w$ **implies** $\sum_{\text{twin}} w \gt  0$. **That is what makes it a sufficient condition, and it is a legitimate way to force a zero**: for an integer-valued non-negative statistic, an upper bound on the mean below one produces a vanishing value, and arguments of exactly that shape are standard.

*An earlier version of this subsection read the implication as circularity and concluded that every weighted first-moment argument assumes its conclusion. That was a mistake in logic, and it is corrected here.* Proving a sufficient condition is not assuming it. What is true, and is the whole of the difficulty, is narrower: **no upper bound on $\sum w E$ is available from inside this framework**, because $E_p$ is defined from the factorisation of $p+2$, so any bound on its mean is already a statement about how often $p+2$ factors — the sieve delivers rough numbers and does not deliver that. The same applies to any statistic vanishing exactly on twins and bounded away from zero elsewhere, which Theorem 4 guarantees for $1/v$. Higher moments do not supply it either: Paley–Zygmund bounds $\mathbf P(E \gt  0)$ from *below*, and the measured value of that bound is near $0.46$ throughout.

**So this route is open and unequipped, not closed.** What would close it is an upper bound for $\sum_p w(p) E_p$ obtained independently of the twin count — and the four relaxations below say why the obvious way of getting one, widening the zero set, does not.

Relaxing the statistic so that its zero set is *wider* than the twins is the natural repair, and it was tried in four independent families — thresholding the recovered factor, restricting the distance $v-u$, cutting the top of the belt, cutting the bottom. In each, the zero set widens faster than the mean falls: at a mean near $1$ the extra family is already several times the number of twins. Two honest limits on that reading: the mean falling below $1$ is *sufficient* to force a zero, not necessary for every analytic argument; and it does not by itself produce the collapse of Theorem 5, whose proved width $\sqrt{N/3}$ is narrower than the width $\sqrt{2p/3}$ that a mean below $1$ permits. The gap between the two is real and inhabited — at $p = 64{,}373$, with $N = 625\cdot103$ not divisible by $3$, the pair $u = 10{,}522$, $v = 10{,}728$ lies in $S_p$ and in the slice, colliding with $k = 68$ and exposing the factor $103$.

What is established, then, is the complete local geography: a criterion equivalent to the primality of $p+2$, an exact belt for its witness, and an exact collapse in a narrow slice. What is absent is any relation between the belt of one prime and the belt of the next; the factorisations of $p+2$ and of the next $q+2$ are independent, and the measured record bears this out — among the primes below $10^6$ the smallest factor of $p+2$ reaches $991$, no fixed set of small lines accounts for all collisions, and there is a run of $102$ consecutive primes from $850{,}351$ every one of which has a collision.

### 2.14 Counting the witnesses, and why a count of them cannot close the gap

The collisions of §2.11 can be counted exactly rather than estimated, and the count turns out to be a re-encoding of the collisions themselves. Fix a prime $p \gt  121$ with $3 \nmid N$, write $X = N-6u$ as before, and set
$$\Delta \ = \ (N-6v)^2 + 48t, \qquad\text{so that}\qquad X^2 - \Delta \ = \ 24tp .$$

> **Theorem 7.** Within one list $S_p$, among the collisions of the belt — those with $v \le H = (N+9)/6$, which by Theorem 4 always include a witness — the value of $\Delta$ determines the collision: two such collisions with the same $\Delta$ are the same pair.

*Proof.* Subtracting the two identities gives $(X_1-X_2)(X_1+X_2) = 24p(t_1-t_2)$. The belt restriction is what puts $X_i = N-6u_i$ strictly between $0$ and $p$: $u_i \lt  v_i \le (N+9)/6$ gives $X_i \gt  N - (N+9) + 6 \gt  0$ and $u_i \ge 1$ gives $X_i \le N-6 = p-4$. Both $X_i$ are then odd and in $(0,p)$, so the difference is smaller than $p$ and the sum is an even number below $2p$; neither can be divisible by the prime $p$ unless the difference vanishes. Hence $X_1 = X_2$, so $u_1 = u_2$ and then $t_1 = t_2$; the equality of $\Delta$ then forces $(N-6v_1)^2 = (N-6v_2)^2$, so either $v_1 = v_2$ or $v_1+v_2 = N/3$, and the second is impossible when $3 \nmid N$. $\blacksquare$

Verified over the $267{,}575$ collisions of the belt on $1{,}121$ prime lines below $2\cdot10^4$: no value of $\Delta$ repeats inside any list. **So within the belt the number of collisions equals the number of distinct values of $\Delta$, and recoding each collision by a single number is not a relaxation of anything.**

*The restriction to the belt is load-bearing in the proof and is not known to be removable.* Off the belt $X$ leaves the range the proof needs: at $p = 131$ the collisions $(25,32)$ and $(44,51)$ of $S_p$ give $X = -17$ and $X = -131$, the second divisible by $p$ itself. A search to $p = 2\cdot10^4$ found no repeated $\Delta$ off the belt either, so the wider statement may well be true; what is established here is the narrower one. The prohibition of §2.13 removes shapes that would contradict the primality of $p$; it removes no valid collision at a prime line.

**A counting bound follows, and it is constructive.** Each $\Delta$ satisfies $\Delta \equiv 1 \pmod{24}$ and is never a square, so the admissible values begin $73, 97, 145, 193, 217, 241$ — the squares $1, 25, 49, 121, 169$ being excluded. Inside a slice whose first admissible position is $U = \max(1, \lceil H-L \rceil)$, every collision has $u \ge U$ and $t \ge 1$, whence
$$\Delta \ \le \ M \ = \ (N-6U)^2 - 24p ,$$
and the number of collisions is at most the number of non-square integers congruent to $1$ modulo $24$ below $M$. If $M \lt  73$ the slice is empty; if $M = 73$ there is one candidate, at $M = 97$ two. Checked against direct enumeration on $786$ slices with no case exceeding the bound. Four instances:

| $p$ | slice width $L$ | admissible $\Delta$ | collisions |
|---|---|---|---|
| $131$ | $10$ | $0$ | $0$ |
| $389$ | $18$ | $1$ | $1$ |
| $64{,}373$ | $209$ | $2$ | $1$ |
| $64{,}373$ | $210$ | $587$ | $1$ |

**And the first row is the limit of the whole approach.** At $p = 131$ the slice is provably empty, yet $N = 133 = 7 \cdot 19$ is composite: the witness is $u = 6$, $v = 13$ with $13^2 - 6^2 = 133$, both in $S_p$, and the slice begins at $U = 14$, above them. The emptiness is an artefact of where we looked.

So the requirement on any relaxation is now exact: **it must retain at least one witness for every composite $p+2$.** The counting bound does not guarantee that, and therefore cannot carry an empty slice to a twin. That is the same conclusion §2.13 reaches from the side of means and weights, here reached by construction: a bound that proves zero, and an example showing the zero can be false.

### 2.15 The pattern of the whole work

$$\boxed{ \text{Across the tested routes, the local laws are much sharper than the available summed bounds.} }$$

The routes examined here exhibit this repeatedly: the pigeonhole constraint ([P11, App. B.2.2]), the deletion budget ([P11, App. B.2.1]), the criterion $K\lt G$ ([P11, App. B.2.1.3]), the collective cancellation [P4, §4], and the covering condition for Jacobsthal (§2.4). In each case a sharp local law is followed by a summation — or, equivalently, a passage from cycle to short window — whose loss exceeds the margin available. **[P3, §5.2] isolates why with unusual clarity: making the layers disjoint removes the double-counting entirely, so the summed bound stops diverging and stays below $1$ for every depth — yet it then returns exactly $\prod(1-1/q)$. The interference was never in the intersections; it lives in the size of each layer, which already contains the product of all the layers before it.** **We therefore treat this as the recurring limitation revealed by the present tests, rather than as a theorem excluding every possible summation method.**

---

---

*The computations and much of the prose in this paper were prepared with AI assistance (ChatGPT, OpenAI; Claude, Anthropic), used for algebraic derivation, for drafting and rewriting code and text, for running the computations, and for auditing the papers against their own scripts. All statements were checked by the author, who is responsible for them; the repository README sets out the division of labour in full.*
---

## References

The companion papers of this set are cited as [P1] to [P12], and the numbered entries below are the external works. The two kinds never share a number: a bracket with a P is a companion paper, a bare number is a reference in the list below. This paper imports only the definitions and statements of the companion papers, never their proofs.

1. D. Bazzanella, *Primes between consecutive squares*, Arch. Math. (Basel) **75** (2000), no. 1, 29–34.
2. D. Bazzanella, *Some conditional results on primes between consecutive squares*, Funct. Approx. Comment. Math. **45** (2011), no. 2, 255–263.
3. M. Bordignon, D. R. Johnston and V. Starichkova, *An explicit version of Chen's theorem and the linear sieve*, Int. J. Number Theory **21** (2025), 2497–2572.
4. V. Brun, *Le crible d'Ératosthène et le théorème de Goldbach*, Skrifter utgit av Videnskapsselskapet i Kristiania I, no. 3, J. Dybwad, Kristiania, 1920.
5. P. Campbell, *On the existence of integers with at most 3 prime factors between every pair of consecutive squares*, arXiv:2603.10356 (2026).
6. J.-R. Chen, *On the distribution of almost primes in an interval*, Scientia Sinica **18** (1975), 611–627.
7. A. W. Dudek and D. R. Johnston, *Almost primes between all squares*, J. Number Theory **278** (2026), 726–745.
8. K. Ford, B. Green, S. Konyagin, J. Maynard and T. Tao, *Long gaps between primes*, J. Amer. Math. Soc. **31** (2018), 65–105.
9. H. Iwaniec, *On the error term in the linear sieve*, Acta Arith. **19** (1971), 1–30.
10. H. Iwaniec, *On the problem of Jacobsthal*, Demonstratio Math. **11** (1978), 225–231.
11. E. Jacobsthal, *Über Sequenzen ganzer Zahlen von denen keine zu $n$ teilerfremd ist*, I–III, Norske Vid. Selsk. Forh. Trondheim **33** (1960), 117–139.
12. D. R. Johnston, J. P. Sorenson, S. N. Thomas and J. E. Webster, *Primes and almost primes between cubes*, arXiv:2601.15564 (2026).
13. B. Krause, H. Mousavi, T. Tao and J. Teräväinen, *Quantitative bounds for sets lacking polynomial progressions with shifted prime difference*, arXiv:2608.19525 (2026).
14. P. Kuhn, *Neue Abschätzungen auf Grund der Viggo Brunschen Siebmethode*, Proc. 12th Scandinavian Math. Congress (Lund, 1953), 160–168, 1954.
15. H. Maier and C. Pomerance, *Unusually large gaps between consecutive primes*, Trans. Amer. Math. Soc. **322** (1990), 201–237.
16. OEIS Foundation, sequence A048670 (Jacobsthal's function at the primorials).
17. J. Pintz, *Landau's problems on primes*, J. Théor. Nombres Bordeaux **21** (2009), 357–404.
18. H.-E. Richert, *Selberg's sieve with weights*, Mathematika **16** (1969), 1–22.
19. A. Schinzel and W. Sierpiński, *Sur certaines hypothèses concernant les nombres premiers*, Acta Arith. **4** (1958), 185–208; erratum, ibid. **5** (1959), 259.
20. T. Tao and J. Teräväinen, *Quantitative bounds for Gowers uniformity of the Möbius and von Mangoldt functions*, J. Eur. Math. Soc. **27** (2025), 1321–1384.
