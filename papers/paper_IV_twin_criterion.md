# The Twin Criterion in Cell Coordinates

## IV. What the framework proves about twin pairs

---

### Abstract

This paper collects what the cell coordinates prove outright about the twin problem. The measurements, the two test cases and the account of where the framework stops are Paper V.

The gap between consecutive odd composites takes only the values $2$, $4$ and $6$, and gap $6$ *is* a twin pair (Theorem 1), so the twin conjecture becomes the statement that the maximal possible gap is attained infinitely often — a cap that is free and proved. Below it the ladder is complete: gap $2$ needs no prime, gap $4$ one use of Dirichlet, gap $6$ two primes simultaneously (Theorems 2, 3).

The central result is local. After switching on every line $p \le M$ in the sector $(M^2,(M+6)^2)$, **at most six cells can be open without being a twin pair, and their positions are given by an explicit formula in $M$** (Theorem 4). The lines $5$ and $7$ alone cut six to three, and the three occur only when $(M+2,M+4)$ is itself a twin, so a twin follows from three open cells rather than seven (Corollary 2). Over a full period of $35$ sectors the budget falls to $31$, and no finite set of lines lowers it further: one configuration survives every residue argument and is admissible at every prime, so killing it would contradict Hypothesis H rather than weaken the twin problem (§3.3).

The remaining sections read the same window in four other units — the clock, in which primality is a zero-test and originality along a row is primality of the cofactor (Theorems 8–10); the sequence of sectors, which a fixed set of lines never catches (Theorems 11, 12); the belt between consecutive prime gates, where the newly born line's reach depends on the gap and not on its size (Theorem 13, Verified Law 14); and four named quadratic tracks near the window's ends, whose densities differ by a factor of three and a half and on which simultaneous double duty admits exactly nine primes (Theorems 15, 16).

Each of these is exact, and none of them binds. Proposition 5 says why, by construction rather than by measurement: give each of any fixed list of named cells its own line and combine the congruences, and one obtains an explicit infinite progression along which every one of them is closed while $q$ is prime and $q+2$ composite. **No fixed number of named cells can force a twin**; an argument of this shape can bite only when the number of cells grows with the window. Two appendices carry exact material that is not part of the twin argument, the second of them an auxiliary model whose object is a prime pair $(p,p+6)$.

**No progress toward the twin-prime conjecture is claimed.** Every statement here is exact; none of them is a lower bound on anything.
**How to read the claims in this paper.** Statements set as Theorems, Propositions and Corollaries are proved, and the proofs are given. Everything else falls into two kinds, and we try to keep them apart. A *measurement* is a computation over a stated finite range; it is labelled with that range, and it supports a claim about that range only. A *reading* is our own judgement about what a measurement or a proof appears to mean — where a route seems to lead, why an attempt seems to fail — and we mark it as ours rather than stating it as established. Where the two are easy to confuse we say which is which, and where we are unsure we say that too.



**Keywords:** twin primes, gap alphabet, minimum vertex cover, sieve cycles, cell coordinates.

**MSC 2020:** 11N35, 11N05, 11A41.

---

## Summary of the main results

*Grouped by section. Each line is informal; the precise statement and its proof are in the section named on the right. One result is labelled **Verified Law**: it is checked exactly on a stated finite range and is **not** proved. Statements marked **M** are measurements reported alongside the theorems they qualify, not theorems themselves.*

**§2 — The gap alphabet, and the ladder of proofs**

| Result | What it says | Section |
|-------------|----------------------------------------------------|---------|
| **Theorem 1** | The gap between consecutive odd composites takes only the values $2$, $4$ or $6$. | §2.1 |
| **Theorem 2** | Gaps $2$ and $4$ occur infinitely often with no prime input; gap $6$ infinitely often is *equivalent* to the twin conjecture. | §2.2 |
| **Theorem 3** | On one rail, no five survivors above $5$ lie in arithmetic progression of step $6$. | §2.3 |
| **Corollary 1** | The run counts $G_k$ at spacing $6$ obey $G_k = \prod(q-k)$, capping runs at four. | §2.3 |

**§3 — The twin problem inside the framework**

| Result | What it says | Section |
|--------------------|-------------------------------------|-----------------|
| ***The pivot*** | Inside $(u^2,v^2)$ with every line up to $u$ switched on, **a cell that survives *is* a twin pair** — no primality test is needed. Everything downstream rests on this. | §3.1 |
| **Theorem 4** | At most **six** cells of a sector can be open without being twin pairs, with their positions given explicitly in $M$. | §3.2 |
| **Corollary 2** | The dichotomy: if $(M+2,M+4)$ is not a twin then $\lvert S_M \cap E_M\rvert  \le 2$, so the sufficient count falls from $C_M \ge 7$ to $C_M \ge 3$. | §3.2 |
| **Proposition 1** | The admissible exceptional configurations in a block of $N = 35L$ sectors number $B_L \ll L/\log^2 L$, by the Selberg sieve. | §3.4, App. C.1 |
| **Theorem 5** | A newly born line closes **at most one** twin cell in its own first window: $D_p \in \lbrace 0,1\rbrace$. | §3.5 |
| **Corollary 3** | $D_p = 1$ exactly when two primality conditions hold together, so the error term is itself twin-like. | §3.5 |
| **Theorem 6** | The bridge pair: $B' = (q-2-\chi_q(2))B$ — the only law here that knows the window is anchored at a square. | §3.6 |
| **Theorem 7** | The summation identity over $M$ consecutive square windows. | §3.6 |
| ***Recorded, not used*** | Two constructions that do not help — the balanced window, and ownership through the cofactor — kept so they are not retried. | §3.8, App. C.3 |
| **Proposition 6** | The odd Bonferroni truncation is a **proved** lower bound on $C_M$, evaluated in one pass by the multiplicity $m(d)$, and exact once the order reaches $\max_d m(d)$ — which grows like $\log\log M$, not like $\pi(M)$. | §3.9 |
| ***Placement*** | The same finite-window obstruction, reached independently from the Goldbach side. | §3.10 |
| **Propositions 7–9** | A mirror law for the sector index; the exact discrepancy $s(d-s)/(dH)$ of a Fejér window, whence $d/(4H)$; and $\ll d^3/(HT^2)$ for a moving one, with a sharp exponent. The kernels are classical and cited; together they gain a factor of nine on $L_7$ and **reach none of $S_5$ and beyond**. | §3.11, App. C.4 |

**§4 — Clocks, and primality as a zero-test**

| Result | What it says | Section |
|-------------|----------------------------------------------------|---------|
| **Theorem 8** | The shift law $\phi_q(p+2) = \phi_q(p) - 1 \pmod q$ for every old line. | §4.1 |
| **Corollary 4** | $p$ is composite **iff** some old clock reads $0$ at its birth. | §4.1 |
| **Corollary 5** | The clock of $L_3$ cycles $2 \to 1 \to 0$, so its two non-zero states are exactly the two rails. | §4.1 |
| **Theorem 9** | Surviving cofactors are prime, for $p \ge 11$ and $p \lt t \le 9p$. | §4.2 |
| **Theorem 10** | A row reads primality off originality — a recoding of trial division, not a new test. | §4.3 |

**§5 — Inheritance across sectors, and the capacity of one line**

| Result | What it says | Section |
|---------------|--------------------------------------------------|---------|
| **Theorem 11** | The sector inheritance law $B(M + 6Q) = B(M) + 12S$. | §5.1 |
| **Proposition 2** | A window synchronised with its lines: the primes dividing $p+1$ give four **exact** identities with no edge term. Not twin-specific, and not a reduction. | §5.1 |
| **Theorem 12** | The capacity of one new line on one family, through $\Delta_q \equiv (3Q)^{-1} \pmod q$. | §5.2 |
| **Proposition 3** | The three mirror channels: the first is empty exactly for a twin, the second is the synchronised set, the third is not empty in general. | §5.2 |
| **Corollary 6** | The lines that can close two copies of a family are finite in number. | §5.3 |

**§6 — The gate belt: what a line can do between its own square and the next**

| Result | What it says | Section |
|-----------------|------------------------------------------------|---------|
| **Theorem 13** | The exact size of a belt between the squares of consecutive primes. | §6.1 |
| **Verified Law 14** | *Conditional on $g^2 \lt 2q$*, and **verified rather than proved**: a new line's reach depends on the gap, not on its size. | §6.2 |
| **Proposition 4** | In a belt of length $L$, any line $s$ makes at most $\lceil L/2s \rceil$ strikes — the layer ceiling. | §6.4 |

**§7 — Four named cells inside the window**

| Result | What it says | Section |
|---------------|--------------------------------------------------|---------|
| **Theorem 15** | Which lines can ever own a track: for $r \gt 3$, by the quadratic character of the discriminant. | §7.1 |
| **Theorem 16** | Simultaneity: a prime closes two of the four tracks in one window only under a stated congruence — nine primes in all. | §7.2 |
| **Proposition 5** | And why Theorem 16 obstructs nothing — $k$ tracks always admit a simultaneous solution. | §7.3 |

**Appendices**

| Result | What it says | Section |
|--------------|--------------------------------------------------------|---------|
| ***Counting details*** | The raw cell count, its residue mod $4$, and the local deviation $\varepsilon_r(u)$, quoted by §3. | App. A |
| **Theorems B1–B3, Corollary B1** | An auxiliary exact model: the minimum deletion cover $\tau = T-U+Q$ of the distance-$6$ graph, its propagation laws and its tail compression. **Its object is a prime pair $(p,p+6)$, not a twin pair.** | App. B |

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

*Terms used throughout, all as defined in [I].* A **line** $L_p$ is the odd multiples of $p$ from $p^2$ onward; a **cell** is a pair $C_b = (6b-1,\ 6b+1)$; a **strike** is a member of a cell that lies on some line; a member is a **survivor** of a set of lines if none of them strikes it, and a cell is **open** if both its members survive. A **gap** here always means the numerical distance between two consecutive odd composites, not a count of cells. A **sector** is the interval between consecutive odd squares; a **belt** is the interval between the squares of consecutive primes.

Before turning to the deviation analysis we record what the framework proves outright about gaps, and where the ladder stops.

### 2.1 Theorem 1 (the gap alphabet)

> **Theorem 1.** The gap between consecutive odd composites takes only the values $2$, $4$ or $6$.

*Proof.* Among any three consecutive odd numbers the residues modulo $3$ are a permutation of $\lbrace 0,1,2\rbrace$:
$$n,\ n+2,\ n+4 \ \longrightarrow\ \text{one of them lies on } L_3 .$$
So, so one is divisible by $3$; and every odd multiple of $3$ from $9$ onward lies on $L_3$. Hence beyond $7$ no three consecutive survivors exist, and the gap is capped at $6$. $\blacksquare$

Correspondingly: gap $2$ means no survivor between; gap $4$ means one isolated prime; and **gap $6$ means two adjacent survivors, i.e. a twin pair.** Verified: every gap-$6$ interval contains a twin, zero failures among $2{,}992$ instances below $3\times10^5$.

Measured over $9\times10^8$ gaps up to $2\times10^9$, the three letters occur with frequencies $0.89816$, $0.09475$ and $0.00708$; the maximum observed gap is $6$, first attained at $9$.

Hence an equivalent form of the twin conjecture: **the maximal possible gap is attained infinitely often.** The cap is free and proved; the statement concerns composites, which are the objects the framework actually constructs.

### 2.2 The ladder, and where it stops

> **Theorem 2.** Gap $2$ occurs infinitely often, requiring no prime; gap $4$ occurs infinitely often, requiring one prime.

*Proof.* For gap $2$ take
$$n = 30j+3, \qquad n+2 = 30j+5 .$$
The first lies on $L_3$, the second on $L_5$, both for every $j\ge1$. For gap $4$: let $p \equiv 8 \pmod{15}$ be prime; then $p-2 \equiv 6$ is divisible by $3$ and $p+2 \equiv 10$ by $5$, so $p$ is an isolated survivor, and Dirichlet's theorem supplies infinitely many such $p$. $\blacksquare$

$$\begin{array}{lll}
\text{gap } 2 & \text{zero primes required} & \textbf{proved} \cr 
\text{gap } 4 & \text{one prime (Dirichlet)} & \textbf{proved} \cr 
\text{gap } 6 & \textbf{two primes simultaneously} & \textbf{open}
\end{array}$$

**Dirichlet supplies one prime in an arithmetic progression; nothing supplies two at a prescribed distance.** That is the whole of the remaining distance.

**Why this reciprocal-sum test cannot bridge it.** Summing reciprocals by gap type:

| $N$ | gap 2 | gap 4 | gap 6 |
|------|-------|-------|-------|
| $10^6$ | 2.805 | 0.887 | 0.464 |
| $10^8$ | 4.556 | 1.127 | 0.488 |
| $2\times10^9$ | 5.762 | 1.257 | **0.498** |

Gaps $2$ and $4$ have **divergent** reciprocal sums (growing like $\log\log N$), and divergence proves infinitude. The gap-$6$ sum **converges** — flattening toward a constant. That constant is the analogue of Brun's constant in the present alphabet and not Brun's constant itself: the latter is $\sum_{\text{twins}}\big(1/p + 1/(p+2)\big) = 1.9021605\ldots$, whereas the column above carries one reciprocal per gap-$6$ event. A convergent reciprocal sum cannot distinguish "infinitely many" from "finitely many". Thus this particular divergence-based density test has no route to the twin conclusion.

### 2.3 Runs and the cap at four

> **Theorem 3.** On a single rail, no five survivors with $x \gt  5$ can lie in arithmetic progression with common difference $6$; and $5, 11, 17, 23, 29$ is the only exception.

*Proof.* Since $6 \equiv 1 \pmod 5$, the five terms
$$x, \quad x+6, \quad x+12, \quad x+18, \quad x+24$$
run through all residues modulo $5$, so exactly one of them is divisible by $5$. If that term exceeds $5$ it is an odd multiple of $5$ at least $25$, hence lies on $L_5$ and is struck. The term can fail to be struck only when it equals $5$ itself, which forces $x = 5$. $\blacksquare$

**The exception is real and must be carried in the statement.** For $x = 5$ the run is $5, 11, 17, 23, 29$, and all five are prime; an exhaustive search to $2\times10^5$ finds this and no other. It exists purely because $L_5$ is born at $25$: as a statement about the *residue classes* the argument is exact, and only the birth rule creates the exception.

*Verification.* At sieve depth $97$ over $6\times10^7$ cells, the run-length census is $6{,}448{,}150$ of length $1$; $2{,}404{,}092$ of length $2$; $778{,}762$ of length $3$; $211{,}170$ of length $4$; and **none of length $5$ or more.**

> **Corollary 1.** With $G_k$ the number of runs of $k$ consecutive survivors at spacing $6$ on one rail, the full-cycle counts satisfy $G_k = \prod_{q}(q-k)$.

*Proof.* A run of $k$ forbids exactly $k$ marks on each ruler, leaving $q-k$. $\blacksquare$

*Verification* (direct count on the $t$-axis at $p = 101$):

| lines | $k{=}1$ | 2 | 3 | 4 | **5** |
|-------|------|-----|----|----|---|
| $\lbrace 5\rbrace$ | 4 | 3 | 2 | 1 | **0** |
| $\lbrace 5,7\rbrace$ | 24 | 15 | 8 | 3 | **0** |
| $\lbrace 5,7,11\rbrace$ | 240 | 135 | 64 | 21 | **0** |

**The four laws $(q-1),\dots,(q-4)$ are therefore not four phenomena but one ruler with different numbers of marks.**

---

## 3. The twin problem inside the framework

### 3.1 A surviving cell is a twin pair

Let $u\lt v$ be consecutive integers coprime to $6$. Every survivor of all lines $\le u$ inside $(u^2, v^2)$ is necessarily prime, since a composite $x \lt  v^2$ has a prime factor $\le \sqrt{x} \lt  v$, and there is no prime strictly between $u$ and $v$. Hence
$$\boxed{ \text{a surviving } NN \text{ cell in } (u^2,v^2)  =  \text{a twin prime pair.} } \qquad\text{(3.1)}$$

**The identity, measured, and what it forecloses.** Because (3.1) is an equality and not a bound, $C_M$ *is* the twin count of the sector, and must therefore agree with the Hardy–Littlewood prediction for a window of $\lvert W\rvert = 12M+36$ integers at height $M^2$. Write
$$\mathrm{HL}  =  \frac{2C_2\,\lvert W\rvert}{\log^2(M^2)}, \qquad \mathrm{SP}  =  \lvert W_{\text{cells}}\rvert \prod_{5\le p\le M}\Big(1-\frac2p\Big)$$
for that prediction and for the raw sieve product over the cells. Then:

| $M$ | cells | $C_M$ | $\mathrm{HL}$ | $C_M/\mathrm{HL}$ | $\mathrm{SP}$ | $C_M/\mathrm{SP}$ |
|------|---------|-------|---------|-------|---------|-------|
| $1{,}005$ | 2,016 | 87 | 83.6 | 1.041 | 104.7 | 0.831 |
| $5{,}001$ | 10,008 | 281 | 273.2 | 1.028 | 343.4 | 0.818 |
| $10{,}005$ | 20,016 | 504 | 467.3 | 1.079 | 587.8 | 0.857 |
| $20{,}001$ | 40,008 | 796 | 807.9 | 0.985 | 1,017.6 | 0.782 |
| $50{,}001$ | 100,008 | 1,679 | 1,691.9 | 0.992 | 2,131.8 | 0.788 |
| $100{,}005$ | 200,016 | 2,936 | 2,988.6 | 0.982 | 3,766.1 | 0.780 |

The first ratio settles to $1$ from below within about $2$%; the second settles at $0.78$, which is the classical discrepancy between the sieve product and the truth at depth $\sqrt{x}$ and is not a property of these coordinates. **The point of the table is the first column pair, and it is a constraint rather than a confirmation.** This leaves no room for an argument that hopes to make $C_M$ exceed the Hardy–Littlewood count by exploiting structure in the sector — its anchoring at a square, the coupling between the lines' phases, the trajectory of the sector start. $C_M$ is the twin count itself, so it cannot differ from it.

Two controls make the same point from the other side, and both are recorded because each closed a route that had been proposed. First, replacing the true phases by random ones while keeping the same lines and the same two classes per line raises the survivor count from $1{,}679$ to $2{,}131 \pm 34$ at $M = 50{,}001$ — but that gap is entirely the height of the window, not its arithmetic: placing the same sieve on a block of the same length at a comparable height $y \in (M^2, 3M^2)$ gives $1{,}797 \pm 60$, within two standard deviations of the truth. Second, a control that *keeps* the phase coupling implied by the sector trajectory — all lines in one layer drawing their phase from a single number — but changes that number gives $2{,}127 \pm 34$, indistinguishable from the fully independent $2{,}131 \pm 34$. **The coupling between the lines' phases is a description of the sector, not a constraint on it.**

### 3.2 Theorem 4: only six cells in a sector can be open without being a twin

Take the sector in the form used throughout this section: $M \equiv 3 \pmod 6$ and the interval $(M^2, (M+6)^2)$, which carries $A_M = 2M+6$ cells
$$C_j = \big(M^2+6j+2,\ M^2+6j+4\big), \qquad j = 0,1,\dots,2M+5 .$$

> **Theorem 4.** Switch on every line $p \le M$. Then at most **six** cells of the sector can be open without being a twin pair, and their positions are given explicitly by
> $$E_M  =  \underbrace{\Big\lbrace \tfrac{2M}{3},\ \ M+1,\ \ \tfrac{5M}{3}+2,\ \ 2M+3\Big\rbrace }_{\text{present only if } M+2 \text{ is prime}}  \cup  \underbrace{\Big\lbrace \tfrac{4M}{3}+2,\ \ 2M+5\Big\rbrace }_{\text{present only if } M+4 \text{ is prime}} .$$
> Consequently **every open cell whose index lies outside $E_M$ is a twin pair.**

*Proof.* The argument has three steps: identify the only possible least prime factor, list its products inside the sector, and place them.

**Step 1: the least prime factor is $M+2$ or $M+4$.** Let $N$ be a composite endpoint of an open cell. Every prime factor of $N$ exceeds $M$, since otherwise some line $p \le M$ would have closed it. The least prime factor cannot be $\ge M+6$ either, since then
$$N  \ge  (M+6)^2,$$
which is outside the sector. As $M \equiv 3 \pmod 6$ and $N$ is coprime to $6$, the only remaining candidates are $M+2$ and $M+4$.

**Step 2: six products, not more.** Take $p = M+2$ first. Its strikes below $(M+6)^2 = (p+4)^2$ are
$$p^2, \qquad p(p+2), \qquad p(p+4), \qquad p(p+6), \qquad p(p+8),$$
since the next one, $p(p+10)$, already exceeds $(p+4)^2$. Of these,
$$p(p+4)  =  (M+2)(M+6)$$
is divisible by $3$ and so lies on $L_3$, not in a cell; **four remain**. Now take $q = M+4$. Its strikes below $(q+2)^2$ are
$$q^2, \qquad q(q+2), \qquad q(q+4),$$
of which
$$q(q+2)  =  (M+4)(M+6)$$
lies on $L_3$; **two remain**. Six in total.

**Step 3: their positions.** Write each surviving product in the form $M^2+6j+2$ or $M^2+6j+4$. For instance
$$(M+2)^2  =  M^2+4M+4  =  M^2+6j+4, \qquad j = \tfrac{2M}{3},$$
$$(M+2)(M+8)  =  M^2+10M+16  =  M^2+6j+4, \qquad j = \tfrac{5M}{3}+2,$$
and each $j$ is an integer because $3 \mid M$. The other four are placed the same way.

Finally, if $M+2$ is composite then it has a prime factor $\le M$, so its four products were already closed by an older line and are not exceptions; likewise for $M+4$. $\blacksquare$

*Verification.* Zero violations over every $M = 9, 15, \dots, 19{,}999$ — **$3{,}332$ sectors.** In each, every open cell outside $E_M$ was checked to be a twin.

**Example, $M = 9$.** The sector $(81,225)$ has $24$ cells; $E_9 = \lbrace 6, 10, 14, 17, 21, 23\rbrace$, carrying
$$121 = 11^2,\quad 143 = 11\cdot13,\quad 169 = 13^2,\quad 187 = 11\cdot17,\quad 209 = 11\cdot19,\quad 221 = 13\cdot17 .$$
No other composite can inhabit an open cell of that sector.

**The candidate set $E_M$ has $0$, $2$, $4$ or $6$ elements**, according to the primality of $M+2$ and $M+4$:

| $M+2$ | $M+4$ | $\lvert E_M\rvert$ |
|-----------|-----------|------------|
| composite | composite | $0$ |
| prime | composite | $4$ |
| composite | prime | $2$ |
| prime | prime | $6$ |

At $M = 999$ both $1001 = 7\cdot11\cdot13$ and $1003 = 17\cdot59$ are composite, so $E_M$ is empty and **all $93$ open cells of that sector are twin pairs** — as measured.

*Two remarks on the sharpness of this count.* $E_M$ is a set of candidate **positions**, and the number of cells that are actually open without being twins is smaller. The position $B$ carries $(M+2)(M+4)$ and so requires **both** $M+2$ and $M+4$ prime; when $M+4$ is composite its least prime factor is at most $\sqrt{M+4} \lt M$, so that cell has already been closed by an older line and cannot be an exception at all. Hence the row "$M+2$ prime, $M+4$ composite" admits at most **three** actual exceptions, not four. And the caps are not attained on any tested range: over every $M \equiv 3 \pmod 6$ below $4000$ the largest number of open non-twin cells in a sector is $0$, $2$, $2$ and $3$ in the four rows respectively. What Theorem 4 asserts, and all that is used below, is the inclusion $S_M \setminus E_M \subseteq \lbrace \text{twins}\rbrace$.

**What this buys, stated precisely.** Writing $C_M$ for the number of open cells, one has $T_M \ge C_M - |E_M| \ge C_M - 6$, so a twin follows from $C_M \ge 7$. Theorem 4 replaces that by the much weaker requirement
$$S_M \not\subseteq E_M, \qquad\text{(3.2)}$$
where $S_M$ is the set of open indices: **a single open cell suffices, provided it is not at one of six named places.** And the six places are fixed by the geometry of the square — they are not chosen by the lines, whose phases are periodic and unrelated to $M$.

**The lines $5$ and $7$ alone cut six to three, and the pair is not interchangeable.** Writing $M = 6n+3$, the six positions are exact quadratics in $n$ as absolute cell indices:
$$A = 6n^2+10n+4, \qquad B = 6n^2+12n+6, \qquad C = 6n^2+14n+8,$$
$$D = 6n^2+16n+9, \qquad E = 6n^2+18n+11, \qquad F = 6n^2+18n+13.$$
(verified for $n = 1,\dots,3999$ against the definition). Each is therefore a function of $n \bmod p$ modulo any $p$, so the state of all six under the lines $5$ and $7$ depends on $n \bmod 35$ alone: **the $35$ classes are not a sample but the whole question**, and checking them is a proof rather than an experiment. Doing so gives $\max|S_M \cap E_M| \le 3$ after those two lines alone, with only four maximal patterns —
$$\lbrace A,B,C\rbrace , \quad \lbrace A,E,F\rbrace , \quad \lbrace C,D,F\rbrace , \quad \lbrace C,E,F\rbrace ,$$
writing $A,\dots,F$ for the six positions in the order listed above. The collapse from $2^6 = 64$ conceivable patterns to four is what makes the next step possible.

The pair is special. Line $5$ alone leaves four open; adding $7$ gives three; and **adding $11$, then $13$, changes nothing at all** — the same bound and the same four patterns. The reason is structural rather than numerical: a larger line can choose a phase striking none of the six, and the Chinese remainder theorem then combines that phase freely with the phase of $5$ and $7$ that leaves three. **So the route "add more small lines until the six are closed" is shut**, and we record it so that it is not attempted again in another notation.

> **Corollary 2 (the dichotomy).** Suppose $(M+2, M+4)$ is not a twin pair. Then $|S_M \cap E_M| \le 2$, and consequently
> $$C_M \ge 3 \quad\Longrightarrow\quad \text{the sector contains a twin, or } (M+2,M+4) \text{ is one.}$$

*Proof.* Theorem 4 splits the six positions by what each one needs:
$$A, D, E \ \text{require} \ M+2 \ \text{prime}; \qquad C, F \ \text{require} \ M+4 \ \text{prime};$$
$$B \ \text{carries} \ (M+2)(M+4) \ \text{and so requires both}.$$
If the open set met both groups, $M+2$ and $M+4$ would both be prime and $(M+2, M+4)$ would be the twin. So under the hypothesis the open set lies inside $\lbrace A,D,E\rbrace$ or inside $\lbrace C,F\rbrace$, and $B$ is closed.

Each of the four maximal patterns listed above meets both groups, so none survives. Inspecting the $35$ classes, the patterns that do survive are
$$\varnothing, \quad \lbrace A\rbrace, \quad \lbrace C\rbrace, \quad \lbrace F\rbrace, \quad \lbrace A,D\rbrace, \quad \lbrace A,E\rbrace, \quad \lbrace C,F\rbrace,$$
all of size at most two. $\blacksquare$

*Verification.* Over the same $3{,}332$ sectors $M = 9, 15, \dots, 19{,}999$: the maximum of $|S_M \cap E_M|$ is $3$ in the $340$ sectors where $(M+2,M+4)$ is a twin and **exactly $2$ in the other $2{,}992$**; zero violations of the forcing (an open member of $\lbrace A,D,E\rbrace$ with $M+2$ composite, or of $\lbrace C,F\rbrace$ with $M+4$ composite, or $B$ open without the twin), and zero cases where the open set met both groups without the twin being present. **The separation is exact: three open positions occur only when the twin is already there.** Both bounds are attained — three in $3$ sectors, two in $13$ of the twinless ones — so neither is an artefact of a range too short to reach them.

**Five residue classes in which the two lines close all six.** Of the $35$ classes, five leave nothing open: $n \equiv 0, 8, 23, 25, 33 \pmod{35}$, that is
$$M \equiv 3,\ 51,\ 141,\ 153,\ 201 \pmod{210}.$$
There $S_M \cap E_M = \varnothing$ from the lines $5$ and $7$ alone, so **every** open cell is a twin. Condition (3.2) remains the weakest form of the criterion — it asks for no count at all — but in these classes it becomes *equivalent* to the bare $C_M \ge 1$, and Corollary 2 lowers the sufficient count in a general sector from $C_M \ge 7$ to $C_M \ge 3$. The improvement is to the numerical threshold, not to the criterion. Measured over the $713$ such sectors below $M = 30{,}000$: $444{,}958$ open cells and **not one of them fails to be a twin**, against $155$ non-twin survivors in the $428$ ordinary sectors below $M = 3000$ alone. And the restriction costs nothing in the count itself — the survivor density in these five classes, against all other classes, is $0.934$ up to $M = 4000$, $0.997$ up to $12000$ and $1.000$ up to $30000$; fixing the phases of $5$ and $7$ changes which cells die, not how many.

**And what it does not buy.** $C_M$ exceeds the twin count of the sector by at most six. Any lower bound on $C_M$ is therefore a lower bound on twins, and (3.2) is an exact reformulation rather than a route. We record it because it is the sharpest form the framework has produced of the twin criterion, not because it weakens the problem.

### 3.3 The exception budget over a full period, and the limit of local arguments

Corollary 2 bounds the exceptions in one sector. Consecutive sectors are not independent, and taking a whole period of them together lowers the bound further — up to a point that can be identified exactly.

**The sectors tile:** $(M^2,(M+6)^2)$ is followed immediately by $((M+6)^2,(M+12)^2)$, so a prime forced near the top of one is forced near the bottom of the next. Taking the $35$ sectors of one full period together — the window $(M_0^2,(M_0+210)^2)$ with $M_0 = 210k+3$ — and writing each exceptional position's requirement as a set of offsets that must be prime ($A$ needs $M+2$; $C$ needs $M+4$; $D$ needs $M+2,M+8$; $E$ needs $M+2,M+10$; $F$ needs $M+4,M+8$), the twinless hypothesis forbids any two forced offsets differing by $2$ across the whole window, not merely within a sector.

Summing the per-phase caps independently gives $5\cdot0+20\cdot1+10\cdot2 = 40$. The coupling costs three of those: three pairs of adjacent phases cannot both attain their caps, because the offsets clash across the join — for instance a phase reaching two via $\lbrace C,F\rbrace$ forces $M+8$, and its successor reaching two the same way forces $M'+4 = M+10$. **A fourth adjacent pair with the same caps does not clash**, which is the point: the obstruction is arithmetic in the offsets, not a consequence of adjacency. Hence $37$, and with the lines $11,13,17$ admitted as well, an exhaustive scan over all $5\cdot7\cdot11\cdot13\cdot17/35 = 2431$ alignments gives

$$\sum_{i=0}^{34}\bigl|S_{M_i}\cap E_{M_i}\bigr| \le 31 \qquad\text{(no twin in the window)},$$

the ceiling $31$ being attained in $9$ of the $2431$ alignments, and the distribution of the $2431$ values peaking at $26$.

**That ceiling cannot be lowered by any finite set of lines, and this is a theorem rather than a report of failed attempts.**

*What is and is not claimed.* The budget is a maximum over residues, so what is proved is that for every finite set of lines there is a choice of residues at which the extremal configuration survives them all; no residue-based argument brings the ceiling below $31$. It is *not* a claim that an integer $M_0$ realising the configuration exists, still less that infinitely many do — that would require all $133$ polynomials to be simultaneously prime, which is Hypothesis H and is not assumed anywhere here.

*The system.* The $9$ extremal alignments carry $28$ distinct maximal configurations. Each demands not only that certain $M_0+a$ be prime — $27$ to $30$ of them — but also that the *partner* member of each of the $31$ cells survive, and those partners are quadratics in $n$: $36n^2+60n+23$ for $A$, $36n^2+84n+47$ for $C$, $36n^2+96n+53$ for $D$, $36n^2+108n+67$ for $E$ and $36n^2+108n+79$ for $F$ (verified against the definition for $n \lt 3000$).

*The surviving configuration.* Testing the full linear-and-quadratic systems for a fixed prime divisor kills **$27$ of the $28$** — $q=23$ disposes of fourteen, $q=31$ of ten, $q=19$ of three. One survives, at $M_0 \equiv 448353 \pmod{510510}$, with $28$ linear and $31$ quadratic conditions: $59$ polynomials of total degree $90$. Every prime $q \le 90$ leaves at least one admissible residue — the tightest are $q=19$ and $q=31$, with exactly one each — and for $q \gt 90$ a residue survives automatically, since $90$ polynomials of that total degree have at most $90$ roots.

**The system is therefore admissible at every prime, so by the Chinese remainder theorem the residues can be chosen simultaneously against any finite list of further lines: no residue-based argument, however many primes it uses, reaches $30$.**

**Nor does the order in which the lines are born supply the missing constraint.** One might hope that a line $M_0+a$, forced prime by one exceptional cell, strikes another of the $31$ once it is born. Modulo $p = M_0+a$ one has $M_0 \equiv -a$, so a member $(M_0+u)(M_0+v)+e$ with $e \in \lbrace 0,\pm2\rbrace$ reduces to the integer $(u-a)(v-a)+e$, and $|u|,|v|,|a| \lt 216$ while $p \asymp M_0$; the line divides the member only if that small integer is exactly zero. Excluding the cell's own factors, this needs $|u-a| \cdot |v-a| = 2$, hence $|u-v| \in \lbrace 1,3\rbrace$. **But $u$ and $v$ are the offsets $6i+d$ with $d \in \lbrace 2,4,8,10\rbrace$, so $|u-v|$ is even, and the collision is impossible.** The check finds none, for the $28$ lines or for any $M_0+b$ with $b \le 216$. The timing of the lines carries no information the residues did not already carry, and the escapee's survival is equivalent to the simultaneous primality of its $59$ irreducible polynomials — precisely the setting of Schinzel's Hypothesis H [8], which predicts infinitely many $t$ realising it. **Proving the configuration impossible would mean contradicting that prediction for a specific family, which is not a weakening of the twin problem but an apparent strengthening of it.**

### 3.4 Blocks of consecutive periods, and why lengthening the block does not help

Section 3.3 fixes the ceiling at a single period. Lengthening the window to a block of $L$ consecutive periods raises the budget to $B_L$, and one may hope that the budget grows more slowly than the block, so that a long enough block forces a twin. It does not help: **Proposition 1** gives the sieve dimensions of the five exception types and the resulting order $B_L \ll L/\log^2 L$, which is exactly the order the twin count itself has, so the two grow together and no length of block separates them. The measured budgets $B_3 = 67$, $B_5 = 100$, $B_7 = 138$, $B_9 = 163$ are consistent with that order.

*The full account, with the block scan and the dimension computation, is in Appendix C.1.*

---

### 3.5 Theorem 5: a new line kills at most one pair in its own first window

The sector $[p^2,(p+2)^2)$ is where the line $L_p$ is born. Index gap-2 pairs by their offset from the centre $C = (p+1)^2$, writing $P(j) = (C+2j-1,\ C+2j+1)$ with $-p \le j \le p$, so the window holds exactly $2p+1$ pair slots. Let $T_p^-$ count the surviving pairs before $L_p$ is switched on, $T_p^+$ after, and $D_p = T_p^- - T_p^+$.

$L_p$ has exactly three strikes in this window: $p^2$, $p(p+2)$ and $p(p+4)$, since $p(p+6) \gt  (p+2)^2$.

> **Theorem 5.** $D_p \in \lbrace 0,1\rbrace$ for every prime $p \gt  3$.

*Proof.* Three strikes, and each is disposed of by the grid $L_3$.

1. **$p^2$.** Of the two pairs it meets, only $(p^2, p^2+2)$ lies in the window — the other has index $-p-1$. For $p\gt 3$, $p^2 \equiv 1 \pmod 3$, so $p^2+2 \equiv 0$: **that pair is already dead.**
2. **The strike divisible by $3$.** One of $p+2, p+4$ is $\equiv 3 \pmod 6$, so one of $p(p+2), p(p+4)$ lies on $L_3$ and was struck before $L_p$ existed; both pairs it meets were already dead.
3. **The surviving strike.** Call it
$$H_p = \begin{cases} p(p+2), & p \equiv 5 \pmod 6,\\[2pt] p(p+4), & p \equiv 1 \pmod 6.\end{cases}$$
   In either case $H_p \equiv 5 \pmod 6$, so $H_p - 2 \equiv 3 \pmod 6$ and the pair $(H_p-2, H_p)$ is **also already dead.**

Only $(H_p, H_p+2)$ remains. $\blacksquare$

> **Corollary 3.** $D_p = 1$ if and only if **two** primality conditions hold together:
> $$p \equiv 5 \ (6): \qquad p+2 \ \text{prime} \quad\text{and}\quad p(p+2)+2 \ \text{prime};$$
> $$p \equiv 1 \ (6): \qquad p+4 \ \text{prime} \quad\text{and}\quad p(p+4)+2 \ \text{prime}.$$

*Proof.* The cell $H_p$ survives the older lines exactly when its cofactor,
$$p+2 \quad\text{or}\quad p+4,$$
has no prime factor below $p$; being less than $2p$, that means the cofactor is prime. And $H_p+2 \lt  (p+2)^2$ is not divisible by $p$, so if composite its least prime factor is below $p$ and it was struck earlier; hence $H_p+2$ survives iff it is prime. $\blacksquare$

*Verification.* Corollary 3 predicts $D_p$ from two primality tests alone; checked against the directly computed $D_p$ for every prime $5 \le p \lt  4000$, with **zero mismatches**. Examples: $p=5$ gives $7$ and $37$ both prime, so $D_5=1$; $p=11$ gives $13$ prime but $145 = 5\cdot29$ composite, so $D_{11}=0$; $p=13$ gives $17$ and $223$ both prime, so $D_{13}=1$.

**What this does and does not buy.** Since $T_p^+ = T_p^- - D_p$ and every survivor in the window is prime (the cofactor argument of §4.2), $T_p^+$ *is* the number of twin pairs in $[p^2,(p+2)^2)$. Theorem 5 therefore says:

$$\boxed{ T_p^- \ \text{is the twin count of the window, up to an error of } 0 \text{ or } 1, \text{ and the error is characterised.} }$$

That is the strongest local statement in this paper, and it is worth being explicit that it is not a reduction. $T_p^-$ and $T_p^+$ differ by at most one, so proving anything about $T_p^-$ is proving it about the twin count. In particular the sufficient condition "$T_p^- \ge 2$" is *stronger* than the conclusion "$T_p^+ \ge 1$", not weaker. What Corollary 3 adds is that even the discrepancy between the two is governed by a twin-like coincidence — two simultaneous primality conditions — so the error term is of the same nature as the quantity.

### 3.6 Theorem 6: the bridge pair, and the only law that knows about squares

Index gap-2 pairs by $x$ as above but on an absolute scale, the pair being $(2x+1, 2x+3)$. The window for odd $m$ begins at $a_m = (m^2-1)/2$ and holds $2m+1$ slots, while $a_{m+2} - a_m = 2m+2$. **So consecutive square windows do not abut: exactly one pair slot falls between them,**
$$g_m  =  a_m + 2m + 1, \qquad \text{the pair } \big((m+2)^2-2,\ (m+2)^2\big),$$
whose upper member is the next square itself. The line is partitioned as window, bridge, window, bridge, …, with no slack and no overlap.

Let $B$ count the bridges surviving a line set, over a full cycle of roots.

> **Theorem 6.** $B' = \big(q - 2 - \chi_q(2)\big) B$, where $\chi_q(2)$ is the Legendre symbol: $+1$ for $q \equiv \pm1 \pmod 8$ and $-1$ for $q \equiv \pm3 \pmod 8$.

*Proof.* The bridge at root $r$ dies under $q$ when $q \mid r^2$, i.e. $r \equiv 0$ — one class — or when $r^2 \equiv 2 \pmod q$, which has $1+\chi_q(2)$ solutions. The two conditions are disjoint for $q\gt 2$, so $2+\chi_q(2)$ classes are lost. $\blacksquare$

*Verification.* $B = 2,\ 8,\ 32,\ 320,\ 3840,\ 53760,\ 967680$ for the line sets up to $3, 5, 7, 11, 13, 17, 19$, against $T = 1,\ 3,\ 15,\ 135,\ 1485,\ 22275,\ 378675$. Brute-forced from the definition for $\lbrace 3\rbrace$, $\lbrace 3,5\rbrace$, $\lbrace 3,5,7\rbrace$, $\lbrace 3,5,7,11\rbrace$: exact.

So the cycle fingerprint is not three numbers but four, with four distinct degrees:
$$(M, S, T, B)  \longmapsto  \big(qM,\ (q-1)S,\ (q-2)T,\ (q-2-\chi_q(2))B\big).$$
**$B$ is the only one of the four that knows the window is anchored at a square**, and the arithmetic that enters is whether $2$ is a quadratic residue.

> **Theorem 7 (the summation identity).** Over $M$ consecutive square windows,
> $$\sum_{i=0}^{M-1} T_{m+2i}  =  2(m+M) T  -  B .$$

*Proof.* The $M$ windows together with their $M$ bridges tile a stretch of
$$a_{m+2M}-a_m  =  2M(m+M)$$
pair slots, that is exactly $2(m+M)$ complete cycles, holding $2(m+M)T$ surviving pairs. The $M$ bridge roots are $M$ consecutive odd numbers, and since $M$ is odd they cover every residue class modulo $M$ exactly once, so exactly $B$ of them survive. $\blacksquare$

*Verification.* Checked for $\lbrace 3,5\rbrace$ and $\lbrace 3,5,7\rbrace$ at $m = 9, 15, 101$ — six cases, all exact.

**The collective bias, quantified.** Against the density prediction $T (2m+2M-1)$ for the same total length, the windows hold exactly $T-B$ fewer pairs; measured sums of deviations $-1, -5, -17, -185$ for the four line sets, matching $T-B$ each time. Now
$$\frac BT  =  \prod_q \Big(1 - \frac{\chi_q(2)}{q-2}\Big),$$
which converges: measured $2.5554,\ 2.5517,\ 2.5614,\ 2.5615,\ 2.5622$ at $z = 19,\ 10^3,\ 10^4,\ 10^5,\ 10^6$. The reduced product $\prod(1-\chi_q(2)/q)$ reaches $1.604401$ at $z = 10^6$ against
$$\frac{1}{L(1,\chi_8)} = 1.604556, \qquad L(1,\chi_8) = \frac{\log(1+\sqrt2)}{\sqrt2} = 0.623225 .$$
**So the square geometry enters this framework through a Dirichlet $L$-value at $1$ for the character modulo $8$.**

And the bias, though real, is not usable: $T-B \approx -1.56 T$ is a fixed number independent of $m$, spread over $M$ windows, so the deficit per window is $O(T/M)$ and vanishes against the per-window average as $M$ grows.

### 3.7 The square-phase mean, and the end of the "poor window" question

One may ask whether a window anchored at a square is systematically poorer than a window placed anywhere. The answer is an identity rather than an experiment: the average over all square phases has the exact closed form (3.3), and on the tested range it tracks the generic density prediction to within about $1$% from $p = 29$ onward. So the anchoring at a square carries no penalty at the level of the mean, and the "poor window" question closes.

*The derivation and the comparison table are in Appendix C.2.*

---

### 3.8 Two constructions that do not help, recorded so they are not retried

Two natural constructions were tried and neither adds anything: a window balanced so that every line strikes it equally often, and an attempt to read ownership through the cofactor rather than through the smallest factor. Both are exact, both reduce to statements already in the framework, and both are recorded so that they are not attempted again in another notation.

*The two constructions and the measurements that close them are in Appendix C.3.*

---

### 3.9 Proposition 6: a proved lower bound on $C_M$, and the order at which it becomes exact

Every count of $C_M$ in this paper so far has been a direct enumeration. This subsection gives the first *proved* lower bound on it, by importing a classical inequality and observing where it terminates.

Fix a sector and write $W$ for its set of cells, $N = |W| = 2M+6$. For each line $p \le M$ let $B_p \subseteq W$ be the cells it closes — two residue classes modulo $p$, by [I, Thm 3]. For a cell $d$ put
$$m(d)  =  \#\lbrace p \le M : d \in B_p \rbrace,$$
the number of lines striking it, and define
$$S_0 = N, \qquad S_i  =  \sum_{d \in W} \binom{m(d)}{i} \quad (i \ge 1). \qquad\text{(3.5)}$$
The right-hand side of (3.5) is the count of $i$-fold intersections $\lvert \bigcap_{p \in J} B_p \rvert$ summed over all $i$-subsets $J$, each cell contributing once for every $i$-subset of the lines that strike it. Written this way the whole hierarchy is computed in a **single pass over the cells**, at cost $O(N \log\log M)$, rather than by enumerating $\binom{\pi(M)}{i}$ intersections.

> **Proposition 6.** With the notation above, for every $\ell \ge 0$
> $$C_M  \ge  S_0 - S_1 + S_2 - \cdots - S_{2\ell+1}, \qquad\text{(3.6)}$$
> and the alternating sum is **exactly** $C_M$ as soon as the truncation order reaches $\max_{d} m(d)$.

*Proof.* A cell struck by exactly $m$ lines contributes
$$\sum_{i=0}^{L}(-1)^i\binom{m}{i}$$
to the truncated sum. For $m = 0$ that is $1$. For $m \ge 1$ and $L < m$ the partial alternating binomial sum equals $(-1)^L\binom{m-1}{L}$, which is $\le 0$ when $L$ is odd; hence every struck cell contributes at most $0$ and every open cell exactly $1$, giving (3.6). For $L \ge m \ge 1$ the sum is the complete alternating binomial sum $(1-1)^m = 0$, so once $L \ge \max_d m(d)$ every struck cell contributes $0$ and every open cell $1$, and the total is $C_M$ exactly. $\blacksquare$

The inequality itself is the odd Bonferroni truncation and is classical; the multiplicity form (3.5) and the observation that it terminates at $\max_d m(d)$ are what make it usable here. The same evaluation appears independently in Nguyen [7], in the Goldbach setting of symmetric pairs about a multiple of a primorial — see §3.10.

**How far the low orders reach.** Writing $L_j$ for the truncation at order $j$, measured:

| $M$ | cells | $L_1$ | $L_3$ | $L_5$ | $L_7$ | $C_M$ |
|------|-------|------|------|------|------|------|
| 9 | 24 | 7 | **10** | 10 | 10 | 10 |
| 15 | 36 | 1 | **11** | 11 | 11 | 11 |
| 21 | 48 | $-13$ | **7** | 7 | 7 | 7 |
| 51 | 108 | $-72$ | 2 | **10** | 10 | 10 |
| 105 | 216 | $-208$ | $-27$ | 20 | **21** | 21 |
| 141 | 288 | $-313$ | $-76$ | 25 | **29** | 29 |
| 201 | 408 | $-501$ | $-191$ | 19 | **28** | 28 |
| 381 | 768 | $-1104$ | $-492$ | 8 | **47** | 47 |
| 501 | 1008 | $-1538$ | $-839$ | $-40$ | 46 | 47 |
| 753 | 1512 | $-2490$ | $-1431$ | $-93$ | 74 | 75 |

The first moment $L_1 = N - S_1$ is the union bound, and it dies at once: $\sum_p 2/p$ passes $1$ at $M = 13$ and grows like $2\log\log M$ thereafter, so $L_1$ is negative from $M = 21$ on and carries no information. Order three is exact through $M = 21$; order five through $M = 141$; order seven through $M = 381$, and at $M = 753$ it is short by one.

**Why the order needed grows so slowly.** By Proposition 6 the hierarchy terminates at $\max_d m(d)$, and the mean of $m(d)$ over the sector is $\sum_{p \le M} 2/p \approx 2\log\log M$ — about $4.1$ at $M = 10^6$. The maximum over $2M+6$ cells therefore grows like $\log\log M$ as well, and measurement confirms it:

| $M$ | $10^3$ | $5\cdot10^3$ | $10^4$ | $5\cdot10^4$ | $10^5$ | $2\cdot10^5$ | $5\cdot10^5$ | $10^6$ |
|--------------------------|------|------|------|------|------|------|------|------|
| $\max_d m(d)$ | 9 | 9 | 10 | 11 | 11 | 12 | 13 | 13 |
| least odd $j$ with $L_j \gt 0$ | 7 | 7 | 9 | 9 | 9 | 9 | 9 | 11 |

**Across three orders of magnitude in $M$ the order required rises only from seven to eleven** — against $\pi(M) = 78{,}498$ lines at the top of that range. So the natural reading of "one would have to take every order" as "one would have to take $\pi(M)$ orders" is wrong by four orders of magnitude, and the exact point is reached at a quantity that (3.5) already computes for free.

**And what this does not buy, stated plainly.** The bound is proved and the order is small; the *number of terms* is not. Turning (3.6) into a theorem about all $M$ requires asymptotic control of $S_1, \dots, S_j$ for $j \asymp \log\log M$, and $S_j$ is a sum over $j$-tuples of primes of the same shape that makes $S_1$ diverge. The hierarchy therefore moves the difficulty from "the union bound is negative" to "a uniform estimate is needed for sums of order $\log\log M$" — a shorter distance, and the same kind of distance. It is recorded here as an exact computational tool and as a sharper statement of where the estimate is missing, not as a route.

### 3.10 The same obstruction from the Goldbach side

The finite-window difficulty this section keeps returning to — a full CRT period has positive density, but the interval belonging to one centre is a *translated fragment* of that period — was reached independently, and stated in almost the same words, by Nguyen [7]. The setting there is Goldbach rather than twins: symmetric pairs $\lbrace C-d, C+d\rbrace$ about a centre $C = a\, p_k^{\#}$, so the pairs have fixed **sum** where ours have fixed **difference**, and the window is anchored at a multiple of a primorial where ours is anchored at a square. Under that translation the two frameworks correspond term by term: the two forbidden cell classes $\pm 6^{-1} \pmod p$ of [I, Thm 3] are the one or two forbidden lift residues there; $C_M$ corresponds to the survivor sets there; and the survivor density $\prod(1-2/q)$ is the same product.

**One point in that dictionary needs care, and Nguyen raised it.** His $U(C)$ is deliberately *conservative*: it is the set of offsets avoiding every obstruction congruence, whereas the actual terminal set $T(C)$ also contains the **endpoint-prime exceptions** — offsets whose divisible endpoint is the prime $q$ itself, so that nothing is destroyed. In general $U(C) \subsetneq T(C)$, and his own example at $C = 30$ has the offset $23$ giving the surviving pair $\lbrace 7,53\rbrace$ while $19$ gives the genuinely destroyed endpoint $49 = 7^2$.

On this side the two coincide, and for a reason worth stating: **the window sits above $M^2$ while every line is at most $M$**, so an endpoint equal to a sieving prime is impossible — a member of a cell in $(M^2,(M+6)^2)$ exceeds $M^2 \ge p^2 \gt p$ for every $p \le M$. There are therefore no endpoint-prime exceptions here, and $C_M$ equals both $|U|$ and $|T|$ in his letters. The equality is a consequence of anchoring at a square, not of the definitions, and a framework whose window sat elsewhere would have to distinguish them.

Two things are worth recording. First, the correspondence is evidence rather than coincidence: two constructions built for different problems, with no contact between them, isolate the same difficulty and label it the central one. Second, the tools are complementary — the Bonferroni evaluation of §3.9 is imported from there, while the measurement of $\max_d m(d)$ and the covering control of [V, §3.5] were not made there and bear on its open problems. Nguyen has confirmed in correspondence that $S_j = 0$ for $j \gt \max_d m(d)$ in his notation too, so the effective depth of the inclusion–exclusion is that maximum rather than the number of sieving primes; whether it also grows like $\log\log$ on the primorial wheel is open. Nguyen claims no Goldbach theorem and no new infinite family, and says so repeatedly; the reference is to contemporaneous independent work, not to a settled result.

---

### 3.11 Smoothing the window, and where it does not reach

A sharp window pays a boundary error of order $1$ per residue class, and replacing it by a Fejér kernel removes most of that error. Three exact statements are proved for this: a mirror law for the sector index (Proposition 7), an exact discrepancy formula for the Fejér window whose corollary is the classical bound $d/(4H)$ (Proposition 8), and a bound $\ll d^3/(HT^2)$ for a window that also moves (Proposition 9). The kernels, the order, the pointwise estimate and the $\csc^4$ sum are all classical and are cited as such; the exact discrepancy formula is the part we have not found stated anywhere.

The smoothing gains a factor of about nine on $L_7$ at $M = 50{,}001$ and does not change its sign. **On our reading it does not reach the part that decides the answer:** the share of $S_i$ carried by moduli below the window scale is $90$%, $45$%, $9$%, $0.2$% and $0$% for $i = 1,\dots,5$, so it controls the term that had already died at $M = 21$ and none of the terms that fix the sign.

*The three propositions with their proofs, the measured tables, and a further route closed by an equivalence with Jacobsthal's function, are in Appendix C.4.*

---

## 4. Clocks, and primality as a zero-test

### 4.1 Theorem 8 (the shift law) and primality

> **Theorem 8.** $\phi_q(p+2) = \phi_q(p) - 1 \pmod q$ for every old line $q$; and when $p$ itself becomes an old line, $\phi_p(p+2) = p-1$.

*Proof.* Substituting $p+2$ for $p$ in [III, (2.2)] subtracts $1$. For the second, $\phi_p(p+2) = (p-(p+2))/2 = -1 \equiv p-1$. $\blacksquare$

*Verification.* Zero failures among $4{,}983$ instances, and zero for the insertion rule.

Hence, writing $\Phi(n) = (\phi_3, \phi_5, \phi_7,\dots)$, the transition $n \mapsto n+2$ acts as
$$\Phi  \longmapsto  \Phi - 1, \qquad\text{(4.1)}$$
each component on its own circle, and the whole system evolves by three small numbers:
$$\text{step } +4, \qquad \text{first square gap } +8, \qquad \text{all clocks } -1,$$
with one clock inserted at $p-1$ whenever $p$ is prime. The system is *shift, zero-test, insert*; nothing is rebuilt.

> **Corollary 4.** $p$ is composite if and only if some old clock reads $0$ at its birth. Equivalently, **a prime is a step at which no clock lands on zero.**

*Verification.* Zero failures over all odd $p \lt  2000$.

> **Corollary 5.** The clock of $L_3$ cycles $2 \to 1 \to 0$, so the two non-zero states are exactly the cell $(6a-1, 6a+1)$. **The cell, taken as a definition in [I, §3], is a consequence.**

### 4.2 Theorem 9 (surviving cofactors are prime)

> **Theorem 9.** For $p \ge 11$ and $p \lt  t \le 9p$, a cofactor $t$ surviving all lines below $p$ is prime.

*Proof.* $t \le 9p \lt  p^2$. A composite $t$ surviving all lines $\lt p$ would need two prime factors $\ge p$, giving $t \ge p^2 \gt  9p$. $\blacksquare$

*Verification.* Zero violations at $p = 11,13,17,101,499$.

Hence $J_j$, the number of new strikes in sector $j$, equals the number of **primes** among that block's cofactors. Primality appears as *a slot no ruler reached*, with no change to its definition.

**Worked example ($p=11$, computed without writing a single strike).**

| quantity | value |
|----------|----------------------------------------------------------------|
| $\kappa_j$ | 0, 2, 4, 7, 10, 14, 18, 22, 27, 32, 38, 44 |
| $H_j$ | 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6 |
| clocks | $\phi_3=2$, $\phi_5=2$, $\phi_7=5$ |
| $J_j$ | 1, 2, 1, 2, 1, 3, 1, 2, 3, 2, 2 |

The "new" cofactors are exactly $13,17,19,23,\dots,97$, all prime, as Theorem 9 requires.

### 4.3 The general form: a row reads primality off originality

Theorem 9 is the case that arises inside one sector. Read along the whole row of $p$ it has a general form, and the general form is worth stating because it makes the twin condition geometric.

Call a cell of the row **original** if no line below $p$ owns it. Everything before $p^2$ is inherited — a strike $p m$ with $m \lt  p$ carries the smallest prime factor of $m$, which is below $p$ — so $p^2$ is the first original cell on the row. Past it:

> **Theorem 10.** For $p$ prime and $p \le p+2j \lt  p^2$,
> $$p (p+2j) \ \text{ is original with respect to the lines below } p \quad\Longleftrightarrow\quad p+2j \ \text{ is prime}.$$

*Proof.* Suppose $p+2j$ is composite. Being below $p^2$, its least prime factor is below $p$:
$$p+2j = rs \quad\text{with}\quad r \le \sqrt{p+2j} \lt p,$$
so the line $r$ already owns the cell. If $p+2j$ is prime it has no factor below $p$ at all, and $p$ itself begins at $p^2$. $\blacksquare$

*Verification.* Zero failures over $1{,}782{,}933$ instances: every prime $p \lt  400$ and every $j$ with $p+2j \lt  p^2$.

**So a row is a reader.** The row of $p$ carries, in the originality of its cells, the primality of every odd number from $p$ up to $p^2$ — one bit per cell, with no change to the definition of a prime. Two consequences are worth recording.

**First, the twin condition becomes a two-step statement at the diagonal.** The cells at $p^2$ and $p(p+2)$ are the first two on the row past the inherited region, and by Theorem 10
$$(p, p+2)\ \text{is a twin pair} \quad\Longleftrightarrow\quad \text{originality survives one step past } p^2 .$$
Writing $\mathsf O$ for original and $\mathsf I$ for inherited, the row crosses the diagonal as $\dots\mathsf I \mid \mathsf O \mathsf O\dots$ at a twin and $\dots\mathsf I\mid \mathsf O \mathsf I\dots$ otherwise: at $p=23$, $529$ is original but $575 = 23\cdot 5^2$ is not, and $(23,25)$ is not a twin.

**Second, the shadow lies on a curve already in the series.** The tested cell is
$$p (p+2)  =  (p+1)^2 - 1,$$
so every twin test sits one unit below an even square: $35 = 36-1$, $143 = 144-1$, $323 = 324-1$, $899 = 900-1$. **That is [I, Thm 5] read along the row instead of across the window** — the cell $(n^2-1,\ n^2+1)$ with $n = p+1$, whose lower member $(n-1)(n+1)$ is composite by construction. The two statements are the same fact.

**And the reformulation is exact, which is precisely why it is not progress.** Writing $\sigma(p)$ for the smallest line owning $p(p+2)$, one has $\sigma(p) = \mathrm{spf}(p+2) \le \sqrt{p+2}$ when $p+2$ is composite, and $\sigma(p) = \infty$ exactly when $(p,p+2)$ is a twin. Proving $\sigma(p) = \infty$ infinitely often is proving the twin conjecture, in the same words. What the row picture adds is a suggestion — that if twins were finite, every new diagonal point would need its shadow claimed by some line below $\sqrt p$ — and the suggestion does not survive measurement: over $6{,}835$ composite cases with $p \lt  200{,}000$ the claimant is at most $13$ in $63.6$% of them and at most $100$ in $89.9$%, the counts being $5$: $2248$, $7$: $1125$, $11$: $557$, $13$: $415$, $17$: $303$. **The $\sqrt p$ bound is nowhere near tight; the shadows are claimed by the smallest lines, not by a delicate conspiracy of many.**

---

## 5. Inheritance across sectors, and the capacity of a single line

Sections 2–4 treat one sector at a time. This section treats the *sequence* of sectors, indexing them by $M = 9, 15, 21, \dots$ — the odd multiples of $3$ — with the sector $(M^2, (M+6)^2)$ carrying $A(M) = 2M+6$ cells. Three exact laws come out, all sharper than the average statement "line $q$ removes $2/q$ of what remains", because each is a statement about a *named* gap rather than about a count.

### 5.1 Theorem 11: the sector inheritance law

Fix any finite set of lines $p_1 \lt  \dots \lt  p_r$ above $3$, and put
$$Q = \prod_i p_i, \qquad S = \prod_i (p_i - 2),$$
so that $S$ cells survive that set in each cycle of $Q$ consecutive cells. Let $B(M)$ be the number of cells of the sector at $M$ that survive those lines.

> **Theorem 11.** $B(M + 6Q)  =  B(M)  +  12 S.$

*Proof.* Two facts. First, the sector grows by exactly $12Q$ cells: $A(M+6Q) - A(M) = 12Q$. Second — and this is what makes the law exact rather than approximate — the **phase is preserved**: the sector at $M$ begins near cell $M^2/6$, and
$$\frac{(M+6Q)^2}{6} - \frac{M^2}{6}  =  2MQ + 6Q^2  \equiv  0 \pmod Q .$$
So the first $A(M)$ cells of the later sector repeat the earlier sector's pattern exactly, and the tail of $12Q$ new cells is precisely twelve complete cycles, each leaving $S$ survivors. $\blacksquare$

*Verification.* Exact at every $M$ tested, for each of the three sets: $\lbrace 5\rbrace$ ($Q=5$, $S=3$, increment $36$); $\lbrace 5,7\rbrace$ ($Q=35$, $S=15$, increment $180$); $\lbrace 5,7,11\rbrace$ ($Q=385$, $S=135$, increment $1620$).

**What it says.** A *fixed* set of old lines never catches up with the window. Each time its cycle returns to the same phase, the sector has grown, and a known positive number $12S$ of fresh open cells appears. Only lines born after the set was fixed can close them.


**A window whose lines are synchronised with it.** Theorem 11 moves along the cycle. The opposite situation — a window whose length is a whole number of periods of the lines acting on it — also occurs, and there the counts are identities rather than estimates. Fix $p \equiv 5 \pmod 6$, put $C = (p+1)^2$ and index the interval $(p^2,(p+2)^2)$ by the cells $X_d = (C+6d-1,\ C+6d+1)$ for $-(2m-1) \le d \le 2m-1$ where $p+1 = 6m$, so the interval holds $N = 4m-1$ cells. A line $r \ge 5$ completes a whole number of its cycles inside the strip if and only if $r \mid 4m$, and since $r$ is odd and larger than $3$ this is $r \mid p+1$.

> **Proposition 2.** Let $S$ be the set of primes $r \ge 5$ dividing $p+1$, and put $P = \prod_{r \in S} r$, $A = \prod (r-1)$, $B = \prod (r-2)$ and $m = aP$. Then, exactly,
> where $N_{\varnothing}$, $N_L$, $N_R$, $N_{LR}$ count the cells untouched by $S$, struck on the left only, on the right only, and on both:
> $$N_{\varnothing} = 4aB - 1, \qquad N_{L} = N_{R} = 4a(A-B), \qquad N_{LR} = 4a(P - 2A + B),$$

*Verification.* At $p = 2309$, where $S = \lbrace 5,7,11\rbrace$, $P = 385$, $a = 1$, $A = 240$, $B = 135$: the direct census of the $1539$ cells gives $539 + 420 + 420 + 160$, matching the four formulas exactly. The identities were then checked over every $p \equiv 5 \pmod 6$ below $2000$ — $59$ of them twin, $273$ not — with no exception.

*Two things it is not.* It is **not** a statement about twins: primality of $p$ and $p+2$ enters nowhere in the derivation, which needs only $6 \mid p+1$. And it is **not** a reduction: the surviving fraction is $U/N = 0.3502$ against $\prod_{r \in S}(1 - 2/r) = 0.3506$ at $p = 2309$, so the drop from $1539$ to $539$ is the ordinary sieve by those three lines and nothing more. What the synchronisation buys is exactness — no edge term — not size.

### 5.2 Theorem 12: the capacity of one new line on one family

Each survivor of the fixed set appears in the new tail exactly twelve times, at cells
$$x,\ x+Q,\ x+2Q,\ \dots,\ x+11Q,$$
which we call a **family**. A new line $q$ closes a cell $c$ when $c \equiv \pm 6^{-1} \pmod q$, so on a family it closes the copies $t$ solving $x + tQ \equiv \pm 6^{-1}$. There are two such $t$ modulo $q$, and their separation does not depend on $x$:

> **Theorem 12.** Put $\Delta_q \equiv (3Q)^{-1} \pmod q$ and $d_q = \min(\Delta_q,\ q - \Delta_q)$. Then a line $q \gt  11$ closes at most two copies of any family, and **at most one** whenever $d_q \gt  11$.

*Proof.* The two solutions differ by $2\cdot 6^{-1} Q^{-1} = (3Q)^{-1}$, whose least absolute representative is $\pm d_q$. Two copies lie in the family only if two values of $t \in \lbrace 0,\dots,11\rbrace$ differ by $d_q$, which needs $d_q \le 11$. $\blacksquare$

*Verification.* For $Q = 385$, brute force over all $x$ and all $q$ from $13$ to $101$ reproduces the predicted capacity with **zero mismatches**. Sample values of $d_q$: $13{:}6$, $17{:}1$, $19{:}5$, $23{:}9$, $31{:}4$, $37{:}14$, $53{:}24$, $83{:}12$, $101{:}39$.

**The reflection of that window, and what a single line can do to it.** The interval $(p^2,(p+2)^2)$ is two consecutive Legendre intervals glued at $C = (p+1)^2$, and the map $d \mapsto -d$ exchanges them. A line respects the reflection $x \mapsto 2C-x$ exactly when it divides $2C$, that is when it belongs to the set $S$ of Proposition 2 — so the synchronised lines are precisely the lines the reflection preserves.

> **Proposition 3.** A single line $q \lt  p$ can strike both cells of a mirror pair $X_d, X_{-d}$ only if $q \mid p(p+2)$, or $q \mid (p+1)^2$, or $q \mid (p+1)^2+1$.

*Proof.* Add the two members in each of the three ways: $L_d + L_{-d} = 2(C-1) = 2p(p+2)$, $L_d + R_{-d} = 2C$, and $R_d + R_{-d} = 2(C+1)$. If $q$ divides both members of a pair it divides their sum, and $q$ is odd. $\blacksquare$

*What the three channels are worth.* The first is empty exactly when $p$ and $p+2$ are both prime, since then $p(p+2)$ has no factor below $p$ — this is the one place in this subsection where the twin hypothesis does any work. The second is the set $S$ itself. The third is not empty in general: the number of lines closing both cells of a mirror pair is $5, 12, 0, 0, 375, 657, 4$ at $p = 101, 137, 2309, 3299, 5741, 10007, 17789$, the zeros being the accident that $(p+1)^2+1$ is prime there.

*And the reflection settles nothing about twins, which is the point of recording it.* Measured over those same $p$: the two halves carry exactly equal cell counts and exactly equal survivor counts, every time, while the twin counts differ by $-1, -2, -1, -8, +2, +10$. The symmetry transports the structure perfectly and constrains the one quantity one wants not at all — a symmetry gives structure on a set when it is non-empty, and never gives non-emptiness.

### 5.3 Corollary 6: the exceptional lines are finite in number

> **Corollary 6.** A line $q$ can close two copies of a family only if $q \mid 3Qr \pm 1$ for some $1 \le r \le 11$. Consequently every $q \gt  33Q + 1$ closes **at most one** copy of every family.

*Proof.* The condition $d_q \le 11$ means $\Delta_q \equiv \pm r$ with $r \le 11$, that is
$$3Qr \equiv \pm 1 \pmod q \qquad\text{for some } 1 \le r \le 11;$$ and $0 \lt  3Qr \mp 1 \le 33Q+1$, so $q$ cannot divide it once $q$ exceeds that bound. $\blacksquare$

For $Q = 385$ the threshold is $12{,}706$. This is a genuinely local statement: it names, for each family, a bound on what a *specific* line can do, whereas $2/q$ only bounds a total.


---

## 6. The gate belt: what a line can do between its own square and the next

Sections 3–5 work inside a sector bounded by consecutive odd squares. This section changes the unit: since every prime $q\gt 3$ has $q^2 \equiv 1 \pmod 6$, each prime has a **gate** $G_q$ with $q^2 = 6G_q+1$, and the cell $C_{G_q} = (q^2-2, q^2)$ is closed by $q$ itself. Consecutive primes $q\lt r$ therefore delimit a **belt** of cells $C_{G_q+1},\dots,C_{G_r-1}$ between two gates that are certainly closed. The belts tile the cell axis.

### 6.1 Theorem 13: the size of a belt

> **Theorem 13.** For consecutive primes $q\lt r$ with $g = r-q$, the belt holds exactly
> $$G(q,r)  =  \frac{r^2-q^2}{6}-1  =  \frac{g(2q+g)}{6}-1$$
> cells, so its size grows like $qg$.

*Proof.* Both $q^2$ and $r^2$ are $\equiv 1 \pmod 6$, so the cells strictly between the two gates are exactly the $(r^2-q^2)/6 - 1$ complete cells of $L_3$ in the interval. $\blacksquare$

*Verification.* $G = 3, 11, 7, 19, 11, 27, 51, 19, 67$ for the nine consecutive belts $5\to7, 7\to11, \dots, 31\to37$, and $247, 67, 667, 4011$ for $89\to97$, $101\to103$, $499\to503$ and $997\to1009$; each reproduces from the formula.

### 6.2 Verified Law 14: the new line's reach depends on the gap, not on its size

> **Verified Law 14 (conditional).** Suppose $g^2 \lt  2q$. Then, within its own belt, the number of cells the line $L_q$ can strike at all is
> $$H_q  =  \left\lfloor \frac{2g}{3}\right\rfloor,$$
> **independent of $q$.**

*Proof under the hypothesis.* If $g^2 \lt  2q$ the line completes no extra lap before the next gate, so it reaches only the cofactors $q+2, q+4, \dots, q+2g$, giving $g$ candidate strikes; one in every three falls on $L_3$ and so touches no cell of the grid, leaving $\lfloor 2g/3 \rfloor$. $\blacksquare$

**We do not call this a theorem, because the hypothesis is not available.** $g^2 \lt  2q$ is far weaker than Cramér's conjecture $g = O(\log^2 q)$, which would give it at once — but it is **stronger than anything currently proved, and stronger than the Riemann hypothesis supplies**: RH gives only $g \ll \sqrt q \log q$, hence $g^2 \ll q\log^2 q$, which does not suffice. **Verified over $17{,}981$ belts, every consecutive prime pair with $q \lt  200{,}000$: no failure.**

**The consequence is worth stating plainly.** The belt has $\sim qg/6$ cells and the line born at its left end can touch $\sim 2g/3$ of them. **For a twin gap $g=2$ the line touches exactly one cell, however large $q$ is** — one cell out of $\sim q/3$. A line at $q \approx 10^6$ entering a belt of some hundred thousand cells has a single strike available before the next gate opens.

### 6.3 The collapse of the new line's effect

Raw reach is not closing power: a strike may land on a cell an older line has already closed. Write $K_q$ for the cells the new line closes **first**.

| belt | $G$ | $H_q$ | $K_q$ | twins left |
|------|------|------|------|------------|
| $5\to7$ | 3 | 1 | 1 | 2 |
| $7\to11$ | 11 | 2 | 2 | 4 |
| $11\to13$ | 7 | 1 | **0** | 2 |
| $13\to17$ | 19 | 2 | 1 | 7 |
| $17\to19$ | 11 | 1 | **0** | 2 |
| $23\to29$ | 51 | 4 | **0** | 8 |
| $31\to37$ | 67 | 4 | **0** | 11 |
| $89\to97$ | 247 | 5 | **0** | 21 |
| $101\to103$ | 67 | 1 | **0** | 7 |

*Measured over every consecutive prime pair below $5{,}000$:* $K_q = 0$ in $71.1$% of belts with $q\lt 1000$ and $76.8$% of belts with $1000\lt q\lt 5000$; mean $K_q$ falls from $0.331$ to $0.259$; the maximum ever observed is $3$. **A new line typically arrives at its own gate to find that the work has already been done.**

**A monotone version of this is false, and we record it because it is the natural guess.** It is not the case that a newer line always closes fewer cells than every older one: in the belt $31\to37$ the first closures are $17:1$, $19:3$, $23:2$, $29:3$, so $29$ — newer than $19$ and $23$ — closes more than both. **The weakness is collective, not line by line.**

### 6.4 A deterministic ceiling for a whole age layer

Nothing above uses primality of the intermediate lines, and the next bound deliberately gives them more power than they have.

> **Proposition 4.** In the belt $q\to r$ of length $L = r^2-q^2$, any line $s$ makes at most $\lceil L/2s \rceil$ strikes, of which at most a fraction $2/3$ touch cells of the grid. Hence, allowing **every** odd $s$ not divisible by $3$ in a range to act as an independent line and ignoring all overlap between them, the layer $q-D \le s \le q$ can close at most
> $$C_D(q,r)  =  \sum_{\substack{q-D \le s \le q\cr  s \text{ odd},\ 3\nmid s}} \left\lceil \tfrac{2}{3}\left\lceil \tfrac{L}{2s}\right\rceil\right\rceil$$
> cells.

For the belt $499 \to 503$ ($G = 667$): the newest quarter has ceiling $C = 168$ ($25$% of the belt) and closes $6$ in fact; the newest half has ceiling $376$ ($56$%) and closes $15$. For $997 \to 1009$ ($G = 4011$): the newest tenth has ceiling $316$ and closes $14$; the newest quarter $836$ and closes $28$; the newest half $1{,}977$ — under half the belt — and closes $68$. **The ceilings are generous by one to two orders of magnitude, and the real burden falls on lines far below $q/2$.**

### 6.5 And why the layer ceilings do not close the argument

Proposition 4 invites an obvious attempt: build the full pyramid of age layers $(q/2,q]$, $(q/4,q/2]$, … down to $s=5$, sum the ceilings, and hope the total falls short of $G$. **It does not.**

| belt | $G$ | $\sum$ ceilings over all layers | ratio |
|------|-------|------------------------------------------------------|-------|
| $499\to503$ | 667 | 2,094 | $3.1\times$ |
| $997\to1009$ | 4,011 | 13,935 | $3.5\times$ |
| $10007\to10009$ | 6,671 | 35,045 | $5.3\times$ |

and the cumulative total already passes $G$ at the **second** layer.

The asymptotic is worth getting right, because it is the point of the section. **The sum runs over every $s$ coprime to $6$, not over the primes**, and those have density $1/3$, so
$$\sum_{\substack{s \le q\cr (s,6)=1}} \frac1s  =  \frac13\log q + O(1), \qquad\text{whence}\qquad \sum_s \tfrac23\cdot\tfrac{L}{2s}  =  \frac L3\sum_s\frac1s  \sim  \frac L9 \log q .$$
Against $G \sim L/6$ the ratio is therefore
$$\frac{\sum_s C_s}{G}  \sim  \frac23\log q$$
— a **logarithm**, not an iterated logarithm. Checked against the table: $\tfrac23\log(q/4)$ gives $3.22$, $3.68$, $5.22$ at $q = 499,\ 997,\ 10007$ against the measured $3.14$, $3.47$, $5.25$.

> **So the belt decomposition establishes three of the four things one would want — the belt grows like $qg$, the new line's reach is $O(g)$ and independent of $q$, and no fixed set of old lines can serve arbitrarily long belts — and refutes the fourth. The moving tail of recent lines is not capacity-limited; its ceilings exceed the belt by a factor that grows.** What is left is the forced overlap between the layers, which is $\prod(1-2/q)$ and describes the cycle, not the belt. This is [V, §§2–3] again, reached from the belt side.

---

## 7. Four named cells inside the window

Paper I, §4, indexes the window by its own cell numbers: it is the interval $c_0,\dots,c_0+N-1$ with $c_0 = 6a^2-2a+1$ and $N = 4a-1$, where $n = 6a$ and the window is $[(n-1)^2,(n+1)^2]$. This section uses that indexing to study the four cells nearest its two ends.


*A note on notation.* The four cells of this section are written $T_1,\dots,T_4$ and are **not** the exception types $A, C, D, E, F$ of §3.3 and §3.4; the two families are unrelated, and the letters are kept apart on purpose.

### 7.1 The four tracks, their character conditions and their densities

The window's template [I, §4.2] singles out four cells near its two ends. Writing $q = 6a-1$ they are
$$T_1 = (q^2{+}4,\ q^2{+}6), \quad T_2 = (q^2{+}10,\ q^2{+}12), \quad T_3 = ((q{+}2)^2{-}14,\ (q{+}2)^2{-}12), \quad T_4 = ((q{+}2)^2{-}8,\ (q{+}2)^2{-}6),$$
and as $a$ runs they trace four **tracks**. Substituting $q = 6a-1$ makes every member a quadratic in $a$:

| cell | lower member | upper member |
|------|--------------|--------------|
| $T_1$ | $36a^2-12a+5$ | $36a^2-12a+7$ |
| $T_2$ | $36a^2-12a+11$ | $36a^2-12a+13$ |
| $T_3$ | $36a^2+12a-13$ | $36a^2+12a-11$ |
| $T_4$ | $36a^2+12a-7$ | $36a^2+12a-5$ |

*Verification.* Exact for $a = 1,\dots,399$.

> **Theorem 15 (which lines can ever own a track).** Let $r \gt  3$. Then $r$ divides $36a^2+Ba+C$ for some $a$ exactly when the discriminant $B^2-144C$ is a quadratic residue modulo $r$, the case of discriminant $\equiv 0$ counting as a residue and giving a double root. (For $r = 2, 3$ the leading coefficient vanishes modulo $r$ and the criterion does not apply; those two lines are handled by the grid itself.) For the eight members the discriminants are $144k$ with
> $$k  =  -4,\ -6 \ (T_1); \qquad -10,\ -12 \ (T_2); \qquad 14,\ 12 \ (T_3); \qquad 8,\ 6 \ (T_4),$$
> so the conditions read $r \equiv 1 \pmod 4$ and $(-6 | r) = 1$ for $T_1$; $(-10 | r)=1$ and $r \equiv 1 \pmod 3$ for $T_2$; $(14 | r)=1$ and $(3 | r)=1$ for $T_3$; $r \equiv \pm1 \pmod 8$ and $(6 | r)=1$ for $T_4$.

*Verification.* Every prime factor of every member for $a = 1,\dots,400$ — $4{,}209$ checks — satisfies its condition; no violation.

Each individual condition admits half the primes (measured over primes below $10^5$: $49.7$–$50.0$%), but a cell falls to a strike on **either** member, so the union admits three quarters: measured $75.0,\ 74.8,\ 75.0,\ 75.0$% for $T_1,T_2,T_3,T_4$. Requiring eligibility for all four at once cuts this to **exactly a quarter** — the eight discriminants reduce to the five independent characters $(-1),(2),(3),(5),(7)$, giving $32$ sign patterns of which $8$ pass; measured $24.84$% against the naive independent guess $(3/4)^4 = 31.6$%.

**The four tracks are not equivalent.** Each is a pair of quadratics, so its twin density is governed by a Bateman–Horn constant [1] $S = \prod_r (1-\nu_r/r)/(1-1/r)^2$, where $\nu_r$ counts the roots of the pair modulo $r$. The correct baseline is a generic cell $(6c-1,6c+1)$, whose constant is $12C_2 = 7.9219$ — **not** the twin constant $2C_2 = 1.320$, which is for pairs $(n,n+2)$ over all $n$ and counts the even $n$ a cell never has.

| track | $\nu_5$ | $\nu_7$ | $\nu_{11}$ | $S$ | $S/12C_2$ |
|-------|------|------|------|------|------|
| $T_1$ | **4** | 2 | 2 | $3.230$ | $0.408$ |
| $T_2$ | 1 | 4 | 2 | $5.797$ | $0.732$ |
| $T_3$ | 2 | 1 | 4 | $8.739$ | $1.103$ |
| $T_4$ | 2 | 2 | **0** | $11.324$ | $1.429$ |

*Verification.* Predicted density $S/\log^2(36a^2)$ against measured, for $a = 12{,}000,\dots,30{,}000$: $0.0059/0.0062$, $0.0105/0.0100$, $0.0158/0.0156$, $0.0205/0.0214$.

**So the Bateman–Horn model predicts track $T_4$ to be $3.5$ times richer in twins than track $T_1$, and the counts measured below are consistent with that prediction**, and the reason is visible in the table: $\nu_{11} = 0$ for $T_4$ — eleven never divides either of its members — while $\nu_5 = 4$ for $T_1$, the maximum, five dividing both members with two roots each. *(This is directly usable: a search for twin pairs near squares is three and a half times more productive on the $T_4$ track than on the $T_1$ track.)*

### 7.2 Theorem 16: simultaneity, and why it is the sharp question

Eligibility asks which primes can own a track at **some** $a$. The sharper question is which can own two tracks at the **same** $a$, and the answer is finite.

> **Theorem 16.** A prime $r \gt  3$ can close two of $T_1,T_2,T_3,T_4$ in the same window only if it divides the resultant of the corresponding pair of quadratics. The complete list is
>
> | pair | admissible primes |
> |---|---|
> | $T_1$ & $T_2$ | **none** |
> | $T_1$ & $T_3$ | $5,\ 11,\ 13,\ 73$ |
> | $T_1$ & $T_4$ | $5,\ 7$ |
> | $T_2$ & $T_3$ | $5,\ 7,\ 11,\ 13,\ 37$ |
> | $T_2$ & $T_4$ | $7,\ 19,\ 89,\ 97$ |
> | $T_3$ & $T_4$ | **none** |
>
> so the union is the nine primes $\lbrace 5,7,11,13,19,37,73,89,97\rbrace$, and **every $r \gt  97$ closes at most one of the four cells in any single window.**

*Proof of the two empty entries.* The differences between a member of $T_1$ and a member of $T_2$ are $4$, $6$ and $8$; a prime dividing one member of each would divide one of these, impossible for $r\gt 3$. The same three differences occur between $T_3$ and $T_4$. $\blacksquare$

*Proof of the rest.* Two quadratics with the same leading coefficient differ by a linear form, so a common root modulo $r$ forces a linear congruence in $a$; substituting it back leaves a fixed integer that $r$ must divide. For $T_1$ lower against $T_3$ lower, for instance, $24a \equiv 18$ gives $4a \equiv 3$ and then $r \mid 65$. Each entry above was computed as the resultant and then checked for a genuine common root. $\blacksquare$

**The contrast is the point.** Eligibility for one cell admits three quarters of all primes; for all four at once, a quarter — both infinite. **Simultaneous double duty admits nine primes and no more.** The character condition loses the shared variable $a$; restoring it collapses an infinite set to a finite one, and this is the sharpest local statement in the paper after Corollary 6.

**And, as with every local statement here, it does not bind.** Closing all four cells requires at least two lines — a special prime may serve $T_1$ & $T_3$ and another $T_2$ & $T_4$ — and at most four. Measured over $a = 3000,\dots,10000$: of $7{,}000$ windows, $6{,}512$ have all four closed, using two distinct lines in $973$ cases, three in $4{,}748$ and four in $791$, so one of the nine special primes does double duty in $5{,}721$ of them. Against this, the lines available number $\pi(q) = 428$, $2{,}062$ and $6{,}055$ at $a = 500$, $3000$, $10000$. **Four out of six thousand is free.**

---


### 7.3 Proposition 5: and why Theorem 16 does not obstruct anything

Theorem 16 is sharp, and it is sharp for one line. The next statement shows that it dissolves the moment one is allowed four, and it dissolves by construction rather than by measurement.

> **Proposition 5.** Let $k$ tracks be given, each a pair of quadratics in $a$, and let $N$ be any bound. Then there is an arithmetic progression of $a$ — infinite, explicit, and computable — along which all $k$ tracks are closed simultaneously, every closing line exceeding $N$ and all $k$ of them distinct. Any finite number of further congruence conditions may be imposed at the same time.

*Proof.* For each track choose a prime $r_i \gt  N$, distinct from the others, whose discriminant condition (Theorem 15) is satisfied, and a root $a_i$ of one of its members modulo $r_i$. The $k$ conditions $a \equiv a_i \pmod{r_i}$ have pairwise coprime moduli, so the Chinese remainder theorem combines them into a single class modulo $\prod r_i$. Further conditions on coprime moduli are appended the same way. $\blacksquare$

**The contrast with Theorem 16 is the whole point.** There the same line had to satisfy two conditions *at the same $a$*, which is a genuine constraint and collapsed an infinite set to nine primes. Here the conditions sit on different moduli, and the shared variable costs nothing.

*Explicit instance, with every step verified.* Take
$$101 \mid T_1^-, \ a \equiv 54; \qquad 103 \mid T_2^-,\ a \equiv 15; \qquad 107 \mid T_3^-,\ a \equiv 73; \qquad 113 \mid T_4^-,\ a \equiv 77,$$
four distinct lines, all above $97$. The Chinese remainder theorem gives
$$a \equiv 107{,}106{,}110 \pmod{125{,}782{,}673},$$
and along this progression $T_1$, $T_2$, $T_3$ and $T_4$ are all closed. Adjoining the further condition $5 \mid q+2$, i.e. $a \equiv 4 \pmod 5$ — which makes the new line's own central strike $q(q+2)$ inherited rather than new, so that the centre is not a twin either — gives
$$a \equiv 484{,}454{,}129 \pmod{628{,}913{,}365}, \qquad\text{i.e.}\qquad q \equiv 2{,}906{,}724{,}773 \pmod{3{,}773{,}480{,}190}.$$
The residue and the modulus are coprime, so by Dirichlet's theorem the progression contains infinitely many primes $q$. **Along it, $q$ is prime, $q+2$ is composite, and all four named cells are closed — permanently and by construction.**

> **So no fixed number of named cells can force a twin.** Whatever finite list of tracks one selects, one distinct line may be assigned to each and the conditions combined; the construction is immune to how large the tracks' moduli are required to be, and it survives the addition of any finite list of side conditions. **An argument of this shape can only begin to bite when the number of cells grows with the window**, so that the number of conditions grows too and the assignment of a private line to each ceases to be free.

We state this as a proposition rather than a remark because it is the reason to stop, and knowing why one stops is worth more than another negative measurement.

---

## 8. What this paper establishes, and what it does not

**Proved here.**

- The gap alphabet and the ladder — Theorems 1–3, Corollary 1.
- The six exception positions (Theorem 4), and the dichotomy that three of them can be open only when $(M+2,M+4)$ is itself a twin (Corollary 2).
- The exception budget of $31$ over a full period, and the proof that no finite set of lines lowers it — §3.3.
- The block budgets $B_3 = 67$ and $B_5 = 100$, the sieve dimensions of the five exception types, and the resulting order $B_L \ll L/\log^2 L$ — Proposition 1, §3.4.
- The single-kill bound in a line's own first window and its characterisation — Theorem 5, Corollary 3.
- The bridge law and the summation identity over a cycle of windows — Theorems 6, 7.
- The shift law, the primality of surviving cofactors, and the originality law on a row — Theorems 8, 9, 10, Corollaries 4, 5.
- The sector inheritance and single-line capacity laws (Theorems 11, 12, Corollary 6), with the two synchronisation propositions (Propositions 2, 3).
- The belt size and the layer ceiling — Theorem 13, Proposition 4.
- The character conditions on the four outer tracks, the nine-element simultaneity set, and the construction showing it obstructs nothing — Theorems 15, 16, Proposition 5.
- The odd Bonferroni lower bound on $C_M$, its multiplicity evaluation, and its termination at $\max_d m(d)$ — Proposition 6, §3.9.
- The mirror law for the sector index, the exact Fejér discrepancy formula, and the moving-window bound, with the certificate that smoothing preserves the target — Propositions 7, 8, 9, §3.11. The kernels, the pointwise estimate and the $\csc^4$ sum are classical and are cited as such.
- The exact minimum cover with its propagation and compression laws — Theorems B1–B3, Corollary B1, Appendix B.

**Verified but not proved.** Verified Law 14 (the reach $\lfloor 2g/3\rfloor$), proved under $g^2 \lt 2q$ — a hypothesis weaker than Cramér but stronger than the Riemann hypothesis supplies; checked on $17{,}981$ belts with $q \lt 200{,}000$ without failure.

**Measured, and labelled as such where they occur.** Each item below is a computation over a stated finite range and supports a claim about that range only.

- The agreement of $C_M$ with the Hardy–Littlewood twin count to about $2$%, and the two phase controls that go with it — §3.1.
- The frequencies of the three gap letters — §2.1.
- The block values $B_7 = 138$ and $B_9 = 163$, and the values quoted for $L = 21, 51, 101$ — §3.4. These were computed with pruning and are stable across twelve and eight consecutive primes respectively; **they should be read as lower bounds with strong stability, not as certified maxima.**
- The numerical agreement of the square-phase mean with the generic density — §3.7 — and the two constructions of §3.8.
- The collapse of the new line's effect in a belt (§6.3) and the layer-ceiling ratios (§6.5).
- The track densities against Bateman–Horn, and the count of windows in which the four tracks are closed — §7.1, §7.2 — together with the two synchronisation measurements of Propositions 2 and 3.
- The growth of $\max_d m(d)$ and of the least sufficient Bonferroni order, tabulated in §3.9. The inequality there is proved; the growth rate is measured.
- The gains from smoothing, the share of each $S_i$ below the threshold $d \lt r$, and the least admissible half-width against the largest gap, tabulated in §3.11. The bounds there are proved; the tables are measured.

**Where the closed routes are.** Four accounts that were in the body of §3 are now in Appendix C: the block budgets (C.1), the square-phase mean (C.2), the two constructions that do not help (C.3), and the smoothing bounds with the mass they do not reach (C.4). Each has a stub in §3 stating its conclusion and its status.

**Covered by the verification scripts.** `verify_exception_dichotomy.py` covers the closed forms of the six positions, the $\lbrace 5,7\rbrace$ table, Corollary 2, the whole of the period budget of §3.3 (the per-phase caps $5\cdot0+20\cdot1+10\cdot2 = 40$, the coupling to $37$, the ceiling $31$ over all $2431$ alignments, the nine that attain it, and the partner quadratics), and Step 1 of Proposition 1 over all $423$ primes below $3000$. `verify_bonferroni_depth.py` covers Proposition 6 — the geometry of §§3.9 and [I, §4.5], the exception positions of Theorem 4 over every sector below $M = 2500$, the exactness of the alternating sum at order $\max_d m(d)$, and the published values. `verify_first_appearance.py` covers the bad-phase sweep and its least representative. `verify_new_additions.py` covers the exact phase set of [I, Cor 1] over 428 primes, the diamond-centre corollary over 6,320 pairs, the coincidence gap of [I, Cor 3], the third channel and pair count of [II, Cor 1–2], and the two constructions of §3.8 — the rotation of the balanced word over 20 windows and the clean-owner theorem.

**Not yet in a script.** The sector-coupling budget of §3.3, the admissibility of the surviving configuration and the emptiness of the timing table are exhaustive finite computations, and each is a proof; until they are scripted they should be read as stated rather than audited.

**Not here.** Every one of the statements above is an *exact* statement — an identity, a cap, or an explicit list. None is a lower bound, and a lower bound is what the twin conjecture needs. Each of the criteria above turns out, on inspection, to require a lower bound on a quantity that exceeds the twin count of a sector by at most a constant; the criteria are therefore exact reformulations rather than routes.

The measurements that establish that, the two test cases against which the framework was checked, and the account of where and why it stops, are **Paper V**.

---

## Appendix A — Counting details for §3

The two computations below are used in §3 and quoted there. They are routine and are collected here so that §3 is not interrupted by them.

### A.1 Raw cell count and main term

$$C = \frac{v^2-u^2}{6}-1, \qquad C_- = 4n-1  (u=6n-1), \qquad C_+ = 8n+3  (u=6n+1),$$
and $C \equiv 3 \pmod 4$ always (zero failures over 427 consecutive prime pairs) — an exact property which nevertheless supplies no protective invariant, since a single line's deletion count has no fixed parity. The main term is $M = C P_2$.

### A.2 Local deviations

$$\varepsilon_r(u) = D_r(u) - \frac{2 N_{r^-}(u)}{r}. \qquad\text{(A.1)}$$

Inside a sector, line $r$ deletes at $s \equiv -u^2/6$ and $s \equiv (2-u^2)/6 \pmod r$, and the gap between the two positions is exactly $3^{-1} \bmod r$ (zero failures among 85). **Every ruler's phase is therefore a function of the single quantity $u^2$**, and under $u \mapsto u+6$ the phase moves *quadratically*, since $u^2 \mapsto u^2 + 12u + 36$. This quadratic motion is what makes cancellation possible at all.

---

## Appendix B — An auxiliary exact model: the distance-6 closing budget

**What this appendix is, and why it is not in the body.** Sections 2 and 3 concerned twins: a surviving cell, whose two members differ by $2$. The present appendix concerns a different graph — survivors joined to survivors at distance $6$ — and the two must not be run together, because the word “gap 6” would otherwise cover both the *letter* $6$ of §2.1 (a gap of $6$ between consecutive odd composites, which contains a twin) and the *edge* of length $6$ used here. **What an untouched edge exhibits once the remaining lines have acted is a prime pair $(p, p+6)$, not a twin pair.**

Measured, so that the distinction is not left rhetorical: inside $(P^2, 9P^2)$ at $P = 101$ there are $2{,}903$ edges, of which $1{,}865$ survive the remaining lines and $1{,}410$ are genuine gap-$6$ configurations — for instance $(10247,10253)$, $(10337,10343)$, $(10601,10607)$. **None of them is a twin.**

We keep the material because the budget it produces is exact, and because $(p,p+6)$ is open in precisely the same way and for precisely the same reason; but nothing here bears on the twin conjecture directly. It is placed in an appendix for that reason: it is an exact model that Paper V uses as a test object, not a step in the twin criterion.

Instead of asking what the lines will close, we ask the dual question: **how many deletions are needed, at minimum, to close every distance-$6$ edge?** If the available deletions fall short, a pair survives.

### B.1 Theorem B1 (the exact minimum cover)

Take survivors as vertices and join $x$ to $x+6$. Let $T$, $U$, $Q$ count the edges, the $3$-term runs and the $4$-term runs (runs, not components: a component on $k$ vertices contributes $\max(0,k-2)$ to $U$ and $\max(0,k-3)$ to $Q$).

> **Theorem B1.** The minimum number of deletions required to destroy every distance-$6$ edge is
> $$\tau = T - U + Q.$$

*Proof.* By Theorem 3 of §2.3 every component is a path on at most $4$ vertices. For a path on $v$ vertices the minimum vertex cover has size $\lfloor v/2 \rfloor$, so the cover of a path on $k$ vertices is $\lfloor k/2 \rfloor$. Summing $(k-1)-(k-2)+(k-3)$ over components reproduces $\lfloor k/2\rfloor$ for $k = 2,3,4$ — and **only** for those, since $k=5$ would give $3$ against the true value $2$. The cap of Theorem 3 is thus exactly what makes the identity hold. $\blacksquare$

*Verification* by direct component decomposition:

| lines | component census | min cover | $T-U+Q$ |
|-------|------------------|-----------|------|
| $\lbrace 5,7\rbrace$ | $\lbrace 1{:}4, 2{:}4, 3{:}4, 4{:}6\rbrace$ | 20 | 20 |
| $\lbrace 5,7,11\rbrace$ | $\lbrace 1{:}68, 2{:}56, 3{:}44, 4{:}42\rbrace$ | 184 | 184 |
| $\lbrace 5,7,11,13\rbrace$ | $\lbrace 1{:}1100, 2{:}788, 3{:}524, 4{:}378\rbrace$ | 2068 | 2068 |

**This is an exact combinatorial identity: no independence assumption and no density heuristic enters.**

### B.2 Propagation laws

Let $G = T - D$ count genuine gap-$6$ pairs, $D$ those with a survivor between. *(The twins sit in $D$: the surviving middle differs by $2$ from one of the two endpoints. So $G$ — the object [V, App. C.2.1.3] targets — is exactly the twin-free part, which is the content of the caution above. Incidentally, measured on all four cycles below, $U = D$ exactly; we do not use this.)*

> **Theorem B2.** On the full cycle, the entry of a new line $r$ gives
> $$T' = (r-2)T, \qquad D' = (r-3)D, \qquad G' = (r-2)G + D.$$

*Proof.* Of the $r$ copies of a pair, one has its left member struck and one its right, leaving $r-2$. A $D$-configuration has three sensitive positions (both ends and the middle), leaving $r-3$; and the copy whose middle is deleted becomes a genuine gap-$6$. $\blacksquare$

| lines | $V$ | $T$ | $D$ | $G$ |
|-------|-------|-------|-------|-------|
| $\lbrace 5\rbrace$ | 8 | 6 | 4 | 2 |
| $\lbrace 5,7\rbrace$ | 48 | 30 | 16 | 14 |
| $\lbrace 5,7,11\rbrace$ | 480 | 270 | 128 | 142 |
| $\lbrace 5,7,11,13\rbrace$ | 5,760 | 2,970 | 1,280 | 1,690 |

> **Corollary B1.** On the full cycle, $\dfrac{T}{V} = \rho_p = \prod_{5\le s\le p}\dfrac{s-2}{s-1}$ and $\dfrac{D}{T} = \theta_p = \dfrac{2}{3}\prod_{7\le s\le p}\dfrac{s-3}{s-2}$ — **exact identities, not estimates.**

| $p$ | 23 | 53 | 101 | 199 | 499 | 997 |
|------|--------|--------|--------|--------|--------|--------|
| $\rho_p$ | 0.4358 | 0.3607 | 0.3151 | 0.2746 | 0.2367 | 0.2138 |
| $\theta_p$ | 0.3606 | 0.2967 | 0.2588 | 0.2253 | 0.1941 | 0.1753 |

Both tend to zero: distance-$6$ pairs become rarer, yet a growing share of those remaining become genuine gaps.

### B.3 Theorem B3 (tail compression)

Inside $(P^2,9P^2)$, after the lines up to $P$ have acted, every surviving composite has the form $n=qr$ with
$$P\lt q\lt 3P,\qquad q\le r\lt \frac{9P^2}{q}\lt 9P.$$
Indeed three factors above $P$ would give $n\gt P^3\gt 9P^2$ for $P\gt 9$, and the smaller of the two remaining factors is below $3P$. Consequently the number of genuinely new strikes contributed later by a line $q$ with $P\lt q\lt 3P$ is
$$E_P(q)=\pi(9P^2/q)-\pi(q-1)\lt 2(3P-q)+1,$$
so a line approaching $3P$ loses power because the available cofactor interval contracts.

A related compression occurs among the **late lines in the sweep up to $P$ itself**:

> **Theorem B3.** For $P \ge 243$ and $P/3 \lt  q \lt  P$, every new strike of $q$ inside the window has the form $x = qr$ with $r$ **prime**.

*Proof.* The cofactor satisfies $r \lt  9P^2/q \lt  27P$. If $r$ were composite, all its prime factors would be $\ge q$ (it survived the smaller lines), so $r \ge q^2 \gt  P^2/9$. The contradiction holds precisely when $P^2/9 \ge 27P$, i.e. $P \ge 243$. $\blacksquare$

**Finite check around the threshold.** Direct enumeration of new strikes with composite cofactor:

| $P$ | 101 | 151 | 199 | 211 | **241** | 251 | 307 | 499 | 997 |
|-----------|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| anomalies | 26 | 9 | 6 | 5 | **0** | 0 | 0 | 0 | 0 |

The enumeration exhibits anomalies at smaller $P$ and none in the tested cases from $241$ onward; this is consistent with, but stronger numerically than, the proved sufficient threshold $243$. The sharper pointwise condition is $q^3 \gt  9P^2$, i.e. $q \gt  9^{1/3}P^{2/3}$; and the two conditions cross exactly at
$$\frac{P}{3} = 9^{1/3}P^{2/3} \iff \frac{P^3}{27} = 9P^2 \iff P = 243,$$
so $243$ is the point at which the constraint $q \gt  P/3$ becomes the binding one.

---

## Appendix C — Routes that were tried and closed

Each of the four accounts below was in the body of §3 in an earlier version. They are collected here so that §3 reads as a sequence of results, and kept in full because a route closed by measurement or by proof is worth more written down than left to be attempted again. In each case the conclusion, and its status as proof or as measurement, is stated in the corresponding stub in §3.

### C.1 Blocks of consecutive periods, and why lengthening the block does not help

Section 3.3 bounds the exceptions over one period of $35$ sectors. Consecutive periods are coupled in the same way that consecutive sectors are, so the same question can be asked of a block of $L$ periods — $35L$ sectors — and the answer moves. Write $B_L$ for the maximum of $\sum_i |S_{M_i} \cap E_{M_i}|$ over such a block under the twinless hypothesis, so that $B_1 = 31$ is the content of §3.3 and

$$\sum_i C_{M_i} \gt  B_L \implies \text{a twin in the block}.$$

**How $B_L$ is computed, and a trap that is worth naming.** The natural procedure — enumerate the maximal configurations of each residue class and test each for a fixed prime divisor — is *not* sound for this purpose. A residue class whose maximum is $m$ also carries configurations of size $m-1$, $m-2$ and so on, obtained by deleting cells; deleting a cell removes conditions and can only make admissibility easier. Those sub-configurations are never enumerated, so "every configuration at level $\ell$ dies" establishes nothing about level $\ell$. The sound procedure reverses the order: fix a residue for each prime $q$, switch the line $q$ on *inside* the transfer recursion, and read off the maximum. That maximum is by construction the largest admissible configuration at those residues, and the maximisation over residues is $B_L$. It is also faster by orders of magnitude.

**Values.** By that procedure, maximising over the residues of every prime up to the stated bound:

$$B_1 = 31, \qquad B_3 = 67, \qquad B_5 = 100, \qquad B_7 = 138, \qquad B_9 = 163.$$

The first three are certain: $B_1$ is §3.3; $B_3$ and $B_5$ are stable under every prime tested and $B_5$ was obtained twice, once by the sound procedure and once by exhaustive enumeration with an independent admissibility test, which agree. $B_7$ and $B_9$ are stable across twelve and eight consecutive primes respectively but were computed with pruning, so they are lower bounds with strong stability rather than certified maxima.

The extremal configuration at $L=3$ carries $66$ linear and $67$ quadratic conditions — $133$ polynomials of total degree $200$ — and every prime $q \le 200$ leaves it an admissible residue, so §3.3's conclusion transfers: no finite set of lines lowers $67$ either. Two features of the optimum are worth recording. First, it does *not* preserve the single-window maximum in the middle: the three windows contribute $20, 26, 21$, so the block optimum spends $31 - 26 = 5$ of the central window's capacity to gain elsewhere. Second, the killing is concentrated: across every level from $144$ down to $138$ at $L = 7$, the primes $29$ and $37$ account for about ninety per cent of the eliminated configurations, the remainder falling to $43$, $53$, $71$, $73$, $79$ and $97$.

In requirement per sector, $(B_L+1)/35L$ reads $0.914$, $0.648$, $0.577$, $0.567$, $0.521$. It falls, and the next paragraph says why, and how far.

**The quadratic shadow, and the order of $B_L$.** Each exceptional cell carries, besides its linear primality conditions, the condition that the *other* member of the cell survive. Those partners are

$$Q_A = (M+2)^2-2, \quad Q_C = (M+4)^2-2, \quad Q_D = (M+5)^2-11, \quad Q_E = (M+6)^2-14, \quad Q_F = (M+6)^2-2,$$

so each type forbids, modulo a prime $q \gt  17$, a number of residue classes that is exactly

$$\omega_A = \omega_C = 2+\chi_2(q), \qquad \omega_D = 3+\chi_{11}(q), \qquad \omega_E = 3+\chi_{14}(q), \qquad \omega_F = 3+\chi_2(q),$$

with $\chi_d(q)$ the Legendre symbol. The linear conditions supply one forbidden class for $A$ and $C$ and two for $D$, $E$ and $F$; the partner supplies two more exactly when the relevant $d$ is a quadratic residue. Since the quadratic characters are non-principal, each $\omega$ has mean value $2$ for $A$ and $C$ and $3$ for $D$, $E$ and $F$.

> **Proposition 1.** Let a block of $N = 35L$ consecutive sectors carry an admissible configuration of exceptional cells under the twinless hypothesis, and for $X \in \lbrace A,C,D,E,F\rbrace$ let $I_X$ be the set of sector indices carrying a cell of type $X$. Then
> $$|I_A|, |I_C| \ll \frac{N}{\log^2 N}, \qquad |I_D|, |I_E|, |I_F| \ll \frac{N}{\log^3 N},$$
> and consequently
> $$B_L \ll \frac{L}{\log^2 L}.$$

*Proof.* **Step 1: each type forbids an exact number of residue classes.** Fix a prime $q \gt  17$. Admissibility at $q$ means that some residue may be assigned to $M_0$ modulo $q$ at which no polynomial of the configuration vanishes; fix that residue and write $t \equiv M_i \pmod q$. Since $6$ is invertible modulo $q$, the map $i \mapsto t$ is a bijection of $\mathbb{Z}/q$, so it suffices to count forbidden values of $t$.

A cell of type $A$ at index $i$ carries one linear condition and one quadratic one:
$$M_i+2 \ \text{prime}, \qquad (M_i+2)^2-2 \ \text{surviving}.$$
Modulo $q$ these forbid
$$t \equiv -2 \qquad\text{(one class)}, \qquad (t+2)^2 \equiv 2 \qquad\text{($1+\chi_2(q)$ classes)},$$
with $\chi_d(q)$ the Legendre symbol. The two never coincide, since $t \equiv -2$ would give $0 \equiv 2$. Hence exactly $2+\chi_2(q)$ classes, and the same count for $C$ with $-2$ replaced by $-4$.

A cell of type $D$ carries two linear conditions and one quadratic:
$$M_i+2 \ \text{prime}, \qquad M_i+8 = M_{i+1}+2 \ \text{prime}, \qquad (M_i+5)^2-11 \ \text{surviving}.$$
The linear classes $t \equiv -2$ and $t \equiv -8$ are distinct for $q \gt 3$, and
$$(t+5)^2 \equiv 11$$
contributes $1+\chi_{11}(q)$ further classes, disjoint from them because either substitution gives $9 \equiv 11$, impossible for $q \gt 2$. Hence exactly $3+\chi_{11}(q)$.

The types $E$ and $F$ go the same way. Collecting the four computations, and writing $\omega_X(q)$ for the number of forbidden classes:

| type | linear offsets | quadratic condition | $\omega_X(q)$ |
|------|----------------|---------------------|------|
| $A$ | $-2$ | $(t+2)^2 \equiv 2$ | $2+\chi_2(q)$ |
| $C$ | $-4$ | $(t+4)^2 \equiv 2$ | $2+\chi_2(q)$ |
| $D$ | $-2, -8$ | $(t+5)^2 \equiv 11$ | $3+\chi_{11}(q)$ |
| $E$ | $-2, -10$ | $(t+6)^2 \equiv 14$ | $3+\chi_{14}(q)$ |
| $F$ | $-4, -8$ | $(t+6)^2 \equiv 2$ | $3+\chi_2(q)$ |

In every case the overlap check between the linear and quadratic classes reduces to $16 \equiv 14$ or $4 \equiv 2$, impossible for $q \gt 2$, so the counts add without correction.

*Verification.* Computed directly for all $423$ primes $19 \le q \lt  3000$: zero disagreement with $\omega_A = \omega_C = 2+\chi_2$, $\omega_D = 3+\chi_{11}$, $\omega_E = 3+\chi_{14}$, $\omega_F = 3+\chi_2$.

**Step 2: the sifting dimension is the mean of $\omega_X$.** $I_X$ is contained in $\lbrace 0,1,\dots,N-1\rbrace$ and avoids $\omega_X(q)$ classes modulo every prime $q \gt  17$; the primes $q \le 17$ contribute a bounded factor and are ignored. Since $\chi_2$, $\chi_{11}$ and $\chi_{14}$ are real non-principal characters — of conductors $8$, $44$ and $56$ — the series $\sum_q \chi_d(q)/q$ converges, by the non-vanishing of $L(1,\chi_d)$. Hence

$$\prod_{17 \lt  q \lt  z}\Bigl(1-\frac{\omega_X(q)}{q}\Bigr) = \prod_{17 \lt  q \lt  z}\Bigl(1-\frac{\kappa_X}{q}\Bigr)\cdot\prod_{17 \lt  q \lt  z}\frac{1-\omega_X(q)/q}{1-\kappa_X/q}  \asymp  \frac{1}{(\log z)^{\kappa_X}},$$

with $\kappa_A = \kappa_C = 2$ and $\kappa_D = \kappa_E = \kappa_F = 3$, the second product converging because its logarithm is $-\sum_q \chi_d(q)/q + O(\sum_q q^{-2})$.

**Step 3: the upper-bound sieve.** Selberg's sieve applied to the interval $\lbrace 0,\dots,N-1\rbrace$ with the removed classes of Step 1 gives, for any $z$,

$$|I_X|  \le  N \prod_{q \lt  z}\Bigl(1-\frac{\omega_X(q)}{q}\Bigr)\bigl(1+o(1)\bigr)  +  O\bigl(z^{2+\varepsilon}\bigr).$$
The error is the usual one for sifting an interval: with $|\lambda_d| \le 1$ the remainder is $\sum_{d_1,d_2 \lt  z} |r_{[d_1,d_2]}|$ where $r_m$ counts the removed classes modulo $m$, so it is bounded by a divisor-function factor times $z^2$.

Taking $z = N^{1/3}$ makes the error $O(N^{2/3})$ and, by Step 2, the main term $\ll N/(\log N)^{\kappa_X}$. This is the stated bound for each $I_X$.

**Step 4: summation.** Under the twinless hypothesis the type $B$ is empty, since it requires both $M+2$ and $M+4$ prime. A sector carries at most one cell of any given type, so the number of exceptional cells in the block is exactly $\sum_X |I_X|$, which by Step 3 is $\ll N/(\log N)^2$. With $N = 35L$ this is $\ll L/\log^2 L$. $\blacksquare$

**This is a computation, not a new tool, and it should be read as one.** Reading the sieve dimension off the number of roots of the defining polynomials modulo each prime is the standard definition of dimension — the condition $\sum_{q \lt  s}(\log q)/f(q) = \kappa\log s + O(1)$ of Halberstam and Richert [5] — and the passage from a dimension-$\kappa$ sifting density to an upper bound of order $N/(\log N)^{\kappa}$ is the standard Selberg estimate; see [3] for the higher-dimensional theory and [5] for the sieve itself. The twin problem in this language is the case $\rho(q) = 2$, dimension $2$. What is particular to the present setting is only the input: that the exceptional cells of Theorem 4 have the five partners above, so that the quadratic characters $\chi_2$, $\chi_{11}$ and $\chi_{14}$ appear and split the five types into dimensions $2,2,3,3,3$. The conclusion then follows by quoting the standard machinery, and we claim nothing for the machinery.

*Two remarks on the shape of this.* The bound is an **upper-bound sieve only**, and upper bounds in a fixed dimension are the direction in which sieve methods have no parity obstruction; nothing here bears on the lower-bound side. And the two-sector types are smaller than the one-sector types by a full logarithm, so in a long block almost every exception is of type $A$ or $C$ — a block that is longer is structurally *simpler*, not more complicated.

The first consequence is the one that matters here: **the density of exceptions tends to zero**, so the requirement per sector is not bounded below by any positive constant.

**And the bound is numerically empty over every computable range.** Taking $\rho^{*}(D) \sim D/\log D$ for the largest admissible set in an interval of diameter $D$, the crude form $B_L \le 2\rho^{*}(210L)-1$ gives, per sector, $2.22$ at $L=1$, $1.59$ at $L=9$, $1.06$ at $L=401$, $0.82$ at $L=10^4$ and $0.51$ at $L=10^8$: it does not fall below $1$ until $L \approx 400$ and does not reach $1/2$ until $L \approx 10^8$. The measured values are far below it everywhere in range, so the observed decrease is not this bound taking effect. Nor do the data identify the exponent: over $1 \le L \le 101$ the quantity $B_L\log^2(210L)/(210L)$ reads $4.22, 4.42, 4.61, 4.99, 4.91, 5.80, 6.68, 7.37$ — rising, not settling — while $B_L\log(210L)/(210L)$ reads $0.789, 0.685, 0.663, 0.685, 0.651, 0.691, 0.720, 0.740$. On this range $\log D$ varies only from $5.3$ to $10.0$, and the two laws are not separated by it.

**What the whole calculation does not buy, stated exactly.** Since $B_L = o(L)$, the criterion no longer asks for a survivor every sector or every second sector: it suffices to prove $\sum_i C_{M_i} \ge \varepsilon L$ for any fixed $\varepsilon \gt  0$, that is, that a positive proportion of sectors contains at least one open cell. Measured at $M_0 = 448{,}353$, the survivor total is $366{,}120$, $1{,}100{,}106$ and $3{,}304{,}035$ over $L = 1, 3, 9$ — that is $10{,}461$, $10{,}477$ and $10{,}489$ per sector, flat — so the inequality holds by a factor of $11{,}810$, $16{,}419$ and $20{,}270$, widening with $L$. The survivor total is linear in $L$ with a large constant; its logarithm is $\log M_0$, not $\log L$, so no amount of lengthening changes its shape.

> **The reduction is therefore real and it is not a route.** What is now required of the survivor side is not a rate of growth but an *existence* statement: one open cell in a positive proportion of sectors. By Theorem 4 an open cell is a twin pair unless it sits at one of six named places, and [V, §3.4] measures that discrepancy at $0$, $1$ and $3$ over three full periods. So "prove $\sum_i C_{M_i} \ge \varepsilon L$" is "prove that a positive proportion of sectors contains a twin", and shrinking the right-hand side from $32$ to $O(L/\log^2 L)$ changes the number on the right while leaving the missing ingredient on the left exactly as it was.

---

### C.2 The square-phase mean, and the end of the "poor window" question

One may ask directly whether windows anchored at squares are systematically poorer than windows placed anywhere. The answer is an identity rather than an experiment.

For a window starting at $r^2$, the pair at offset $j$ survives $q$ exactly when $r^2 \not\equiv -2j$ and $r^2 \not\equiv -2j-2 \pmod q$. Writing $\rho_q(a) = \mathrm{card}\lbrace r : r^2 \equiv a\rbrace$ and $\nu_q(j) = \rho_q(-2j) + \rho_q(-2j-2)$ — the two conditions cannot hold at once — the average over **all square phases** is exactly, writing $\mu_{\mathrm{sq}}$ for it,
$$\mu_{\mathrm{sq}}(L)  =  \sum_{j\lt L}\ \prod_{q} \frac{q - \nu_q(j)}{q}. \qquad\text{(3.3)}$$

Computed against the naive density prediction $E = L\prod(q-2)/q$, and against the restricted average $\mu_{\mathrm{cop}}$ over roots that are themselves coprime to every old line:

| $p$ | $T_p^-$ (actual) | $\mu_{\mathrm{sq}}$ | $\mu_{\mathrm{cop}}$ | $E = L\delta$ |
|------|---------------|--------|--------|--------|
| 11 | 2 | 2.943 | 2.833 | 3.286 |
| 29 | 2 | 4.149 | 4.201 | 4.206 |
| 53 | 2 | 5.434 | 5.283 | 5.457 |
| 101 | 7 | 7.653 | 7.473 | 7.774 |
| 499 | 13 | 21.237 | 21.319 | 21.274 |
| 997 | 38 | 34.591 | 34.534 | 34.608 |

$\mu_{\mathrm{sq}}$ agrees with $E$ to within about $1$% from $p = 29$ onward, and restricting the roots changes nothing.

> **The square-phase mean has the exact expression (3.3); numerically it tracks the generic density prediction closely, the two differing by about $1$% or less from $p = 29$ onward in the sample above.** So the exact quantity is available in closed form, and on the tested range it shows no bias at the level of the mean — which replaces the earlier control experiment with a computation, though not with a proof that the two agree in the limit. Individual windows are of course far from the mean — $T_{53}^- = 2$ against $\mu_{\mathrm{sq}} = 5.43$ — but the scatter is governed by the correlation function of [II, Thm 4], not by any property of squares.

---

### C.3 Two constructions that do not help

**A window balanced across a bundle of lines.** One can design the window instead of inheriting it. For every line of a bundle $p_{\min} \le p \le p_{\max}$ to make exactly $2r+1$ strikes about a common centre $A$ divisible by all of them, the half-width $H$ must satisfy $2rp_{\max} \le H \lt  2(r+1)p_{\min}$, so such a window exists iff
$$\frac{p_{\max}}{p_{\min}} \lt  1 + \frac1r.$$
For $r = 1$ that is $p_{\max} \lt  2p_{\min}$ — the lines $11,13,17,19$ with $H = 40$ give three strikes each — and for $r = 2$ it is $p_{\max} \lt  1.5 p_{\min}$. Moreover the side strikes of different lines never coincide as long as $r \lt  p_{\min}$, so the bundle meets only at $A$.

*Why it changes nothing.* Take $p = 1009$, $q = 1013$, $r = 52$, so each makes $105$ strikes in one window, and slide the window along the common multiples $A_t = pq(2t+1)$. The incidence census of those $105$ positions against the lines $3, 5, 7$ is $48, 24, 12, 8, 6, 4, 2, 1$ — identical in every window over $t = 0,\dots,11$, and identical to the census of the odd numbers modulo $210$. Stronger: the **word** itself, the sequence of incidence patterns across the $105$ positions, is a cyclic rotation of the first window's word in every one of $20$ windows tested. The whole object is one word of length $105$ and a rotation, because $105$ consecutive positions cover every residue modulo $105$ exactly once. The construction promised to separate the *count* of overlaps from their *arrangement*; the measurement says there is nothing to separate, since the arrangement is the same word shifted.

**Ownership and the cofactor.** Writing a strike in a sector $[P^2,Q^2)$ as $N = pm$, it is new for $p$ exactly when $\mathrm{spf}(m) \ge p$, and the higher lines that return to it are exactly the primes $q$ with $p \lt  q \le P$ and $q \mid m$. Two consequences are clean: if $q \gt  p$ shares a new point of $p$ then $p^2q \lt  Q^2$, and conversely $P^2 \le p^2q \lt  Q^2$ makes $p^2q$ a guaranteed shared point. And if $p^3 \ge Q^2$ then $m \lt  Q^2/p \le p^2$ while $m$ has no factor below $p$, so $m$ is prime: in that layer every new strike is a product of exactly two primes (verified with no exception in the sectors $101\to103$, $499\to503$, $997\to1009$).

*Why this too changes nothing.* The condition $p^2q_1q_2\cdots \lt  Q^2$ is **not** a bound on interaction depth, and the derived layers $Q^{1/2}, Q^{2/5}, \dots$ do not exist: $10387 = 13\cdot17\cdot47$ sits inside $[101^2,103^2)$ and $1009091 = 97\cdot101\cdot103$ inside $[997^2,1009^2)$. More to the point, even in the clean layer the question "is this strike new?" becomes "is the cofactor prime?", and for smaller $p$ it becomes "is the cofactor free of prime factors below $p$?" — which is Buchstab's decomposition in the vocabulary of lines. The numbers say the same: of the raw strikes of the clean layer, the new ones are $29$ of $73$, $1158$ of $4756$ and $1492$ of $7938$ in those three sectors — 40, 24 and 19 per cent and falling. Even where no higher line can return, most strikes are still repeats from below.

---

---

### C.4 Smoothing the window with the classical kernels

Proposition 6 is stated for a sharp window, and a sharp window pays a boundary error of order $1$ per residue class. Replacing the window by a Fejér kernel removes most of that error, and moving the kernel as well removes more. **The smoothing itself is classical**, and so is the order it gains; what is recorded below is an exact discrepancy formula for the single kernel, a bound for the moving one, and a mirror law for the sector index that the quadratic trajectory of [I, §4.5] supplies. The point of the subsection, though, is the measurement that follows: it says how far this smoothing reaches inside the hierarchy of §3.9, and it does not reach the part that decides the answer.

**A mirror law for the sector index.** Fix an odd modulus $d$ and let $\rho(d)$ be the number of residues it forbids ($2^i$ when $d$ is a product of $i$ lines). Writing $N_d(s)$ for the number of those residues met inside the single sector $I_s = [a_s, a_{s+1})$, put $e_d(s) = N_d(s) - \rho(d)L_s/d$.

> **Proposition 7.** $e_d(s+d) = e_d(s)$; and for $0 \le s \le d-2$,
> $$e_d(d-2-s)  =  -\,e_d(s), \qquad\text{with}\qquad e_d(d-1) = 0 .$$

*Proof.* Periodicity is $a_{s+d} \equiv a_s \pmod d$, which is (4.4) of [I, §4.5]. For the reflection, the two facts needed are
$$a_{d-2-s} \equiv a_{s+1} \pmod d, \qquad L_s + L_{d-2-s} = 12d .$$
The first says that — the mirror sector begins, modulo $d$, exactly where $I_s$ ends — while $L_s + L_{d-2-s} = 12(s+1)+12(d-1-s) = 12d$, so the two sectors together cover exactly twelve full periods of $d$ and their errors must cancel. The sector $s = d-1$ has length $12d$ on its own, whence $e_d(d-1) = 0$. $\blacksquare$

*Verification.* Zero failures over the whole cycle for $d = 5, 7, 11, 13, 35, 55, 77$ and $385$, including the two ingredients of the proof checked separately. **So the word of phase errors along a cycle reads $e_0, e_1, \dots, -e_1, -e_0, 0$: it is odd about its own centre.**

**The triangular weight, and an exact discrepancy formula.** Replace the indicator of a window by the triangular weight of half-width $H$,
$$w_H(u)  =  \max\Big(1-\frac{\lvert u\rvert}{H},\,0\Big),$$
the Cesàro weight, which is the Fejér kernel on $\mathbb{Z}/d\mathbb{Z}$: $H\,w_H$ is the self-convolution of the indicator of $\lbrace 0,\dots,H-1\rbrace$, so its transform is $\lvert \widehat{\mathbf 1}\rvert^2 \ge 0$ and decays like $h^{-2}$ rather than $h^{-1}$. The weight and that representation are standard in exactly this setting; see [2], where sieve functions are averaged over unions of residue classes in a short interval with the same weight.

> **Proposition 8.** Write $H = qd + s$ with $0 \le s \lt d$. Then
> $$\max_{b \bmod d}\ \Big\lvert \sum_{n \equiv b \,(d)} w_H(n) - \frac{H}{d} \Big\rvert  =  \frac{s(d-s)}{dH}  \le  \frac{d}{4H}. \qquad\text{(3.7)}$$
> with the maximum attained at $b = 0$.

*Proof.* Let $c_j$ be the number of $n \lt H$ in the class $j \pmod d$ and $c_j = H/d + \delta_j$. The weighted count is $H/d + H^{-1}\sum_j \delta_j\delta_{j-b}$. Exactly $s$ of the classes have $c_j = q+1$ and the rest have $c_j = q$, and those $s$ classes form a cyclic interval $A$, so $\delta_j = \mathbf 1_A(j) - s/d$ and
$$\sum_j \delta_j\delta_{j-b}  =  \lvert A \cap (A+b)\rvert - \frac{s^2}{d}.$$
This is largest at $b = 0$, where $\lvert A\cap A\rvert = s$ and the value is $s - s^2/d = s(d-s)/d$; and $s(d-s)/d \le d/4$, with equality only when $s = d/2$ — so for the odd moduli of this paper the second inequality in (3.7) is always strict. $\blacksquare$

**Where this sits.** Smoothing by a Fejér kernel, and the resulting order $O(d/H)$, are classical: [6, Ex. 24.2.1.1(d)] asks for the pointwise estimate $0 \le \Delta_N(x) \le \min\lbrace N, 1/(4N\lVert x\rVert^2)\rbrace$, with the constant $\tfrac14$ arising the same way, from $\sin \pi x \ge 2\lVert x\rVert$. That estimate is not (3.6), though. The left side of (3.7) is an *average* of the kernel over a subgroup of frequencies, $d^{-1}\sum_{h\ne0} e(-hb/d)\Delta_H(h/d)$, not a pointwise value of it; applying the pointwise bound term by term and summing recovers the order but overshoots $d/(4H)$ by a factor of $2.93$, $3.25$ and $3.29$ at $d = 11, 101, 1001$, stable in $H$. **The equality in (3.7) is the part we have not found stated anywhere**, and it explains the near-sharpness of $d/(4H)$ without any measurement: the ratio of the two sides is $4s(d-s)/d^2$, which for odd $d$ is largest at $s = (d\pm1)/2$ and equals $(d^2-1)/d^2$.

**Moving the window as well: a double tent.** Now slide the centre linearly, $c_t = c_0 + t$, and weight the times themselves by a second triangle $q_T(t) = T^{-1}(1-\lvert t\rvert/T)$.

> **Proposition 9.** With that weighting,
> $$\lvert E_{d,b}\rvert  \le  \frac{d^4+10d^2-11}{45\,d\,H\,T^2}  \ll  \frac{d^3}{45\,H\,T^2},$$
> using the exact identity $\sum_{h=1}^{d-1}\csc^4(\pi h/d) = (d^4+10d^2-11)/45$.

*Proof.* Each triangle contributes the square of a Dirichlet kernel to the Fourier expansion of the error, giving $d^{-1}\sum_{h\ne 0} \lvert D_H(h)\rvert^2 H^{-1}\lvert D_T(h)\rvert^2T^{-2}$; bounding $\lvert D_N(h)\rvert \le \csc(\pi h/d)$ and summing by the identity gives the statement. $\blacksquare$

*The identity is classical*, one of a family of finite cosecant power sums going back to Euler; see [4] for the $\csc^4$ case and its higher analogues. The bound holds with worst ratio $0.8958$ over all $(d,H,T,b)$ we tested. **Taking $H \asymp T \asymp r$ gives $\lvert E\rvert \ll (d/r)^3$, so every modulus $d = o(r)$ loses its phase error without a full cycle modulo $d$ and without any primorial.**

**A remark on the case $H = T$.** There the Fourier multiplier of the two-stage weight is $\lvert D_N(h)\rvert^4/N^3 = \Delta_N(h/d)^2/N$ — the square of the Fejér kernel, which up to normalisation is the **Jackson kernel** of approximation theory. So at equal parameters the construction is a Jackson-type smoothing on the Fourier side; the spatial weight itself is a convolution of two triangles, not a Jackson kernel, and the two should not be confused.

**The exponent is sharp, and the construction has a name.** Expanding $E_{d,b}$ over the non-zero frequencies and keeping a single Fourier coefficient gives a lower bound for $\max_b \lvert E_{d,b}\rvert$; at $H = T = (d-1)/2$ one has $\lvert D_H(1)\rvert \asymp d$, so that lower bound and $d^3/(HT^2)$ are both of order $1$, and no smaller power of $d$ can hold uniformly in $H$ and $T$. **This settles the exponent $3$, not the sharpness of the constant $1/45$.** Measured at that choice, $\max_b\lvert E_{d,b}\rvert$ against the bound is $0.225/0.237$, $0.191/0.203$ and $0.181/0.193$ at $d = 11, 23, 37$ — a ratio near $0.94$, stable. The two-stage device is **iterated Fejér smoothing on $\mathbb{Z}/d\mathbb{Z}$**: the moving centre turns the time average into a second convolution on the same cyclic group, which is why the two Fejér multipliers multiply. Both the sharpness argument and the name are due to a respondent to a question of mine on MathOverflow; the numbers here are my own check of them.

Proposition 7 is what makes the second of these usable across sectors rather than inside one: the moving centre samples consecutive sectors, and their errors are odd about a common centre, so the sliding average is not merely a smoothing but a cancellation.

**Why the certificate survives smoothing.** Since $w_H(u) = H^{-1}\sum_{h=1}^{H}\mathbf 1_{\lbrace \lvert u\rvert \lt h\rbrace}$ and $q_T \ge 0$, a smoothed Bonferroni value is a positive average of sharp ones. So if the smoothed $\mathcal{L}_k$ exceeds $2$, some sharp window in the family has $L_k \gt 2$, and by Proposition 6 that window holds at least three open cells — inside the same sector, so Theorem 4 and Corollary 2 still apply. **Smoothing changes the estimate, not the target.**

**What the smoothing buys, measured.** Applying Proposition 8 to the single tent and Proposition 9 to the double one, with the fixed choices $H = L/4$ and $H = T = L/8$ centred at the sector midpoint:

| $M$ | sharp $L_7$ | tent $L_7$ | double tent $L_7$ | sharp $L_9$ | tent $L_9$ | double tent $L_9$ |
|------|------------|-----------|------------------|------------|-----------|------------------|
| $10{,}005$ | $-93$ | $-75.0$ | $-43.2$ | $502$ | $120.6$ | $59.4$ |
| $20{,}001$ | $-1{,}236$ | $-286.0$ | $-145.6$ | $779$ | $216.4$ | $110.5$ |
| $50{,}001$ | $-7{,}494$ | $-1{,}653.5$ | $-791.2$ | $1{,}567$ | $395.7$ | $199.2$ |

The gain on $L_7$ is a factor of about nine at $M = 50{,}001$. **It is nevertheless not enough: the sign does not change, and the order required stays where Proposition 6 put it.** Since the kernels are the classical ones and the exponent is sharp, this is not a failure of the particular smoothing chosen — it is as far as smoothing of this kind goes.

**One further route, closed by an equivalence.** Instead of smoothing line by line, one may smooth the survivor mask itself: with $A \subseteq \mathbb{Z}/Q\mathbb{Z}$ the set of cells surviving every line up to $P$, ask for
$$\Big\lvert \sum_t q_T(t)\sum_u w_H(u)\,\mathbf 1_A(c_t+u) - H\frac{\lvert A\rvert}{Q} \Big\rvert  \lt  H\frac{\lvert A\rvert}{Q}$$
for every centre $c$, with $H$ and $T$ polynomial in $P$ rather than in the primorial $Q$. The primorial does drop out — the least $H = T$ for which this holds is $2, 3, 5, 7, 10$ at $P = 7, 11, 13, 17, 19$, against $Q = 35$ up to $1{,}616{,}615$ — but the reason is not a new mechanism:

| $P$ | $Q$ | least $H = T$ | largest gap $g$ in $A$ |
|------|-----------|------------|---------------------------------------------|
| 7 | 35 | 2 | 5 |
| 11 | 385 | 3 | 7 |
| 13 | 5,005 | 5 | 11 |
| 17 | 85,085 | 7 | 18 |
| 19 | 1,616,615 | 10 | 25 |

**In every case $2H$ is the largest gap, to within one**, and necessarily so: the smoothed count is positive at every centre exactly when every window of length $2H$ meets $A$, which is the definition of Jacobsthal's function on this residue system. So establishing that inequality with $H$ polynomial in $P$ *is* a bound on $h(k)$, an open problem for over fifty years whose best bound comes from the linear sieve rather than from Fourier analysis. The route is recorded as closed; it is a restatement, not a reduction. It is also weaker than what §3.1 needs, which is not one survivor at some centre but three at a prescribed one.

**Our reading of why is a matter of where the mass sits.** Proposition 9 controls a modulus $d$ only while $d \ll r$. Splitting each $S_i$ by whether the product $d = p_1\cdots p_i$ of its subset falls below $r$:

| $M$ | $r$ | $S_1$ | $S_2$ | $S_3$ | $S_4$ | $S_5$–$S_7$ |
|------|------|-------|-------|-------|-------|-----------|
| $20{,}001$ | $3{,}333$ | $88.5$% | $40.1$% | $5.6$% | $0$% | $0$% |
| $50{,}001$ | $8{,}333$ | $90.0$% | $44.7$% | $8.7$% | $0.2$% | $0$% |

**Smoothing reaches almost all of $S_1$ and none of $S_5$ and beyond.** The arithmetic is immediate: for $p_1\cdots p_i \lt r$ the primes must average $r^{1/i}$, which at $i = 4$ and $r = 8{,}333$ means all four drawn from $\lbrace 5,7,11,13\rbrace$ — one subset — and at $i = 5$ means none at all. Since $S_1$ is the term that died at $M = 21$ and the terms that decide the sign of $L_7$ are $S_4$ through $S_7$, **the smoothing controls exactly the part that never needed controlling.** We record this as a closed route on that reading: the boundary error does not appear to be what makes the sign negative, and since the exponent of the moving kernel is sharp we do not expect a different window shape to change it.

---

---

---

**No progress toward the twin-prime conjecture is claimed, and no new bound.** Priority is not claimed for any result.

*The computations and much of the prose in this paper were prepared with AI assistance (Claude, Anthropic), used for drafting and rewriting code and text, running the computations, searching the literature, and auditing the paper against its own scripts. The research direction, the questions asked, the decisions about what to publish and what to withdraw, and the responsibility for every claim are the author's. The full note is in the repository README.*

---

## References

The companion papers are cited as [0], [I], [II], [III], [V]. This paper imports only their definitions and proves everything else. The eight works below are the only external ones it needs; the fuller comparison with the literature is in Paper V.

1. P. T. Bateman and R. A. Horn, *A heuristic asymptotic formula concerning the distribution of prime numbers*, Math. Comp. **16** (1962), 363–367.
2. G. Coppola and M. Laporta, *Sieve functions in arithmetic bands*, Hardy–Ramanujan J. **39** (2016), 21–37; arXiv:1503.07502.
3. H. G. Diamond and H. Halberstam, *A higher-dimensional sieve method*, Cambridge Tracts in Mathematics **177**, Cambridge University Press, 2008.
4. S. B. Ekhad, appendix to *Human and automated approaches for finite trigonometric sums*, arXiv:2204.08228 — Proposition Ton_2 and its higher analogues.
5. H. Halberstam and H.-E. Richert, *Sieve Methods*, Academic Press, 1974.
6. H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory III*, Cambridge University Press, in preparation.
7. T. T. K. Nguyen, *Finite-window noncovering on primorial wheels: higher-order CRT bounds and shift correlations*, Preprints.org (2026), doi:10.20944/preprints202608.1299.v1. — *A preprint, not peer reviewed; cited as contemporaneous independent work reaching the same finite-window diagnosis from the Goldbach side.*
8. A. Schinzel and W. Sierpiński, *Sur certaines hypothèses concernant les nombres premiers*, Acta Arith. **4** (1958), 185–208; erratum, ibid. **5** (1959), 259.
