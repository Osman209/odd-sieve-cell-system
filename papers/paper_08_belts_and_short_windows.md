# Belts and Short Windows

## Paper 8. What a line can do between its own square and the next, and the anatomy of the window between consecutive squares

---

### Abstract

Two local geographies. The belt between the squares of consecutive primes has an exact size, a new line's reach inside its own belt depends on the gap and not on the size of the line, and a whole age layer admits a deterministic ceiling; none of the three closes the argument, and the section says why. The short window between consecutive squares is then read in depth: which lines can create a new deep composite, how the shells of neighbouring lines overlap, and four named cells whose owners are governed by the quadratic character of a discriminant. **No progress toward the twin-prime conjecture is claimed.**

**Numbering.** This paper is one part of a set that was written as a single document and is now published in parts. Each part numbers its own results from one and is self-contained: a reference of the form [Pn, Thm 1] means Theorem 1 of Paper n, and an unqualified "Theorem 1" always means this paper's own. Result numbers therefore differ from those of releases before 2.0.0, where the whole set shared the numbering of the single document.

**How to read the claims in this paper.** Statements set as Theorems, Propositions and Corollaries are proved, and the proofs are given. One result in the set is labelled **Verified Law**: it is proved under a stated hypothesis and verified numerically outside it. Anything described as *measured* is a computation over a stated finite range and is labelled as such where it occurs.

**Keywords:** twin primes, sieve cycles, short intervals, cell coordinates.

**MSC 2020:** 11N35, 11N05, 11A41.

---

## Summary of the results in this part

**§2 — The gate belt: what a line can do between its own square and the next**

| Result | What it says | Section |
|-----------------|------------------------------------------------|---------|
| **Theorem 1** | The exact size of a belt between the squares of consecutive primes. | §2.1 |
| **Verified Law 2** | *Conditional on $g^2 \lt 2q$*, and **verified rather than proved**: a new line's reach depends on the gap, not on its size. | §2.2 |
| **Proposition 1** | In a belt of length $L$, any line $s$ makes at most $\lceil L/2s \rceil$ strikes — the layer ceiling. | §2.4 |

**§3 — The short window between consecutive squares**

| Result | What it says | Section |
|---------------|--------------------------------------------------|---------|
| **Corollary 1** | No integer of the window carries three shell factors, so the shell's whole overlap is the single count $R_2$ and the composites split into core and shell with no inclusion–exclusion. | §3.1 |
| **Proposition 1b** | A *new* strike of depth $\Omega \ge r$ forces its line below $(M+2)^{2/r}$, so the large lines lose the power to make deep composites one layer at a time. | §3.1 |
| **Proposition 1c** | Two shell cofactor strips meet only for twin lines above $M/2$, share at most one odd cofactor, and never meet three at a time. | §3.1 |
| **Proposition 1d** | The two shell thresholds differ by exactly $2$, and above the upper one the handover between adjacent lines is a single bit with a closed form in $\lfloor X/(p-2)\rfloor$ and $\lceil X/p\rceil$. | §3.1 |
| **Theorem 3** | Which lines can ever own a track: for $r \gt 3$, by the quadratic character of the discriminant. | §3.3.1 |
| **Theorem 4** | Simultaneity: a prime closes two of the four tracks in one window only under a stated congruence — nine primes in all. | §3.3.2 |
| **Proposition 2** | And why Theorem 4 obstructs nothing — $k$ tracks always admit a simultaneous solution. | §3.3.3 |

This part has no appendix of its own. The counting details for the window are in [P6, App. A], and the auxiliary distance-$6$ model — whose object is a prime pair $(p,p+6)$, not a twin pair — is in [P7, App. B].

---

## 1. Setting

We use Papers [P1] and [P2]–[P4] as follows. Paper [P9]–[P11] is a companion rather than a source: it is cited where the obstruction it derives explains why a cut is placed where it is, and nothing else is imported from it.

- **[P1]** supplies the window combinatorics: the increments $W_j$ of $\lfloor 2j^2/p\rfloor$, their uniform bound and their exact histogram.
- **[P2]** supplies the coordinates: the line $L_p(k) = p(p+2k)$ beginning at $p^2$, the grid $L_3$, the cells $C_b = (6b-1, 6b+1)$, and the square window with its $+8$ growth.
- **[P3]** supplies the exact cycle laws: the four-state law, its refinement by inheritance depth, arbitrary weights in $\Omega_{\le z}$, the refinement by line size, and the disjoint ownership layers.
- **[P4]** studies the transfer to a window of length $\asymp z^2$. On the tested windows, linear depth weights measure $1.0000$ to the reported precision, the tested soft truncations remain close to $1$, and the sharp depth-zero indicator is the exceptional endpoint with ratio near $0.80$. These are measurements, not an exact window theorem.

A word on the last point, since it is what makes this paper's organisation possible. The indicator of depth zero is the condition "both members of the cell survive" — that is, the twin condition. Thus, in the tested family, the largest transfer loss occurs precisely at the depth-zero indicator, the quantity that becomes a primality/twin condition inside the moving square window.

---

## 2. The gate belt: what a line can do between its own square and the next

Sections 3–5 work inside a sector bounded by consecutive odd squares. This section changes the unit: since every prime $q\gt 3$ has $q^2 \equiv 1 \pmod 6$, each prime has a **gate** $G_q$ with $q^2 = 6G_q+1$, and the cell $C_{G_q} = (q^2-2, q^2)$ is closed by $q$ itself. Consecutive primes $q\lt r$ therefore delimit a **belt** of cells $C_{G_q+1},\dots,C_{G_r-1}$ between two gates that are certainly closed. The belts tile the cell axis.

### 2.1 Theorem 1: the size of a belt

> **Theorem 1.** For consecutive primes $q\lt r$ with $g = r-q$, the belt holds exactly
> $\displaystyle G(q,r)  =  \frac{r^2-q^2}{6}-1  =  \frac{g(2q+g)}{6}-1$
> cells, so its size grows like $qg$.

*Proof.* Both $q^2$ and $r^2$ are $\equiv 1 \pmod 6$, so the cells strictly between the two gates are exactly the $(r^2-q^2)/6 - 1$ complete cells of $L_3$ in the interval. $\blacksquare$

*Verification.* $G = 3, 11, 7, 19, 11, 27, 51, 19, 67$ for the nine consecutive belts $5\to7, 7\to11, \dots, 31\to37$, and $247, 67, 667, 4011$ for $89\to97$, $101\to103$, $499\to503$ and $997\to1009$; each reproduces from the formula.

### 2.2 Verified Law 2: the new line's reach depends on the gap, not on its size

> **Verified Law 2 (conditional).** Suppose $g^2 \lt  2q$. Then, within its own belt, the number of cells the line $L_q$ can strike at all is
> $\displaystyle H_q  =  \left\lfloor \frac{2g}{3}\right\rfloor,$
> **independent of $q$.**

*Proof under the hypothesis.* If $g^2 \lt  2q$ the line completes no extra lap before the next gate, so it reaches only the cofactors $q+2, q+4, \dots, q+2g$, giving $g$ candidate strikes; one in every three falls on $L_3$ and so touches no cell of the grid, leaving $\lfloor 2g/3 \rfloor$. $\blacksquare$

**We do not call this a theorem, because the hypothesis is not available.** $g^2 \lt  2q$ is far weaker than Cramér's conjecture $g = O(\log^2 q)$, which would give it at once — but it is **stronger than anything currently proved, and stronger than the Riemann hypothesis supplies**: RH gives only $g \ll \sqrt q \log q$, hence $g^2 \ll q\log^2 q$, which does not suffice. **Verified over $17{,}981$ belts, every consecutive prime pair with $q \lt  200{,}000$: no failure.**

**The consequence is worth stating plainly.** The belt has $\sim qg/6$ cells and the line born at its left end can touch $\sim 2g/3$ of them. **For a twin gap $g=2$ the line touches exactly one cell, however large $q$ is** — one cell out of $\sim q/3$. A line at $q \approx 10^6$ entering a belt of some hundred thousand cells has a single strike available before the next gate opens.

### 2.3 The collapse of the new line's effect

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

### 2.4 A deterministic ceiling for a whole age layer

Nothing above uses primality of the intermediate lines, and the next bound deliberately gives them more power than they have.

> **Proposition 1.** In the belt $q\to r$ of length $L = r^2-q^2$, any line $s$ makes at most $\lceil L/2s \rceil$ strikes, of which at most a fraction $2/3$ touch cells of the grid. Hence, allowing **every** odd $s$ not divisible by $3$ in a range to act as an independent line and ignoring all overlap between them, the layer $q-D \le s \le q$ can close at most
> $\displaystyle C_D(q,r)  =  \sum_{\substack{q-D \le s \le q\cr  s \text{ odd},\ 3\nmid s}} \left\lceil \tfrac{2}{3}\left\lceil \tfrac{L}{2s}\right\rceil\right\rceil$
> cells.

For the belt $499 \to 503$ ($G = 667$): the newest quarter has ceiling $C = 168$ ($25$% of the belt) and closes $6$ in fact; the newest half has ceiling $376$ ($56$%) and closes $15$. For $997 \to 1009$ ($G = 4011$): the newest tenth has ceiling $316$ and closes $14$; the newest quarter $836$ and closes $28$; the newest half $1{,}977$ — under half the belt — and closes $68$. **The ceilings are generous by one to two orders of magnitude, and the real burden falls on lines far below $q/2$.**

### 2.5 And why the layer ceilings do not close the argument

Proposition 1 invites an obvious attempt: build the full pyramid of age layers $(q/2,q]$, $(q/4,q/2]$, … down to $s=5$, sum the ceilings, and hope the total falls short of $G$. **It does not.**

| belt | $G$ | $\sum$ ceilings over all layers | ratio |
|------|-------|------------------------------------------------------|-------|
| $499\to503$ | 667 | 2,094 | $3.1\times$ |
| $997\to1009$ | 4,011 | 13,935 | $3.5\times$ |
| $10007\to10009$ | 6,671 | 35,045 | $5.3\times$ |

and the cumulative total already passes $G$ at the **second** layer.

The asymptotic is worth getting right, because it is the point of the section. **The sum runs over every $s$ coprime to $6$, not over the primes**, and those have density $1/3$, so
$$\sum_{\substack{s \le q\cr (s,6)=1}} \frac1s  =  \frac13\log q + O(1), \qquad\text{whence}\qquad \sum_s \tfrac23\cdot\tfrac{L}{2s}  =  \frac{L}{3}\sum_s\frac1s  \sim  \frac{L}{9} \log q .$$
Against $G \sim L/6$ the ratio is therefore
$$\frac{\sum_s C_s}{G}  \sim  \frac23\log q$$
— a **logarithm**, not an iterated logarithm. Checked against the table: $\tfrac23\log(q/4)$ gives $3.22$, $3.68$, $5.22$ at $q = 499,\ 997,\ 10007$ against the measured $3.14$, $3.47$, $5.25$.

> **So the belt decomposition establishes three of the four things one would want — the belt grows like $qg$, the new line's reach is $O(g)$ and independent of $q$, and no fixed set of old lines can serve arbitrarily long belts — and refutes the fourth. The moving tail of recent lines is not capacity-limited; its ceilings exceed the belt by a factor that grows.** What is left is the forced overlap between the layers, which is $\prod(1-2/q)$ and describes the cycle, not the belt. This is [P9, §2]–[P9, §3] again, reached from the belt side.

---

## 3. The short window between consecutive squares

Sections 3–5 work inside a sector bounded by consecutive odd squares three apart, and §2 changes the unit to the belt between the squares of consecutive primes. This section uses a third unit, the **short window**
$$W_M = (M^2,\ (M+2)^2), \qquad \lvert W_M\rvert = 4M+4,$$
between two consecutive odd squares — one third of a sector. Two things live naturally here and nowhere else in the paper: the depth a line can create, in §3.1 and §3.2, and the four named cells of §3.3 onwards, which Paper 2 already indexes on this window. The results below are stated for $W_M$ and are not statements about the sector.

### 3.1 A depth ladder: which lines can create a new deep composite

The cut of [P9, §2.1] takes $z$ with $z^3$ above the window, so that every surviving endpoint is prime or a product of exactly two primes. Read line by line rather than as a single cut, the same inequality becomes a ladder.

> **Proposition 1b.** Let $N$ lie in $(M^2,(M+2)^2)$ and let $p$ be its least prime factor, so that the strike $N$ on the line $p$ is *new* — not inherited from any smaller line. If $\Omega(N) \ge r$ then $N \ge p^r$, and therefore
> $\displaystyle p  \lt  (M+2)^{2/r} .$

*Proof.* Every prime factor of $N$ is at least $p$, so $N \ge p^{\Omega(N)} \ge p^r$; and $N \lt (M+2)^2$. $\blacksquare$

*Verification.* Zero violations of $p^{\Omega(N)} \lt (M+2)^2$ over the $959{,}468$ new strikes arising in all windows with odd $M \lt 1500$.

So the layers come off one at a time as the lines grow:

| requirement on a new strike | bound on the line | at $M = 10^5$ |
|-----------|-----------|-----------|
| $\Omega \ge 3$ | $p \lt (M+2)^{2/3}$ | $p \lt 2{,}155$ |
| $\Omega \ge 4$ | $p \lt (M+2)^{1/2}$ | $p \lt 316$ |
| $\Omega \ge 5$ | $p \lt (M+2)^{2/5}$ | $p \lt 100$ |

**Above the first rung, at $(M+2)^{2/3} \lt p \le M$, every new strike is $N = pq$ with $q$ prime**, and any strike with composite cofactor is inherited from a smaller line. At $M = 10^5$ that leaves $2{,}155$ of the $9{,}593$ lines able to create a strike of depth three, $316$ able to create one of depth four, and $100$ of depth five.

The bound is necessary and not sufficient: a line below the rung may still fail to produce such a strike in a given window because none of the eligible products lands there. At $M = 65$ the line $13$ is admissible, since $13^3 = 2{,}197 \lt 67^2 = 4{,}489$, yet the largest line actually making a deep new strike in that window is $11$. The narrowest case we found is $M = 35$, where $11^3 = 1331 = 11 \times 121$ lands inside $(35^2, 37^2)$ with $11 \lt 37^{2/3} = 11.10$.

**One number per line: its depth capacity.** Collecting the rungs, define
$$D_M(p)  =  \max\lbrace r : p^r \lt (M+2)^2 \rbrace ,$$
the deepest composite the line $p$ can be the first owner of. Every line then carries two numbers — how often it strikes, and how deep it may go:
$$H_M(p) \approx \frac{2M+2}{p}, \qquad D_M(p) .$$
Both fall as $p$ grows. Small lines strike often and go deep; large lines strike twice and never past $\Omega = 2$.

At $M = 499$, where $(M+2)^2 = 251{,}001$, the capacity partitions the lines exactly:

| lines | $D_M(p)$ |
|-----------------|-------|
| $67 \le p \le 499$ | 2 |
| $23 \le p \le 61$ | 3 |
| $13 \le p \le 19$ | 4 |
| $p = 11$ | 5 |
| $p = 7$ | 6 |
| $p = 5$ | 7 |
| $p = 3$ | 11 |

The boundaries are sharp, not approximate. $61^3 = 226{,}981 \lt 251{,}001$, and the line $61$ does own a triple in that window, $249{,}307 = 61^2\cdot 67$; while $67^3 = 300{,}763$ exceeds it, and every number the line $67$ owns there is a semiprime, for instance $249{,}173 = 67 \cdot 3719$. One rung up, $23^4 = 279{,}841$ is already too large, so $23$ cannot start an $\Omega = 4$, but it does start triples such as $249{,}343 = 23\cdot37\cdot293$.

**Capacity is not a promise, and the gap is where one would not guess.** $19^4 = 130{,}321$ is comfortably inside the window at $M = 499$, so that line is permitted depth four, yet the deepest number it owns there has $\Omega = 3$. Comparing capacity with what is actually owned, over all lines that own anything, the capacity is reached by $74$ of $83$ lines at $M = 499$, $118$ of $128$ at $M = 999$ and $460$ of $482$ at $M = 4{,}999$ — **and in each case the shortfall is confined to the smallest lines**:

| $M$ | $p=3$ | $p=5$ | $p=7$ | $p=11$ | $p=13$ | first line attaining its capacity |
|-------|-------|-------|-------|-------|-------|-------|
| 499 | 11 / 9 | 7 / 5 | 6 / 5 | 5 / 4 | 4 / 3 | 23 |
| 999 | 12 / 8 | 8 / 6 | 7 / 5 | 5 / 4 | 5 / 4 | 17 |
| 4,999 | 15 / 10 | 10 / 8 | 8 / 6 | 7 / 5 | 6 / 5 | 19 |

(capacity / deepest owned). The line $3$ has room for eleven or twelve factors and reaches eight or nine. The reason is the shortness of the window rather than any arithmetic obstruction: a number of that depth owned by $3$ must be smooth as well as large, and a window of length $4M+4$ near $M^2$ is too thin to be likely to contain one. From the middle lines upward the capacity is met exactly, and for $p$ above the first rung it is met trivially, every owned number there being a semiprime.

**The shell takes over the line range as $M$ grows.** The share of lines with $D_M(p) = 2$ — those that can do nothing but $pq$ — is $72$%, $81.9$%, $85.6$%, $91.0$%, $92.8$% and $95.8$% at $M = 101$, $499$, $999$, $4{,}999$, $9{,}999$ and $49{,}999$. **Almost every line, in the limit, is incapable of any depth at all.**

In terms of the cofactor: if $p$ owns $N = pm$ and $m$ has $t$ prime factors then $m \ge p^t$, so $p^{t+1} \lt (M+2)^2$ and $t \le D_M(p) - 1$ — zero violations over the $848$ composites of that window. Writing $p \sim M^{\alpha}$ turns the rungs into shells of the exponent, $\alpha r \lt 2$, and the boundaries $M^{2/3}, M^{1/2}, M^{2/5}, M^{1/3}, \dots$: **each shell inward permits one more factor.**

**How much of the line range this removes, measured.** Each line meets the window through a cofactor window of its own,
$$\frac{M^2}{p} \lt  m \lt  \frac{(M+2)^2}{p},$$
of length $(4M+4)/p$, so it makes about $(2M+2)/p$ strikes there — verified to within $1.5$ for all $346{,}798$ pairs $(M,p)$ with odd $M \lt 3000$. At $p \approx M$ that is about **two**, which is why the last lines have so little to do: at $M = p = 17$ the cofactors are $19$ and $21$, one prime and one composite, so one new strike and one inherited.

Splitting the lines at the first rung and counting what each half actually produces:

| $M$ | region | lines | strikes | new $pq$ | new deep | inherited |
|-------|-------|-------|-------|-------|-------|-------|
| 1,005 | $p \le (M+2)^{2/3}$ | 24 | 5,242 | 446 | 1,073 | 3,723 |
| 1,005 | $(M+2)^{2/3} \lt p \le M$ | 143 | 1,594 | 204 | **0** | 1,390 |
| 10,005 | $p \le (M+2)^{2/3}$ | 89 | 63,493 | 4,095 | 12,259 | 47,139 |
| 10,005 | $(M+2)^{2/3} \lt p \le M$ | 1,139 | 15,867 | 1,440 | **0** | 14,427 |

**At $M = 10^4$ the $89$ lines below the rung are $7.2$% of the $1{,}228$ lines and produce all of the new depth; the other $93$% produce none.** They also carry four times as many strikes. The share below the rung falls as $M$ grows — $28$%, $14.4$%, $7.2$% at $M = 101$, $1{,}005$, $10{,}005$ — so the asymmetry sharpens.

**A sharper form of the same fact.** For a line above the rung the composite strikes are not merely inherited from *some* smaller line — they are inherited from a line below the rung. If $p \gt (M+2)^{2/3}$ and the cofactor $m = N/p$ is composite with least prime factor $r$, then $r \le \sqrt m$ and $m \lt (M+2)^2/p$, so
$$r  \lt  \frac{M+2}{\sqrt p}  \lt  \frac{M+2}{(M+2)^{1/3}}  =  (M+2)^{2/3} .$$
Zero exceptions over the $2{,}162{,}075$ composite-cofactor strikes on lines above the rung for odd $M \lt 2500$. So the lines split into a small **core** that builds every deep composite and a large **shell** whose strikes are either new semiprimes or revisits to numbers the core already owns.

The window $(17^2, 19^2)$ shows it in full: the core is $\lbrace 3,5,7\rbrace$ and the shell $\lbrace 11,13,17\rbrace$; the shell's new strikes are $11\cdot29$, $11\cdot31$, $13\cdot23$ and $17\cdot19$, all semiprimes; and the eight deep composites of the window — $297$, $315$, $325$, $333$, $343$, $345$, $351$, $357$ — have least prime factors $3,3,5,3,7,3,3,3$, every one of them in the core.

**The ladder is close to attained.** The bound $(M+2)^{2/r}$ is not merely an upper limit that the numbers stay far below; at the top of each layer the largest owner sits just under it. In the window $(499^2, 501^2)$, which holds $999$ odd integers:

| $\Omega$ | count | largest owner | bound $(M+2)^{2/r}$ |
|-------|-------|-------|-------|
| 2 | 355 | 499 | 501.00 |
| 3 | 285 | 61 | 63.08 |
| 4 | 135 | 11 | 22.38 |
| 5 | 50 | 7 | 12.02 |
| 6 | 17 | 3 | 7.94 |
| $\ge 7$ | 6 | 3 | 5.91 |

At $M = 999$ the same shape holds with owners $991$, $89$, $29$, $7$, $5$, $3$ against bounds $1001$, $100.1$, $31.6$, $15.9$, $10.0$, $7.2$. The layers collapse towards the first lines very fast: **almost all depth beyond $\Omega = 5$ is owned by $3$ alone.**

The window at $M = 499$ decomposes as
$$999  =  151\ \text{primes} + 355\ P_2 + 493\ \text{deeper},$$
and every one of the $493$ deeper composites is owned by the core — the shell contributes none.

### 3.2 The shell: overlap, strips, and the handover bit

**The shell's whole behaviour, in one bound and one identity.** Three prime factors all above $P_0 = (M+2)^{2/3}$ would give a product above $P_0^3 = (M+2)^2$, outside the window. Hence:

> **Corollary 1.** No integer of the window carries three shell factors: **a shell line strikes a number that at most one other shell line also strikes.**

A shell strike $N = pm$ is therefore of exactly three kinds. If $m$ is prime the strike is new, and then $m \gt M$, since $m \le M$ would put $N \le M^2$; such an $N$ is struck by one shell line only. If $m$ is composite the number already belongs to the core, and it is revisited by one shell line or by two — never three. Writing $S$ for the new positions, $R_1$ and $R_2$ for the core positions visited once and twice, the raw strike count and the number of distinct positions touched are
$$H = S + R_1 + 2R_2, \qquad D = S + R_1 + R_2, \qquad\text{so}\qquad H - D = R_2 .$$
**All of the shell's internal overlap is one number.** Measured:

| $M$ | $S$ | $R_1$ | $R_2$ | $H$ | three shell factors |
|-------|-------|-------|-------|-------|-------|
| 35 | 12 | 6 | 2 | 22 | 0 |
| 101 | 28 | 28 | 8 | 72 | 0 |
| 499 | 105 | 122 | 77 | 381 | 0 |
| 999 | 195 | 279 | 156 | 786 | 0 |
| 1,999 | 350 | 599 | 312 | 1,573 | 0 |
| 4,999 | 790 | 1,613 | 775 | 3,953 | 0 |

A double visit looks like $249065 = 5 \cdot 109 \cdot 457$ in the window at $M = 499$: the core owns it through $5$, and the shell lines $109$ and $457$ each pass over it later without creating anything. A third shell line on the same number is impossible.

**So the composites of the window split without any inclusion–exclusion between the parts:**
$$\mathcal{C}_{\text{core}} = \lbrace N : P^-(N) \le P_0 \rbrace, \qquad \mathcal{C}_{\text{shell}} = \lbrace N = pq : P_0 \lt p \le M \lt q \rbrace\rvert,$$
the second consisting entirely of semiprimes, the first holding every $N$ with $\Omega \ge 3$ together with the semiprimes whose small factor is in the core.

**The strips of two shell lines almost never meet.** Each shell line inspects the cofactor strip $I_p = (M^2/p,\ (M+2)^2/p)$. For $p \lt r \le M$ these overlap exactly when $rM^2 \lt p(M+2)^2$; writing $r = p+g$ this is $gM^2 \lt 4p(M+1)$.

> **Proposition 1c.** Two shell strips meet only if $r - p = 2$, and then only if $p \gt M^2/2(M+1)$, roughly $p \gt M/2$. The overlap has width less than $2$, so the two lines share **at most one odd cofactor**. Three strips never meet.

*Proof.* If $g \ge 4$ then $p \le M-4$, so $4p(M+1) \le 4(M-4)(M+1) \lt 4M^2 \le gM^2$ and the condition fails. With $g = 2$ it reads $2M^2 \lt 4p(M+1)$, which is the stated bound on $p$. The width is
$$\frac{(M+2)^2}{p+2} - \frac{M^2}{p}  =  \frac{4p(M+1) - 2M^2}{p(p+2)}  \lt  2$$
because the numerator less twice the denominator is $-2(M-p)^2 \lt 0$, and $p \le M-2$; an interval shorter than $2$ holds at most one odd number. A triple would need $p, p+2, p+4$ all prime, impossible above $7$. $\blacksquare$

*Verification.* Over odd $M \lt 3000$: **all $27{,}673$ overlapping strip pairs have gap $2$**, the condition on $p$ misclassifies none of the $71{,}926$ twin-line pairs, no overlap has width $2$ or more — $21{,}157$ share exactly one odd cofactor and $6{,}516$ share none — and there are **no triple overlaps at all**.

So the shell is a sequence of disjoint strips with isolated single touches, and the touches occur only at twin lines above $M/2$. At $M = 499$ the twin lines $461, 463$ share the cofactor $541$, and $431, 433$ share $579$; at $M = 17$ the lines $11, 13$ share $27$.

*One thing that is not a correlation.* At a touch the two strikes are both new or both inherited, never one of each — but this is forced, not observed: the shared cofactor is a single number, and both strikes are new exactly when it is prime. Nothing is measured by it.

**Two thresholds, two apart.** The shell has a second structure that owes nothing to primality. Measure the window in odd cells, so that its length is $L = 2M+2$, and let $a_p$ be the first cell a line strikes. Then $M^2 + 2a_p \equiv 0 \pmod p$, so
$$a_p \equiv -\tfrac{1}{2}M^2 \pmod p ,$$
which is the ordinary start offset of a segmented sieve; nothing is claimed for it here. What the window adds is that two thresholds appear, and they are adjacent:
$$T_- = \frac{M^2}{2(M+1)}, \qquad T_+ = \frac{(M+2)^2}{2(M+1)}, \qquad T_+ - T_-  =  \frac{4M+4}{2M+2}  =  2 .$$
Below $T_-$ no two cofactor strips can meet at all; above $T_+$ adjacent odd lines are guaranteed to hand over without a gap. **Since the difference is exactly $2$, the transition holds at most one odd line** — zero failures over odd $M \lt 3000$. At $M = 499$ that line is $251$, with $T_- = 249.001$ and $T_+ = 251.001$.

**Above $T_+$ the handover carries one bit.** Writing $q_{\min}, q_{\max}$ for the first and last cofactor of a line, the difference $q_{\min}(p-2) - q_{\max}(p)$ takes **only the values $0$ and $2$** — zero exceptions over $89{,}698$ adjacent pairs. So the cofactor blocks of the top shell form a single strip on the odd axis with no gaps at all, and the only repetition permitted is one shared value. Below $T_+$ the differences grow without bound, which is what the threshold marks.

> **Proposition 1d.** For $T_+ \lt p \le M$ put $X = 2(s+1)^2$ with $s = (M-p)/2$, and let $\varepsilon_p = 1$ when the lines $p$ and $p-2$ share a cofactor and $0$ otherwise. Then
> $\displaystyle \varepsilon_p = 1 \quad\Longleftrightarrow\quad \left\lfloor \frac{X}{p-2} \right\rfloor + 1 = \left\lceil \frac{X}{p} \right\rceil .$

*Proof.* The last diagonal a line reaches is $\lceil X/p\rceil$, since $2s^2 + 2M + 2 = X + 2p$; the first diagonal of the next line is $\lfloor X/(p-2)\rfloor + 1$. The two coincide exactly when the blocks share a value. $\blacksquare$

*Verification.* Zero failures over $561{,}748$ adjacent pairs above $T_+$ for odd $M \lt 3000$. The share with $\varepsilon = 1$ settles: $0.807$, $0.771$, $0.777$, $0.776$, $0.773$ at $M = 499$, $999$, $4999$, $9999$, $49999$.

**So the bit is a comparison of a floor and a ceiling of the same number on two adjacent denominators — computable from $M$ and $p$ by two divisions, with no primality anywhere in it.** A prime gap of $2$ between two lines *permits* them to share a cofactor; $\varepsilon_p$ decides whether they do. The two levels are independent, and the geometric one exists before any question of primality is asked.

*What this is and is not.* It is a restriction on which lines can manufacture depth, and it is the reason the cut of [P9, §2.1] is placed where it is. It is not a constraint on the survivors, since it says nothing about the cells a line leaves open.

---

### 3.3 Four named cells inside the window

Paper 2, [P7, §2], indexes the window by its own cell numbers: it is the interval $c_0,\dots,c_0+N-1$ with $c_0 = 6a^2-2a+1$ and $N = 4a-1$, where $n = 6a$ and the window is $[(n-1)^2,(n+1)^2]$. This section uses that indexing to study the four cells nearest its two ends.


*A note on notation.* The four cells of this section are written $T_1,\dots,T_4$ and are **not** the exception types $A, C, D, E, F$ of [P6, §2.3] and [P6, §2.4]; the two families are unrelated, and the letters are kept apart on purpose.

#### 3.3.1 The four tracks, their character conditions and their densities

The window's template [P7, §2.2] singles out four cells near its two ends. Writing $q = 6a-1$ they are
$$T_1 = (q^2{+}4,\ q^2{+}6), \quad T_2 = (q^2{+}10,\ q^2{+}12), \quad T_3 = ((q{+}2)^2{-}14,\ (q{+}2)^2{-}12), \quad T_4 = ((q{+}2)^2{-}8,\ (q{+}2)^2{-}6),$$
and as $a$ runs they trace four **tracks**. Substituting $q = 6a-1$ makes every member a quadratic in $a$:

| cell | lower member | upper member |
|------|--------------|--------------|
| $T_1$ | $36a^2-12a+5$ | $36a^2-12a+7$ |
| $T_2$ | $36a^2-12a+11$ | $36a^2-12a+13$ |
| $T_3$ | $36a^2+12a-13$ | $36a^2+12a-11$ |
| $T_4$ | $36a^2+12a-7$ | $36a^2+12a-5$ |

*Verification.* Exact for $a = 1,\dots,399$.

> **Theorem 3 (which lines can ever own a track).** Let $r \gt  3$. Then $r$ divides $36a^2+Ba+C$ for some $a$ exactly when the discriminant $B^2-144C$ is a quadratic residue modulo $r$, the case of discriminant $\equiv 0$ counting as a residue and giving a double root. (For $r = 2, 3$ the leading coefficient vanishes modulo $r$ and the criterion does not apply; those two lines are handled by the grid itself.) For the eight members the discriminants are $144k$ with
> $\displaystyle k  =  -4,\ -6 \ (T_1); \qquad -10,\ -12 \ (T_2); \qquad 14,\ 12 \ (T_3); \qquad 8,\ 6 \ (T_4),$
> so the conditions read $r \equiv 1 \pmod 4$ and $(-6 | r) = 1$ for $T_1$; $(-10 | r)=1$ and $r \equiv 1 \pmod 3$ for $T_2$; $(14 | r)=1$ and $(3 | r)=1$ for $T_3$; $r \equiv \pm1 \pmod 8$ and $(6 | r)=1$ for $T_4$.

*Verification.* Every prime factor of every member for $a = 1,\dots,400$ — $4{,}209$ checks — satisfies its condition; no violation.

Each individual condition admits half the primes (measured over primes below $10^5$: $49.7\text{--}50.0$%), but a cell falls to a strike on **either** member, so the union admits three quarters: measured $75.0,\ 74.8,\ 75.0,\ 75.0$% for $T_1,T_2,T_3,T_4$. Requiring eligibility for all four at once cuts this to **exactly a quarter** — the eight discriminants reduce to the five independent characters $(-1),(2),(3),(5),(7)$, giving $32$ sign patterns of which $8$ pass; measured $24.84$% against the naive independent guess $(3/4)^4 = 31.6$%.

**The four tracks are not equivalent.** Each is a pair of quadratics, so its twin density is governed by a Bateman–Horn constant [1] $S = \prod_r (1-\nu_r/r)/(1-1/r)^2$, where $\nu_r$ counts the roots of the pair modulo $r$. The correct baseline is a generic cell $(6c-1,6c+1)$, whose constant is $12C_2 = 7.9219$ — **not** the twin constant $2C_2 = 1.320$, which is for pairs $(n,n+2)$ over all $n$ and counts the even $n$ a cell never has.

| track | $\nu_5$ | $\nu_7$ | $\nu_{11}$ | $S$ | $S/12C_2$ |
|-------|------|------|------|------|------|
| $T_1$ | **4** | 2 | 2 | $3.230$ | $0.408$ |
| $T_2$ | 1 | 4 | 2 | $5.797$ | $0.732$ |
| $T_3$ | 2 | 1 | 4 | $8.739$ | $1.103$ |
| $T_4$ | 2 | 2 | **0** | $11.324$ | $1.429$ |

*Verification.* Predicted density $S/\log^2(36a^2)$ against measured, for $a = 12{,}000,\dots,30{,}000$: $0.0059/0.0062$, $0.0105/0.0100$, $0.0158/0.0156$, $0.0205/0.0214$.

**So the Bateman–Horn model predicts track $T_4$ to be $3.5$ times richer in twins than track $T_1$, and the counts measured below are consistent with that prediction**, and the reason is visible in the table: $\nu_{11} = 0$ for $T_4$ — eleven never divides either of its members — while $\nu_5 = 4$ for $T_1$, the maximum, five dividing both members with two roots each. *(This is directly usable: a search for twin pairs near squares is three and a half times more productive on the $T_4$ track than on the $T_1$ track.)*

#### 3.3.2 Theorem 4: simultaneity, and why it is the sharp question

Eligibility asks which primes can own a track at **some** $a$. The sharper question is which can own two tracks at the **same** $a$, and the answer is finite.

> **Theorem 4.** A prime $r \gt  3$ can close two of $T_1,T_2,T_3,T_4$ in the same window only if it divides the resultant of the corresponding pair of quadratics. The complete list is
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

**The contrast is the point.** Eligibility for one cell admits three quarters of all primes; for all four at once, a quarter — both infinite. **Simultaneous double duty admits nine primes and no more.** The character condition loses the shared variable $a$; restoring it collapses an infinite set to a finite one, and this is the sharpest local statement in the paper after [P7, Cor 3].

**And, as with every local statement here, it does not bind.** Closing all four cells requires at least two lines — a special prime may serve $T_1$ & $T_3$ and another $T_2$ & $T_4$ — and at most four. Measured over $a = 3000,\dots,10000$: of $7{,}000$ windows, $6{,}512$ have all four closed, using two distinct lines in $973$ cases, three in $4{,}748$ and four in $791$, so one of the nine special primes does double duty in $5{,}721$ of them. Against this, the lines available number $\pi(q) = 428$, $2{,}062$ and $6{,}055$ at $a = 500$, $3000$, $10000$. **Four out of six thousand is free.**

---


#### 3.3.3 Proposition 2: and why Theorem 4 does not obstruct anything

Theorem 4 is sharp, and it is sharp for one line. The next statement shows that it dissolves the moment one is allowed four, and it dissolves by construction rather than by measurement.

> **Proposition 2.** Let $k$ tracks be given, each a pair of quadratics in $a$, and let $N$ be any bound. Then there is an arithmetic progression of $a$ — infinite, explicit, and computable — along which all $k$ tracks are closed simultaneously, every closing line exceeding $N$ and all $k$ of them distinct. Any finite number of further congruence conditions may be imposed at the same time.

*Proof.* For each track choose a prime $r_i \gt  N$, distinct from the others, whose discriminant condition (Theorem 3) is satisfied, and a root $a_i$ of one of its members modulo $r_i$. The $k$ conditions $a \equiv a_i \pmod{r_i}$ have pairwise coprime moduli, so the Chinese remainder theorem combines them into a single class modulo $\prod r_i$. Further conditions on coprime moduli are appended the same way. $\blacksquare$

**The contrast with Theorem 4 is the whole point.** There the same line had to satisfy two conditions *at the same $a$*, which is a genuine constraint and collapsed an infinite set to nine primes. Here the conditions sit on different moduli, and the shared variable costs nothing.

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

---

*The computations and much of the prose in this paper were prepared with AI assistance (ChatGPT, OpenAI; Claude, Anthropic), used for algebraic derivation, for drafting and rewriting code and text, for running the computations, and for auditing the papers against their own scripts. All statements were checked by the author, who is responsible for them; the repository README sets out the division of labour in full.*
---

## References

The eleven papers of this set are cited as [P1] to [P11], and the numbered entries below are the external works. The two kinds never share a number: a bracket with a P is a companion paper, a bare number is a reference in the list below. This paper imports only the definitions and statements of the companion papers, never their proofs.

1. P. T. Bateman and R. A. Horn, *A heuristic asymptotic formula concerning the distribution of prime numbers*, Math. Comp. **16** (1962), 363–367.
