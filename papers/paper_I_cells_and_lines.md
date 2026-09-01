# Cells and Lines

## I. A coordinate system for the odd sieve

---

### Abstract

We give a coordinate system for the odd integers in which several statements usually carried as estimates become identities.

The primitive object is not the prime but the **line** $L_m(k) = m(m+2k)$, the odd multiples of $m$ from $m^2$ onward; only prime $m$ contribute anything, in both directions (Theorem 1). The line $L_3$ has step $6$ and so leaves exactly two odd numbers between consecutive strikes, which makes it not the first sieving line but the **coordinate grid**: the odd integers compress into cells $C_b = (6b-1,6b+1)$. Every line then acts on the cells by a single map (Theorem 2), from which a line's mirror symmetry is seen to be *inherited from the cell* rather than intrinsic to the line. The two cell positions a line closes are $\pm 6^{-1}$ modulo that line and are always distinct, so exactly two of every $p$ cells lose a member (Theorem 3) — the factor $(p-2)$ of the sieve product, read as geometry rather than as a density. Two further readings of the same picture are recorded: the diamond coordinates, in which the fingerprint law is the projection of a single straight line (Corollary 4), and the change at a square front from a difference of the two factors' distances to a sum of them (§3.7).

The same coordinates are then applied to the window $[(6a-1)^2,(6a+1)^2]$ (§4). It is exactly an interval of consecutive **cell indices**, starting at $6a^2-2a+1$ and of length $4a-1$, on which every line is two arithmetic progressions (Theorem 4); its midpoint cell is $(n^2-1,n^2+1)$ and so is never a twin (Theorem 5); and indexing by each line's strike number makes $t = k-6j$ invariant under the passage to the next window, in which coordinate two further laws are exact (Theorems 6, 7).

Section 4.5 then reads the same coordinates across sectors rather than inside one: the sectors anchored at $M = 6r+3$ have start $a_r = 6r(r+1)+2$ and length $12(r+1)$, and the two are linked by $a_{r+1}-a_r = L_r$ exactly, so the sectors **tile** the cell strip. Since the cell and the two closed classes $n \equiv \pm 6^{-1} \pmod p$ are fixed once and for all, no sector carries a phase of its own — what looks like one is the position of the moving quadratic start inside a strip that never moves.

Section 5 settles a second, independent ownership question about the same object: a line holds the *centre* of its strikes — it remains the largest divisor below the square root — for exactly $a+b+2$ steps, where $ab = m$ is the central pair of $m$ (Theorem 8). The loss is a handover with its index named, and the two steps of $2$ in the bound are exactly where the odd lattice enters.

This paper uses no analytic sieve estimates: no Mertens constant, no prime-distribution input, no error terms. The exact histogram carried by the square window was separated out as Paper 0, since it concerns no primes at all; it is quoted here where needed and proved there.


**Keywords:** sieve of Eratosthenes, cell coordinates, difference of squares, integer lattices.

**MSC 2020:** 11N35, 11A41, 11B83.

**How to read the claims in this paper.** Statements set as Theorems, Propositions and Corollaries are proved, and the proofs are given. Everything else falls into two kinds, and we try to keep them apart. A *measurement* is a computation over a stated finite range; it is labelled with that range, and it supports a claim about that range only. A *reading* is our own judgement about what a measurement or a proof appears to mean, and we mark it as ours rather than stating it as established.

---

### Summary of the main results

| | statement | where |
|-------------|------------------------------------------------------|-------|
| **Theorem 1** | A line $L_m$ contributes a position no smaller line already covers **if and only if** $m$ is prime. | §2.4 |
| **Theorem 2** | The cell map $p(6b+\varepsilon) = 6(pb+a\varepsilon)+\sigma\varepsilon$: a line sends the two members of $C_b$ to the cells $pb-a$ and $pb+a$. **A line's fingerprint symmetry is inherited from the cell, not created by the line.** | §3.2 |
| **Theorem 3** | A line closes exactly the two cell positions $j \equiv \pm 6^{-1}$, always distinct; hence exactly two of every $p$ cells lose a member, one per rail. | §3.5 |
| **Corollary 1** | Among twin pairs the forbidden position $u=-1$ is never occupied, and $u=+1$ only at the line's own birth index — so $+1$ is birth first and closure thereafter, $-1$ closure always. | §3.5 |
| **Corollary 2** | For distinct twin pairs $C_a, C_b$, none of the four primes $6a\pm1, 6b\pm1$ reaches the centre $C_{6ab}$ of their diamond: a killer must come from a third row. | §3.6 |
| **Corollary 3** | Around a $k$-line coincidence on $L_3$ at $3P$, every image cell lies at distance $\ge \sqrt{P+1}$: the fan-out grows in number and is pushed away at the same time. | §3.6 |
| **Corollary 4** | The strikes of $L_p$ on the cell axis are two interleaved progressions of step $p$ with alternating gaps $2a,\ p-2a$ — the projection of the single straight line $S-D = 2a$ in the diamond coordinates. | §3.6 |

| | statement | where |
|---------------|----------------------------------------------------|-------|
| **Theorem 4** | The window $[(6a-1)^2,(6a+1)^2]$ is exactly the interval of cell indices $c_0,\dots,c_0+N-1$ with $c_0 = 6a^2-2a+1$ and $N = 4a-1$; on it every line is two arithmetic progressions. | §4.1 |
| **Theorem 5** | Its midpoint cell is $(n^2-1, n^2+1)$ with $n^2-1 = (n-1)(n+1)$, so **the midpoint is never a twin pair.** | §4.2 |
| **Theorem 6** | In the shared index $k = 6j+t$ the two members of a layer are $4n+4t$ apart against a window of width $4n$, so only the newly born pair has both members inside; every older pair crosses in two disjoint passes. | §4.4 |
| **Theorem 7** | The role of a strike — upper rail, lower rail, or wasted on $L_3$ — is decided by $t \bmod 3$ alone. | §4.4 |
| **Proposition 2** | The sectors anchored at $M = 6r+3$ **tile** the cell strip: start $a_r = 6r(r+1)+2$, length $12(r+1)$, and $a_{r+1}-a_r$ is exactly the length. So no sector carries a phase of its own. | §4.5 |

| | statement | where |
|-------------|------------------------------------------------------|-------|
| **Theorem 8** | $L_m$ holds the centre of its strikes — it stays the largest divisor below the square root — for exactly $a+b+2$ steps, where $(a,b)$ is the central pair of $m$; the displacing divisor is $m+2a$. | §5.3 |
| **Corollary 5** | The first loss is a handover with its index named: $L_m(a+b+2) = L_{m+2a}(b-a)$. At a square it lands on the new line's birth; at a prime it reads $L_p(p+3) = L_{p+2}(p-1)$. | §5.4 |
| **Corollary 6** | $T(m) = m+2a = a(b+2)$, so a composite hands over to a composite: under iteration of $T$ the primes are a transient set. | §5.5 |

Everything in this paper is proved. The histogram results — Theorems 4, 5, 6, 7 and 8 of the earliest version — are now Paper 0, where they are stated for all odd $n$ and without reference to primes; Theorem 8 above is a new statement and unrelated to them.

### 0. What this paper is, and what it is not

This is one of six papers built on one coordinate system. The division is by mathematical dependence, not by topic:

| | | depends on |
|-----|-------------------------------------------|--------------------------|
| **0** | *An exact histogram for a quadratic staircase* | — (no primes occur in it) |
| **I** | *Cells and lines* (this paper) | — |
| **II** | *The inheritance law on the cycle* | the cell coordinates of §3 |
| **III** | *From cycle to window* | 0, I and II |
| **IV** | *The twin criterion in cell coordinates* | 0, I, II, III |
| **V** | *Where the framework stops* | 0, I, II, III, IV |

Papers 0, I and II are independent of one another. Paper 0 is pure arithmetic: it concerns the increments of $\lfloor 2j^2/n\rfloor$ for odd $n$ and mentions no primes at all. Paper I fixes the coordinates; Paper II runs the fixed periodic structure. Paper III is the first that needs several of them at once, because it evaluates II's cycle laws on the window whose combinatorics Paper 0 supplies.

**This paper uses no analytic sieve estimates.** No density asymptotic, no Mertens constant and no prime-distribution theorem is used below. Everything here is an exact statement about a periodic pattern, and a reader with no interest in primes may read it as such. Priority is not claimed for any result; the searches we ran found no exact match, but the absence of a match found by search is not evidence of novelty.

### 0.1 The three objects, in one picture

Everything below is built from three things. They are elementary, and it is worth seeing them once before any formula.

**(i) The line.** $L_p$ is the odd multiples of $p$, starting at $p^2$:

```
 L_3 :   9   15   21   27   33   39   45   51  ...      step  6
 L_5 :  25   35   45   55   65   75   85   95  ...      step 10
 L_7 :  49   63   77   91  105  119  133  147  ...      step 14
```

Each begins at its own square, so a line is responsible exactly for what no smaller line already covers (Theorem 1).

**(ii) The cell.** $L_3$ has step $6$, so between two of its strikes lie exactly **two** odd numbers. It is therefore not the first sieving line but the **coordinate grid**, and the odd numbers compress to cells $C_b = (6b-1,\ 6b+1)$. Marking the strikes of $L_3$ with $\times$ and the two cell members between them with $\bullet$:

```
 odd n :   3    5    7    9   11   13   15   17   19   21   23   25   27   29   31   33
 L_3   :   .    .    .    x    .    .    x    .    .    x    .    .    x    .    .    x
 cell  :        *----*         *----*         *----*         *----*         *----*
                 C_1            C_2            C_3            C_4            C_5
```

($3$ itself is the root of the line, not one of its strikes: $L_3$ begins at $3^2 = 9$.) Every cell is symmetric about its centre $6b$, and that single symmetry is the source of the mirror symmetry later seen in every line's fingerprint (Theorem 2): a line does not create it, it transports it.

**(iii) The moving window.** The odd squares slide across this fixed grid, and the gap between consecutive squares is $4p+8j+4$ — two full line-steps plus a residue that grows by $8$ each time. For $p = 5$ the five sectors of the first cycle are

| sector | $(25,49]$ | $(49,81]$ | $(81,121]$ | $(121,169]$ | $(169,225]$ |
|-----------------|--------|------------|------------------|-------------|-------------|
| width | 24 | 32 | 40 | 48 | 56 |
| strikes of $L_5$ | 35, 45 | 55, 65, 75 | 85, 95, 105, 115 | 125, …, 165 | 175, …, 225 |
| $H_j$ | **2** | **3** | **4** | **5** | **6** |

The widths climb by exactly $8$; the strike count climbs $2,3,4,5,6$ **and stops there**. Writing $H_j = 2 + W_j$ with $W_j = \lfloor 2(j+1)^2/p\rfloor - \lfloor 2j^2/p\rfloor$, both the fact that it stops and the exact multiplicities of the five values are **[0, Theorems 1 and 2]** — statements about odd $n$ in general, with no reference to primes, which is why they were separated into Paper 0.


---

## 1. The two objects

**The line.** For odd $p$, $L_p(k) = p^2 + 2pk = p(p+2k)$ — the odd multiples of $p$ from $p^2$ onward. Starting at $p^2$ makes each line responsible exactly for what it alone contributes (§2.2), and only prime $p$ contribute anything (Theorem 1).

**The window.** The odd squares $S_j = (p+2j)^2$. The gap between consecutive squares is $4p + 8j + 4$: two full line steps, plus a residue of $8j+4$ that grows by $8$ each time. **That $+8$ is the clock behind every window statement**; its consequences — the uniform bound on the strike count, its exact histogram, and the identity tying the count to the fingerprint $D_j \equiv 4j^2 \pmod{2p}$ — are Paper 0.

---


## 2. Lines

### 2.1 Definition

For odd $p$,
$$L_p(k)  =  p^2 + 2pk  =  p (p+2k), \qquad k = 0,1,2,\dots \qquad\text{(2.1)}$$

The line begins at $p^2$ and has step $2p$.

| line | strikes |
|------|------------------------|
| $L_3$ | 9, 15, 21, 27, 33, … |
| $L_5$ | 25, 35, 45, 55, 65, … |
| $L_7$ | 49, 63, 77, 91, 105, … |

### 2.2 Why the line begins at $p^2$

Any odd multiple of $p$ below $p^2$ has the form $p\cdot s$ with $s\lt p$, hence lies on a smaller line. Starting at $p^2$ makes each line responsible exactly for what it alone contributes.

### 2.3 A difference-of-squares identity

$$L_m(k)  =  (m+k)^2 - k^2 \qquad\text{(2.2)}$$

Every strike is a difference of two squares whose roots differ by the fixed amount $m$. This is the first link between lines and squares; it returns in §3.6 and §3.7, and again in Paper 0.

### 2.4 Theorem 1 (only primes contribute)

> **Theorem 1.** For every odd $m\ge3$, $L_m$ contributes at least one position unreached by any smaller line if and only if $m$ is prime.

*Proof.* Suppose first that $m$ is composite and let $q$ be its least prime factor, so $q\lt m$. Every strike $n = m(m+2k)$ is divisible by $q$. Since $n \ge m^2 \gt  q^2$ we have $q \le \sqrt n$, so the line $L_q$ has already been born at this position and has struck it. Hence $L_m$ contributes nothing new.

Conversely, let $m=p$ be prime. Its first strike is $p^2$. If a smaller line $L_q$ with $3\le q\lt p$ had already struck $p^2$, then $q\mid p^2$, hence $q=p$, impossible. Thus $p^2$ is new when $L_p$ is born, so $L_p$ contributes at least one previously unreached position. $\blacksquare$

*Remark.* The hypothesis $q \le \sqrt n$ is essential and is often left implicit: a line $L_q$ does not reach any position before $q^2$. Here it holds automatically because $n \ge m^2 \gt  q^2$.

*Verification.* Over every composite odd $m \lt  200$ and every strike $m(m+2k) \le 10^5$ — $38{,}904$ strikes in all — the number carrying no smaller line is **zero**.

Consequently the underlying network consists of the odd prime lines alone.

### 2.5 Why the prime $2$ is excluded

With $L_2$ admitted, gaps between consecutive struck numbers lie in $\lbrace 1,2\rbrace$ with maximum $2$, and a twin pair becomes the *word* $(2,2)$ — not an extremal object. Restricted to odd integers, the gaps lie in $\lbrace 2,4,6\rbrace$ and a twin pair is the *maximal letter* $6$. Measured over $10^6$ integers. Excluding $2$ therefore sharpens the description rather than weakening it.

---


## 3. Cells

### 3.1 Definition

$$\underbrace{6b-3}_{\text{on } L_3}  \Big|  \underbrace{6b-1,   6b+1}_{\textbf{cell } C_b}  \Big|  \underbrace{6b+3}_{\text{on } L_3} \qquad\text{(3.1)}$$

The cell is symmetric about its centre $6b$; this symmetry is inherited by everything that follows.

### 3.2 Theorem 2 (the cell map)

Write $p = 6a+\sigma$ with $\sigma = \pm 1$.

> **Theorem 2.** For all $b$ and $\varepsilon = \pm 1$,
> $$p (6b+\varepsilon)  =  6 (pb + a\varepsilon)  +  \sigma\varepsilon. \qquad\text{(3.2)}$$

*Proof.* Direct expansion: $p(6b+\varepsilon) = (6a+\sigma)(6b+\varepsilon) = 36ab + 6a\varepsilon + 6b\sigma + \sigma\varepsilon = 6(pb + a\varepsilon) + \sigma\varepsilon$, using $6ab + b\sigma = b(6a+\sigma) = pb$. $\blacksquare$

*Verification.* Zero failures over every prime $p \lt  200$, every $b$ with $0 \le b \lt  50$ and both signs $\varepsilon = \pm1$: $4{,}400$ instances.

**Interpretation.** The line $p$ sends the two members of the factor-cell $C_b$ into the cells centred at $pb-a$ and $pb+a$ — two positions symmetric about $pb$, at distance $2a$.

| $p$ | $\sigma$ | $a$ | image of $C_2 = (11,13)$ |
|------|------|------|---------------|
| 5 | $-1$ | 1 | $C_9,  C_{11}$ |
| 7 | $+1$ | 1 | $C_{13},  C_{15}$ |
| 11 | $-1$ | 2 | $C_{20},  C_{24}$ |
| 13 | $+1$ | 2 | $C_{24},  C_{28}$ |

Two consequences are immediate. First, **the symmetry of a line's fingerprint is not a property of the line**: it is inherited from the symmetry of the cell about $6b$, and multiplication by $p$ transports it. Second, the step contracts: on the integers each branch steps by $6p$; in cell coordinates it steps by $p$.

### 3.3 The repeating unit

Among $p,  p+2,  p+4$ exactly one is divisible by $3$, so every line $p\gt 3$ has the fixed repeating unit
$$L_3 \to \text{strike} \to \text{strike} \to L_3 \to \cdots$$

> **Proposition 1.** If $p \equiv +1 \pmod 6$ the $L_3$-meeting is the *first* strike $p(p+2)$; if $p \equiv -1 \pmod 6$ it is the *second*, $p(p+4)$.

*Proof.* If $p = 6a+1$ then $p+2 = 6a+3$ is divisible by $3$; if $p = 6a-1$ then $p+4 = 6a+3$ is. $\blacksquare$

*Verification.* Zero failures over all $428$ primes below $3000$.

Hence the "two strikes in a newborn line's first sector" is not an independent observation: they are the two cell slots between consecutive $L_3$-meetings.

### 3.4 Cell states, and where they lead

Assign to each factor-cell the state of its two members ($N$ = alive, $O$ = already struck), giving $NN$, $NO$, $ON$, $OO$. When line $p$ enters, its genuinely new strikes are exactly the surviving members:

| state | $NN$ | $NO$ | $ON$ | $OO$ |
|-------------|------|------|------|------|
| new strikes | 2 | 1 | 1 | 0 |

*Reason.* If $6b+1$ is divisible by some $r\lt p$, then so is $p(6b+1)$. **The state of the factor-cell is transported by multiplication.** Hence
$$\text{effect of } L_p  =  (\text{its geometric track})  \cap  (\text{previous survivors}). \qquad\text{(3.3)}$$

The counting form of this law, its closed solution and its refinement by inheritance depth are the subject of Paper II; nothing below depends on them.

*Verification.* Mean new strikes per state $= 2.00 / 1.00 / 1.00 / 0.00$ at $p = 11, 13, 17$, with no deviation.

### 3.5 The survivor law as a geometric statement

A line's cycle in cell coordinates has length $p$ cells, and the line has two branches; it therefore closes two cells out of every $p$:
$$|R_{Mp}| = (p-2) |R_M| \qquad\Longrightarrow\qquad |R_M| = \prod_{3\lt p\le z}(p-2). \qquad\text{(3.4)}$$

| lines | 5 | 7 | 11 | 13 | 17 |
|-------|---|----|-----|-------|--------|
| $\lvert R_M\rvert$ | 3 | 15 | 135 | 1,485 | 22,275 |

Thus $(p-2)$ — the factor of the classical sieve product [1] — is here not a coefficient but the geometric statement
$$(p-2) = (p \text{ cells per cycle}) - (2 \text{ branches}).$$

> **Theorem 3.** The two closed positions are $j \equiv \pm 6^{-1} \pmod p$, and they are always distinct.

*Proof.* $6j \equiv \pm 1$ gives $j \equiv \pm 6^{-1}$. If the two coincided then $2\cdot 6^{-1} \equiv 0$, i.e. $p \mid 2$, impossible for odd $p$. $\blacksquare$

*Closed form.* $6^{-1} = (p+1)/6$ if $p \equiv 5 \pmod 6$, and $(5p+1)/6$ if $p \equiv 1$. Zero failures to $p = 20{,}000$. In particular the two forbidden positions always sit at one sixth and five sixths of the modulus: for $p \sim 10^3$ the smaller lies in $[0.16650, 0.16683]$ against $1/6 = 0.16667$.

**Which of the two positions a twin row can occupy.** Theorem 3 forbids both positions to a surviving cell, but the two are not alike once one asks which cells are twin pairs. Write $c = 6^{-1} \bmod p$, so the forbidden positions are $j \equiv \pm c$, and put $u_p(j) = jc^{-1} \bmod p$, so that they become $u = \pm 1$. If $u_p(j) = +1$ then $j = c + mp$ and the member of $C_j$ that $L_p$ reaches is $p(6m+1)$; at $m = 0$ that member is $p$ itself, which is prime, and for $m \ge 1$ it is composite. If $u_p(j) = -1$ then $j = mp - c$ and the member reached is $p(6m-1)$, composite for every $m \ge 1$ and with no $m = 0$ case, since $j$ would be negative.

> **Corollary 1.** Among cells that are twin pairs, the position $u = -1$ is never occupied, and the position $u = +1$ is occupied at the single index $j = c$ and nowhere else — and there only when $C_c$ is itself a twin pair. In short: $+1$ is birth first and closure thereafter, $-1$ is closure always.

*Verification.* Over the $428$ primes $5 \le p \lt  3000$, against every twin pair with index below $20{,}000$: the set of twin indices at $u = +1$ is exactly $\lbrace c\rbrace$ when $C_c$ is a twin pair and empty otherwise, and no twin index ever sits at $u = -1$. Zero exceptions either way.

*Why it is worth stating.* The birth index is a permanent exception to any law phrased over residue classes, because at $j = c$ the line meets itself rather than a multiple of itself. Written as $S_p = \mathbb{F}_p \setminus \lbrace \pm 1\rbrace$ the set is wrong by one point, and that point is where several natural-looking laws about rows break — and, being the smallest index, also where their most convincing examples come from.

---


### 3.6 The diamond coordinates, and the fingerprint as a projection

Theorem 2 has a consequence that is worth isolating, because it turns a law that looks separate into the shadow of a straight line.

**The coordinates.** Take two cells $C_a$ and $C_b$ with $a \ge b$ and multiply their members. Writing $X_{a,\varepsilon} = 6a+\varepsilon$ with $\varepsilon = \pm1$, the identity behind Theorem 2 reads
$$X_{a,\varepsilon} X_{b,\delta}  =  6\big(6ab + a\delta + b\varepsilon\big) + \varepsilon\delta. \qquad\text{(3.5)}$$
Verified with zero errors over $1 \le a,b \lt  100$ and all four sign pairs. Now set
$$S = a+b, \qquad D = a-b, \qquad M = 6ab = \tfrac{3}{2}\big(S^2-D^2\big),$$
so the four products land at cell indices $M-S,\ M-D,\ M+D,\ M+S$, on the rails $+,-,-,+$ respectively — an exact symmetry about $M$, not an approximate one.

**What the coordinates make visible.** Three of the objects of this paper become coordinate statements:

| | in $(S,D)$ |
|---------------------------------|-----------------------------------------|
| the line of the smaller factor | $S-D = 2b$, a family of **parallel** lines |
| the squares | $D = 0$ |
| the birth of a line at its square | the point where $S-D = 2b$ meets $D=0$, i.e. $(S,D) = (2b, 0)$ |

Writing $u = S-D = 2b$ and $v = S+D = 2a$ gives $M = \tfrac{3}{2}uv$: a fixed line is $u$ constant, motion along it is motion in $v$, and the squares are $u = v$.

**The centre is not a vertex, and its own generators cannot reach it.** The four products sit at $M \pm S$ and $M \pm D$; the centre $M = 6ab$ itself is not among them, and it is the index of an ordinary cell, with members $36ab \mp 1$.

> **Corollary 2.** Let $C_a$ and $C_b$ be distinct twin pairs. Then none of the four primes $6a\pm1$, $6b\pm1$ divides either member of $C_M$ with $M = 6ab$.

*Proof.* Write $p = 6a-1$ and $c = a$, so $u_p(a) = 1$ in the notation of Corollary 1. Since $36 \equiv c^{-2} \pmod p$, one has $36ab \equiv u_p(a)u_p(b) = u_p(b)$, and $u_p(b) = \pm 1$ would put the index $b$ at a forbidden position of $L_p$, contradicting that $C_b$ is a twin pair. The same argument with $p = 6a+1$, and with $a$ and $b$ exchanged, gives the other three. $\blacksquare$

*Verification.* Zero strikes over all $6{,}320$ ordered pairs of distinct twin indices below $500$. The self-diamond is the opposite case: at $a = b$ the identity $36a^2-1 = (6a-1)(6a+1)$ closes the centre with the generators themselves.

**A gap around a common strike.** The same coordinates give a lower bound on how far the images of a multi-line coincidence must sit from it. Let $S$ be a set of $k$ primes above $3$ and $P = \prod_{r\in S} r$. A cell whose two members are struck by the lines of $S$, split in any way between the rails, has centre $x = 6j$ with $x \equiv \pm1 \pmod r$ for every $r \in S$, hence $x^2 \equiv 1 \pmod P$: the $2^k$ ways of splitting are exactly the square roots of $1$ modulo $P$.

> **Corollary 3.** Let $x = 3P + d$ be the centre of such a cell. Then $|d| \ge \sqrt{P+1}$.

*Proof.* From $x^2 \equiv 1 \pmod P$ and $x \equiv d \pmod P$ one gets $P \mid d^2-1$. The centre of a cell is divisible by $6$ while $3P \equiv 3 \pmod 6$, so $d \equiv 3 \pmod 6$ and in particular $d \ne \pm1$; hence $d^2-1 \ne 0$ and $|d^2-1| \ge P$. $\blacksquare$

So the more lines meet at a point of $L_3$, the larger the fan-out is in number and the further its images are pushed from the meeting point — the two effects work against each other, which is worth knowing before treating a high coincidence as a local source of open cells.

*What it is and is not.* Read arithmetically the statement is small — $6a-1$ divides $36ab-1 = 6b(6a-1) + (6b-1)$ only if it divides $6b-1$, impossible for distinct primes. What the coordinates add is the reason it is not a coincidence: the phase of a row at its own line is $+1$, and multiplying by $+1$ cannot move an admissible phase onto a forbidden one. A killer of the centre, if there is one, must therefore come from a third row.


Pictorially the whole multiplication of cells lives in a triangular lattice, in which the lines form one family of parallels and the squares are the single axis they all cross:

```
   D
   ^
   |                                              upper edge  D = S - 2
   |                                         . '     (smallest factor-cell b = 1)
   |                                    . '
   |                               . '      /       /       /
   |                          . '          /       /       /
   |                     . '              /       /       /      each diagonal
   |                . '                  /       /       /       S - D = 2b
   |           . '                      /       /       /        is ONE line
   |      . '                          /       /       /         (fixed smaller cell b)
   |  . '                             /       /       /
   +----o-------o-------o-------o----o-------o-------o------------------>  S
        2       4       6       8    10      12      14
      b=1     b=2     b=3     b=4                    D = 0 : the squares (a = b)
```

Three readings of the same picture, and they are the three facts above:

- moving **along** a diagonal is the line $b$ advancing through its cofactors;
- the point where a diagonal meets the axis $D = 0$ is that line's **birth at its own square**;
- moving **towards** the upper edge $D = S-2$ makes the smaller factor smaller, so ownership — "the smallest line owns the strike" — is the most unbalanced representation available, the one nearest that edge.


**The corollary.** Fix the line $p = 6a+\sigma$ and let it act on the cell axis. By Theorem 2 its strikes sit at $c = pb - a$ and $c = pb + a$ for $b = a, a+1, \dots$, so:

> **Corollary 4.** The strikes of $L_p$ on the cell axis form two interleaved arithmetic progressions of common difference $p$, and the gaps between consecutive strikes alternate
> $$2a, \quad p-2a.$$
> Explicitly, $p = 6a-1$ gives $(2a,\ 4a-1)$ and $p = 6a+1$ gives $(4a+1,\ 2a)$.

Verified with zero errors for every prime $5 \le p \lt  200$. Examples: $p=5$ gives $(2,3)$; $p=7$ gives $(5,2)$; $p=11$ gives $(4,7)$; $p=13$ gives $(9,4)$.

**So the fingerprint of a line is not an independent law.** It is the projection onto the cell axis of the single straight line $S-D = 2a$, and the two numbers in it are the distance across the pair of strikes and the distance to the next pair. The asymmetry between $p \equiv 1$ and $p \equiv -1 \pmod 6$ — which in a direct computation looks like a case distinction — is only the order in which the two gaps appear.

**Two honest remarks.** First, the map $(a,b) \leftrightarrow (S,D)$ is a bijection, so nothing is compressed by it: it is the multiplication table rotated through $45^\circ$, and visiting every point of one is visiting every point of the other. Second, $M = \tfrac{3}{2}(S^2-D^2)$ is Fermat's difference of squares in cell coordinates, and the associated counting function — representations as a difference of two squares — has its own literature; we claim nothing new for the coordinates themselves, only for the reading of the fingerprint above.

**One exact statement the coordinates do give, for completeness.** A number in the strip $6c\pm1$ is composite if and only if it is the image of some pair of cells under (3.5). Checked to $N = 200{,}000$: of $66{,}666$ strip members, $48{,}684$ are composite and $48{,}684$ are covered, with **zero** composites missed and **zero** primes covered. The proof is immediate — a composite coprime to $6$ has all its factors in the strip — and the value of the check is that it fixes the boundary conventions, not that the statement is in doubt.

### 3.7 The square front: difference below, sum above

The diamond coordinates give one further statement, and it is the sharpest form of "a square is where subtraction turns into addition".

Fix an odd $m$ coprime to $6$. Then $m^2 \equiv 1 \pmod{24}$, so $m^2$ is the upper member of some cell; index the cells above it by $t$, their members being $m^2+6t-2$ and $m^2+6t$. Now ask which cell a product of two odd numbers **near $m$** falls into. There are exactly two regimes, according to whether the two factors straddle $m$ or both exceed it.

**Straddling — a difference.** With $q = m-d$ and $r = m+e$, $d, e$ even and positive, one has $qr = m^2 + m(e-d) - de$, so the product lands at

$$6t  =  m(e-d) - de  +  \lbrace 0, 2\rbrace . \qquad\text{(3.6)}$$

**Both above — a sum.** With $q = m+u$ and $r = m+v$, $u, v$ even and positive, one has $qr = m^2 + m(u+v) + uv$, so

$$6t  =  m(u+v) + uv  +  \lbrace 0, 2\rbrace . \qquad\text{(3.7)}$$

In each case the ambiguity $\lbrace 0,2\rbrace$ is only which member of the cell is hit.

*Verification.* Zero failures over $10{,}760$ products at $m = 1001,\ 4999,\ 10007,\ 100003,\ 1000003$.

The two formulas are the same expression with one sign changed, and §3.6 shows why: $e-d$ and $u+v$ are the two ways of reaching a lattice point from the diagonal $D = 0$ — one crossing it, one staying on a single side of it. **The square is exactly the place where the additive coordinate of a product turns from a difference of the two factors' distances into a sum of them.**

Two consequences are immediate, and they are why the pair of formulas is worth stating rather than decorative.

- **(3.7) confines the second regime to a triangle.** If the product is to lie below $(m+h)^2$ then $m(u+v)+uv \lt  2mh+h^2$, and when $h^2 \lt  2m$ this forces $u+v \le h$. The pairs $(u,v)$ with $1 \le u \le v$ available at all therefore number
$$\sum_{s=2}^{h} \Big\lfloor \tfrac s2 \Big\rfloor  =  \Big\lfloor \tfrac{h^2}{4}\Big\rfloor .$$
- **(3.6) admits no such confinement**, since $e-d$ may be small while $d$ and $e$ are both large.

That asymmetry — a bounded triangle above the square, against an unbounded strip across it — is the difference between the two regimes stated quantitatively.

*(These are recorded as facts about the coordinates. Nothing later in this paper uses them.)*


## 4. The window in its own coordinates

The coordinates of §3 are fixed; this section applies them to the natural window and finds that everything about it reduces to two integers, a permanent exclusion, and two laws in a shared index.

Write $n = 6a$, so the two integers adjacent to the multiple of six are $q = n-1$ and $r = n+1$, and take
$$W_a  =  [ q^2,\ r^2 ],$$
the sector between consecutive odd squares, anchored so that its root is the lower member of a cell.

### 4.1 Theorem 4: start and length

> **Theorem 4.** The cells $C_c = (6c-1, 6c+1)$ lying strictly inside $W_a$ are exactly those with
> $$c  =  c_0,\ c_0+1,\ \dots,\ c_0+N-1, \qquad c_0 = 6a^2-2a+1, \qquad N = 4a-1 .$$
> Moreover a line $\ell$ closes the cell $c_0+j$ exactly when $j \equiv \pm 6^{-1} - c_0 \pmod \ell$ — **two residue classes, always.**

*Proof.* $q^2 = 36a^2-12a+1$, so the smallest $c$ with $6c-1 \gt  q^2$ is $(q^2+5)/6 = 6a^2-2a+1$; the largest with $6c+1 \lt  r^2 = 36a^2+12a+1$ is $c_0+4a-2$. The second statement is Theorem 3 translated by $c_0$. $\blacksquare$

*Verification.* Exact for every $a = 1,\dots,299$.

**So the whole sector is a segment of the integers of length $4a-1$, and every line is two arithmetic progressions on it.** Nothing about squares survives except the two numbers $c_0$ and $N$.

### 4.2 Theorem 5: the midpoint is never a twin

> **Theorem 5.** The cell at the exact midpoint of $W_a$ is $(n^2-1,\ n^2+1)$, and its lower member factors as
> $$n^2-1 = (n-1)(n+1) = q r .$$
> **It is therefore composite for every $a$, so the midpoint cell is never a twin pair.**

*Proof.* The midpoint of $[q^2,r^2]$ is $(q^2+r^2)/2 = n^2+1$, and $n^2-1 = (n-1)(n+1)$. $\blacksquare$

Examples: $(35,37)$, $(143,145)$, $(323,325)$, $(575,577)$, $(899,901)$, and $(359999,360001) = (599\cdot601,\ \cdot)$.

**This complements [IV, Thm 4] from the other side.** That theorem lists the at most six positions that can be *open without being twins*; Theorem 5 names one position that can *never be a twin at all*. Both are consequences of the anchoring, not of any counting.

*(The same anchoring gives a template of six landmarks at distances $u = 0, 2, 2n-2, 2n, 4n-4, 4n$ from the left endpoint — the left square, the first strike of $L_3$, the midpoint cell's lower member $qr$, the midpoint $n^2+1$, the last strike of $L_3$ which coincides with $q(q+4)$, and the right square. Verified for every $n = 6,12,\dots,894$. We record it as a frame rather than a result: everything inside it moves quadratically, since a line's first position in $u$ is $-q^2 \bmod \ell$.)*

### 4.3 The split at $\ell = N$, and who closes the window

Theorem 4 makes one thing immediate that the outside indexing hides. **A line's two classes each occur at most once in an interval of $N$ indices as soon as $\ell \ge N$.** So the lines divide at the window's own length:

- $\ell \lt  N = 4a-1$: the line **wraps**, and takes about $2N/\ell$ cells;
- $\ell \ge N$: the line **does not wrap**, and its entire budget is $2$ — usually already spent by the small lines.

| $a$ | $N$ | lines $\ell\lt N$ | cells they close | lines $\ell \ge N$ | cells they close | twins |
|------|-------|------------|------------------|------------|------------------|-------|
| 3 | 11 | 2 | 8 | 4 | 1 | 2 |
| 17 | 67 | 16 | 60 | 9 | **0** | 7 |
| 167 | 667 | 119 | 629 | 47 | 7 | 31 |
| 1667 | 6,667 | 857 | **6,500** | 370 | **20** | 147 |

**Eight hundred and fifty-seven small lines close six and a half thousand cells; three hundred and seventy large ones close twenty between them.** And the concentration inside the small group is just as sharp: in the window $a = 17$ the closures by line are $5:27$, $7:11$, $11:6$, $13:4$, $17:2$, $19:3$, $23:2$, $31:1$, $37:2$, $41:1$, $59:1$ — **the four smallest lines do $80$% of the work, and every line above $n/2$ together closes one cell.**

> **This is the cleanest statement of a fact that appears throughout this paper: the large lines are not weak because they are large, but because the window is shorter than their period.** The threshold is neither $\sqrt n$ nor $n/2$ but the window's own length $N = 4a-1$, and it follows from the two-class law alone.

---

### 4.4 The shared index, and two laws in it

Sections 4.1–4.3 index the window by position. This one indexes it by the *strike number* of each line, which turns two facts that were previously counted into consequences of the coordinate.

Keep $n = 6a$, and call **layer $j$** the pair of lines
$$p = n-6j-1, \qquad s = n-6j+1,$$
running them on the shared index $k = 6j+t$. Translating the anchor identity $L_{q-6j}(6j) = q^2-36j^2$ of [IV, Thm 12] into the window coordinate $u$ gives, exactly,
$$u^-(t) = 2pt - 36j^2, \qquad u^+(t) = 4n - 36j^2 + 2st. \qquad\text{(4.1)}$$

*Verification.* Zero failures over $695{,}968$ checks ($a \lt  120$, all $j$, $t \in [-40,60]$).

Under the passage $W_n \to W_{n+6}$ an old layer has $j \to j+1$ and $k \to k+6$, so
$$t  =  k - 6j \quad\text{is invariant},$$
while the two positions shift by $-(72j+36)$ and $-(72j+12)$ — differing by $24$, which is exactly the increase in window width. **The state of the whole window is therefore $(n, j, t)$, and inheritance is $(n,j,t) \mapsto (n+6, j+1, t)$.** (This compresses the bookkeeping and not the arithmetic: the *active range* of $t$ is recomputed each time from $\lceil 18j^2/p\rceil$, and that ceiling is the phase. We record the state because the two laws below are clean in it.)

> **Theorem 6 (two-pass crossing).** At a common index $t$ the two members of a layer are
> $$u^+ - u^-  =  4n + 4t$$
> apart, against a window of width $4n$. Hence a layer has both members inside the window only at $t = 0$; and since $j \gt  0$ forces $t \ge \lceil 18j^2/p\rceil \gt  0$, **every old layer crosses the window in two disjoint passes — the family-$7$ member first, the family-$5$ member after — and only the newly born layer has both members present, sitting exactly on the two endpoints.**

*Proof.* Subtract the two lines of (4.1); the $36j^2$ cancels and $s-p = 2$. The window admits $u^+-u^- \le 4n$ only at $t \le 0$, and the left member requires $2pt \ge 36j^2$. $\blacksquare$

*Verification.* Over every window and layer with $a \lt  200$ the two $t$-ranges never overlap: zero exceptions.

**The reading is worth stating.** The window is cut exactly to the size of the pair that is born at its edges; every older pair has already opened wider than the window and can only pass through one member at a time.

> **Theorem 7 (the role of a strike is $t \bmod 3$).** Since $p \equiv -1$, $s \equiv +1$ and $4n \equiv 0 \pmod 6$, equation (4.1) gives
> $$u^-(t) \equiv 4t, \qquad u^+(t) \equiv 2t \pmod 6 .$$
> With $(n-1)^2 \equiv 1 \pmod 6$, a strike at $u \equiv 0$ falls on the upper member of a cell, at $u \equiv 4$ on the lower member, and at $u \equiv 2$ on $L_3$ — where it touches no cell at all. Hence:

| $t \bmod 3$ | left line ($p$) | right line ($s$) |
|------|------------------|-------------------|
| $0$ | upper rail | upper rail |
| $1$ | lower rail | wasted on $L_3$ |
| $2$ | wasted on $L_3$ | lower rail |

*Verification.* Zero failures over $428{,}340$ checks.

**Two consequences.** First, **exactly one strike in three of every line is spent on $L_3$** — a fact used by counting in [IV, §6.2] and elsewhere, here obtained from the coordinate instead. Measured over the whole window at $a = 1667$, the strikes split $33.32\text{ per cent} / 33.32\text{ per cent} / 33.36$% between $u \equiv 0, 2, 4$.

Second, the scheduling is **asymmetric between the rails**: the two members of a layer both act on the upper rail at $t \equiv 0$, but on the lower rail at opposite residues, $t\equiv1$ for the left and $t\equiv2$ for the right.

**That asymmetry has a testable consequence, and it fails.** If it mattered, cells closed only on the upper rail would differ systematically from cells closed only on the lower. Over $1{,}000$ windows ($a = 200,\dots,1199$) the difference has mean $-1.03$ with standard deviation $20.05$, giving $t = -1.62$, and is positive in $470$ of $1000$ windows. **No effect.** We report it because the asymmetry in $t$ is real and it was the one place in this section from which a statement about twins could have come.

### 4.5 The strip is fixed and the sectors tile it

Theorem 4 says that one sector is a segment of cell indices. Read across sectors it says something stronger, and it is worth stating separately because it removes an object we have been carrying without need.

Take the sectors anchored at the odd multiples of three rather than at twin candidates: put $M = 6r+3$ and
$$W_r  =  \big(M^2,\ (M+6)^2\big),$$
so that consecutive $W_r$ meet end to end. Then $M^2+3$ is divisible by $6$, and writing $a_r = (M^2+3)/6$ for the first cell index inside $W_r$,
$$a_r  =  6r(r+1)+2, \qquad L_r  =  2M+6  =  12(r+1), \qquad\text{(4.2)}$$
and the two are linked by an exact telescoping:

> **Proposition 2.** $a_{r+1} - a_r = L_r$ for every $r \ge 0$. Hence the sectors $W_r$ partition the cell strip: $W_r$ is precisely the block of indices $[a_r,\ a_{r+1}-1]$, with no gap and no overlap.

*Proof.* $a_{r+1} - a_r = 6(r+1)(r+2) - 6r(r+1) = 6(r+1)\lbrace (r+2)-r\rbrace = 12(r+1) = L_r$. $\blacksquare$

*Verification.* Exact for every $r \lt 2000$. At $r = 1$: $M = 9$, $a_1 = 14$, $L_1 = 24$, so $W_1 = (81,225)$ is the cells $14,\dots,37$ — from $(83,85)$ to $(221,223)$ — and the next sector starts at $a_2 = 38$.

**What this removes.** The cell $C_n = (6n-1,6n+1)$ is defined once and for all, and by Theorem 3 each line $p$ closes the two classes $n \equiv \pm 6^{-1} \pmod p$ — also once and for all. Neither depends on the sector. **There is therefore no phase attached to a sector**: what looks like one is only the position of the moving start $a_r$ inside a strip that never moves. The whole of the twin question in these coordinates is
$$C_r  =  \#\lbrace n \in [a_r,\ a_{r+1}) : n \not\equiv \pm 6^{-1} \pmod p \ \text{ for every } 5 \le p \le M \rbrace, \qquad\text{(4.3)}$$
one fixed periodic pattern read along one moving quadratic trajectory.

**And the trajectory has an exact displacement law.** From (4.2),
$$a_s - a_r  =  6\big(s(s+1) - r(r+1)\big)  =  6\,(s-r)(s+r+1), \qquad\text{(4.4)}$$
so $a_{r+p} \equiv a_r \pmod p$ — the start's motion against a line of step $p$ has period exactly $p$ in $r$ — and if two starts agree modulo every prime of a set $S$ (none of them $2$ or $3$), then $\prod_{p \in S} p$ divides $(s-r)(s+r+1)$. For distinct $r,s \le R$ that product is at most $R(2R+1)$, so **two different starts below $R$ cannot agree modulo more than about $2\log R$ worth of prime mass.** The trajectory is multiplicatively spread.

*What (4.4) does not do, stated here so that it is not attempted again.* It compares two starts. If the start $a_r$ is itself the bad one there is no second start to compare it with: $s = r$ makes the right-hand side zero, every product divides zero, and no contradiction arises. Any displacement law is a two-point statement, and the question — whether one particular $a_r$ lands badly — is a one-point statement. Strengthening the law cannot repair that, because the distance it measures is not there.

---

## 5. A second sense of ownership: the central factor

Theorem 1 asks which line is *responsible* for a position — the smallest line reaching it. This section asks a different ownership question about the same object $L_m(k)=m(m+2k)$, and it has an exact answer.

### 5.1 The central pair, and the loss index

For odd $m \ge 3$ write $m = ab$ with
$$a  =  \max\lbrace d : d \mid m,\ d^2 \le m\rbrace , \qquad b  =  m/a ,$$
so $a \le b$; we call $(a,b)$ the **central pair** of $m$. For prime $m$ it is $(1,m)$. (These are the classical *middle divisors*, sequences A033676 and A033677 of [2]; $a+b$ is the least semiperimeter of an integral rectangle of area $m$ — see the note in §5.6.)

At the strike $N = L_m(k) = m(m+2k)$ we have $m \lt  \sqrt N \lt  m+2k$, so $m$ is a divisor of $N$ below its square root. Say that $L_m$ **holds the centre** of that strike if $m$ is still the *largest* such divisor, and define
$$\ell(m)  =  \min\lbrace  k \ge 1 : L_m \text{ does not hold the centre of } L_m(k) \rbrace .$$

### 5.2 A reformulation

> **Lemma.** For $n \gt  m$, the line $L_m$ fails to hold the centre of $N = mn$ **iff** $N$ has a divisor strictly between $m$ and $n$.

*Proof.* If $d \mid N$ with $m \lt  d \le \sqrt N$ then $d \lt  n$, since $\sqrt N \lt  n$. Conversely let $d \mid N$ with $m \lt  d \lt  n$. Either $d \le \sqrt N$, and we are done; or $d \gt  \sqrt N$, and then $N/d \lt  \sqrt N$ while $N/d = mn/d \gt  mn/n = m$, so $N/d$ serves instead. $\blacksquare$

### 5.3 Theorem 8 (when the centre is lost)

> **Theorem 8.** For every odd $m \ge 3$ with central pair $(a,b)$,
> $$\boxed{ \ell(m)  =  a+b+2 }$$
> The first loss is the strike
> $$L_m(a+b+2)  =  m\big(m + 2(a+b+2)\big)  =  ab (a+2)(b+2),$$
> and the divisor that displaces $m$ from the centre is $a(b+2) = m+2a$.

*Proof.* **The value is attained.** Put $n = (a+2)(b+2) = m + 2(a+b+2)$, which is odd. Then $a(b+2)$ divides $mn$ and
$$m  =  ab  \lt   ab+2a  =  a(b+2)  \lt   ab+2a+2b+4  =  n ,$$
so by the Lemma the centre is already lost at $k = a+b+2$.

**No earlier $k$ is possible.** Let $n = m+2k$ and suppose $mn$ has a divisor $d$ with $m \lt  d \lt  n$. Splitting prime by prime, write $d = g d_1$ with $g \mid m$ and $d_1 \mid n$, and set $m_1 = m/g$, $e_1 = n/d_1$. Then
$$d \gt  m \iff g d_1 \gt  g m_1 \iff d_1 \gt  m_1, \qquad d \lt  n \iff g d_1 \lt  d_1 e_1 \iff g \lt  e_1 .$$
Now $m$ and $n$ are odd, so $g, m_1, d_1, e_1$ are **all odd**; two distinct odd numbers differ by at least $2$, giving $d_1 \ge m_1+2$ and $e_1 \ge g+2$. Hence
$$n  =  d_1 e_1  \ge  (m_1+2)(g+2)  =  g m_1 + 2(g+m_1) + 4  =  m + 2(g+m_1) + 4 .$$
Over all factorisations $m = g m_1$ the sum $g+m_1$ is least for the central pair, so $g+m_1 \ge a+b$ and $n \ge m + 2(a+b) + 4$, i.e. $k \ge a+b+2$. $\blacksquare$

*Where the odd world enters.* The two steps of $2$ are the whole content of the bound. Without the parity hypothesis one gets only $d_1 \ge m_1+1$, $e_1 \ge g+1$ and the weaker floor $n \ge (m_1+1)(g+1) = m + (a+b) + 1$; and for even $m$ the value $a+b+2$ is indeed **not** attained.

*Verification.* Over every odd $3 \le m \lt  4000$, the first $k$ at which the largest divisor of $m(m+2k)$ below the square root exceeds $m$ equals $a+b+2$: **zero exceptions**. Over every even $4 \le m \lt  600$ the equality fails in all $298$ cases, while the weaker floor above is never breached. The Lemma was checked separately: the two formulations agree on all $39{,}800$ pairs $(m,n)$ with $m \lt  400$ odd and $m \lt  n \lt  m+400$.

### 5.4 Corollary 5 (the handover)

The regrouping in Theorem 8 is symmetric: $ab(a+2)(b+2) = \big[a(b+2)\big]\big[b(a+2)\big]$, and the two new factors are $m+2a$ and $m+2b$, differing by $2(b-a)$. Writing $T(m) = m+2a$ for the displacing divisor:

> **Corollary 5.** $L_m(a+b+2)  =  L_{T(m)}(b-a)$ with $T(m) = m+2a$.

So the first loss is not merely a coincidence of two lines at one integer: it names the receiving line **and its strike index**. Two special cases:

- **Squares.** For $m = c^2$ the central pair is $(c,c)$, so $\ell = 2c+2$, $T(m) = c(c+2)$ and $b-a = 0$: the loss lands exactly on the *birth* of the new line,
 $$L_{c^2}(2c+2)  =  L_{c(c+2)}(0)  =  \big[c(c+2)\big]^2 .$$
 For $c=3$: $L_9(8) = 9\cdot 25 = 225 = 15^2$.
- **Primes.** For $m = p$ the central pair is $(1,p)$, so $\ell(p) = p+3$, $T(p) = p+2$, and
 $$L_p(p+3)  =  L_{p+2}(p-1)  =  3p(p+2).$$
 For $p=5$: $L_5(8) = 105 = L_7(4)$.

### 5.5 Corollary 6 (the composites absorb)

> **Corollary 6.** $T(m) = m+2a = a(b+2)$. Hence if $m$ is composite then $T(m)$ is composite.

*Proof.* $a \gt  1$ and $b+2 \gt  1$. $\blacksquare$

Under iteration of $T$ the primes are therefore a transient set: an orbit may leave them and can never return. Verified over every composite odd $m \lt  20{,}001$: no $T(m)$ is prime.

### 5.6 What this does not give, and where it sits

Theorem 8 makes $\ell$ maximal exactly on the primes, since
$$\ell(m) = m+3 \iff a+b = ab+1 \iff (a-1)(b-1) = 0 \iff a = 1 .$$
**This is a restatement of the definition of a prime, not a characterisation of one:** evaluating $\ell(m)$ requires the central pair, that is, a factorisation of $m$. We record it because it marks precisely the point at which this construction reproduces the definition rather than reaching past it — the same boundary Theorem 1 meets from the other side.

*Placement.* The central pair is classical: $a$ and $b$ are the *middle divisors* $\rho_1(m) = \max\lbrace d \mid m: d \le \sqrt m\rbrace$ and $\rho_2(m) = m/\rho_1(m)$, whose average orders were determined by Tenenbaum [3]; $a+b$ is the least semiperimeter of an integral rectangle of area $m$, studied under that name by Martin [4], who also records that it equals $m+1$ exactly for $m$ prime — the display above, in other words, is already in the literature. The reformulation of §5.2 places the question inside the study of divisors of an integer in a short interval. A targeted search did not find the identity $\ell(m) = a+b+2$ itself recorded; it is elementary enough that it may well be folklore, and no priority is claimed for it. What the section adds here is that it is the exact answer to an ownership question this framework asks anyway, and that the two steps of $2$ come from the odd lattice.

---
---


## Appendix A — Fingerprint and sector tables

$D_p(j) = 4j^2 \bmod 2p$:

| $p$ | fingerprint |
|------|--------------------------------------------------------------------|
| 3 | 0, 4, 4, 0 |
| 5 | 0, 4, 6, 6, 4, 0 |
| 7 | 0, 4, **2**, 8, 8, **2**, 4, 0 |
| 11 | 0, 4, 16, 14, 20, 12, 12, 20, 14, 16, 4, 0 |

$H_j = 2 + W_j$ over the first cycle (the histogram of these values is [0, Thm 2]):

| $p$ | $H_j$ |
|------|--------------------------------------------------------------------|
| 7 | 2, 3, 3, 4, 5, 5, 6 |
| 11 | 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6 |
| 13 | 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6 |


## Appendix B — The mod-24 identity card

Combining $p \bmod 6$ (which strike carries the $L_3$-meeting) with $p \bmod 8$ (whether $D = 2$ is reachable, i.e. whether $2$ is a quadratic residue):

| $p \bmod 24$ | 1 | 5 | 7 | 11 | 13 | 17 | 19 | 23 |
|--------------|-----|----|-----|----|----|-----|----|-----|
| reaches $D=2$ | yes | no | yes | no | no | yes | no | yes |

Zero failures over 428 primes. Writing $D_j = 2h_j$ one has $h_j \equiv 2j^2 \pmod p$, so a line's reachable distances to squares are exactly twice the squares mod $p$; the number of distinct values is $(p+1)/2$, which is the true source of $D_j = D_{p-j}$. Note that $D = 4$ is reachable by **every** line, since $2j^2 \equiv 2$ means $j^2 \equiv 1$.


## Appendix C — The triple $T(a)$

Each cell $C_a$ generates three equally spaced cells in the square plane:
$$a  \longmapsto  \big(6a^2-2a,   6a^2,   6a^2+2a\big),$$
arising from $(6a-1)^2$, $(6a-1)(6a+1)$ and $(6a+1)^2$, with spacing $2a$.

| $a$ | $(6a-1)^2$ | $(6a-1)(6a+1)$ | $(6a+1)^2$ |
|------|------|------|------|
| 1 | $25 \to C_4$ | $35 \to C_6$ | $49 \to C_8$ |
| 2 | $121 \to C_{20}$ | $143 \to C_{24}$ | $169 \to C_{28}$ |
| 3 | $289 \to C_{48}$ | $323 \to C_{54}$ | $361 \to C_{60}$ |

Moreover $p_+^2 - p_-^2 = 2p_- + 2p_+$ exactly, so the two lines' steps fill the square gap without remainder: $49-25 = 24 = 10+14$; $169-121 = 48 = 22+26$; $361-289 = 72 = 34+38$.

**Caveat.** The law holds for every $a$, twin or not; at $a=4$ the member $25$ is composite. The geometric law therefore does not distinguish twins, and the distinction reverts to whether the outer squares are births or inherited — a question about the older lines.


---

## Appendix D — Note on method

One rule was followed throughout: **every deviation was measured against an explicit baseline before it was interpreted.** Two consequences worth recording.

- The constant $2$ in $H_j = 2 + W_j$ is essential and was found by failure, not by design: the formula without it fails in $57$ of $78$ tested cases. (Recorded again in [0, App. B], since it is easy to mislay.)
- $D$ is **not** monotone. The ascending quantity is the raw $4j^2$; after folding modulo $2p$ the order scrambles. For $p = 7$ the fingerprint reads $0, 4, \mathbf{2}, 8, 8, \mathbf{2}, 4, 0$. Monotonicity holds only for $p = 3, 5$. Note also that $H$ satisfies a *sum* symmetry ($=8$) whereas $D$ satisfies an *equality*.

Verification code and the tables behind every "zero failures" claim accompany the monograph from which this series is drawn. The claims of §5 are regenerated by `verify_central_pair.py`.

---

**No progress toward the twin-prime conjecture is claimed, and no new bound.** Priority is not claimed for any result.

*The computations and much of the prose in this paper were prepared with AI assistance (Claude, Anthropic), used for drafting and rewriting code and text, running the computations, searching the literature, and auditing the paper against its own scripts. The research direction, the questions asked, the decisions about what to publish and what to withdraw, and the responsibility for every claim are the author's. The full note is in the repository README.*

---

## References

The companion papers are cited as [0] and [IV].

1. J. Friedlander and H. Iwaniec, *Opera de Cribro*, AMS Colloquium Publications **57**, 2010. — *used once, in §3.5, to name the classical object of which the geometric statement there is a reading.*
2. N. J. A. Sloane (ed.), *The On-Line Encyclopedia of Integer Sequences*, sequences A033676, A033677 (the middle divisors) and A063655 (their sum). — *the central pair of §5.1 under its standard names.*
3. G. Tenenbaum, *Sur deux fonctions de diviseurs*, J. London Math. Soc. (2) **14** (1976), 521--526. — *the average order of the upper middle divisor $\rho_2$, cited in §5.6 for placement only.*
4. G. Martin, *Farmer Ted goes natural*, Mathematics Magazine **72** (1999), 259--276; arXiv:math/9807108. — *the least semiperimeter $a+b$ of an integral rectangle of area $m$, cited in §5.6.*

*No proof imports anything: reference 1 names an object, and references 2--4 place the central pair of §5 in the existing literature. No analytic estimate is used anywhere.*
