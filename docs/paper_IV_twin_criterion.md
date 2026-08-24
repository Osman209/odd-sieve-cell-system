# The Twin Criterion in Cell Coordinates

## IV. What the framework proves about twin pairs

---

### Abstract

This paper collects what the cell coordinates prove outright about the twin problem. Everything below is proved, with one exception flagged as such (Verified Law 17, proved under a hypothesis on prime gaps and verified beyond it); the measurements, the test cases and the account of where the framework stops are Paper V.

The gap between consecutive odd composites takes only the values $2$, $4$ and $6$, and gap $6$ *is* a twin pair (Theorem 1), so the twin conjecture becomes the statement that the maximal possible gap is attained infinitely often — a cap that is free and proved. The ladder below it is complete: gap $2$ occurs infinitely often with no prime input, gap $4$ with one use of Dirichlet, and gap $6$ needs two primes simultaneously (Theorem 2). No five survivors lie in arithmetic progression at spacing $6$ on one rail, beyond a single small exception, and the full-cycle run counts are $\prod(q-k)$ (Theorem 3, Corollary 1).

Inside a single sector the criterion sharpens as far as the framework can take it: after switching on every line $p \le M$, **at most six cells can be open without being a twin pair, and their positions are given by an explicit formula in $M$** (Theorem 4). A twin therefore follows from one open cell that avoids six named places — the places being fixed by the geometry of the square rather than chosen by the lines.

The closing budget is exact: the distance-$6$ graph has minimum deletion cover $\tau = T-U+Q$ (Theorem 8), the four-state census transports under a new line (Theorem 9), and the late lines of a sweep compress (Theorem 10). The clock coordinate turns primality into a zero-test (Theorem 11) and forces every surviving cofactor in a range to be prime (Theorem 12). Read along a whole row that becomes a general law: for $p \le p+2j < p^2$ the cell $p(p+2j)$ is **original** — owned by no smaller line — exactly when $p+2j$ is prime (Theorem 13), so a row carries the primality of every odd number up to $p^2$ in one bit per cell, the twin condition becomes "originality survives one step past the diagonal", and the cell it tests is $(p+1)^2-1$, which is [I, Thm 5] read along the row. Finally, across the *sequence* of sectors, a fixed set of lines leaves exactly $12S$ fresh open cells each time its cycle returns to the same phase (Theorem 14); a later line closes at most two of the twelve copies of any surviving class and at most one beyond an explicit threshold (Theorem 15, Corollary 6).

A last section takes the four cells nearest the window's ends and turns them into four **tracks** as $a$ runs, each member a quadratic in $a$; a prime can own a track only if the corresponding discriminant is a quadratic residue (Theorem 18), which makes the four tracks unequal — Bateman–Horn gives them densities $0.41$, $0.73$, $1.10$ and $1.43$ times that of a generic cell, so the last is three and a half times richer in twins than the first. And where eligibility admits three quarters of the primes for one track and a quarter for all four, **simultaneous double duty inside one window admits exactly nine primes, so every $r > 97$ can close at most one of the four** (Theorem 19). That constraint is sharp for a single line and empty for four: assigning a distinct line to each track and combining the congruences produces an explicit infinite progression along which all four cells are closed, $q$ is prime and $q+2$ is composite (Proposition 2), so **no fixed number of named cells can force a twin.** The same coordinates make the operative threshold visible: a line whose modulus reaches the window's own length cannot wrap inside it and has a total budget of two, so at $a = 1667$ the $857$ lines below $N$ close $6{,}500$ cells while the $370$ above it close $20$.

A further section changes the unit from the sector to the **belt** between consecutive prime gates $q^2$ and $r^2$. The belt holds exactly $(r^2-q^2)/6-1$ cells and so grows like $qg$ with $g = r-q$ (Theorem 16), while the line born at its left end can strike only $\lfloor 2g/3\rfloor$ of them — **a count independent of $q$** (Verified Law 17, proved under $g^2<2q$). Measured, the new line closes nothing at all in about three quarters of belts. A deterministic ceiling for a whole age layer follows (Proposition 1), generous by one to two orders of magnitude; but summed over the full pyramid of layers it exceeds the belt by a factor $\sim\tfrac23\log q$, so the recent lines are not capacity-limited and the argument does not close. We report that negative outcome with the rest.

**No progress toward the twin-prime conjecture is claimed.** Every statement here is exact; none of them is a lower bound on anything.

**Keywords:** twin primes, gap alphabet, minimum vertex cover, sieve cycles, cell coordinates.

**MSC 2020:** 11N35, 11N05, 11A41.

---

## 1. Setting

We use Papers I–III as follows and import nothing else.

- **[0]** supplies the window combinatorics: the increments $W_j$ of $\lfloor 2j^2/p\rfloor$, their uniform bound and their exact histogram.
- **[I]** supplies the coordinates: the line $L_p(k) = p(p+2k)$ beginning at $p^2$, the grid $L_3$, the cells $C_b = (6b-1, 6b+1)$, and the square window with its $+8$ growth.
- **[II]** supplies the exact cycle laws: the four-state law, its refinement by inheritance depth, arbitrary weights in $\Omega_{\le z}$, the refinement by line size, and the disjoint ownership layers.
- **[III]** studies the transfer to a window of length $\asymp z^2$. On the tested windows, linear depth weights measure $1.0000$ to the reported precision, the tested soft truncations remain close to $1$, and the sharp depth-zero indicator is the exceptional endpoint with ratio near $0.80$. These are measurements, not an exact window theorem.

A word on the last point, since it is what makes this paper's organisation possible. The indicator of depth zero is the condition "both members of the cell survive" — that is, the twin condition. Thus, in the tested family, the largest transfer loss occurs precisely at the depth-zero indicator, the quantity that becomes a primality/twin condition inside the moving square window.

---


## 2. The gap alphabet and the ladder of proofs

Before turning to the deviation analysis we record what the framework proves outright about gaps, and where the ladder stops.

### 2.1 Theorem 1 (the gap alphabet)

> **Theorem 1.** The gap between consecutive odd composites takes only the values $2$, $4$ or $6$.

*Proof.* Among any three consecutive odd numbers $n, n+2, n+4$ the residues mod $3$ are a permutation of $\lbrace 0,1,2\rbrace$, so one is divisible by $3$; and every odd multiple of $3$ from $9$ onward lies on $L_3$. Hence beyond $7$ no three consecutive survivors exist, and the gap is capped at $6$. $\blacksquare$

Correspondingly: gap $2$ means no survivor between; gap $4$ means one isolated prime; and **gap $6$ means two adjacent survivors, i.e. a twin pair.** Verified: every gap-$6$ interval contains a twin, zero failures among $2{,}992$ instances below $3\times10^5$.

Measured over $9\times10^8$ gaps up to $2\times10^9$, the three letters occur with frequencies $0.89816$, $0.09475$ and $0.00708$; the maximum observed gap is $6$, first attained at $9$.

Hence an equivalent form of the twin conjecture: **the maximal possible gap is attained infinitely often.** The cap is free and proved; the statement concerns composites, which are the objects the framework actually constructs.

### 2.2 The ladder, and where it stops

> **Theorem 2.** Gap $2$ occurs infinitely often, requiring no prime; gap $4$ occurs infinitely often, requiring one prime.

*Proof.* For gap $2$: take $n = 30j+3$ and $n+2 = 30j+5$; the first lies on $L_3$, the second on $L_5$, both for every $j\ge1$. For gap $4$: let $p \equiv 8 \pmod{15}$ be prime; then $p-2 \equiv 6$ is divisible by $3$ and $p+2 \equiv 10$ by $5$, so $p$ is an isolated survivor, and Dirichlet's theorem supplies infinitely many such $p$. $\blacksquare$

$$\begin{array}{lll}
\text{gap } 2 & \text{zero primes required} & \textbf{proved} \cr 
\text{gap } 4 & \text{one prime (Dirichlet)} & \textbf{proved} \cr 
\text{gap } 6 & \textbf{two primes simultaneously} & \textbf{open}
\end{array}$$

**Dirichlet supplies one prime in an arithmetic progression; nothing supplies two at a prescribed distance.** That is the whole of the remaining distance.

**Why this reciprocal-sum test cannot bridge it.** Summing reciprocals by gap type:

| $N$ | gap 2 | gap 4 | gap 6 |
|---|---|---|---|
| $10^6$ | 2.805 | 0.887 | 0.464 |
| $10^8$ | 4.556 | 1.127 | 0.488 |
| $2\times10^9$ | 5.762 | 1.257 | **0.498** |

Gaps $2$ and $4$ have **divergent** reciprocal sums (growing like $\log\log N$), and divergence proves infinitude. The gap-$6$ sum **converges** — flattening toward a constant. That constant is the analogue of Brun's constant in the present alphabet and not Brun's constant itself: the latter is $\sum_{\text{twins}}\big(1/p + 1/(p+2)\big) = 1.9021605\ldots$, whereas the column above carries one reciprocal per gap-$6$ event. A convergent reciprocal sum cannot distinguish "infinitely many" from "finitely many". Thus this particular divergence-based density test has no route to the twin conclusion.

### 2.3 Runs and the cap at four

> **Theorem 3.** On a single rail, no five survivors with $x > 5$ can lie in arithmetic progression with common difference $6$; and $5, 11, 17, 23, 29$ is the only exception.

*Proof.* Since $6 \equiv 1 \pmod 5$, the five terms $x, x+6, \dots, x+24$ run through all residues modulo $5$, so exactly one of them is divisible by $5$. If that term exceeds $5$ it is an odd multiple of $5$ at least $25$, hence lies on $L_5$ and is struck. The term can fail to be struck only when it equals $5$ itself, which forces $x = 5$. $\blacksquare$

**The exception is real and must be carried in the statement.** For $x = 5$ the run is $5, 11, 17, 23, 29$, and all five are prime; an exhaustive search to $2\times10^5$ finds this and no other. It exists purely because $L_5$ is born at $25$: as a statement about the *residue classes* the argument is exact, and only the birth rule creates the exception.

*Verification.* At sieve depth $97$ over $6\times10^7$ cells, the run-length census is $6{,}448{,}150$ of length $1$; $2{,}404{,}092$ of length $2$; $778{,}762$ of length $3$; $211{,}170$ of length $4$; and **none of length $5$ or more.**

> **Corollary 1.** With $G_k$ the number of runs of $k$ consecutive survivors at spacing $6$ on one rail, the full-cycle counts satisfy $G_k = \prod_{q}(q-k)$.

*Proof.* A run of $k$ forbids exactly $k$ marks on each ruler, leaving $q-k$. $\blacksquare$

*Verification* (direct count on the $t$-axis at $p = 101$):

| lines | $k{=}1$ | 2 | 3 | 4 | **5** |
|---|---|---|---|---|---|
| $\lbrace 5\rbrace$ | 4 | 3 | 2 | 1 | **0** |
| $\lbrace 5,7\rbrace$ | 24 | 15 | 8 | 3 | **0** |
| $\lbrace 5,7,11\rbrace$ | 240 | 135 | 64 | 21 | **0** |

**The four laws $(q-1),\dots,(q-4)$ are therefore not four phenomena but one ruler with different numbers of marks.**

---



## 3. The twin problem inside the framework

### 3.1 A surviving cell is a twin pair

Let $u<v$ be consecutive integers coprime to $6$. Every survivor of all lines $\le u$ inside $(u^2, v^2)$ is necessarily prime, since a composite $x < v^2$ has a prime factor $\le \sqrt{x} < v$, and there is no prime strictly between $u$ and $v$. Hence
$$\boxed{ \text{a surviving } NN \text{ cell in } (u^2,v^2)  =  \text{a twin prime pair.} } \tag{3.1}$$

### 3.2 Theorem 4: only six cells in a sector can be open without being a twin

Take the sector in the form used throughout this section: $M \equiv 3 \pmod 6$ and the interval $(M^2, (M+6)^2)$, which carries $A_M = 2M+6$ cells
$$C_j = \big(M^2+6j+2,\ M^2+6j+4\big), \qquad j = 0,1,\dots,2M+5 .$$

> **Theorem 4.** Switch on every line $p \le M$. Then at most **six** cells of the sector can be open without being a twin pair, and their positions are given explicitly by
> $$E_M  =  \underbrace{\Big\lbrace \tfrac{2M}{3},\ \ M+1,\ \ \tfrac{5M}{3}+2,\ \ 2M+3\Big\rbrace }_{\text{present only if } M+2 \text{ is prime}}  \cup  \underbrace{\Big\lbrace \tfrac{4M}{3}+2,\ \ 2M+5\Big\rbrace }_{\text{present only if } M+4 \text{ is prime}} .$$
> Consequently **every open cell whose index lies outside $E_M$ is a twin pair.**

*Proof.* Let $N$ be a composite endpoint of an open cell. Every prime factor of $N$ exceeds $M$, since otherwise some line $p \le M$ would have closed it; and the least prime factor cannot be $\ge M+6$, since then $N \ge (M+6)^2$. As $M \equiv 3 \pmod 6$ and $N$ is coprime to $6$, the least prime factor is therefore $M+2$ or $M+4$.

For $p = M+2$ the strikes below $(M+6)^2 = (p+4)^2$ are $p^2,\ p(p+2),\ p(p+4),\ p(p+6),\ p(p+8)$ — the next one, $p(p+10)$, already exceeds $(p+4)^2$. Of these, $p(p+4) = (M+2)(M+6)$ is divisible by $3$ and so lies on $L_3$, not in a cell; four remain. For $q = M+4$ the strikes below $(q+2)^2$ are $q^2,\ q(q+2),\ q(q+4)$, of which $q(q+2) = (M+4)(M+6)$ lies on $L_3$; two remain. Six in total.

Their positions follow by writing each product in the form $M^2+6j+2$ or $M^2+6j+4$. For instance $(M+2)^2 = M^2+4M+4 = M^2+6j+4$ with $j = 2M/3$, and $(M+2)(M+8) = M^2+10M+16 = M^2+6j+4$ with $j = 5M/3+2$; each is an integer because $3 \mid M$. Finally, if $M+2$ is composite then it has a prime factor $\le M$, so its four products were already closed by an older line and are not exceptions; likewise for $M+4$. $\blacksquare$

*Verification.* Zero violations over every $M = 9, 15, \dots, 19{,}999$ — **$3{,}332$ sectors.** In each, every open cell outside $E_M$ was checked to be a twin.

**Example, $M = 9$.** The sector $(81,225)$ has $24$ cells; $E_9 = \lbrace 6, 10, 14, 17, 21, 23\rbrace$, carrying
$$121 = 11^2,\quad 143 = 11\cdot13,\quad 169 = 13^2,\quad 187 = 11\cdot17,\quad 209 = 11\cdot19,\quad 221 = 13\cdot17 .$$
No other composite can inhabit an open cell of that sector.

**The count of exceptions is $0$, $2$, $4$ or $6$**, according to the primality of $M+2$ and $M+4$:

| $M+2$ | $M+4$ | maximum exceptions |
|---|---|---|
| composite | composite | $0$ |
| prime | composite | $4$ |
| composite | prime | $2$ |
| prime | prime | $6$ |

At $M = 999$ both $1001 = 7\cdot11\cdot13$ and $1003 = 17\cdot59$ are composite, so $E_M$ is empty and **all $93$ open cells of that sector are twin pairs** — as measured.

**What this buys, stated precisely.** Writing $C_M$ for the number of open cells, one has $T_M \ge C_M - |E_M| \ge C_M - 6$, so a twin follows from $C_M \ge 7$. Theorem 4 replaces that by the much weaker requirement
$$S_M \not\subseteq E_M, \tag{3.2}$$
where $S_M$ is the set of open indices: **a single open cell suffices, provided it is not at one of six named places.** And the six places are fixed by the geometry of the square — they are not chosen by the lines, whose phases are periodic and unrelated to $M$.

**And what it does not buy.** $C_M$ exceeds the twin count of the sector by at most six. Any lower bound on $C_M$ is therefore a lower bound on twins, and (3.2) is an exact reformulation rather than a route. We record it because it is the sharpest form the framework has produced of the twin criterion, not because it weakens the problem.

### 3.3 Raw cell count and main term

$$C = \frac{v^2-u^2}{6}-1, \qquad C_- = 4n-1  (u=6n-1), \qquad C_+ = 8n+3  (u=6n+1),$$
and $C \equiv 3 \pmod 4$ always (zero failures over 427 consecutive prime pairs) — an exact property which nevertheless supplies no protective invariant, since a single line's deletion count has no fixed parity. The main term is $M = C P_2$.

### 3.4 Local deviations

$$\varepsilon_r(u) = D_r(u) - \frac{2 N_{r^-}(u)}{r}. \tag{3.3}$$

Inside a sector, line $r$ deletes at $s \equiv -u^2/6$ and $s \equiv (2-u^2)/6 \pmod r$, and the gap between the two positions is exactly $3^{-1} \bmod r$ (zero failures among 85). **Every ruler's phase is therefore a function of the single quantity $u^2$**, and under $u \mapsto u+6$ the phase moves *quadratically*, since $u^2 \mapsto u^2 + 12u + 36$. This quadratic motion is what makes cancellation possible at all.

### 3.5 Theorem 5: a new line kills at most one pair in its own first window

The sector $[p^2,(p+2)^2)$ is where the line $L_p$ is born. Index gap-2 pairs by their offset from the centre $C = (p+1)^2$, writing $P(j) = (C+2j-1,\ C+2j+1)$ with $-p \le j \le p$, so the window holds exactly $2p+1$ pair slots. Let $T_p^-$ count the surviving pairs before $L_p$ is switched on, $T_p^+$ after, and $D_p = T_p^- - T_p^+$.

$L_p$ has exactly three strikes in this window: $p^2$, $p(p+2)$ and $p(p+4)$, since $p(p+6) > (p+2)^2$.

> **Theorem 5.** $D_p \in \lbrace 0,1\rbrace$ for every prime $p > 3$.

*Proof.* Three strikes, and each is disposed of by the grid $L_3$.

1. **$p^2$.** Of the two pairs it meets, only $(p^2, p^2+2)$ lies in the window — the other has index $-p-1$. For $p>3$, $p^2 \equiv 1 \pmod 3$, so $p^2+2 \equiv 0$: **that pair is already dead.**
2. **The strike divisible by $3$.** One of $p+2, p+4$ is $\equiv 3 \pmod 6$, so one of $p(p+2), p(p+4)$ lies on $L_3$ and was struck before $L_p$ existed; both pairs it meets were already dead.
3. **The surviving strike.** Call it $H_p = p(p+2)$ when $p \equiv 5 \pmod 6$ and $p(p+4)$ when $p \equiv 1 \pmod 6$. In either case $H_p \equiv 5 \pmod 6$, so $H_p - 2 \equiv 3 \pmod 6$ and the pair $(H_p-2, H_p)$ is **also already dead.**

Only $(H_p, H_p+2)$ remains. $\blacksquare$

> **Corollary 2.** $D_p = 1$ if and only if **two** primality conditions hold together:
> $$p \equiv 5 \ (6): \quad p+2 \ \text{prime} \ \text{ and } \ p(p+2)+2 \ \text{prime}; \qquad p \equiv 1 \ (6): \quad p+4 \ \text{prime} \ \text{ and } \ p(p+4)+2 \ \text{prime}.$$

*Proof.* $H_p$ survives the older lines iff its cofactor ($p+2$ or $p+4$) has no prime factor below $p$; being less than $2p$, that means the cofactor is prime. And $H_p+2 < (p+2)^2$ is not divisible by $p$, so if composite its least prime factor is below $p$ and it was struck earlier; hence $H_p+2$ survives iff it is prime. $\blacksquare$

*Verification.* Corollary 2 predicts $D_p$ from two primality tests alone; checked against the directly computed $D_p$ for every prime $5 \le p < 4000$, with **zero mismatches**. Examples: $p=5$ gives $7$ and $37$ both prime, so $D_5=1$; $p=11$ gives $13$ prime but $145 = 5\cdot29$ composite, so $D_{11}=0$; $p=13$ gives $17$ and $223$ both prime, so $D_{13}=1$.

**What this does and does not buy.** Since $T_p^+ = T_p^- - D_p$ and every survivor in the window is prime (the cofactor argument of §5.2), $T_p^+$ *is* the number of twin pairs in $[p^2,(p+2)^2)$. Theorem 5 therefore says:

$$\boxed{ T_p^- \ \text{is the twin count of the window, up to an error of } 0 \text{ or } 1, \text{ and the error is characterised.} }$$

That is the strongest local statement in this paper, and it is worth being explicit that it is not a reduction. $T_p^-$ and $T_p^+$ differ by at most one, so proving anything about $T_p^-$ is proving it about the twin count. In particular the sufficient condition "$T_p^- \ge 2$" is *stronger* than the conclusion "$T_p^+ \ge 1$", not weaker. What Corollary 2 adds is that even the discrepancy between the two is governed by a twin-like coincidence — two simultaneous primality conditions — so the error term is of the same nature as the quantity.

### 3.6 Theorem 6: the bridge pair, and the only law that knows about squares

Index gap-2 pairs by $x$ as above but on an absolute scale, the pair being $(2x+1, 2x+3)$. The window for odd $m$ begins at $a_m = (m^2-1)/2$ and holds $2m+1$ slots, while $a_{m+2} - a_m = 2m+2$. **So consecutive square windows do not abut: exactly one pair slot falls between them,**
$$g_m  =  a_m + 2m + 1, \qquad \text{the pair } \big((m+2)^2-2,\ (m+2)^2\big),$$
whose upper member is the next square itself. The line is partitioned as window, bridge, window, bridge, …, with no slack and no overlap.

Let $B$ count the bridges surviving a line set, over a full cycle of roots.

> **Theorem 6.** $B' = \big(q - 2 - \chi_q(2)\big) B$, where $\chi_q(2)$ is the Legendre symbol: $+1$ for $q \equiv \pm1 \pmod 8$ and $-1$ for $q \equiv \pm3 \pmod 8$.

*Proof.* The bridge at root $r$ dies under $q$ when $q \mid r^2$, i.e. $r \equiv 0$ — one class — or when $r^2 \equiv 2 \pmod q$, which has $1+\chi_q(2)$ solutions. The two conditions are disjoint for $q>2$, so $2+\chi_q(2)$ classes are lost. $\blacksquare$

*Verification.* $B = 2,\ 8,\ 32,\ 320,\ 3840,\ 53760,\ 967680$ for the line sets up to $3, 5, 7, 11, 13, 17, 19$, against $T = 1,\ 3,\ 15,\ 135,\ 1485,\ 22275,\ 378675$. Brute-forced from the definition for $\lbrace 3\rbrace$, $\lbrace 3,5\rbrace$, $\lbrace 3,5,7\rbrace$, $\lbrace 3,5,7,11\rbrace$: exact.

So the cycle fingerprint is not three numbers but four, with four distinct degrees:
$$(M, S, T, B)  \longmapsto  \big(qM,\ (q-1)S,\ (q-2)T,\ (q-2-\chi_q(2))B\big).$$
**$B$ is the only one of the four that knows the window is anchored at a square**, and the arithmetic that enters is whether $2$ is a quadratic residue.

> **Theorem 7 (the summation identity).** Over $M$ consecutive square windows,
> $$\sum_{i=0}^{M-1} T_{m+2i}  =  2(m+M) T  -  B .$$

*Proof.* The $M$ windows together with their $M$ bridges tile a stretch of $a_{m+2M}-a_m = 2M(m+M)$ pair slots, that is exactly $2(m+M)$ complete cycles, holding $2(m+M)T$ surviving pairs. The $M$ bridge roots are $M$ consecutive odd numbers, and since $M$ is odd they cover every residue class modulo $M$ exactly once, so exactly $B$ of them survive. $\blacksquare$

*Verification.* Checked for $\lbrace 3,5\rbrace$ and $\lbrace 3,5,7\rbrace$ at $m = 9, 15, 101$ — six cases, all exact.

**The collective bias, quantified.** Against the density prediction $T (2m+2M-1)$ for the same total length, the windows hold exactly $T-B$ fewer pairs; measured sums of deviations $-1, -5, -17, -185$ for the four line sets, matching $T-B$ each time. Now
$$\frac BT  =  \prod_q \Big(1 - \frac{\chi_q(2)}{q-2}\Big),$$
which converges: measured $2.5554,\ 2.5517,\ 2.5614,\ 2.5615,\ 2.5622$ at $z = 19,\ 10^3,\ 10^4,\ 10^5,\ 10^6$. The reduced product $\prod(1-\chi_q(2)/q)$ reaches $1.604401$ at $z = 10^6$ against
$$\frac{1}{L(1,\chi_8)} = 1.604556, \qquad L(1,\chi_8) = \frac{\log(1+\sqrt2)}{\sqrt2} = 0.623225 .$$
**So the square geometry enters this framework through a Dirichlet $L$-value at $1$ for the character modulo $8$.**

And the bias, though real, is not usable: $T-B \approx -1.56 T$ is a fixed number independent of $m$, spread over $M$ windows, so the deficit per window is $O(T/M)$ and vanishes against the per-window average as $M$ grows.

### 3.7 The square-phase mean, and the end of the "poor window" question

One may ask directly whether windows anchored at squares are systematically poorer than windows placed anywhere. The answer is an identity rather than an experiment.

For a window starting at $r^2$, the pair at offset $j$ survives $q$ exactly when $r^2 \not\equiv -2j$ and $r^2 \not\equiv -2j-2 \pmod q$. Writing $\rho_q(a) = \mathrm{card}\lbrace r : r^2 \equiv a\rbrace$ and $\nu_q(j) = \rho_q(-2j) + \rho_q(-2j-2)$ — the two conditions cannot hold at once — the average over **all square phases** is exactly
$$\mu_{\square}(L)  =  \sum_{j<L}\ \prod_{q} \frac{q - \nu_q(j)}{q}. \tag{3.4}$$

Computed against the naive density prediction $E = L\prod(q-2)/q$, and against the restricted average $\mu^{\times}$ over roots that are themselves coprime to every old line:

| $p$ | $T_p^-$ (actual) | $\mu_{\square}$ | $\mu^{\times}$ | $E = L\delta$ |
|---|---|---|---|---|
| 11 | 2 | 2.943 | 2.833 | 3.286 |
| 29 | 2 | 4.149 | 4.201 | 4.206 |
| 53 | 2 | 5.434 | 5.283 | 5.457 |
| 101 | 7 | 7.653 | 7.473 | 7.774 |
| 499 | 13 | 21.237 | 21.319 | 21.274 |
| 997 | 38 | 34.591 | 34.534 | 34.608 |

$\mu_{\square}$ agrees with $E$ to within about $1$% from $p = 29$ onward, and restricting the roots changes nothing.

> **The square-phase mean has the exact expression (3.4); numerically it tracks the generic density prediction closely, the two differing by about $1$% or less from $p = 29$ onward in the sample above.** So the exact quantity is available in closed form, and on the tested range it shows no bias at the level of the mean — which replaces the earlier control experiment with a computation, though not with a proof that the two agree in the limit. Individual windows are of course far from the mean — $T_{53}^- = 2$ against $\mu_{\square} = 5.43$ — but the scatter is governed by the correlation function of [II, Thm 4], not by any property of squares.

## 4. The closing budget: $\tau$ against $S$

**A change of object, stated before anything else.** Sections 2 and 3 concerned twins: a surviving cell, whose two members differ by $2$. The present section concerns a different graph — survivors joined to survivors at distance $6$ — and the two must not be run together, because the word “gap 6” would otherwise cover both the *letter* $6$ of §2.1 (a gap of $6$ between consecutive odd composites, which contains a twin) and the *edge* of length $6$ used here. **What an untouched edge exhibits once the remaining lines have acted is a prime pair $(p, p+6)$, not a twin pair.**

Measured, so that the distinction is not left rhetorical: inside $(P^2, 9P^2)$ at $P = 101$ there are $2{,}903$ edges, of which $1{,}865$ survive the remaining lines and $1{,}410$ are genuine gap-$6$ configurations — for instance $(10247,10253)$, $(10337,10343)$, $(10601,10607)$. **None of them is a twin.**

We keep the section because the budget it produces is exact, and because $(p,p+6)$ is open in precisely the same way and for precisely the same reason; but nothing here bears on the twin conjecture directly.

Instead of asking what the lines will close, we ask the dual question: **how many deletions are needed, at minimum, to close every distance-$6$ edge?** If the available deletions fall short, a pair survives.

### 4.1 Theorem 8 (the exact minimum cover)

Take survivors as vertices and join $x$ to $x+6$. Let $T$, $U$, $Q$ count the edges, the $3$-term runs and the $4$-term runs (runs, not components: a component on $k$ vertices contributes $\max(0,k-2)$ to $U$ and $\max(0,k-3)$ to $Q$).

> **Theorem 8.** The minimum number of deletions required to destroy every distance-$6$ edge is
> $$\tau = T - U + Q.$$

*Proof.* By Theorem 3 every component is a path on at most $4$ vertices, and the minimum vertex cover of a path on $k$ vertices is $\lfloor k/2 \rfloor$. Summing $(k-1)-(k-2)+(k-3)$ over components reproduces $\lfloor k/2\rfloor$ for $k = 2,3,4$ — and **only** for those, since $k=5$ would give $3$ against the true value $2$. The cap of Theorem 3 is thus exactly what makes the identity hold. $\blacksquare$

*Verification* by direct component decomposition:

| lines | component census | min cover | $T-U+Q$ |
|---|---|---|---|
| $\lbrace 5,7\rbrace$ | $\lbrace 1{:}4, 2{:}4, 3{:}4, 4{:}6\rbrace$ | 20 | 20 |
| $\lbrace 5,7,11\rbrace$ | $\lbrace 1{:}68, 2{:}56, 3{:}44, 4{:}42\rbrace$ | 184 | 184 |
| $\lbrace 5,7,11,13\rbrace$ | $\lbrace 1{:}1100, 2{:}788, 3{:}524, 4{:}378\rbrace$ | 2068 | 2068 |

**This is an exact combinatorial identity: no independence assumption and no density heuristic enters.**

### 4.2 Propagation laws

Let $G = T - D$ count genuine gap-$6$ pairs, $D$ those with a survivor between. *(The twins sit in $D$: the surviving middle differs by $2$ from one of the two endpoints. So $G$ — the object [V, §3.3] targets — is exactly the twin-free part, which is the content of the caution above. Incidentally, measured on all four cycles below, $U = D$ exactly; we do not use this.)*

> **Theorem 9.** On the full cycle, the entry of a new line $r$ gives
> $$T' = (r-2)T, \qquad D' = (r-3)D, \qquad G' = (r-2)G + D.$$

*Proof.* Of the $r$ copies of a pair, one has its left member struck and one its right, leaving $r-2$. A $D$-configuration has three sensitive positions (both ends and the middle), leaving $r-3$; and the copy whose middle is deleted becomes a genuine gap-$6$. $\blacksquare$

| lines | $V$ | $T$ | $D$ | $G$ |
|---|---|---|---|---|
| $\lbrace 5\rbrace$ | 8 | 6 | 4 | 2 |
| $\lbrace 5,7\rbrace$ | 48 | 30 | 16 | 14 |
| $\lbrace 5,7,11\rbrace$ | 480 | 270 | 128 | 142 |
| $\lbrace 5,7,11,13\rbrace$ | 5,760 | 2,970 | 1,280 | 1,690 |

> **Corollary 3.** On the full cycle, $\dfrac{T}{V} = \rho_p = \prod_{5\le s\le p}\dfrac{s-2}{s-1}$ and $\dfrac{D}{T} = \theta_p = \dfrac{2}{3}\prod_{7\le s\le p}\dfrac{s-3}{s-2}$ — **exact identities, not estimates.**

| $p$ | 23 | 53 | 101 | 199 | 499 | 997 |
|---|---|---|---|---|---|---|
| $\rho_p$ | 0.4358 | 0.3607 | 0.3151 | 0.2746 | 0.2367 | 0.2138 |
| $\theta_p$ | 0.3606 | 0.2967 | 0.2588 | 0.2253 | 0.1941 | 0.1753 |

Both tend to zero: distance-$6$ pairs become rarer, yet a growing share of those remaining become genuine gaps.

### 4.3 Theorem 10 (tail compression)

Inside $(P^2,9P^2)$, after the lines up to $P$ have acted, every surviving composite has the form $n=qr$ with
$$P<q<3P,\qquad q\le r<\frac{9P^2}{q}<9P.$$
Indeed three factors above $P$ would give $n>P^3>9P^2$ for $P>9$, and the smaller of the two remaining factors is below $3P$. Consequently the number of genuinely new strikes contributed later by a line $q$ with $P<q<3P$ is
$$E_P(q)=\pi(9P^2/q)-\pi(q-1)<2(3P-q)+1,$$
so a line approaching $3P$ loses power because the available cofactor interval contracts.

A related compression occurs among the **late lines in the sweep up to $P$ itself**:

> **Theorem 10.** For $P \ge 243$ and $P/3 < q < P$, every new strike of $q$ inside the window has the form $x = qr$ with $r$ **prime**.

*Proof.* The cofactor satisfies $r < 9P^2/q < 27P$. If $r$ were composite, all its prime factors would be $\ge q$ (it survived the smaller lines), so $r \ge q^2 > P^2/9$. The contradiction holds precisely when $P^2/9 \ge 27P$, i.e. $P \ge 243$. $\blacksquare$

**Finite check around the threshold.** Direct enumeration of new strikes with composite cofactor:

| $P$ | 101 | 151 | 199 | 211 | **241** | 251 | 307 | 499 | 997 |
|---|---|---|---|---|---|---|---|---|---|
| anomalies | 26 | 9 | 6 | 5 | **0** | 0 | 0 | 0 | 0 |

The enumeration exhibits anomalies at smaller $P$ and none in the tested cases from $241$ onward; this is consistent with, but stronger numerically than, the proved sufficient threshold $243$. The sharper pointwise condition is $q^3 > 9P^2$, i.e. $q > 9^{1/3}P^{2/3}$; and the two conditions cross exactly at
$$\frac{P}{3} = 9^{1/3}P^{2/3} \iff \frac{P^3}{27} = 9P^2 \iff P = 243,$$
so $243$ is the point at which the constraint $q > P/3$ becomes the binding one.

## 5. Clocks, and primality as a zero-test

### 5.1 Theorem 11 (the shift law) and primality

> **Theorem 11.** $\phi_q(p+2) = \phi_q(p) - 1 \pmod q$ for every old line $q$; and when $p$ itself becomes an old line, $\phi_p(p+2) = p-1$.

*Proof.* Substituting $p+2$ for $p$ in [III, (2.2)] subtracts $1$. For the second, $\phi_p(p+2) = (p-(p+2))/2 = -1 \equiv p-1$. $\blacksquare$

*Verification.* Zero failures among $4{,}983$ instances, and zero for the insertion rule.

Hence, writing $\Phi(n) = (\phi_3, \phi_5, \phi_7,\dots)$, the transition $n \mapsto n+2$ acts as
$$\Phi  \longmapsto  \Phi - 1, \tag{5.1}$$
each component on its own circle, and the whole system evolves by three small numbers:
$$\text{step } +4, \qquad \text{first square gap } +8, \qquad \text{all clocks } -1,$$
with one clock inserted at $p-1$ whenever $p$ is prime. The system is *shift, zero-test, insert*; nothing is rebuilt.

> **Corollary 4.** $p$ is composite if and only if some old clock reads $0$ at its birth. Equivalently, **a prime is a step at which no clock lands on zero.**

*Verification.* Zero failures over all odd $p < 2000$.

> **Corollary 5.** The clock of $L_3$ cycles $2 \to 1 \to 0$, so the two non-zero states are exactly the cell $(6a-1, 6a+1)$. **The cell, taken as a definition in [I, §3], is a consequence.**

### 5.2 Theorem 12 (surviving cofactors are prime)

> **Theorem 12.** For $p \ge 11$ and $p < t \le 9p$, a cofactor $t$ surviving all lines below $p$ is prime.

*Proof.* $t \le 9p < p^2$. A composite $t$ surviving all lines $<p$ would need two prime factors $\ge p$, giving $t \ge p^2 > 9p$. $\blacksquare$

*Verification.* Zero violations at $p = 11,13,17,101,499$.

Hence $J_j$, the number of new strikes in sector $j$, equals the number of **primes** among that block's cofactors. Primality appears as *a slot no ruler reached*, with no change to its definition.

**Worked example ($p=11$, computed without writing a single strike).**

| quantity | value |
|---|---|
| $\kappa_j$ | 0, 2, 4, 7, 10, 14, 18, 22, 27, 32, 38, 44 |
| $H_j$ | 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6 |
| clocks | $\phi_3=2$, $\phi_5=2$, $\phi_7=5$ |
| $J_j$ | 1, 2, 1, 2, 1, 3, 1, 2, 3, 2, 2 |

The "new" cofactors are exactly $13,17,19,23,\dots,97$, all prime, as Theorem 12 requires.
### 5.3 The general form: a row reads primality off originality

Theorem 12 is the case that arises inside one sector. Read along the whole row of $p$ it has a general form, and the general form is worth stating because it makes the twin condition geometric.

Call a cell of the row **original** if no line below $p$ owns it. Everything before $p^2$ is inherited — a strike $p m$ with $m < p$ carries the smallest prime factor of $m$, which is below $p$ — so $p^2$ is the first original cell on the row. Past it:

> **Theorem 13.** For $p$ prime and $p \le p+2j < p^2$,
> $$p (p+2j) \ \text{ is original with respect to the lines below } p \quad\Longleftrightarrow\quad p+2j \ \text{ is prime}.$$

*Proof.* If $p+2j$ is composite and below $p^2$ its least prime factor is below $p$, so that line already owns the cell. If $p+2j$ is prime it has no factor below $p$ at all, and $p$ itself begins at $p^2$. $\blacksquare$

*Verification.* Zero failures over $1{,}782{,}933$ instances: every prime $p < 400$ and every $j$ with $p+2j < p^2$.

**So a row is a reader.** The row of $p$ carries, in the originality of its cells, the primality of every odd number from $p$ up to $p^2$ — one bit per cell, with no change to the definition of a prime. Two consequences are worth recording.

**First, the twin condition becomes a two-step statement at the diagonal.** The cells at $p^2$ and $p(p+2)$ are the first two on the row past the inherited region, and by Theorem 13
$$(p, p+2)\ \text{is a twin pair} \quad\Longleftrightarrow\quad \text{originality survives one step past } p^2 .$$
Writing $\mathsf O$ for original and $\mathsf I$ for inherited, the row crosses the diagonal as $\dots\mathsf I \mid \mathsf O \mathsf O\dots$ at a twin and $\dots\mathsf I\mid \mathsf O \mathsf I\dots$ otherwise: at $p=23$, $529$ is original but $575 = 23\cdot 5^2$ is not, and $(23,25)$ is not a twin.

**Second, the shadow lies on a curve already in the series.** The tested cell is
$$p (p+2)  =  (p+1)^2 - 1,$$
so every twin test sits one unit below an even square: $35 = 36-1$, $143 = 144-1$, $323 = 324-1$, $899 = 900-1$. **That is [I, Thm 5] read along the row instead of across the window** — the cell $(n^2-1,\ n^2+1)$ with $n = p+1$, whose lower member $(n-1)(n+1)$ is composite by construction. The two statements are the same fact.

**And the reformulation is exact, which is precisely why it is not progress.** Writing $\sigma(p)$ for the smallest line owning $p(p+2)$, one has $\sigma(p) = \mathrm{spf}(p+2) \le \sqrt{p+2}$ when $p+2$ is composite, and $\sigma(p) = \infty$ exactly when $(p,p+2)$ is a twin. Proving $\sigma(p) = \infty$ infinitely often is proving the twin conjecture, in the same words. What the row picture adds is a suggestion — that if twins were finite, every new diagonal point would need its shadow claimed by some line below $\sqrt p$ — and the suggestion does not survive measurement: over $6{,}835$ composite cases with $p < 200{,}000$ the claimant is at most $13$ in $63.6$% of them and at most $100$ in $89.9$%, the counts being $5$: $2248$, $7$: $1125$, $11$: $557$, $13$: $415$, $17$: $303$. **The $\sqrt p$ bound is nowhere near tight; the shadows are claimed by the smallest lines, not by a delicate conspiracy of many.**


## 6. Inheritance across sectors, and the capacity of a single line

Sections 2–5 treat one sector at a time. This section treats the *sequence* of sectors, indexing them by $M = 9, 15, 21, \dots$ — the odd multiples of $3$ — with the sector $(M^2, (M+6)^2)$ carrying $A(M) = 2M+6$ cells. Three exact laws come out, all sharper than the average statement "line $q$ removes $2/q$ of what remains", because each is a statement about a *named* gap rather than about a count.

### 6.1 Theorem 14: the sector inheritance law

Fix any finite set of lines $p_1 < \dots < p_r$ above $3$, and put
$$Q = \prod_i p_i, \qquad S = \prod_i (p_i - 2),$$
so that $S$ cells survive that set in each cycle of $Q$ consecutive cells. Let $B(M)$ be the number of cells of the sector at $M$ that survive those lines.

> **Theorem 14.** $B(M + 6Q)  =  B(M)  +  12 S.$

*Proof.* Two facts. First, the sector grows by exactly $12Q$ cells: $A(M+6Q) - A(M) = 12Q$. Second — and this is what makes the law exact rather than approximate — the **phase is preserved**: the sector at $M$ begins near cell $M^2/6$, and
$$\frac{(M+6Q)^2}{6} - \frac{M^2}{6}  =  2MQ + 6Q^2  \equiv  0 \pmod Q .$$
So the first $A(M)$ cells of the later sector repeat the earlier sector's pattern exactly, and the tail of $12Q$ new cells is precisely twelve complete cycles, each leaving $S$ survivors. $\blacksquare$

*Verification.* Exact at every $M$ tested, for each of the three sets: $\lbrace 5\rbrace$ ($Q=5$, $S=3$, increment $36$); $\lbrace 5,7\rbrace$ ($Q=35$, $S=15$, increment $180$); $\lbrace 5,7,11\rbrace$ ($Q=385$, $S=135$, increment $1620$).

**What it says.** A *fixed* set of old lines never catches up with the window. Each time its cycle returns to the same phase, the sector has grown, and a known positive number $12S$ of fresh open cells appears. Only lines born after the set was fixed can close them.

### 6.2 Theorem 15: the capacity of one new line on one family

Each survivor of the fixed set appears in the new tail exactly twelve times, at cells
$$x,\ x+Q,\ x+2Q,\ \dots,\ x+11Q,$$
which we call a **family**. A new line $q$ closes a cell $c$ when $c \equiv \pm 6^{-1} \pmod q$, so on a family it closes the copies $t$ solving $x + tQ \equiv \pm 6^{-1}$. There are two such $t$ modulo $q$, and their separation does not depend on $x$:

> **Theorem 15.** Put $\Delta_q \equiv (3Q)^{-1} \pmod q$ and $d_q = \min(\Delta_q,\ q - \Delta_q)$. Then a line $q > 11$ closes at most two copies of any family, and **at most one** whenever $d_q > 11$.

*Proof.* The two solutions differ by $2\cdot 6^{-1} Q^{-1} = (3Q)^{-1}$, whose least absolute representative is $\pm d_q$. Two copies lie in the family only if two values of $t \in \lbrace 0,\dots,11\rbrace$ differ by $d_q$, which needs $d_q \le 11$. $\blacksquare$

*Verification.* For $Q = 385$, brute force over all $x$ and all $q$ from $13$ to $101$ reproduces the predicted capacity with **zero mismatches**. Sample values of $d_q$: $13{:}6$, $17{:}1$, $19{:}5$, $23{:}9$, $31{:}4$, $37{:}14$, $53{:}24$, $83{:}12$, $101{:}39$.

### 6.3 Corollary 6: the exceptional lines are finite in number

> **Corollary 6.** A line $q$ can close two copies of a family only if $q \mid 3Qr \pm 1$ for some $1 \le r \le 11$. Consequently every $q > 33Q + 1$ closes **at most one** copy of every family.

*Proof.* $d_q \le 11$ means $\Delta_q \equiv \pm r$ with $r \le 11$, i.e. $3Qr \equiv \pm 1 \pmod q$; and $0 < 3Qr \mp 1 \le 33Q+1$, so $q$ cannot divide it once $q$ exceeds that bound. $\blacksquare$

For $Q = 385$ the threshold is $12{,}706$. This is a genuinely local statement: it names, for each family, a bound on what a *specific* line can do, whereas $2/q$ only bounds a total.


---

## 7. The gate belt: what a line can do between its own square and the next

Sections 3–6 work inside a sector bounded by consecutive odd squares. This section changes the unit: since every prime $q>3$ has $q^2 \equiv 1 \pmod 6$, each prime has a **gate** $G_q$ with $q^2 = 6G_q+1$, and the cell $C_{G_q} = (q^2-2, q^2)$ is closed by $q$ itself. Consecutive primes $q<r$ therefore delimit a **belt** of cells $C_{G_q+1},\dots,C_{G_r-1}$ between two gates that are certainly closed. The belts tile the cell axis.

### 7.1 Theorem 16: the size of a belt

> **Theorem 16.** For consecutive primes $q<r$ with $g = r-q$, the belt holds exactly
> $$G(q,r)  =  \frac{r^2-q^2}{6}-1  =  \frac{g(2q+g)}{6}-1$$
> cells, so its size grows like $qg$.

*Proof.* Both $q^2$ and $r^2$ are $\equiv 1 \pmod 6$, so the cells strictly between the two gates are exactly the $(r^2-q^2)/6 - 1$ complete cells of $L_3$ in the interval. $\blacksquare$

*Verification.* $G = 3, 11, 7, 19, 11, 27, 51, 19, 67, 247, 67, 667, 4011$ for the belts $5\to7$ through $997\to1009$; each reproduces from the formula.

### 7.2 Verified Law 17: the new line's reach depends on the gap, not on its size

> **Verified Law 17 (conditional).** Suppose $g^2 < 2q$. Then, within its own belt, the number of cells the line $L_q$ can strike at all is
> $$H_q  =  \left\lfloor \frac{2g}{3}\right\rfloor,$$
> **independent of $q$.**

*Proof under the hypothesis.* If $g^2 < 2q$ the line completes no extra lap before the next gate, so it reaches only the cofactors $q+2, q+4, \dots, q+2g$, giving $g$ candidate strikes; one in every three falls on $L_3$ and so touches no cell of the grid, leaving $\lfloor 2g/3 \rfloor$. $\blacksquare$

**We do not call this a theorem, because the hypothesis is not available.** $g^2 < 2q$ is far weaker than Cramér's conjecture $g = O(\log^2 q)$, which would give it at once — but it is **stronger than anything currently proved, and stronger than the Riemann hypothesis supplies**: RH gives only $g \ll \sqrt q \log q$, hence $g^2 \ll q\log^2 q$, which does not suffice. **Verified over $17{,}981$ belts, every consecutive prime pair with $q < 200{,}000$: no failure.**

**The consequence is worth stating plainly.** The belt has $\sim qg/6$ cells and the line born at its left end can touch $\sim 2g/3$ of them. **For a twin gap $g=2$ the line touches exactly one cell, however large $q$ is** — one cell out of $\sim q/3$. A line at $q \approx 10^6$ entering a belt of some hundred thousand cells has a single strike available before the next gate opens.

### 7.3 The collapse of the new line's effect

Raw reach is not closing power: a strike may land on a cell an older line has already closed. Write $K_q$ for the cells the new line closes **first**.

| belt | $G$ | $H_q$ | $K_q$ | twins left |
|---|---|---|---|---|
| $5\to7$ | 3 | 1 | 1 | 2 |
| $7\to11$ | 11 | 2 | 2 | 4 |
| $11\to13$ | 7 | 1 | **0** | 2 |
| $13\to17$ | 19 | 2 | 1 | 7 |
| $17\to19$ | 11 | 1 | **0** | 2 |
| $23\to29$ | 51 | 4 | **0** | 8 |
| $31\to37$ | 67 | 4 | **0** | 11 |
| $89\to97$ | 247 | 5 | **0** | 21 |
| $101\to103$ | 67 | 1 | **0** | 7 |

*Measured over every consecutive prime pair below $5{,}000$:* $K_q = 0$ in $71.1$% of belts with $q<1000$ and $76.8$% of belts with $1000<q<5000$; mean $K_q$ falls from $0.331$ to $0.259$; the maximum ever observed is $3$. **A new line typically arrives at its own gate to find that the work has already been done.**

**A monotone version of this is false, and we record it because it is the natural guess.** It is not the case that a newer line always closes fewer cells than every older one: in the belt $31\to37$ the first closures are $17:1$, $19:3$, $23:2$, $29:3$, so $29$ — newer than $19$ and $23$ — closes more than both. **The weakness is collective, not line by line.**

### 7.4 A deterministic ceiling for a whole age layer

Nothing above uses primality of the intermediate lines, and the next bound deliberately gives them more power than they have.

> **Proposition 1.** In the belt $q\to r$ of length $L = r^2-q^2$, any line $s$ makes at most $\lceil L/2s \rceil$ strikes, of which at most a fraction $2/3$ touch cells of the grid. Hence, allowing **every** odd $s$ not divisible by $3$ in a range to act as an independent line and ignoring all overlap between them, the layer $q-D \le s \le q$ can close at most
> $$C_D(q,r)  =  \sum_{\substack{q-D \le s \le q\cr  s \text{ odd},\ 3\nmid s}} \left\lceil \tfrac{2}{3}\left\lceil \tfrac{L}{2s}\right\rceil\right\rceil$$
> cells.

For the belt $499 \to 503$ ($G = 667$): the newest quarter has ceiling $C = 168$ ($25$% of the belt) and closes $6$ in fact; the newest half has ceiling $376$ ($56$%) and closes $15$. For $997 \to 1009$ ($G = 4011$): the newest tenth has ceiling $316$ and closes $14$; the newest quarter $836$ and closes $28$; the newest half $1{,}977$ — under half the belt — and closes $68$. **The ceilings are generous by one to two orders of magnitude, and the real burden falls on lines far below $q/2$.**

### 7.5 And why the layer ceilings do not close the argument

Proposition 1 invites an obvious attempt: build the full pyramid of age layers $(q/2,q]$, $(q/4,q/2]$, … down to $s=5$, sum the ceilings, and hope the total falls short of $G$. **It does not.**

| belt | $G$ | $\sum$ ceilings over all layers | ratio |
|---|---|---|---|
| $499\to503$ | 667 | 2,094 | $3.1\times$ |
| $997\to1009$ | 4,011 | 13,935 | $3.5\times$ |
| $10007\to10009$ | 6,671 | 35,045 | $5.3\times$ |

and the cumulative total already passes $G$ at the **second** layer.

The asymptotic is worth getting right, because it is the point of the section. **The sum runs over every $s$ coprime to $6$, not over the primes**, and those have density $1/3$, so
$$\sum_{\substack{s \le q\cr (s,6)=1}} \frac1s  =  \frac13\log q + O(1), \qquad\text{whence}\qquad \sum_s \tfrac23\cdot\tfrac{L}{2s}  =  \frac L3\sum_s\frac1s  \sim  \frac L9 \log q .$$
Against $G \sim L/6$ the ratio is therefore
$$\frac{\sum_s C_s}{G}  \sim  \frac23\log q$$
— a **logarithm**, not an iterated logarithm. Checked against the table: $\tfrac23\log(q/4)$ gives $3.22$, $3.68$, $5.22$ at $q = 499,\ 997,\ 10007$ against the measured $3.14$, $3.47$, $5.25$.

> **So the belt decomposition establishes three of the four things one would want — the belt grows like $qg$, the new line's reach is $O(g)$ and independent of $q$, and no fixed set of old lines can serve arbitrarily long belts — and refutes the fourth. The moving tail of recent lines is not capacity-limited; its ceilings exceed the belt by a factor that grows.** What is left is the forced overlap between the layers, which is $\prod(1-2/q)$ and describes the cycle, not the belt. This is [V, §6] again, reached from the belt side.

---

## 8. Four named cells inside the window

Paper I, §4, indexes the window by its own cell numbers: it is the interval $c_0,\dots,c_0+N-1$ with $c_0 = 6a^2-2a+1$ and $N = 4a-1$, where $n = 6a$ and the window is $[(n-1)^2,(n+1)^2]$. This section uses that indexing to study the four cells nearest its two ends.


### 8.1 The four tracks, their character conditions and their densities

The window's template [I, §4.2] singles out four cells near its two ends. Writing $q = 6a-1$ they are
$$A = (q^2{+}4,\ q^2{+}6), \quad B = (q^2{+}10,\ q^2{+}12), \quad C = ((q{+}2)^2{-}14,\ (q{+}2)^2{-}12), \quad D = ((q{+}2)^2{-}8,\ (q{+}2)^2{-}6),$$
and as $a$ runs they trace four **tracks**. Substituting $q = 6a-1$ makes every member a quadratic in $a$:

| cell | lower member | upper member |
|---|---|---|
| $A$ | $36a^2-12a+5$ | $36a^2-12a+7$ |
| $B$ | $36a^2-12a+11$ | $36a^2-12a+13$ |
| $C$ | $36a^2+12a-13$ | $36a^2+12a-11$ |
| $D$ | $36a^2+12a-7$ | $36a^2+12a-5$ |

*Verification.* Exact for $a = 1,\dots,399$.

> **Theorem 18 (which lines can ever own a track).** A prime $r$ divides $36a^2+Ba+C$ for some $a$ exactly when the discriminant $B^2-144C$ is a quadratic residue modulo $r$. For the eight members the discriminants are $144k$ with
> $$k  =  -4,\ -6 \ (A); \qquad -10,\ -12 \ (B); \qquad 14,\ 12 \ (C); \qquad 8,\ 6 \ (D),$$
> so the conditions read $r \equiv 1 \pmod 4$ and $(-6 | r) = 1$ for $A$; $(-10 | r)=1$ and $r \equiv 1 \pmod 3$ for $B$; $(14 | r)=1$ and $(3 | r)=1$ for $C$; $r \equiv \pm1 \pmod 8$ and $(6 | r)=1$ for $D$.

*Verification.* Every prime factor of every member for $a = 1,\dots,400$ — $4{,}209$ checks — satisfies its condition; no violation.

Each individual condition admits half the primes (measured over primes below $10^5$: $49.7$–$50.0$%), but a cell falls to a strike on **either** member, so the union admits three quarters: measured $75.0,\ 74.8,\ 75.0,\ 75.0$% for $A,B,C,D$. Requiring eligibility for all four at once cuts this to **exactly a quarter** — the eight discriminants reduce to the five independent characters $(-1),(2),(3),(5),(7)$, giving $32$ sign patterns of which $8$ pass; measured $24.84$% against the naive independent guess $(3/4)^4 = 31.6$%.

**The four tracks are not equivalent.** Each is a pair of quadratics, so its twin density is governed by a Bateman–Horn constant $S = \prod_r (1-\nu_r/r)/(1-1/r)^2$, where $\nu_r$ counts the roots of the pair modulo $r$. The correct baseline is a generic cell $(6c-1,6c+1)$, whose constant is $12C_2 = 7.9220$ — **not** the twin constant $2C_2 = 1.320$, which is for pairs $(n,n+2)$ over all $n$ and counts the even $n$ a cell never has.

| track | $\nu_5$ | $\nu_7$ | $\nu_{11}$ | $S$ | $S/12C_2$ |
|---|---|---|---|---|---|
| $A$ | **4** | 2 | 2 | $3.230$ | $0.408$ |
| $B$ | 1 | 4 | 2 | $5.797$ | $0.732$ |
| $C$ | 2 | 1 | 4 | $8.739$ | $1.103$ |
| $D$ | 2 | 2 | **0** | $11.324$ | $1.429$ |

*Verification.* Predicted density $S/\log^2(36a^2)$ against measured, for $a = 12{,}000,\dots,30{,}000$: $0.0059/0.0062$, $0.0105/0.0100$, $0.0158/0.0156$, $0.0205/0.0214$.

**So track $D$ is $3.5$ times richer in twins than track $A$**, and the reason is visible in the table: $\nu_{11} = 0$ for $D$ — eleven never divides either of its members — while $\nu_5 = 4$ for $A$, the maximum, five dividing both members with two roots each. *(This is directly usable: a search for twin pairs near squares is three and a half times more productive on the $D$ track than on the $A$ track.)*

### 8.2 Theorem 19: simultaneity, and why it is the sharp question

Eligibility asks which primes can own a track at **some** $a$. The sharper question is which can own two tracks at the **same** $a$, and the answer is finite.

> **Theorem 19.** A prime $r > 3$ can close two of $A,B,C,D$ in the same window only if it divides the resultant of the corresponding pair of quadratics. The complete list is
>
> | pair | admissible primes |
> |---|---|
> | $A$ & $B$ | **none** |
> | $A$ & $C$ | $5,\ 11,\ 13,\ 73$ |
> | $A$ & $D$ | $5,\ 7$ |
> | $B$ & $C$ | $5,\ 7,\ 11,\ 13,\ 37$ |
> | $B$ & $D$ | $7,\ 19,\ 89,\ 97$ |
> | $C$ & $D$ | **none** |
>
> so the union is the nine primes $\lbrace 5,7,11,13,19,37,73,89,97\rbrace$, and **every $r > 97$ closes at most one of the four cells in any single window.**

*Proof of the two empty entries.* The differences between a member of $A$ and a member of $B$ are $4$, $6$ and $8$; a prime dividing one member of each would divide one of these, impossible for $r>3$. The same three differences occur between $C$ and $D$. $\blacksquare$

*Proof of the rest.* Two quadratics with the same leading coefficient differ by a linear form, so a common root modulo $r$ forces a linear congruence in $a$; substituting it back leaves a fixed integer that $r$ must divide. For $A$ lower against $C$ lower, for instance, $24a \equiv 18$ gives $4a \equiv 3$ and then $r \mid 65$. Each entry above was computed as the resultant and then checked for a genuine common root. $\blacksquare$

**The contrast is the point.** Eligibility for one cell admits three quarters of all primes; for all four at once, a quarter — both infinite. **Simultaneous double duty admits nine primes and no more.** The character condition loses the shared variable $a$; restoring it collapses an infinite set to a finite one, and this is the sharpest local statement in the paper after Corollary 6.

**And, as with every local statement here, it does not bind.** Closing all four cells requires at least two lines — a special prime may serve $A$ & $C$ and another $B$ & $D$ — and at most four. Measured over $a = 3000,\dots,10000$: of $7{,}000$ windows, $6{,}512$ have all four closed, using two distinct lines in $973$ cases, three in $4{,}748$ and four in $791$, so one of the nine special primes does double duty in $5{,}721$ of them. Against this, the lines available number $\pi(q) = 428$, $2{,}062$ and $6{,}055$ at $a = 500$, $3000$, $10000$. **Four out of six thousand is free.**

---


### 8.3 Proposition 2: and why Theorem 19 does not obstruct anything

Theorem 19 is sharp, and it is sharp for one line. The next statement shows that it dissolves the moment one is allowed four, and it dissolves by construction rather than by measurement.

> **Proposition 2.** Let $k$ tracks be given, each a pair of quadratics in $a$, and let $N$ be any bound. Then there is an arithmetic progression of $a$ — infinite, explicit, and computable — along which all $k$ tracks are closed simultaneously, every closing line exceeding $N$ and all $k$ of them distinct. Any finite number of further congruence conditions may be imposed at the same time.

*Proof.* For each track choose a prime $r_i > N$, distinct from the others, whose discriminant condition (Theorem 18) is satisfied, and a root $a_i$ of one of its members modulo $r_i$. The $k$ conditions $a \equiv a_i \pmod{r_i}$ have pairwise coprime moduli, so the Chinese remainder theorem combines them into a single class modulo $\prod r_i$. Further conditions on coprime moduli are appended the same way. $\blacksquare$

**The contrast with Theorem 19 is the whole point.** There the same line had to satisfy two conditions *at the same $a$*, which is a genuine constraint and collapsed an infinite set to nine primes. Here the conditions sit on different moduli, and the shared variable costs nothing.

*Explicit instance, with every step verified.* Take
$$101 \mid A^-, \ a \equiv 54; \qquad 103 \mid B^-,\ a \equiv 15; \qquad 107 \mid C^-,\ a \equiv 73; \qquad 113 \mid D^-,\ a \equiv 77,$$
four distinct lines, all above $97$. The Chinese remainder theorem gives
$$a \equiv 107{,}106{,}110 \pmod{125{,}782{,}673},$$
and along this progression $A$, $B$, $C$ and $D$ are all closed. Adjoining the further condition $5 \mid q+2$, i.e. $a \equiv 4 \pmod 5$ — which makes the new line's own central strike $q(q+2)$ inherited rather than new, so that the centre is not a twin either — gives
$$a \equiv 484{,}454{,}129 \pmod{628{,}913{,}365}, \qquad\text{i.e.}\qquad q \equiv 2{,}906{,}724{,}773 \pmod{3{,}773{,}480{,}190}.$$
The residue and the modulus are coprime, so by Dirichlet's theorem the progression contains infinitely many primes $q$. **Along it, $q$ is prime, $q+2$ is composite, and all four named cells are closed — permanently and by construction.**

> **So no fixed number of named cells can force a twin.** Whatever finite list of tracks one selects, one distinct line may be assigned to each and the conditions combined; the construction is immune to how large the tracks' moduli are required to be, and it survives the addition of any finite list of side conditions. **An argument of this shape can only begin to bite when the number of cells grows with the window**, so that the number of conditions grows too and the assignment of a private line to each ceases to be free.

We state this as a proposition rather than a remark because it is the reason to stop, and knowing why one stops is worth more than another negative measurement.

---

## 9. What this paper establishes, and what it does not

**Proved here.** The gap alphabet and the ladder (Theorems 1–3, Corollary 1); the belt size and the layer ceiling (Theorem 16, Proposition 1); the character conditions on the four outer tracks, the nine-element simultaneity set, and the construction that shows it obstructs nothing (Theorems 17, 18, Proposition 2); the six exception positions (Theorem 4); the single-kill bound in a line's own first window and its characterisation (Theorem 5, Corollary 2); the bridge law and the summation identity over a cycle of windows (Theorems 6, 7); the exact minimum cover and the propagation and compression laws (Theorems 8–10, Corollaries 3–5); the shift law, the primality of surviving cofactors, and the originality law on a row (Theorems 11, 12, 13); and the sector inheritance and single-line capacity laws (Theorems 13, 14, Corollary 6).

**Verified but not proved.** Verified Law 17 (the reach $\lfloor 2g/3\rfloor$), proved under $g^2 < 2q$ — a hypothesis weaker than Cramér but stronger than the Riemann hypothesis supplies; checked on $17{,}981$ belts with $q < 200{,}000$ without failure.

**Not here.** Every one of these is an *exact* statement — an identity, a cap, or an explicit list. None is a lower bound, and a lower bound is what the twin conjecture needs. Each of the criteria above turns out, on inspection, to require a lower bound on a quantity that exceeds the twin count of a sector by at most a constant; the criteria are therefore exact reformulations rather than routes.

The measurements that establish that, the two test cases against which the framework was checked, and the account of where and why it stops, are **Paper V**.


---

## References

The companion papers are cited as [0], [I], [II], [III], [V]. This paper imports only their definitions and proves everything else; the external literature is discussed in Paper V, where the framework is compared with it.
