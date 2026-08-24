# From Cycle to Window

## III. What survives when an exact periodic law is evaluated on a short interval

---

### Abstract

Paper II establishes exact transport laws for the divisor census of the odd sieve over a full cycle of length $\prod q$. Every application needs a window of length $\asymp z^2$ — exponentially shorter. This paper asks what survives the passage, and answers it with a curve rather than a verdict.

We first show that the two motions are compatible in a strong sense: an old line appears to a new one as a **periodic ruler**. For rulers $q\ge7$, a first-cycle square sector is shorter than the period, so the local question is presence or absence rather than counting; $q=5$ is kept as a fixed core exception (Theorems 1 and 2). We then run the sieve at **moving depth** — each sector $(u^2,v^2)$ sieved by all lines $\le u$ — and measure a stable deficit $T/M \approx 0.80$ across three orders of magnitude. We interpret this as the expected dimension-2 Buchstab-type correction at the critical scale $s=2$, but the value $0.80$ itself is a measurement in this paper.

The deviations then admit a useful decomposition. A CRT-based mean law carrying a Legendre symbol and a companion square-cycle cancellation identity are verified exactly on the ranges tested in §4; a complete symbolic proof of those two identities is not supplied here, so they are kept separate from the proved results. The normalised survivor masks do form a **martingale** on the full CRT cycle, with orthogonal differences and total energy $\sum \mathbf{E}(\Delta_r^2)=1/P_z-1$ (Theorem 4). On short windows, the numerical $L^2$ data grow much faster than the target scale: a power fit over the tested range is about $U^{3.16}$. This is evidence against the desired bound at accessible scales, not an asymptotic refutation.

Finally we measure the transfer directly. On the tested windows, linear depth weights give ratio $1.0000$ to the reported precision; the tested truncations $\max(0,1-j/t)$ remain close to $1$ for $t\ge1.5$; and at $t\le1$, where the weight is exactly the depth-zero indicator, the measured ratio is near $0.80$ (Proposition 1). The indicator of depth zero is the twin condition in the moving square window. Thus the sharp loss appears at the endpoint of the measured family, while the interior of the curve remains empirical. A second measurement (§6) tests the general pattern law of [II, §6.3] instead of a weight, and finds it transferring at $1.0000$ for admissible patterns of up to five cells; taken together the two locate the loss in the one-point density rather than in the correlations.

**Keywords:** Buchstab function, sieve of dimension two, martingale decomposition, large sieve, weighted sieves.

**MSC 2020:** 11N35, 11N05, 11K38.

---

## 1. Setting, and what is imported

Coordinates from Paper I: $L_p(k) = p(p+2k)$; $L_3$ as the grid; cells $C_b = (6b-1,6b+1)$; sectors bounded by consecutive odd squares. Window combinatorics from Paper 0: the increments $W_j$ of $\lfloor 2j^2/p\rfloor$, with $H_j = 2+W_j$. Exact cycle laws from Paper II: the four-state law and its refinement by inheritance depth, with generating function $\prod_q((q-2)+xu+xv)$.

Two imported facts do real work below and are stated once:

- **[0, Thm 1].** Within the first cycle, a square sector contains between two and six strikes of any line, for every odd $p$ — the uniform bound on the increments of $\lfloor 2j^2/p\rfloor$. This is what makes §2.3 a *binary* statement for old rulers $q\ge7$; $L_5$ is handled separately as part of the fixed core.
- **[II, Thm 2].** On the full cycle, each line contributes nothing with probability $(q-2)/q$, a lower-rail strike with probability $1/q$ and an upper-rail strike with probability $1/q$, independently across lines. This is the exact reference distribution against which every window measurement below is compared.

The comparison object throughout is a ratio: a quantity measured on the window, divided by the same quantity computed from [II, Thm 2] on the cycle. A ratio of $1$ means the law transfers.

---


## 2. The strip, and old lines as rulers

### 2.1 The strip

A line is nothing but the strip $k = 0,1,2,\dots$, and the squares do not alter it — they cut it into blocks. For $L_7$:

| sector | $k$ | $H$ |
|---|---|---|
| $(49,81]$ | 1, 2 | 2 |
| $(81,121]$ | 3, 4, 5 | 3 |
| $(121,169]$ | 6, 7, 8 | 3 |
| $(169,225]$ | 9–12 | 4 |
| $(225,289]$ | 13–17 | 5 |
| $(289,361]$ | 18–22 | 5 |
| $(361,441]$ | 23–28 | 6 |

**The blocks are contiguous** (verified over 20 sectors): the squares never reset a line's phase, so a bias in one sector is continued, not restarted, by the next.

### 2.2 Theorem 1 (old lines as rulers)

> **Theorem 1.** For a new line $p$ and an old line $q<p$, with $x = L_p(k)$,
> $$x + 6j \equiv 0 \pmod q \iff k \equiv k_0 - j d \pmod q, \qquad d = 3 p^{-1} \bmod q, \tag{2.1}$$
> where $k_0 = -p^2(2p)^{-1} \bmod q$.

*Proof.* $x+6j = p^2+2pk+6j \equiv 0$ gives $k \equiv (-p^2-6j)(2p)^{-1} = k_0 - 3jp^{-1}$. $\blacksquare$

*Verification.* Zero failures among $35{,}868$ instances.

The coefficient is $3$, not $6$, because one step in $k$ moves the integer by $2p$; matching a displacement of $6$ modulo $q$ requires $2pd \equiv 6 \pmod q$.

**Equivalently, in clock form.** The first inherited strike index is
$$\phi_q(p) \equiv \frac{q-p}{2} \pmod q, \tag{2.2}$$
zero failures among $4{,}983$ instances.

### 2.3 Theorem 2 (binary decision) and phase collisions

Let $\kappa_j = 2j + \lfloor 2j^2/p\rfloor$ be the last $k$-index at the left square boundary, as in [0, §1]. For an old ruler $q$, define the distance from the start of the block to its next mark by
$$\delta_q(j)=1+\big((\phi_q(p)-\kappa_j-1)\bmod q\big)\in\lbrace 1,\dots,q\rbrace .$$
Thus the block contains a mark of $q$ exactly when this next-mark distance does not exceed the block length.

> **Theorem 2.** For every old line $q \ge 7$ and every sector $j$ **in the first cycle** $0 \le j \le p-1$, the number of strikes of $q$ inside the block is $C_q(j) \in \lbrace 0,1\rbrace$; and $C_q(j)=1$ exactly when $\delta_q(j) \le H_j$, in which case the strike falls in slot $s = \delta_q(j)$.

*Proof.* By [0, Thm 1], $H_j \le 6 < 7 \le q$ throughout the first cycle, so a block is shorter than the ruler's period and cannot contain two of its marks. $\blacksquare$

**Two hypotheses, both necessary.**

- *The first cycle.* Beyond it $H_j = H^{(0)}_j + 4r$, so a block can be longer than the ruler's period and the conclusion fails. Counterexamples at $p = 11$, $q = 7$: the sectors $j = 18, 21, 23, 25, 27, 28, 29, 30$ (with $H_j = 9$ to $13$) each contain **two** marks of $7$ — ten such sectors in the first three cycles. Every use of Theorem 2 below is inside the first cycle.
- *The ruler $q \ge 7$.* The ruler $q=5$ can meet a block of length $6$ twice. In the moving-depth calculations $L_5$ is included explicitly in the fixed core; all subsequent uses of the binary ruler statement refer to $q\ge7$.

For those rulers the local question changes from counting to presence/absence, and the state of a block is a **word** $W_j$ of length $H_j \le 6$.

**Composites are phase collisions.** If $\delta_{q_1}(j) = \delta_{q_2}(j) = s$, both lines mark slot $s$, i.e. the integer there carries both factors. Verified at $p=11$, sector 2: the cofactors $21, 23, 25$ give $O_{\lbrace 3,7\rbrace },  N,  O_{\lbrace 5\rbrace }$ — and $21 = 3\times 7$ appears precisely because the two rulers' phases coincided.



## 3. Moving depth

### 3.1 Setup

Let the depth track the window: sieve each sector $(u^2,v^2)$ by all lines $\le u$, and set
$$T(U) = \sum_{u\le U}(\text{survivors}), \qquad M(U) = \sum_{u\le U} C(u) P(u).$$

### 3.2 The measured ratio

| range of $n$ | 2–50 | 51–150 | 151–300 | 301–600 | 601–1000 | 1001–1600 |
|---|---|---|---|---|---|---|
| $T/M$ | 0.80567 | 0.81865 | 0.81020 | 0.80320 | 0.79456 | 0.79404 |

$$\boxed{ T/M \approx 0.80,\ \text{stable across three orders of magnitude.} }$$

**The discrepancy is systematic, not numerical noise.** At moving depth the sieve variable is $s = \log(u^2)/\log u = 2$ exactly, the critical scale at which a naive product is expected to need a Buchstab-type correction [2]. For comparison, in one dimension the familiar factor at $s=2$ is $e^{\gamma}/2=0.8905362$; in the present two-rail experiment the corresponding measured ratio is about $0.80$.

### 3.3 Why accumulation matters more than a single sector

One does not need $T(u)>0$ for every sector, only $T(U) \to \infty$. Since $\sum C(u) \asymp U^2/6$ and $P(U) \asymp 1/\log^2 U$,
$$M(U) \asymp \frac{U^2}{\log^2 U}, \tag{3.1}$$
so **any error bound of size $O(U\log^A U)$ suffices** — a requirement weaker by a full factor of $U$ than square-root cancellation.

### 3.4 Theorem 3 (telescoping to a single sum)

> **Theorem 3.** With $P(r) = \prod_{5\le q\le r}(1-2/q)$,
> $$T(u) = P(u)\left[C(u) - \sum_{r\le u}\frac{\varepsilon_r(u)}{P(r)}\right], \qquad T(U)-M(U) = \sum_{r\le U} B_r(U),$$
> where $B_r(U) = -P(r)^{-1}\sum_{u\ge r}P(u) \varepsilon_r(u)$.

*Proof.* From $N_r = N_{r^-}(1-2/r) - \varepsilon_r$, divide by $P(r)$ and telescope. $\blacksquare$

*Verification.* At $U=1019$: $T = 2920.0$, $M = 3535.3$, $T-M = -615.3 = \sum B_r$. At $U = 2039$: $-2143.2$ on both sides.

$$\boxed{ 2^{\pi(U)} \text{ intersections}  \longrightarrow  \text{one sum over primes.} }$$

This is the first point in the framework at which stacking the lines does not blow up.

### 3.5 The state space is the cycle

Define the clock vector here by $\Phi_z(p)=(\phi_3(p),\phi_5(p),\dots,\phi_z(p))$, using (2.2) componentwise. It takes values in a set of size $\prod_{3\le q\le z} q$, while a trajectory of length $N$ visits at most $N$ of them:

| $z$ | lines | states $\prod q$ |
|---|---|---|
| 13 | 5 | 15,015 |
| 31 | 10 | $1.0\times10^{11}$ |
| 59 | 16 | $9.6\times10^{20}$ |
| 101 | 25 | $1.2\times10^{38}$ |

The survivor pattern of the lines up to $z$ has period exactly $\prod q$ and, by [II, Thm 1], exactly $\prod(q-2)$ surviving cells in it. **Any “compressed law for the next survivor” — a rule carrying a state materially smaller than the cycle — would therefore be a compression of the cycle itself.** We record this as an observation rather than a theorem, but it is the reason any “successor tower” for the sieved strip is a re-description and not a reduction.

---



## 4. Decomposing the deviations

### 4.1 Verified identity A (the mean, and its Legendre symbol)

Split $\varepsilon_r = \mu_r + \xi_r$ into mean and fluctuation.

> **Verified identity A (proof not supplied here).** $\displaystyle \mu_r = -\frac{\chi_r}{r} Q_{r^-}$, where $\chi_r = \left(\frac{2}{r}\right)$ and $Q_r = \prod_{5\le q\le r}\left(1-\frac{2+\chi_q}{q}\right)$.

*Origin of the symbol.* At a square boundary the line $r$ can strike when $u^2 \equiv 0$ or $u^2 \equiv 2 \pmod r$; the number of admissible phases of $u$ is therefore $1 + (1+\chi_r) = 2+\chi_r$, and a CRT count suggests the product structure across a set of lines. The formula below is verified extensively, but the full symbolic CRT derivation is not included in this paper.

*Verification.* Over 1,400 sectors with standard errors, the $z$-scores against the prediction are $0.04,  0.01,  -0.44,  0.26,  0.49,  0.33,  -1.03,  0.48,  0.32,  -0.80$ for $r = 5,\dots,101$ — all within one standard error. The two cleanest cases agree to three digits: $r=5$ predicts $0.200000$ and measures $0.200286$; $r=7$ predicts $-0.114286$ and measures $-0.113959$.

### 4.2 Verified identity B (square-cycle cancellation)

> **Verified identity B (proof not supplied here).** With $\eta_r(n) = D_r^{(0)}(n) - 2C(n)/r$, summed over a full cycle of $r$ sectors,
> $$\sum_{\text{cycle}} \eta_r = -\left(\frac{2}{r}\right);$$
> and for any set $S$ of lines, over a cycle of length $M_S = \prod_{r\in S} r$,
> $$\sum_{\text{cycle}} \eta_S = 2^{|S|} - \prod_{r\in S}\left(2 + \left(\frac{2}{r}\right)\right).$$

*Verification.* The single-line law holds exactly for $r = 5,7,11,13,17,19,23,29,31,37,41,43,47$. The general law gives $\lbrace 5,7\rbrace \mapsto 1$, $\lbrace 5,11\rbrace \mapsto 3$, $\lbrace 7,17\rbrace \mapsto -5$, $\lbrace 7,11\rbrace \mapsto 1$, $\lbrace 11,13\rbrace \mapsto 3$, $\lbrace 5,13\rbrace \mapsto 3$, $\lbrace 5,7,11\rbrace \mapsto 5$ — every value exact.

**$r$ boundary errors, each of size $O(1)$, collapse to $\pm1$.** Consequently the whole inclusion–exclusion compresses into two products:
$$E_{\text{cycle}} = M\left[\prod_{r}\left(1-\frac2r\right) - \prod_{r}\left(1-\frac{2+(2/r)}{r}\right)\right]. \tag{4.1}$$
The second product is a factor the purely periodic model does not contain; it is contributed by the square clock.

### 4.3 Algebraic consequence of identity A

Assuming identity A, $\sum_r -\mu_r/P_r = 1 - Q_z/P_z$, whence
$$E_{\text{mean}}(U) = \sum_{u\le U}(P_u - Q_u) = O\left(\frac{U}{\log^2 U}\right), \tag{4.2}$$
smaller than the main term (3.1) by a full factor of $U$.

*Verification.* At $U = 1000$ the total error is $-2057$ while the mean part contributes $-6.93$; at $U = 2000$, $-6479$ against $-11.24$. **The means account for $0.17$% of the deviation.**

### 4.4 Theorem 4 (martingale structure)

Normalise the survivor mask by $Z_z = A_z/P_z$ and set $\Delta_r = Z_r - Z_{r^-}$.

> **Theorem 4.** Over a full CRT cycle, $\mathbf{E}(\Delta_r \mid \mathcal{F}_{r^-}) = 0$, $\mathbf{E}(\Delta_r\Delta_s) = 0$ for $r \ne s$, and
> $$\sum_{r\le z}\mathbf{E}(\Delta_r^2) = \frac{1}{P_z} - 1.$$

*Proof.* Put the uniform probability measure on one full CRT cycle, and let $\mathcal F_{r^-}$ be the sigma-algebra generated by the residue coordinates of the lines below $r$. Write $A_r=A_{r^-}B_r$, where $B_r$ is the indicator that the $r$-coordinate avoids the two forbidden rail positions. Conditional on $\mathcal F_{r^-}$, the new CRT coordinate is uniform, so
$$\mathbf E(B_r\mid\mathcal F_{r^-})=1-\frac2r,$$
and it is independent of the earlier coordinates. Since $P_r=P_{r^-}(1-2/r)$,
$$\mathbf E(Z_r\mid\mathcal F_{r^-})=\mathbf E\left(\frac{A_{r^-}B_r}{P_{r^-}(1-2/r)}\middle|\mathcal F_{r^-}\right)=Z_{r^-}.$$
Hence $\mathbf E(\Delta_r\mid\mathcal F_{r^-})=0$, so the $\Delta_r$ are martingale differences and are pairwise orthogonal. Finally $\mathbf{E}(Z_z)=1$ and, because $A_z\in\lbrace 0,1\rbrace$,
$$\mathbf{E}(Z_z^2)=\frac{P_z}{P_z^2}=\frac1{P_z}.$$
Thus $\mathrm{Var}(Z_z)=1/P_z-1$, and orthogonality gives $\sum_{r\le z}\mathbf E(\Delta_r^2)=1/P_z-1$. $\blacksquare$

*Verification.* For $\lbrace 5,7,11,13\rbrace$ with $W = 5005$: the individual energies are $0.6666667,  0.6666667,  0.5185185,  0.5185185$, summing to $\mathbf{2.3703703704}$, while $1/P-1 = \mathbf{2.3703703704}$ — agreement to ten digits. All six cross-correlations are $\sim 10^{-17}$, i.e. zero to machine precision.

Since $P_z \asymp 1/\log^2 z$, the total $L^2$ energy of *all* lines is $O(\log^2 z)$, not exponential. **The primorial is present as a period, but the size of the $L^2$ error does not carry it.**

---



## 5. The decisive $L^2$ question

### 5.1 Statement

By Cauchy–Schwarz, $\left|\sum_{r\le U} D_r\right| \le \sqrt{\pi(U)}\left(\sum_{r\le U}|D_r|^2\right)^{1/2}$. Hence if
$$\sum_{r\le U}\big|D_r(X)\big|^2  \ll  (X+U^2) \mathrm{polylog}(U), \qquad X \asymp U^2, \tag{5.1}$$
the total error would be $O(U^{3/2} \mathrm{polylog})$ against a main term $\asymp U^2/\log^2 U$, giving $T(U)\to\infty$ and hence infinitely many twin primes.

### 5.2 Why $X \asymp U^2$ is the critical scale

The available sector window at depth $U$ has length $\asymp U^2$, while the full network cycle has length $\asymp e^{U}$. Theorem 4 establishes orthogonality **on the full cycle**; the question is whether it survives restriction to a window exponentially shorter.

### 5.3 Numerical stress test of the bound

| $U$ | lines | $\sum\lvert D_r\rvert^2$ | $X+U^2$ | ratio |
|---|---|---|---|---|
| 300 | 60 | $1.819\times10^5$ | $1.05\times10^5$ | 1.73 |
| 600 | 107 | $1.310\times10^6$ | $4.20\times10^5$ | 3.12 |
| 1,200 | 194 | $1.326\times10^7$ | $1.68\times10^6$ | 7.89 |
| 2,400 | 355 | $1.245\times10^8$ | $6.72\times10^6$ | **18.53** |

Across this range the ratio rises rapidly with $U$. A log-log power fit to the displayed data gives an **effective exponent** about $3.16$ for $\sum|D_r|^2$, compared with the target base scale $U^2$. This is a finite-range fit, not an asymptotic law. Normalising by $U^2\log^A U$ for $A=2,4,6,8,10$ still leaves rising sequences on the tested range, by factors $56, 31, 17, 9.0, 4.9$ respectively.

**Restricting the depth improves the finite-range level but does not flatten the observed trend.** At $z=U^{1/2}$ the ratio is $0.00831,\ 0.02220,\ 0.08504,\ 0.20556,\ 0.85696$ at $U=2400,\dots,38400$. A naive extrapolation of that trend would cross $1$ near $U\approx45{,}000$, but that crossing is not a theorem and is not used as one.

$$\boxed{ \text{On the tested range, the }L^2\text{ data grow much faster than the target base scale }U^2. }$$

### 5.4 Why: the nested masks

The full-cycle orthogonality of Theorem 4 is not observed to transfer uniformly to the tested windows of length $U^2$. A natural explanation is that $\Delta_r$ is not a free difference: it is the quadratic motion seen **through the mask of all smaller lines**, $A_{r^-}=A_{\lbrace 5,\dots,r^-\rbrace }$, so the sequence being tested changes with $r$. The data are consistent with the nesting cost overwhelming the full-cycle orthogonality on these ranges.

A large-sieve-type inequality adapted to such *nested* masks would be the kind of estimate needed for (5.1). No such estimate is proved in this paper.

### 5.5 What would have sufficed

Precisely a bound
$$\big|S_r(V)\big|  \le  C\sqrt{N_r(V)} \log^A U, \tag{5.2}$$
where $S_r(V)$ is the centred partial sum since the line's birth and $N_r(V)$ the number of sectors observed. **This is weaker than Hardy–Littlewood: no constant need be identified and no asymptotic formula proved — only a bound.**

The tested data do not support a small uniform constant: the worst ratio $\max|S_r|/\sqrt{N_r}$ rises from $4.25$ at $U=4199$ to $5.75$ at $U=7199$. This does **not** refute the existence of some larger eventual constant. The polylogarithmic form is **beyond what computation can settle here**: each sector costs $O(u)$ work, so distinguishing $\sqrt N \log^A$ from $\sqrt N \log^{A+1}$ would require $U$ in the millions.

---



## 6. Transferring the depth distribution to a window

The question is whether the depth distribution of [II, Thm 2] transfers from cycle to short window more stably than the raw survivor count. **On the tested ranges it does for soft weights.** The deterioration is not perfectly monotone — there is a small overshoot near $t=3$ — but the sharp depth-zero endpoint is clearly separated, with ratio near $0.80$.

*Setup.* Moving depth: each sector $(u^2,v^2)$ is sieved by all lines $\le u$, and each cell is recorded with its state and its inheritance depth $j$. The comparison is against the exact cycle distribution implied by [II, Thm 2] — each line contributes nothing with probability $(q-2)/q$, a lower-rail strike with probability $1/q$, an upper-rail strike with probability $1/q$. Four bands of $u$, up to $1.3\times10^{6}$ cells per band.

*Raw ratios.* Window over cycle: $NN$ gives $0.80$, $NO/ON$ gives $0.914$, $OO$ gives $1.063$ — the deficit of §3.2 seen state by state. The total-variation distance between the window and cycle depth *shapes* within a state is $0.106$ ($NO/ON$) and $0.089$ ($OO$), i.e. the shape already transfers about twice as well as the count.

*The curve.* Transfer ratio for the weight $\max(0, 1-j/t)$:

| $t$ | 400–800 | 800–1600 | 1600–3200 | 3200–6400 |
|---|---|---|---|---|
| 12 (linear on this range) | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| 8 | 0.9998 | 0.9997 | 0.9996 | 0.9994 |
| 5 | 0.9979 | 0.9973 | 0.9975 | 0.9979 |
| 3 | 1.0176 | 1.0200 | 1.0209 | 1.0214 |
| 2.5 | 1.0082 | 1.0081 | 1.0083 | 1.0079 |
| 2 | 0.9832 | 0.9753 | 0.9724 | 0.9684 |
| 1.5 | 0.9528 | 0.9484 | 0.9461 | 0.9424 |
| $\le 1$, i.e. the indicator $[j=0]$ | **0.7974** | **0.8056** | **0.8016** | **0.7953** |

Two structural remarks, both of which the table makes visible.

1. **Linear weights measure $1.0000$ to the reported precision on these windows.** Structurally, each line contributes its cyclic mean up to an $O(1)$ boundary term, so linear statistics are expected to be much more stable than sharp indicators; the finite-window equality is empirical here, not an exact theorem.
2. **The ratio is nearly flat in $u$** for the softer tested weights, drifts by about $-0.015$ at $t=2$, and is flat again near the $0.80$ endpoint. The dependence on $t$ is not strictly monotone because of the small overshoot around $t=3$.

*And at Richert's own parameters the transfer is essentially perfect.* Taking $\mathcal{A}$ to be the integers $6b\pm1$ in $(u^2,v^2)$, sieving by the lines below $z = X^{1/8}$ and weighting the primes in $[z, y)$ with $y = X^{1/3.17}$ and $\lambda = 0.83$: the survivor-count ratio measures $1.0000$ and the weighted-sum ratio $0.9998$, flat across $u = 300$ to $4800$. The reason is that at $k_1 = 8$ the sieve variable is $s = (1/2)/(1/8) = 4$, comfortably above $2$ — Campbell [1] runs at $s = 3.33$. **The window-transfer deficit does not bite at those parameters at all; the bottleneck in the almost-primes problem is the numerical optimisation, not the transfer.**

> **Proposition 1 (measured).** On the tested moving-depth windows, linear functions of inheritance depth give transfer ratio $1.0000$ to the reported precision. For every **tested** value $t\ge1.5$, the weight $\max(0,1-j/t)$ stays within about $6$% of $1$ (within about $3.2$% for the tested $t\ge2$), while for $t\le1$ — exactly the indicator $[j=0]$ — the measured ratio is approximately $0.80$.

*A second family: pattern transfer at fixed depth.* Proposition 1 measures the transfer of a *weight* on one cell. The cycle law of [II, §6.3] is more general than that: it transports an arbitrary finite pattern $H$ of cells, with $N_{\mathrm{new}}(H) = (q-\nu_q(H)) N_{\mathrm{old}}(H)$. Nothing above tests it beyond $|H| = 2$, and the patterns are the sharpest indicators the framework has — a pattern of $k$ cells is a condition on $2k$ integers at once. This paragraph tests that law directly.

*Setup, and a constraint that appears immediately.* Fix a height $X$ and a depth $z = X^{1/u}$, sieve the whole range $6n\pm1 \le X$ by every line $\le z$, and write $S_n = 1$ when both members of cell $n$ survive. For a pattern $H = \lbrace h_1=0 < \dots < h_k\rbrace$ set
$$J(H)  =  \frac{\Pr\big(S_{n+h_1} = \dots = S_{n+h_k} = 1\big)}{\Pr(S_n=1)^k}, \qquad L(H)  =  \prod_{5\le q\le z}\frac{1-\nu_q(H)/q}{(1-2/q)^{k}} ,$$
so that $J/L = 1$ is exactly the assertion that the cycle law of [II, §6.3] survives the passage to a real window at depth $z$. Here $\nu_q(H) = \mathrm{card}\lbrace \pm 6^{-1} - h_i \bmod q\rbrace$, and the pattern must be admissible: consecutive cells $H = \lbrace 0,1,2\rbrace$ already give $\nu_5 = 5$ and density zero, so the shortest admissible patterns are $\lbrace 0,1\rbrace$, $\lbrace 0,1,3\rbrace$, $\lbrace 0,1,3,5\rbrace$, $\lbrace 0,1,3,5,6\rbrace$ — the last a condition on ten integers spanning $38$.

*Measured*, at $X = 4\times10^{9}$ (all $6.67\times10^{8}$ cells; the $\pm$ column is $1/\sqrt{\text{count}}$):

| $u$ | $z$ | $H$ | count | $J$ | $L$ | $J/L$ | $\pm$ |
|---|---|---|---|---|---|---|---|
| 4 | 251 | $\lbrace 0,1\rbrace$ | 1,688,188 | 0.3978 | 0.3978 | **1.0000** | 0.0008 |
| 4 | 251 | $\lbrace 0,1,3\rbrace$ | 142,416 | 0.4207 | 0.4206 | **1.0002** | 0.0026 |
| 4 | 251 | $\lbrace 0,1,3,5\rbrace$ | 19,817 | 0.7337 | 0.7348 | **0.9985** | 0.0071 |
| 4 | 251 | $\lbrace 0,1,3,5,6\rbrace$ | 727 | 0.3374 | 0.3412 | **0.9887** | 0.0371 |
| 3 | 1587 | $\lbrace 0,1\rbrace$ | 567,431 | 0.3973 | 0.3970 | 1.0007 | 0.0013 |
| 3 | 1587 | $\lbrace 0,1,3\rbrace$ | 27,527 | 0.4164 | 0.4179 | 0.9964 | 0.0060 |
| 3 | 1587 | $\lbrace 0,1,3,5\rbrace$ | 2,167 | 0.7082 | 0.7255 | 0.9762 | 0.0215 |
| 3 | 1587 | $\lbrace 0,1,3,5,6\rbrace$ | 51 | 0.3601 | 0.3340 | 1.0780 | 0.1400 |
| 2 | 63,246 | $\lbrace 0,1\rbrace$ | 85,884 | 0.4014 | 0.3969 | 1.0113 | 0.0034 |
| 2 | 63,246 | $\lbrace 0,1,3\rbrace$ | 1,703 | 0.4442 | 0.4175 | 1.0640 | 0.0242 |
| 2 | 63,246 | $\lbrace 0,1,3,5\rbrace$ | 50 | 0.7280 | 0.7242 | 1.0053 | 0.1414 |

*At the moving depth $u = 2$ the residual deviation shrinks with height.* For $H=\lbrace 0,1\rbrace$, $J/L = 1.0311,\ 1.0160,\ 1.0113$ at $X = 10^{8}, 10^{9}, 4\times10^{9}$. Writing the $k$-tuple count with the integral $\int_2^X \mathrm{d}t/\log^{2k}t$ rather than $X/\log^{2k}X$, and the same for the normalising $\Pr(S)^k$, the leading $1/\log X$ corrections cancel and the first surviving term is $1 + 2k(k-1)/\log^2 X$, i.e. $1.008$ for $k=2$ and $1.025$ for $k=3$ at $X = 4\times10^{9}$; the measured $1.0113$ and $1.0640$ sit within one to two standard errors of those. **We report this as an account of the observed size, not as a derivation.**

> **Proposition 2 (measured).** On the tested range, the pattern law of [II, §6.3] transfers to a real window at fixed depth with $J/L = 1$ to within the statistical error, for every tested admissible pattern of up to five cells — a condition on ten integers — at $u = 3$ and $u = 4$. At the moving depth $u=2$ the ratio exceeds $1$ by one to six per cent, decreasing with height.

*What this adds to Proposition 1, and it changes the reading of this section.* Proposition 1 shows the one-cell statistic losing about $20$% exactly when the weight sharpens to the depth-zero indicator. Proposition 2 shows a far sharper indicator — the simultaneous survival of ten integers — transferring at $1.0000$. **The two are consistent, and together they separate the loss into two factors: it lies entirely in the one-point density, which carries the Buchstab correction at $s=2$ (§3.2), and not in the correlations built on top of it, which transfer exactly for every pattern tested.** In other words the deficit is a function of the depth relative to the window, not of the sharpness of the statistic.

**What this settles, and what it does not.** The experiment shows a sharp distinction inside the tested weight family: soft weights transfer well, whereas the depth-zero indicator carries the large deficit. That indicator is the twin condition in the moving square window. The experiment does not prove a transfer theorem for arbitrary weights or all $t$; it locates the observed loss in this family. Proposition 2 then locates it more precisely still — in the one-point density rather than in the pattern structure — but it too is a measurement on a finite range and proves no transfer theorem.

$$\boxed{ \text{The transfer fails in the one-point density and holds in the correlations, for every pattern tested up to ten integers.} }$$

---

## 7. What this paper establishes

**Proved.** Old lines act as rulers with phase $\phi_q(p)\equiv(q-p)/2$ and the binary decision for $q\ge7$ (Theorems 1, 2); the telescoping identity reducing the iterative deviations to a single sum (Theorem 3); and the full-cycle martingale structure with its energy identity (Theorem 4).

**Verified identities whose complete symbolic proofs are not supplied here.** The mean law with its Legendre symbol (identity A), its algebraic telescoping consequence, and the single-line/multi-line square-cycle cancellation (identity B). They agree with every exact enumeration reported in §4, but they are not counted as proved theorems in this version.

**Measured, not proved.** The stability of $T/M\approx0.80$ (§3.2); the state-space observation (§3.5); the $L^2$ growth in §5.3; the restricted-depth trend; the transfer curve of §6 (Proposition 1); and the pattern transfer of §6 (Proposition 2). The data do not refute a polylogarithmic $L^2$ bound asymptotically, and the finite-window value $1.0000$ for linear weights is a measurement to the reported precision, not an exact equality theorem.

**The shape of the result.** On the tested windows, soft weights preserve the cycle prediction far better than the sharp depth-zero indicator. The latter is precisely the primality/twin atom in this setup.

$$\boxed{ \text{The exact cycle laws are proved; the short-window transfer remains partly empirical.} }$$

The applications of that statement, and the problems it does and does not decide, are Paper IV.

---

## References

The companion papers are cited as [0], [I], [II], [IV].

1. P. Campbell, *On the existence of integers with at most 3 prime factors between every pair of consecutive squares*, arXiv:2603.10356 (2026). — *the almost-primes computation whose parameters are used in §6; it runs at sieve variable $s = 3.33$.*
2. J. Friedlander and H. Iwaniec, *Opera de Cribro*, AMS Colloquium Publications **57**, 2010. — *for the Buchstab-type correction at $s=2$ discussed in §3.2, and for the large-sieve inequalities of the kind §5.4 would need.*

