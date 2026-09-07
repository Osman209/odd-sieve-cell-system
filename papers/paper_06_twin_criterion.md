# The Twin Criterion: Six Exception Positions

## Paper 6. A single open cell in a sector is a twin pair unless it sits at one of six named places

---

### Abstract

After switching on every line $p \le M$ in the sector $(M^2,(M+6)^2)$, **at most six cells can be open without being a twin**, and their positions are explicit quadratics in $M$. The criterion that follows is the sharpest the framework produces: a single open cell suffices, provided it is not at one of six named places. The six are the strikes of the two lines born inside the sector, minus the strikes lost to the line $3$, and the same walk gives the ladder $2k(2k+1)$ in a window widened $k$-fold. Two of the six carry perfect squares and may be discarded; of the four that remain at most one can be open at a time, and in two residue classes modulo $30$ the line $5$ closes them outright. A census over the $166{,}666{,}665$ sectors below $10^9$ finds no violation of any statement here and measures the sifting dimension of the survivors as three. **No progress toward the twin-prime conjecture is claimed.**

**Numbering.** This paper is one part of a set that was written as a single document and is now published in parts. Each part numbers its own results from one and is self-contained: a reference of the form [Pn, Thm 1] means Theorem 1 of Paper n, and an unqualified "Theorem 1" always means this paper's own. Result numbers therefore differ from those of releases before 2.0.0, where the whole set shared the numbering of the single document.

**How to read the claims in this paper.** Statements set as Theorems, Propositions and Corollaries are proved, and the proofs are given. One result in the set is labelled **Verified Law**: it is proved under a stated hypothesis and verified numerically outside it. Anything described as *measured* is a computation over a stated finite range and is labelled as such where it occurs.

**Keywords:** twin primes, exception positions, sieve cycles, cell coordinates, singular series.

**MSC 2020:** 11N35, 11N05, 11A41.

---

## Summary of the results in this part

**§2 — The twin problem inside the framework**

| Result | What it says | Section |
|--------------------|-------------------------------------|-----------------|
| ***The pivot*** | Inside $(u^2,v^2)$ with every line up to $u$ switched on, **a cell that survives *is* a twin pair** — no primality test is needed. Everything downstream rests on this. | §2.1 |
| **Theorem 1** | At most **six** cells of a sector can be open without being twin pairs, with their positions given explicitly in $M$. | §2.2 |
| **Corollary 1** | The dichotomy: if $(M+2,M+4)$ is not a twin then $\lvert S_M \cap E_M\rvert  \le 2$, so the sufficient count falls from $C_M \ge 7$ to $C_M \ge 3$. | §2.2 |
| **Corollary 1a** | The six generalise: in $(M^2,(M+6k)^2)$ with $M \gt  (6k)^2$ there are $2k(2k+1)$ candidate positions and no open cell with two composite endpoints. | §2.2, App. A.3 |
| **Corollary 1b** | A line above $31$ closes at most one of the six exception cells, unless it divides $M+8$, when it closes two. The large lines cannot gather the exceptions. | §2.2, App. A.3 |
| **Corollary 1c** | In the symmetric window between the squares of $6r\mp1$, a single surviving cell of any kind gives a twin pair — the central cell by the primality of its own endpoints. | §2.2, App. A.3 |
| **Corollary 1d** | Discarding cells with a square endpoint leaves at most **one** exception, and none at all when $M \equiv 21 \pmod{30}$. | §2.2, App. A.3 |
| **Corollary 1e** | The sectors carrying an open non-square exception have density zero — the four positions are sifted in dimension three, measured over $1.7\times10^8$ sectors. | §2.2, App. A.3 |
| *Remark* | Each of the six partner quadratics takes square-free values with at most two prime factors infinitely often, by Iwaniec and Lemke Oliver — separately, not simultaneously. | §2.2, App. A.3 |
| **Proposition 2** | The admissible exceptional configurations in a block of $N = 35L$ sectors number $B_L \ll L/\log^2 L$, by the Selberg sieve. | §2.4, App. B.1 |
| **Theorem 2** | A newly born line closes **at most one** twin cell in its own first window: $D_p \in \lbrace 0,1\rbrace$. | §2.5 |
| **Corollary 2** | $D_p = 1$ exactly when two primality conditions hold together, so the error term is itself twin-like. | §2.5 |
| **Theorem 3** | The bridge pair: $B' = (q-2-\chi_q(2))B$ — the only law here that knows the window is anchored at a square. | §2.6 |
| **Theorem 4** | The summation identity over $M$ consecutive square windows. | §2.6 |
| ***Recorded, not used*** | Two constructions that do not help — the balanced window, and ownership through the cofactor — kept so they are not retried. | §2.8, App. B.3 |
| **Proposition 1** | The odd Bonferroni truncation is a **proved** lower bound on $C_M$, evaluated in one pass by the multiplicity $m(d)$, and exact once the order reaches $\max_d m(d)$ — which grows like $\log\log M$, not like $\pi(M)$. | §2.9 |
| ***Placement*** | The same finite-window obstruction, reached independently from the Goldbach side. | §2.10 |
| **Propositions 3–5** | A mirror law for the sector index; the exact discrepancy $s(d-s)/(dH)$ of a Fejér window, whence $d/(4H)$; and $\ll d^3/(HT^2)$ for a moving one, with a sharp exponent. The kernels are classical and cited; together they gain a factor of nine on $L_7$ and **reach none of $S_5$ and beyond**. | §2.11, App. B.4 |

---

## 1. Setting

We use Papers [P1] and [P2]–[P4] as follows. Paper [P9]–[P11] is a companion rather than a source: it is cited where the obstruction it derives explains why a cut is placed where it is, and nothing else is imported from it.

- **[P1]** supplies the window combinatorics: the increments $W_j$ of $\lfloor 2j^2/p\rfloor$, their uniform bound and their exact histogram.
- **[P2]** supplies the coordinates: the line $L_p(k) = p(p+2k)$ beginning at $p^2$, the grid $L_3$, the cells $C_b = (6b-1, 6b+1)$, and the square window with its $+8$ growth.
- **[P3]** supplies the exact cycle laws: the four-state law, its refinement by inheritance depth, arbitrary weights in $\Omega_{\le z}$, the refinement by line size, and the disjoint ownership layers.
- **[P4]** studies the transfer to a window of length $\asymp z^2$. On the tested windows, linear depth weights measure $1.0000$ to the reported precision, the tested soft truncations remain close to $1$, and the sharp depth-zero indicator is the exceptional endpoint with ratio near $0.80$. These are measurements, not an exact window theorem.

A word on the last point, since it is what makes this paper's organisation possible. The indicator of depth zero is the condition "both members of the cell survive" — that is, the twin condition. Thus, in the tested family, the largest transfer loss occurs precisely at the depth-zero indicator, the quantity that becomes a primality/twin condition inside the moving square window.

---

## 2. The twin problem inside the framework

### 2.1 When a surviving cell is automatically a twin pair

Let $u\lt v$ be consecutive integers coprime to $6$. Every survivor of all lines $\le u$ inside $(u^2, v^2)$ is necessarily prime, since a composite $x \lt  v^2$ has a prime factor $\le \sqrt{x} \lt  v$, and there is no prime strictly between $u$ and $v$. Hence
$$\boxed{ \text{a surviving } NN \text{ cell in } (u^2,v^2)  =  \text{a twin prime pair.} } \qquad\text{(3.1)}$$

*The half of this that concerns a single square gap — that the least prime factor of an odd composite between $n^2$ and $(n+1)^2$ is at most $n$ — is stated as Lemma 1A of [4]; what (3.1) adds is the passage to a cell and the consequence that the surviving cell is a twin pair rather than merely a pair of survivors.*

**What (3.1) does and does not give for a sector.** Equation (3.1) is an equality, but its hypothesis is that no prime lies strictly between $u$ and $v$. The sector $(M^2,(M+6)^2)$ with $M \equiv 3 \pmod 6$ does not satisfy that: the two lines $M+2$ and $M+4$ are born inside it, and their strikes are exactly the six positions Theorem 1 names. So for a sector the relation is (3.4) below:
$$C_M  =  T_M + X_M, \qquad 0 \le X_M \le 6, \qquad\text{(3.4)}$$
with $X_M$ the number of open cells that are not twin pairs — all of them at the six named positions. **The sector's geometry can move the survivor count away from the twin count only through those six places, and by at most six.** The table below carries an instance: at $M = 10{,}005$ the sector holds $504$ open cells and $503$ twin pairs, the extra one being the cell $(100{,}180{,}079,\ 100{,}180{,}081)$ whose upper member is $(M+4)^2 = 10{,}009^2$ — position $C$. *Measured over the $49{,}999$ sectors with $M \lt 3\cdot10^5$: $X_M = 0$ in $45{,}439$ of them, $1$ in $4{,}369$, $2$ in $186$ and $3$ in five, and never more — so the bound of six is not attained on that range.*

Because the discrepancy is bounded by an explicit constant, $C_M$ still has to track the Hardy–Littlewood prediction for a window of $\lvert W\rvert = 12M+36$ integers at height $M^2$, and the comparison below is a diagnostic on the twin count itself up to that $O(1)$. Write
$$\mathrm{HL}  =  \frac{2C_2\ \lvert W\rvert}{\log^2(M^2)}, \qquad \mathrm{SP}  =  \lvert W_{\text{cells}}\rvert \prod_{5\le p\le M}\Big(1-\frac2p\Big)$$
for that prediction and for the raw sieve product over the cells. Then:

| $M$ | cells | $C_M$ | $\mathrm{HL}$ | $C_M/\mathrm{HL}$ | $\mathrm{SP}$ | $C_M/\mathrm{SP}$ |
|------|---------|-------|---------|-------|---------|-------|
| $1{,}005$ | 2,016 | 87 | 83.6 | 1.041 | 104.7 | 0.831 |
| $5{,}001$ | 10,008 | 281 | 273.2 | 1.028 | 343.4 | 0.818 |
| $10{,}005$ | 20,016 | 504 | 467.3 | 1.079 | 587.8 | 0.857 |
| $20{,}001$ | 40,008 | 796 | 807.9 | 0.985 | 1,017.6 | 0.782 |
| $50{,}001$ | 100,008 | 1,679 | 1,691.9 | 0.992 | 2,131.8 | 0.788 |
| $100{,}005$ | 200,016 | 2,936 | 2,988.6 | 0.982 | 3,766.1 | 0.780 |

**The same comparison has been made independently, in the same coordinates.** Morpurgo [8] studies twin pairs between $(p_n-2)^2$ and $p_n^2$, writes the candidates as multiples of $6$, discards those congruent to $\pm 1$ modulo each sieving prime — the classes of [P2, Thm 3] in additive form — and compares the count with $\prod (p-2)/p$ corrected by $(2e^{-\gamma})^{2}$, reaching agreement better than one per cent for $p_n$ above $6\cdot 10^{6}$. That paper is a prediction and a measurement rather than a set of theorems, and none of the statements below appears in it; we cite it because the coordinates and the comparison are the same ones, arrived at independently, and because its agreement over a far longer range than ours corroborates the reading of (3.1) given here.

The first ratio settles to $1$ from below within about $2$%; the second settles at $0.78$, which is the classical discrepancy between the sieve product and the truth at depth $\sqrt{x}$ and is not a property of these coordinates. **The point of the table is the first column pair, and it is a constraint rather than a confirmation.** This leaves no room for an argument that hopes to make $C_M$ exceed the Hardy–Littlewood count by exploiting structure in the sector — its anchoring at a square, the coupling between the lines' phases, the trajectory of the sector start. By (3.4) $C_M$ differs from the twin count by at most six, so any excess an argument of that kind could produce would have to be an excess in the twin count itself.

Two controls make the same point from the other side, and both are recorded because each closed a route that had been proposed. First, replacing the true phases by random ones while keeping the same lines and the same two classes per line raises the survivor count from $1{,}679$ to $2{,}131 \pm 34$ at $M = 50{,}001$ — but that gap is entirely the height of the window, not its arithmetic: placing the same sieve on a block of the same length at a comparable height $y \in (M^2, 3M^2)$ gives $1{,}797 \pm 60$, within two standard deviations of the truth. Second, a control that *keeps* the phase coupling implied by the sector trajectory — all lines in one layer drawing their phase from a single number — but changes that number gives $2{,}127 \pm 34$, indistinguishable from the fully independent $2{,}131 \pm 34$. **The coupling between the lines' phases is a description of the sector, not a constraint on it.**

### 2.2 Theorem 1: only six cells in a sector can be open without being a twin

Take the sector in the form used throughout this section: $M \equiv 3 \pmod 6$ and the interval $(M^2, (M+6)^2)$, which carries $A_M = 2M+6$ cells
$$C_j = \big(M^2+6j+2,\ M^2+6j+4\big), \qquad j = 0,1,\dots,2M+5 .$$

> **Theorem 1.** Switch on every line $p \le M$. Then at most **six** cells of the sector can be open without being a twin pair, and their positions are given explicitly by
> $\displaystyle E_M  =  \underbrace{\Big\lbrace \tfrac{2M}{3},\ \ M+1,\ \ \tfrac{5M}{3}+2,\ \ 2M+3\Big\rbrace }_{\text{present only if } M+2 \text{ is prime}}  \cup  \underbrace{\Big\lbrace \tfrac{4M}{3}+2,\ \ 2M+5\Big\rbrace }_{\text{present only if } M+4 \text{ is prime}} .$
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
| composite | prime | $2$ |
| prime | composite | $4$ |
| prime | prime | $6$ |

At $M = 999$ both $1001 = 7\cdot11\cdot13$ and $1003 = 17\cdot59$ are composite, so $E_M$ is empty and **all $93$ open cells of that sector are twin pairs** — as measured.

*Two remarks on the sharpness of this count.* $E_M$ is a set of candidate **positions**, and the number of cells that are actually open without being twins is smaller. The position $B$ carries $(M+2)(M+4)$ and so requires **both** $M+2$ and $M+4$ prime; when $M+4$ is composite its least prime factor is at most $\sqrt{M+4} \lt M$, so that cell has already been closed by an older line and cannot be an exception at all. Hence the row "$M+2$ prime, $M+4$ composite" admits at most **three** actual exceptions, not four. And the caps are not attained on any tested range: over every $M \equiv 3 \pmod 6$ below $4000$ the largest number of open non-twin cells in a sector is $0$, $2$, $2$ and $3$ in the four rows respectively. What Theorem 1 asserts, and all that is used below, is the inclusion $S_M \setminus E_M \subseteq \lbrace \text{twins}\rbrace$.

**Why six: the positions are the steps of the newborn lines.** A line $L_p$ is dormant from its first contact with $L_3$ at $3p$ until its birth at $p^2$ — a stretch of $p(p-3)$, i.e. $(p-3)/2$ steps of $2p$, every one of them owned by a smaller line — and then walks on in steps of $2p$. Because $p^2 \equiv 1 \pmod 6$, the walk lands alternately on an upper member, on $L_3$, and on a lower member: one step in three is spent on $L_3$ and strikes no cell. Only two lines are born inside the sector, $M+2$ and $M+4$. Walking each from its birth, $L_{M+2}$ makes five steps before $(M+6)^2$ ($k = 0,\dots,4$, since $(M+2)^2 + 2(M+2)k \lt  (M+6)^2$ forces $k \le 4$), of which $k = 2$ falls on $L_3$; the other four are $A, B, D, E$. $L_{M+4}$ makes three steps ($k \le 2$), of which $k = 1$ falls on $L_3$; the other two are $C, F$. Four and two make six. This is Theorem 1 again, proved by counting steps instead of factor pairs, and it explains the number rather than only establishing it.

The same walk gives the ladder of Corollary 1a below without algebra: in $(M^2, (M+6k)^2)$ the newborn lines are $M+a$ for the $2k$ admissible offsets $a$, and walking each from its birth and discarding the steps on $L_3$ leaves $4k, 4k-2, \dots, 2$ cells respectively — the rows of that corollary — with $2k^2$ steps lost to $L_3$ in all and $2k(2k+1)$ cells kept. Checked against the corollary's list for $k \le 6$ on four windows each, twenty-four in all, with exact agreement; at $k = 2$ the four newborn lines make $11, 9, 5, 3$ steps inside the window and lose $3, 3, 1, 1$ of them to $L_3$.

**What this buys, stated precisely.** Writing $C_M$ for the number of open cells, one has $T_M \ge C_M - |E_M| \ge C_M - 6$, so a twin follows from $C_M \ge 7$. Theorem 1 replaces that by the much weaker requirement
$$S_M \not\subseteq E_M, \qquad\text{(3.2)}$$
where $S_M$ is the set of open indices: **a single open cell suffices, provided it is not at one of six named places.** And the six places are fixed by the geometry of the square — they are not chosen by the lines, whose phases are periodic and unrelated to $M$.

**The lines $5$ and $7$ alone cut six to three, and the pair is not interchangeable.** Writing $M = 6n+3$, the six positions are exact quadratics in $n$ as absolute cell indices:
$$A = 6n^2+10n+4, \qquad B = 6n^2+12n+6, \qquad C = 6n^2+14n+8,$$
$$D = 6n^2+16n+9, \qquad E = 6n^2+18n+11, \qquad F = 6n^2+18n+13.$$
(verified for $n = 1,\dots,3999$ against the definition). Each is therefore a function of $n \bmod p$ modulo any $p$, so the state of all six under the lines $5$ and $7$ depends on $n \bmod 35$ alone: **the $35$ classes are not a sample but the whole question**, and checking them is a proof rather than an experiment. Doing so gives $\max|S_M \cap E_M| \le 3$ after those two lines alone, with only four maximal patterns —
$$\lbrace A,B,C\rbrace , \quad \lbrace A,E,F\rbrace , \quad \lbrace C,D,F\rbrace , \quad \lbrace C,E,F\rbrace ,$$
writing $A,\dots,F$ for the six positions in the order listed above. The collapse from $2^6 = 64$ conceivable patterns to four is what makes the next step possible.

The pair is special. Line $5$ alone leaves four open; adding $7$ gives three; and **adding $11$, then $13$, changes nothing at all** — the same bound and the same four patterns. The reason is structural rather than numerical: a larger line can choose a phase striking none of the six, and the Chinese remainder theorem then combines that phase freely with the phase of $5$ and $7$ that leaves three. **So the route "add more small lines until the six are closed" is shut**, and we record it so that it is not attempted again in another notation.

> **Corollary 1 (the dichotomy).** Suppose $(M+2, M+4)$ is not a twin pair. Then $|S_M \cap E_M| \le 2$, and consequently
> $\displaystyle C_M \ge 3 \quad\Longrightarrow\quad \text{the sector contains a twin, or } (M+2,M+4) \text{ is one.}$

*Proof.* Theorem 1 splits the six positions by what each one needs:
$$A, D, E \ \text{require} \ M+2 \ \text{prime}; \qquad C, F \ \text{require} \ M+4 \ \text{prime};$$
$$B \ \text{carries} \ (M+2)(M+4) \ \text{and so requires both}.$$
If the open set met both groups, $M+2$ and $M+4$ would both be prime and $(M+2, M+4)$ would be the twin. So under the hypothesis the open set lies inside $\lbrace A,D,E\rbrace$ or inside $\lbrace C,F\rbrace$, and $B$ is closed.

Each of the four maximal patterns listed above meets both groups, so none survives. Inspecting the $35$ classes, the patterns that do survive are
$$\varnothing, \quad \lbrace A\rbrace, \quad \lbrace C\rbrace, \quad \lbrace F\rbrace, \quad \lbrace A,D\rbrace, \quad \lbrace A,E\rbrace, \quad \lbrace C,F\rbrace\rvert,$$
all of size at most two. $\blacksquare$

*Verification.* Over the same $3{,}332$ sectors $M = 9, 15, \dots, 19{,}999$: the maximum of $|S_M \cap E_M|$ is $3$ in the $340$ sectors where $(M+2,M+4)$ is a twin and **exactly $2$ in the other $2{,}992$**; zero violations of the forcing (an open member of $\lbrace A,D,E\rbrace$ with $M+2$ composite, or of $\lbrace C,F\rbrace$ with $M+4$ composite, or $B$ open without the twin), and zero cases where the open set met both groups without the twin being present. **The separation is exact: three open positions occur only when the twin is already there.** Both bounds are attained — three in $3$ sectors, two in $13$ of the twinless ones — so neither is an artefact of a range too short to reach them.

**Five residue classes in which the two lines close all six.** Of the $35$ classes, five leave nothing open: $n \equiv 0, 8, 23, 25, 33 \pmod{35}$, that is
$$M \equiv 3,\ 51,\ 141,\ 153,\ 201 \pmod{210}.$$
There $S_M \cap E_M = \varnothing$ from the lines $5$ and $7$ alone, so **every** open cell is a twin. Condition (3.2) remains the weakest form of the criterion — it asks for no count at all — but in these classes it becomes *equivalent* to the bare $C_M \ge 1$, and Corollary 1 lowers the sufficient count in a general sector from $C_M \ge 7$ to $C_M \ge 3$. The improvement is to the numerical threshold, not to the criterion. Measured over the $713$ such sectors below $M = 30{,}000$: $444{,}958$ open cells and **not one of them fails to be a twin**, against $155$ non-twin survivors in the $428$ ordinary sectors below $M = 3000$ alone. And the restriction costs nothing in the count itself — the survivor density in these five classes, against all other classes, is $0.934$ up to $M = 4000$, $0.997$ up to $12000$ and $1.000$ up to $30000$; fixing the phases of $5$ and $7$ changes which cells die, not how many.

**The six are the first rung of a ladder, and the ladder does not help.** Nothing in the argument requires the window to stop at $(M+6)^2$. Widening it to $W_{M,k} = (M^2,(M+6k)^2)$ with the lines still at $p \le M$ gives exactly $K_k = 2k(2k+1)$ exceptional positions — $6, 20, 42, 72, \dots$ — with $k=1$ reproducing $E_M$; but the ceiling grows like $4k^2$ while the open cells grow like $2kM/\log^2 M$, so **widening the window makes the margin worse** and $k = 1$ is optimal. Two further sharpenings hold at $k=1$: cells with a perfect-square endpoint carry no twin and there are at most two of them, and using the line $5$ alone at most one of $B, D, E, F$ is open when the root pair is not a twin — none at all when $M \equiv 21 \pmod{30}$, only $B$ when $M \equiv 27$. The exception census has been carried to $M = 10^9$. All of it is bookkeeping rather than strength: $C_M^\circ \ge C_M - 2$, so it still amounts to Corollary 1.

*Corollaries 1a to 1e, the census, and the remark on the partner quadratics are in Appendix A.3.*

---

### 2.3 The exception budget over a full period, and the limit of local arguments

Corollary 1 bounds the exceptions in one sector. Consecutive sectors are not independent, and taking a whole period of them together lowers the bound further — up to a point that can be identified exactly.

**The sectors tile:** $(M^2,(M+6)^2)$ is followed immediately by $((M+6)^2,(M+12)^2)$, so a prime forced near the top of one is forced near the bottom of the next. Taking the $35$ sectors of one full period together — the window $(M_0^2,(M_0+210)^2)$ with $M_0 = 210k+3$ — and writing each exceptional position's requirement as a set of offsets that must be prime ($A$ needs $M+2$; $C$ needs $M+4$; $D$ needs $M+2,M+8$; $E$ needs $M+2,M+10$; $F$ needs $M+4,M+8$), the twinless hypothesis forbids any two forced offsets differing by $2$ across the whole window, not merely within a sector.

Summing the per-phase caps independently gives $5\cdot0+20\cdot1+10\cdot2 = 40$. The coupling costs three of those: three pairs of adjacent phases cannot both attain their caps, because the offsets clash across the join — for instance a phase reaching two via $\lbrace C,F\rbrace$ forces $M+8$, and its successor reaching two the same way forces $M'+4 = M+10$. **A fourth adjacent pair with the same caps does not clash**, which is the point: the obstruction is arithmetic in the offsets, not a consequence of adjacency. Hence $37$, and with the lines $11,13,17$ admitted as well, an exhaustive scan over all $5\cdot7\cdot11\cdot13\cdot17/35 = 2431$ alignments gives

$$\sum_{i=0}^{34}\bigl|S_{M_i}\cap E_{M_i}\bigr| \le 31 \qquad\text{(no twin in the window)},$$

the ceiling $31$ being attained in $9$ of the $2431$ alignments, and the distribution of the $2431$ values peaking at $26$.

**That ceiling cannot be lowered by any finite set of lines, and this is a theorem rather than a report of failed attempts.**

*What is and is not claimed.* The budget is a maximum over residues, so what is proved is that for every finite set of lines there is a choice of residues at which the extremal configuration survives them all; no residue-based argument brings the ceiling below $31$. It is *not* a claim that an integer $M_0$ realising the configuration exists, still less that infinitely many do — that would require all $133$ polynomials to be simultaneously prime, which is Hypothesis H and is not assumed anywhere here.

*The system.* The $9$ extremal alignments carry $28$ distinct maximal configurations. Each demands not only that certain $M_0+a$ be prime — $27$ to $30$ of them — but also that the *partner* member of each of the $31$ cells survive, and those partners are quadratics in $n$: $36n^2+60n+23$ for $A$, $36n^2+84n+47$ for $C$, $36n^2+96n+53$ for $D$, $36n^2+108n+67$ for $E$ and $36n^2+108n+79$ for $F$ (verified against the definition for $n \lt 3000$).

*The surviving configuration.* Testing the full linear-and-quadratic systems for a fixed prime divisor kills **$27$ of the $28$** — $q=23$ disposes of fourteen, $q=31$ of ten, $q=19$ of three. One survives, at $M_0 \equiv 448353 \pmod{510510}$, with $28$ linear and $31$ quadratic conditions: $59$ polynomials of total degree $90$. Every prime $q \le 90$ leaves at least one admissible residue — the tightest are $q=19$ and $q=31$, with exactly one each — and for $q \gt 90$ a residue survives automatically, since $90$ polynomials of that total degree have at most $90$ roots.

**The system is therefore admissible at every prime, so by the Chinese remainder theorem the residues can be chosen simultaneously against any finite list of further lines: no residue-based argument, however many primes it uses, reaches $30$.**

**Nor does the order in which the lines are born supply the missing constraint.** One might hope that a line $M_0+a$, forced prime by one exceptional cell, strikes another of the $31$ once it is born. Modulo $p = M_0+a$ one has $M_0 \equiv -a$, so a member $(M_0+u)(M_0+v)+e$ with $e \in \lbrace 0,\pm2\rbrace$ reduces to the integer $(u-a)(v-a)+e$, and $|u|,|v|,|a| \lt 216$ while $p \asymp M_0$; the line divides the member only if that small integer is exactly zero. Excluding the cell's own factors, this needs $|u-a| \cdot |v-a| = 2$, hence $|u-v| \in \lbrace 1,3\rbrace$. **But $u$ and $v$ are the offsets $6i+d$ with $d \in \lbrace 2,4,8,10\rbrace$, so $|u-v|$ is even, and the collision is impossible.** The check finds none, for the $28$ lines or for any $M_0+b$ with $b \le 216$. The timing of the lines carries no information the residues did not already carry, and the escapee's survival is equivalent to the simultaneous primality of its $59$ irreducible polynomials — precisely the setting of Schinzel's Hypothesis H [10], which predicts infinitely many $t$ realising it. **Proving the configuration impossible would mean contradicting that prediction for a specific family, which is not a weakening of the twin problem but an apparent strengthening of it.**

### 2.4 Blocks of consecutive periods, and why lengthening the block does not help

Section 2.3 fixes the ceiling at a single period. Lengthening the window to a block of $L$ consecutive periods raises the budget to $B_L$, and one may hope that the budget grows more slowly than the block, so that a long enough block forces a twin. It does not help: **Proposition 2** gives the sieve dimensions of the five exception types and the resulting order $B_L \ll L/\log^2 L$, which is exactly the order the twin count itself has, so the two grow together and no length of block separates them. The measured budgets $B_3 = 67$, $B_5 = 100$, $B_7 = 138$, $B_9 = 163$ are consistent with that order.

*The full account, with the block scan and the dimension computation, is in Appendix B.1.*

---

### 2.5 Theorem 2: a new line kills at most one pair in its own first window

The sector $[p^2,(p+2)^2)$ is where the line $L_p$ is born. Index gap-2 pairs by their offset from the centre $C = (p+1)^2$, writing $P(j) = (C+2j-1,\ C+2j+1)$ with $-p \le j \le p$, so the window holds exactly $2p+1$ pair slots. Let $T_p^-$ count the surviving pairs before $L_p$ is switched on, $T_p^+$ after, and $D_p = T_p^- - T_p^+$.

$L_p$ has exactly three strikes in this window: $p^2$, $p(p+2)$ and $p(p+4)$, since $p(p+6) \gt  (p+2)^2$.

> **Theorem 2.** $D_p \in \lbrace 0,1\rbrace$ for every prime $p \gt  3$.

*Proof.* Three strikes, and each is disposed of by the grid $L_3$.

1. **$p^2$.** Of the two pairs it meets, only $(p^2, p^2+2)$ lies in the window — the other has index $-p-1$. For $p\gt 3$, $p^2 \equiv 1 \pmod 3$, so $p^2+2 \equiv 0$: **that pair is already dead.**
2. **The strike divisible by $3$.** One of $p+2, p+4$ is $\equiv 3 \pmod 6$, so one of $p(p+2), p(p+4)$ lies on $L_3$ and was struck before $L_p$ existed; both pairs it meets were already dead.
3. **The surviving strike.** Call it
$$H_p = \begin{cases} p(p+2), & p \equiv 5 \pmod 6,\cr p(p+4), & p \equiv 1 \pmod 6.\end{cases}$$
   In either case $H_p \equiv 5 \pmod 6$, so $H_p - 2 \equiv 3 \pmod 6$ and the pair $(H_p-2, H_p)$ is **also already dead.**

Only $(H_p, H_p+2)$ remains. $\blacksquare$

> **Corollary 2.** $D_p = 1$ if and only if **two** primality conditions hold together:
> $\displaystyle p \equiv 5 \ (6): \qquad p+2 \ \text{prime} \quad\text{and}\quad p(p+2)+2 \ \text{prime};$
> $\displaystyle p \equiv 1 \ (6): \qquad p+4 \ \text{prime} \quad\text{and}\quad p(p+4)+2 \ \text{prime}.$

*Proof.* The cell $H_p$ survives the older lines exactly when its cofactor,
$$p+2 \quad\text{or}\quad p+4,$$
has no prime factor below $p$; being less than $2p$, that means the cofactor is prime. And $H_p+2 \lt  (p+2)^2$ is not divisible by $p$, so if composite its least prime factor is below $p$ and it was struck earlier; hence $H_p+2$ survives iff it is prime. $\blacksquare$

*Verification.* Corollary 2 predicts $D_p$ from two primality tests alone; checked against the directly computed $D_p$ for every prime $5 \le p \lt  4000$, with **zero mismatches**. Examples: $p=5$ gives $7$ and $37$ both prime, so $D_5=1$; $p=11$ gives $13$ prime but $145 = 5\cdot29$ composite, so $D_{11}=0$; $p=13$ gives $17$ and $223$ both prime, so $D_{13}=1$.

**What this does and does not buy.** Since $T_p^+ = T_p^- - D_p$ and every survivor in the window is prime (the cofactor argument of [P7, §2.2]), $T_p^+$ *is* the number of twin pairs in $[p^2,(p+2)^2)$. Theorem 2 therefore says:

$$\boxed{ T_p^- \ \text{is the twin count of the window, up to an error of } 0 \text{ or } 1, \text{ and the error is characterised.} }$$

That is the strongest local statement in this paper, and it is worth being explicit that it is not a reduction. $T_p^-$ and $T_p^+$ differ by at most one, so proving anything about $T_p^-$ is proving it about the twin count. In particular the sufficient condition "$T_p^- \ge 2$" is *stronger* than the conclusion "$T_p^+ \ge 1$", not weaker. What Corollary 2 adds is that even the discrepancy between the two is governed by a twin-like coincidence — two simultaneous primality conditions — so the error term is of the same nature as the quantity.

### 2.6 Theorem 3: the bridge pair, and the only law that knows about squares

Index gap-2 pairs by $x$ as above but on an absolute scale, the pair being $(2x+1, 2x+3)$. The window for odd $m$ begins at $a_m = (m^2-1)/2$ and holds $2m+1$ slots, while $a_{m+2} - a_m = 2m+2$. **So consecutive square windows do not abut: exactly one pair slot falls between them,**
$$g_m  =  a_m + 2m + 1, \qquad \text{the pair } \big((m+2)^2-2,\ (m+2)^2\big),$$
whose upper member is the next square itself. The line is partitioned as window, bridge, window, bridge, …, with no slack and no overlap.

Let $B$ count the bridges surviving a line set, over a full cycle of roots.

> **Theorem 3.** $B' = \big(q - 2 - \chi_q(2)\big) B$, where $\chi_q(2)$ is the Legendre symbol: $+1$ for $q \equiv \pm1 \pmod 8$ and $-1$ for $q \equiv \pm3 \pmod 8$.

*Proof.* The bridge at root $r$ dies under $q$ when $q \mid r^2$, i.e. $r \equiv 0$ — one class — or when $r^2 \equiv 2 \pmod q$, which has $1+\chi_q(2)$ solutions. The two conditions are disjoint for $q\gt 2$, so $2+\chi_q(2)$ classes are lost. $\blacksquare$

*Verification.* $B = 2,\ 8,\ 32,\ 320,\ 3840,\ 53760,\ 967680$ for the line sets up to $3, 5, 7, 11, 13, 17, 19$, against $T = 1,\ 3,\ 15,\ 135,\ 1485,\ 22275,\ 378675$. Brute-forced from the definition for $\lbrace 3\rbrace$, $\lbrace 3,5\rbrace$, $\lbrace 3,5,7\rbrace$, $\lbrace 3,5,7,11\rbrace$: exact.

So the cycle fingerprint is not three numbers but four, with four distinct degrees:
$$(M, S, T, B)  \longmapsto  \big(qM,\ (q-1)S,\ (q-2)T,\ (q-2-\chi_q(2))B\big).$$
**$B$ is the only one of the four that knows the window is anchored at a square**, and the arithmetic that enters is whether $2$ is a quadratic residue.

> **Theorem 4 (the summation identity).** Over $M$ consecutive square windows,
> $\displaystyle \sum_{i=0}^{M-1} T_{m+2i}  =  2(m+M) T  -  B .$

*Proof.* The $M$ windows together with their $M$ bridges tile a stretch of
$$a_{m+2M}-a_m  =  2M(m+M)$$
pair slots, that is exactly $2(m+M)$ complete cycles, holding $2(m+M)T$ surviving pairs. The $M$ bridge roots are $M$ consecutive odd numbers, and since $M$ is odd they cover every residue class modulo $M$ exactly once, so exactly $B$ of them survive. $\blacksquare$

*Verification.* Checked for $\lbrace 3,5\rbrace$ and $\lbrace 3,5,7\rbrace$ at $m = 9, 15, 101$ — six cases, all exact.

**The collective bias, quantified.** Against the density prediction $T (2m+2M-1)$ for the same total length, the windows hold exactly $T-B$ fewer pairs; measured sums of deviations $-1, -5, -17, -185$ for the four line sets, matching $T-B$ each time. Now
$$\frac{B}{T}  =  \prod_q \Big(1 - \frac{\chi_q(2)}{q-2}\Big),$$
which converges: measured $2.5554,\ 2.5517,\ 2.5614,\ 2.5615,\ 2.5622$ at $z = 19,\ 10^3,\ 10^4,\ 10^5,\ 10^6$. The reduced product $\prod(1-\chi_q(2)/q)$ reaches $1.604401$ at $z = 10^6$ against
$$\frac{1}{L(1,\chi_8)} = 1.604556, \qquad L(1,\chi_8) = \frac{\log(1+\sqrt2)}{\sqrt2} = 0.623225 .$$
**So the square geometry enters this framework through a Dirichlet $L$-value at $1$ for the character modulo $8$.**

And the bias, though real, is not usable: $T-B \approx -1.56 T$ is a fixed number independent of $m$, spread over $M$ windows, so the deficit per window is $O(T/M)$ and vanishes against the per-window average as $M$ grows.

### 2.7 The square-phase mean, and the end of the "poor window" question

One may ask whether a window anchored at a square is systematically poorer than a window placed anywhere. The answer is an identity rather than an experiment: the average over all square phases has the exact closed form (3.3), and on the tested range it tracks the generic density prediction to within about $1$% from $p = 29$ onward. So the anchoring at a square carries no penalty at the level of the mean, and the "poor window" question closes.

*The derivation and the comparison table are in Appendix B.2.*

---

### 2.8 Two constructions that do not help, recorded so they are not retried

Two natural constructions were tried and neither adds anything: a window balanced so that every line strikes it equally often, and an attempt to read ownership through the cofactor rather than through the smallest factor. Both are exact, both reduce to statements already in the framework, and both are recorded so that they are not attempted again in another notation.

*The two constructions and the measurements that close them are in Appendix B.3.*

---

### 2.9 Proposition 1: a proved lower bound on $C_M$, and the order at which it becomes exact

Every count of $C_M$ in this paper so far has been a direct enumeration. This subsection gives the first *proved* lower bound on it, by importing a classical inequality and observing where it terminates.

Fix a sector and write $W$ for its set of cells, $N = |W| = 2M+6$. For each line $p \le M$ let $B_p \subseteq W$ be the cells it closes — two residue classes modulo $p$, by [P2, Thm 3]. For a cell $d$ put
$$m(d)  =  \lvert\lbrace p \le M : d \in B_p \rbrace\rvert,$$
the number of lines striking it, and define
$$S_0 = N, \qquad S_i  =  \sum_{d \in W} \binom{m(d)}{i} \quad (i \ge 1). \qquad\text{(3.5)}$$
The right-hand side of (3.5) is the count of $i$-fold intersections $\lvert \bigcap_{p \in J} B_p \rvert$ summed over all $i$-subsets $J$, each cell contributing once for every $i$-subset of the lines that strike it. Written this way the whole hierarchy is computed in a **single pass over the cells**, at cost $O(N \log\log M)$, rather than by enumerating $\binom{\pi(M)}{i}$ intersections.

> **Proposition 1.** With the notation above, for every $\ell \ge 0$
> $\displaystyle C_M  \ge  S_0 - S_1 + S_2 - \cdots - S_{2\ell+1}, \qquad\text{(3.6)}$
> and the alternating sum is **exactly** $C_M$ as soon as the truncation order reaches $\max_{d} m(d)$.

*Proof.* A cell struck by exactly $m$ lines contributes
$$\sum_{i=0}^{L}(-1)^i\binom{m}{i}$$
to the truncated sum. For $m = 0$ that is $1$. For $m \ge 1$ and $L \lt m$ the partial alternating binomial sum equals $(-1)^L\binom{m-1}{L}$, which is $\le 0$ when $L$ is odd; hence every struck cell contributes at most $0$ and every open cell exactly $1$, giving (3.6). For $L \ge m \ge 1$ the sum is the complete alternating binomial sum $(1-1)^m = 0$, so once $L \ge \max_d m(d)$ every struck cell contributes $0$ and every open cell $1$, and the total is $C_M$ exactly. $\blacksquare$

The inequality itself is the odd Bonferroni truncation and is classical; the multiplicity form (3.5) and the observation that it terminates at $\max_d m(d)$ are what make it usable here. The same evaluation appears independently in Nguyen [9], in the Goldbach setting of symmetric pairs about a multiple of a primorial — see §2.10.

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

**Why the order needed grows so slowly.** By Proposition 1 the hierarchy terminates at $\max_d m(d)$, and the mean of $m(d)$ over the sector is $\sum_{p \le M} 2/p \approx 2\log\log M$ — about $4.1$ at $M = 10^6$. The maximum over $2M+6$ cells therefore grows like $\log\log M$ as well, and measurement confirms it:

| $M$ | $10^3$ | $5\cdot10^3$ | $10^4$ | $5\cdot10^4$ | $10^5$ | $2\cdot10^5$ | $5\cdot10^5$ | $10^6$ |
|--------------------------|------|------|------|------|------|------|------|------|
| $\max_d m(d)$ | 9 | 9 | 10 | 11 | 11 | 12 | 13 | 13 |
| least odd $j$ with $L_j \gt 0$ | 7 | 7 | 9 | 9 | 9 | 9 | 9 | 11 |

**Across three orders of magnitude in $M$ the order required rises only from seven to eleven** — against $\pi(M) = 78{,}498$ lines at the top of that range. So the natural reading of "one would have to take every order" as "one would have to take $\pi(M)$ orders" is wrong by four orders of magnitude, and the exact point is reached at a quantity that (3.5) already computes for free.

**And what this does not buy, stated plainly.** The bound is proved and the order is small; the *number of terms* is not. Turning (3.6) into a theorem about all $M$ requires asymptotic control of $S_1, \dots, S_j$ for $j \asymp \log\log M$, and $S_j$ is a sum over $j$-tuples of primes of the same shape that makes $S_1$ diverge. The hierarchy therefore moves the difficulty from "the union bound is negative" to "a uniform estimate is needed for sums of order $\log\log M$" — a shorter distance, and the same kind of distance. It is recorded here as an exact computational tool and as a sharper statement of where the estimate is missing, not as a route.

### 2.10 The same obstruction from the Goldbach side

The finite-window difficulty this section keeps returning to — a full CRT period has positive density, but the interval belonging to one centre is a *translated fragment* of that period — was reached independently, and stated in almost the same words, by Nguyen [9]. The setting there is Goldbach rather than twins: symmetric pairs $\lbrace C-d, C+d\rbrace$ about a centre $C$ that is a multiple of a primorial, so the pairs have fixed **sum** where ours have fixed **difference**, and the window is anchored at a multiple of a primorial where ours is anchored at a square. Under that translation the two frameworks correspond term by term: the two forbidden cell classes $\pm 6^{-1} \pmod p$ of [P2, Thm 3] are the one or two forbidden lift residues there; $C_M$ corresponds to the survivor sets there; and the survivor density $\prod(1-2/q)$ is the same product.

**One point in that dictionary needs care, and Nguyen raised it.** His $U(C)$ is deliberately *conservative*: it is the set of offsets avoiding every obstruction congruence, whereas the actual terminal set $T(C)$ also contains the **endpoint-prime exceptions** — offsets whose divisible endpoint is the prime $q$ itself, so that nothing is destroyed. In general $U(C) \subsetneq T(C)$, and his own example at $C = 30$ has the offset $23$ giving the surviving pair $\lbrace 7,53\rbrace$ while $19$ gives the genuinely destroyed endpoint $49 = 7^2$.

On this side the two coincide, and for a reason worth stating: **the window sits above $M^2$ while every line is at most $M$**, so an endpoint equal to a sieving prime is impossible — a member of a cell in $(M^2,(M+6)^2)$ exceeds $M^2 \ge p^2 \gt p$ for every $p \le M$. There are therefore no endpoint-prime exceptions here, and $C_M$ equals both $|U|$ and $|T|$ in his letters. The equality is a consequence of anchoring at a square, not of the definitions, and a framework whose window sat elsewhere would have to distinguish them.

Two things are worth recording. First, the correspondence is evidence rather than coincidence: two constructions built for different problems, with no contact between them, isolate the same difficulty and label it the central one. Second, the tools are complementary — the Bonferroni evaluation of §2.9 is imported from there, while the measurement of $\max_d m(d)$ and the covering control of [P9, §3.5] were not made there and bear on its open problems. Nguyen has confirmed in correspondence that $S_j = 0$ for $j \gt \max_d m(d)$ in his notation too, so the effective depth of the inclusion–exclusion is that maximum rather than the number of sieving primes; whether it also grows like $\log\log$ on the primorial wheel is open. Nguyen claims no Goldbach theorem and no new infinite family, and says so repeatedly; the reference is to contemporaneous independent work, not to a settled result.

---

### 2.11 Smoothing the window, and where it does not reach

A sharp window pays a boundary error of order $1$ per residue class, and replacing it by a Fejér kernel removes most of that error. Three exact statements are proved for this: a mirror law for the sector index (Proposition 3), an exact discrepancy formula for the Fejér window whose corollary is the classical bound $d/(4H)$ (Proposition 4), and a bound $\ll d^3/(HT^2)$ for a window that also moves (Proposition 5). The kernels, the order, the pointwise estimate and the $\csc^4$ sum are all classical and are cited as such; the exact discrepancy formula is the part we have not found stated anywhere.

The smoothing gains a factor of about nine on $L_7$ at $M = 50{,}001$ and does not change its sign. **On our reading it does not reach the part that decides the answer:** the share of $S_i$ carried by moduli below the window scale is $90$%, $45$%, $9$%, $0.2$% and $0$% for $i = 1,\dots,5$, so it controls the term that had already died at $M = 21$ and none of the terms that fix the sign.

*The three propositions with their proofs, the measured tables, and a further route closed by an equivalence with Jacobsthal's function, are in Appendix B.4.*

---

## 3. What this paper establishes, and what it does not

**Proved in this paper.**

- The six exception positions (Theorem 1), the dichotomy that three of them can be open only when $(M+2,M+4)$ is itself a twin (Corollary 1), and the fact that no line above $31$ closes two of them unless it divides $M+8$ (Corollary 1b).
- The ladder in the width of the window and the square-endpoint sharpening — Corollaries 1a, 1c, 1d, 1e, Appendix A.3.
- The exception budget of $31$ over a full period, and the proof that no finite set of lines lowers it — §2.3.
- The block budgets $B_3 = 67$ and $B_5 = 100$, the sieve dimensions of the five exception types, and the resulting order $B_L \ll L/\log^2 L$ — Proposition 2, §2.4.
- The single-kill bound in a line's own first window and its characterisation — Theorem 2, Corollary 2.
- The bridge law and the summation identity over a cycle of windows — Theorems 3, 4.
- The odd Bonferroni lower bound on $C_M$, its multiplicity evaluation, and its termination at $\max_d m(d)$ — Proposition 1, §2.9.
- The mirror law for the sector index, the exact Fejér discrepancy formula, and the moving-window bound, with the certificate that smoothing preserves the target — Propositions 3, 4, 5, §2.11. The kernels, the pointwise estimate and the $\csc^4$ sum are classical and are cited as such.

**Exact results in the companion construction papers, used here.**

- The gap alphabet and the ladder of proofs — [P5, Thms 1–3, Cor 1].
- The shift law, primality as a zero-test, the primality of surviving cofactors, and the originality law on a row — [P7, Thm 1, Cor 1, Thms 2, 3].
- The sector inheritance and single-line capacity laws — [P7, Thms 4, 5, Cor 3] — with the two synchronisation propositions [P7, Props 1, 2].
- The exact minimum cover with its propagation and compression laws — [P7, Thms B1–B3, Cor B1]. **Its object is a prime pair $(p,p+6)$, not a twin pair.**
- The belt size and the layer ceiling — [P8, Thm 1, Prop 1].
- The depth ladder in the short window, the shell's single overlap count and its one-bit handover — [P8, Prop 1b, Cor 1, Props 1c, 1d, §§3.1–3.2].
- The character conditions on the four outer tracks, the nine-element simultaneity set, and the construction showing it obstructs nothing — [P8, Thms 3, 4, Prop 2].

**Verified but not proved.** [P8, Verified Law 2] (the reach $\lfloor 2g/3\rfloor$), proved under $g^2 \lt 2q$ — a hypothesis weaker than Cramér but stronger than the Riemann hypothesis supplies; checked on $17{,}981$ belts with $q \lt 200{,}000$ without failure.

**Measured, and labelled as such where they occur.** Each item below is a computation over a stated finite range and supports a claim about that range only.

- The agreement of $C_M$ with the Hardy–Littlewood prediction to about $2$%, and the two phase controls that go with it — §2.1.
- The frequencies of the three gap letters — [P5, §2.1].
- The block values $B_7 = 138$ and $B_9 = 163$, and the values quoted for $L = 21, 51, 101$ — §2.4. These were computed with pruning and are stable across twelve and eight consecutive primes respectively; **they should be read as lower bounds with strong stability, not as certified maxima.**
- The numerical agreement of the square-phase mean with the generic density — §2.7 — and the two constructions of §2.8.
- The collapse of the new line's effect in a belt ([P8, §2.3]) and the layer-ceiling ratios ([P8, §2.5]).
- The track densities against Bateman–Horn, and the count of windows in which the four tracks are closed — [P8, §3.3] — together with the two synchronisation measurements of [P7, Props 1, 2].
- The growth of $\max_d m(d)$ and of the least sufficient Bonferroni order, tabulated in §2.9. The inequality there is proved; the growth rate is measured.
- The gains from smoothing, the share of each $S_i$ below the threshold $d \lt r$, and the least admissible half-width against the largest gap, tabulated in §2.11. The bounds there are proved; the tables are measured.

**Where the supporting material is.** The counting details and the ladder in the width of the window are in Appendix A, the last of them (A.3) carrying Corollaries 1a to 1e and the census to $M = 10^9$. Four accounts that were in the body of §2 are now in Appendix B: the block budgets (B.1), the square-phase mean (B.2), the two constructions that do not help (B.3), and the smoothing bounds with the mass they do not reach (B.4). Each has a stub in §2 stating its conclusion and its status.

**Covered by the verification scripts.** `verify_exception_dichotomy.py` covers the closed forms of the six positions, the $\lbrace 5,7\rbrace$ table, Corollary 1, the whole of the period budget of §2.3 (the per-phase caps $5\cdot0+20\cdot1+10\cdot2 = 40$, the coupling to $37$, the ceiling $31$ over all $2431$ alignments, the nine that attain it, and the partner quadratics), and Step 1 of Proposition 2 over all $423$ primes below $3000$. `verify_bonferroni_depth.py` covers Proposition 1 — the geometry of §§2.9 and [P2, §4.5], the exception positions of Theorem 1 over every sector below $M = 2500$, the exactness of the alternating sum at order $\max_d m(d)$, and the published values. `verify_first_appearance.py` covers the bad-phase sweep and its least representative. `verify_new_additions.py` covers the exact phase set of [P2, Cor 1] over 428 primes, the diamond-centre corollary over 6,320 pairs, the coincidence gap of [P2, Cor 3], the third channel and pair count of [P3, Cor 1–2], and the two constructions of §2.8 — the rotation of the balanced word over 20 windows and the clean-owner theorem.

**Not here.** Every one of the statements above is an *exact* statement — an identity, a cap, or an explicit list. None is a lower bound, and a lower bound is what the twin conjecture needs. Each of the criteria above turns out, on inspection, to require a lower bound on a quantity that exceeds the twin count of a sector by at most a constant; the criteria are therefore exact reformulations rather than routes.

The measurements that establish that, the four tests against which the framework was checked, and the account of where and why it stops, are **Papers 9 to 11**.

---

*The computations and much of the prose in this paper were prepared with AI assistance (ChatGPT, OpenAI; Claude, Anthropic), used for algebraic derivation, for drafting and rewriting code and text, for running the computations, and for auditing the papers against their own scripts. All statements were checked by the author, who is responsible for them; the repository README sets out the division of labour in full.*
---

---

## Appendix A — Counting details for §2

The two computations below are used in §2 and quoted there. They are routine and are collected here so that §2 is not interrupted by them.

### A.1 Raw cell count and main term

$$C = \frac{v^2-u^2}{6}-1, \qquad C_- = 4n-1  (u=6n-1), \qquad C_+ = 8n+3  (u=6n+1),$$
and $C \equiv 3 \pmod 4$ always (zero failures over 427 consecutive prime pairs) — an exact property which nevertheless supplies no protective invariant, since a single line's deletion count has no fixed parity. The main term is $M = C P_2$.

### A.2 Local deviations

$$\varepsilon_r(u) = D_r(u) - \frac{2 N_{r^-}(u)}{r}.$$

Inside a sector, line $r$ deletes at $s \equiv -u^2/6$ and $s \equiv (2-u^2)/6 \pmod r$, and the gap between the two positions is exactly $3^{-1} \bmod r$ (zero failures among 85). **Every ruler's phase is therefore a function of the single quantity $u^2$**, and under $u \mapsto u+6$ the phase moves *quadratically*, since $u^2 \mapsto u^2 + 12u + 36$. This quadratic motion is what makes cancellation possible at all.

---

### A.3 The ladder in the width of the window, and the square-endpoint sharpening

The four results below sharpen Corollary 1 without strengthening it, and the census that goes with them is the largest computation in this paper. They were in the body of §2.2 in an earlier version; they are collected here so that §2.2 reads as Theorem 1, the criterion, and the dichotomy.

**The six are the first rung of a ladder in the width of the window.** Nothing in the argument requires the window to reach only to $(M+6)^2$. Widen it to $W_{M,k} = (M^2, (M+6k)^2)$, keeping the lines at $p \le M$.

> **Corollary 1a (the $k$-ladder).** Let $M \equiv 3 \pmod 6$ and $k \ge 1$ satisfy $M \gt  (6k)^2$, and switch on every line $p \le M$. Then every composite endpoint of an open cell of $W_{M,k}$ is a product $(M+a)(M+b)$ of two primes with $a \le b$ even, not divisible by $3$, and
> $\displaystyle a+b \le 12k;$
> the number of such positions is
> $\displaystyle K_k  =  4k + (4k-2) + \cdots + 2  =  2k(2k+1).$
> Moreover **no open cell of $W_{M,k}$ has both endpoints composite**, so every exception is a $P_2$ with both factors above $M$ sitting beside a genuine prime, and
> $\displaystyle T_{M,k}  =  C_{M,k} - X_{M,k}, \qquad X_{M,k} \le 2k(2k+1).$

*Proof.* A survivor has every prime factor above $M$, so a composite one has exactly two: three would exceed $M^3 \gt  (M+6k)^2$. Coprimality to $6$ forces both offsets even and prime to $3$.

For the range of the offsets, expand $n = M^2 + M(a+b) + ab$. If $a+b \le 12k$ then $ab \le \big(\tfrac{a+b}{2}\big)^2 \le (6k)^2$, with equality only at $a = b = 6k$, which is divisible by $3$ and so excluded; hence $ab \lt  36k^2$ and $n \lt  (M+6k)^2$. Conversely $a+b$ is even, so if $a+b \gt  12k$ then $a+b \ge 12k+2$ and
$$n - (M+6k)^2  =  M\big(a+b-12k\big) + ab - 36k^2  \ge  2M - 36k^2  \gt  M  \gt  0$$
by the hypothesis $M \gt  36k^2$. So membership of the window is *equivalent* to $a+b \le 12k$. Counting: $a$ runs over the even non-multiples of $3$ in $[1, 6k-2]$, and for each the admissible $b \ge a$ with $b \le 12k-a$ number $4k, 4k-2, \dots, 2$ in turn, giving $K_k = 2k(2k+1)$.

For the last claim, let $n = (M+a)(M+b)$ and $n' = (M+c)(M+d)$ be two such products. Then
$$n' - n  =  M\big((c+d)-(a+b)\big) + (cd - ab).$$
If $c+d = a+b$ the difference is $cd-ab$, divisible by $4$ since all four offsets are even, hence never $2$. If $c+d \ne a+b$ the first term has absolute value at least $2M$ while $|cd-ab| \lt  36k^2 \lt  M$, so $|n'-n| \gt  M \gt  2$. Two composite survivors therefore never sit in the same cell. $\blacksquare$

*Verification.* At $k=1$ the six pairs are $(2,2), (2,4), (2,8), (2,10), (4,4), (4,8)$ — exactly $E_M$. The counts $K_k = 6, 20, 42, 72, 110, 156, 210, 272$ were checked against the definition for $k \le 8$. Over every $M \equiv 3 \pmod 6$ below $1400$ with $M \gt  36k^2$ and $k \le 5$ — $689$ windows — every exception matched the description and **no open cell had both endpoints composite**; the largest $X_{M,k}$ observed was $2$ at $k=1$ against the ceiling $6$, and $6$ at $k=3$ against $42$.

*The hypothesis is load-bearing.* Dropping $M \gt  36k^2$ and running the same range produces both failures at once: open cells with two composite endpoints ($1$ at $k=2$, $7$ at $k=3$, $15$ at $k=5$) and exceptions outside the description ($3$, $13$ and $30$ respectively). The condition is stronger than necessary — Theorem 1 itself needs none at $k=1$ — but it is what makes the short argument above go through.

*And widening does not help.* The ceiling grows like $4k^2$ while the number of open cells grows only like $2kM/\log^2 M$, so the margin $C_{M,k} - K_k$ scales as $M/\big((2k+1)\log^2 M\big)$: linearly worse in $k$. **The case $k = 1$ already in Theorem 1 is the best one**, and the ladder is a completion of the description rather than a step toward forcing a survivor. The missing ingredient is unchanged: a lower bound on $C_{M,k}$.

**Which old lines can close two of the six at once.** Label the six cells by their composite member: $A = (M+2)^2$, $B = (M+2)(M+4)$, $C = (M+4)^2$, $D = (M+2)(M+8)$, $E = (M+2)(M+10)$ and $F = (M+4)(M+8)$. An old line $r$ closes a cell when it divides either of its two members. Then:

> **Corollary 1b.** Suppose $M+2$ and $M+4$ are both prime, so that all six cells exist. For $r \gt 31$, a line closes at most one of the six, with the single exception that $r \mid M+8$ closes $D$ and $F$ together.

*Proof.* Write $p = M+2$, so that $M+4 = p+2$, $M+8 = p+6$ and $M+10 = p+8$. Since $M \equiv 3 \pmod 6$, the partner of each composite is fixed by its residue: the six cells are $(A, A-2)$, $(B, B+2)$, $(C, C-2)$, $(D, D-2)$, $(E, E+2)$, $(F, F+2)$, and in terms of $p$ the six partners are
$$Q_A = p^2-2,\quad Q_B = p^2+2p+2,\quad Q_C = p^2+4p+2,$$
$$Q_D = p^2+6p-2,\quad Q_E = p^2+8p+2,\quad Q_F = p^2+8p+14 .$$

*Closures through the composite member.* A line $r \le M$ is smaller than both $p$ and $p+2$, so $r$ divides none of $A = p^2$, $B = p(p+2)$, $C = (p+2)^2$ except through $M+8$ or $M+10$. Hence $r \mid M+8$ closes $D$ and $F$, and $r \mid M+10$ closes $E$; and $r$ cannot divide both $M+8$ and $M+10$, whose difference is $2$.

*Two partners.* If $r$ divides $Q_X$ and $Q_Y$ it divides their difference. Nine of the fifteen differences are $2p$, $6p$, $2q$, $6q$, $8q$ or $12$ with $q = p+2$, and each forces $r \in \lbrace 2,3\rbrace$ or $r \in \lbrace p,q\rbrace$, all excluded. The remaining six are settled by substituting the resulting congruence back into one of the two partners:

| pair | $r$ divides | substitution | conclusion |
|------|------|------|------|
| $A,C$ | $p+1$ | $Q_A \equiv 1-2$ | $r \mid 1$ |
| $A,E$ | $2p+1$ | $4Q_A \equiv 1-8$ | $r \mid 7$ |
| $B,D$ | $p-1$ | $Q_B \equiv 1+2+2$ | $r \mid 5$ |
| $C,D$ | $p-2$ | $Q_C \equiv 4+8+2$ | $r \mid 14$ |
| $C,F$ | $p+3$ | $Q_C \equiv 9-12+2$ | $r \mid 1$ |
| $D,F$ | $p+8$ | $Q_D \equiv 64-48-2$ | $r \mid 14$ |

*One composite and one partner.* If $r \mid M+8$ then $p \equiv -6$, and the six partners reduce to $34, 26, 14, -2, -10, 2$ modulo $r$, so no partner is divisible by $r$ beyond $D$ and $F$ themselves. If $r \mid M+10$ then $p \equiv -8$ and the partners reduce to $62, 50, 34, 14, 0, 14$; the largest new modulus is $62 = 2\cdot 31$, which is where the constant comes from. $\blacksquare$

*The constant is sharp.* The bound $r \gt 31$ cannot be lowered: $r = 31$ closes $A$ and $E$ together whenever $31 \mid M+10$ and $31 \mid (M+2)^2-2$, which happens in $128$ of the twin sectors below $M = 400{,}000$, the first at $M = 1695$.

*Verification.* Zero violations over all $3{,}802$ sectors below $M = 400{,}000$ in which $M+2$ and $M+4$ are both prime, so that all six cells exist. In those sectors the only multiple closure by a line above $31$ is $\lbrace D,F\rbrace$, occurring $4{,}060$ times; below $31$ every combination appears, the commonest being $\lbrace D,E,F\rbrace$, $\lbrace B,D\rbrace$, $\lbrace B,E\rbrace$ and $\lbrace D,F\rbrace$.

So the large lines cannot gather the exceptions: **collective covering of the six is the small lines' work.** This does not obstruct the covering, and the reason is worth stating so it is not attempted: at $M = 195$, where $197$ and $199$ are both prime and all six cells exist, three lines suffice — $151$ closes $A$, $5$ closes $B$ and $E$, and $7$ closes $C$, $D$ and $F$. Restricting to lines above $31$ still leaves the six closable, by five of them.

**A symmetric window in which one survivor suffices.** The sector can be replaced by the window between the squares of a twin-shaped pair. Put $P = 6r-1$ and $Q = 6r+1$ and take
$$J_r = (P^2,\ Q^2),$$
which contains exactly $N = 4r-1$ complete cells $(6b-1, 6b+1)$ and is centred on $PQ+1 = (6r)^2$ — verified for every $r \lt 3000$. Switch on every prime line $\ell \lt P$. A composite below $Q^2$ has a prime factor below $P$ with the single exception of $PQ$ itself, so:

> **Corollary 1c.** In $J_r$, a surviving cell other than the central one is a twin pair; and if the **central** cell $(PQ, PQ+2)$ survives, then $P$ and $Q$ are both prime, so $(P,Q)$ is a twin pair. **One survivor of any kind suffices.**

*Verification.* Over $r \lt 400$: $12{,}242$ survivors, every one of them a twin by the appropriate clause, no exceptions. Over the first $1000$ windows there is no window without a survivor and the minimum survivor count is $2$.

This is sharper than the sector form, where Corollary 1 lowers the sufficient count to $C_M \ge 3$; here it is $1$. **The gain is in the statement, not in the difficulty:** what has to be shown is still that a set of lines fails to cover a set of cells, and the covering control of [P9, §3.5] applies unchanged.

*Two facts about the window, recorded because they narrow how a covering could be completed.* A line $p = 6k \mp 1$ can close two cells only at separations $\lbrace 2k,\ 4k-1\rbrace$ or $\lbrace 2k,\ 4k+1\rbrace$, so no line closes two adjacent cells. And a line $\ell \gt N$ that closes two cells not already closed does so with **prime** cofactors differing by $2$ or $4$ — the window has length $24r$ and $\ell \gt 4r-1$, forcing the cofactor gap below $6$, and both cofactors are coprime to $6$. Measured over the first $1000$ windows: $303$ such lines, $224$ at gap $2$ and $79$ at gap $4$, none otherwise and no composite cofactor.

*And why this does not become a route.* At $r = 1000$ the small lines leave $140$ cells open, the $233$ larger lines could close $466$ between them, and they close $18$ — all singletons, leaving $122$ survivors. The true count of open cells behaves like $r/\log^2 r$ and what the large lines close like $r/\log^3 r$, while the crude bound on their capacity is $4r/\log r$: **the separation is real and lies between two logarithms, where no counting bound reaches it.** Moving the split point from $X^{0.235}$ to $X^{0.49}$ does not make the crude bound smaller than the count of open cells at any depth.

**Removing the two square positions, and what is left.** Two of the six carry perfect squares, $A = (M+2)^2$ and $C = (M+4)^2$, and these are the only cells of the sector with a square endpoint: the squares between $M^2$ and $(M+6)^2$ are $(M+j)^2$ for $1 \le j \le 5$, and only $j = 2, 4$ give a member coprime to $6$. A twin has two prime members, so **discarding the cells with a square endpoint discards no twin.** Write $C_M^{\circ}$ for the number of open cells with neither member a perfect square.

> **Corollary 1d.** Suppose $(M+2, M+4)$ is not a twin pair. Then at most **one** of the four non-square positions $B, D, E, F$ is open, so
> $\displaystyle C_M^{\circ} \ge 2 \quad\Longrightarrow\quad \text{the sector contains a twin.}$
> Moreover the line $5$ alone settles two residue classes of $M$: if $M \equiv 21 \pmod{30}$ then none of $B, D, E, F$ is open, whatever $M+2$ and $M+4$ are, and if $M \equiv 27 \pmod{30}$ then only $B$ can be, so in both classes
> $\displaystyle C_M^{\circ} \ge 1 \quad\Longrightarrow\quad \text{the sector contains a twin, or } (M+2,M+4) \text{ is one.}$

*Proof.* By the grouping in Corollary 1, $B$ needs both $M+2$ and $M+4$ prime and so is closed under the hypothesis, while $D, E$ need $M+2$ prime and $F$ needs $M+4$ prime, so $F$ cannot be open together with $D$ or $E$. It remains to rule out $D$ and $E$ together. Write $p = M+2$. The cell of $D$ is $\big(p(p+6)-2,\ p(p+6)\big)$, whose members are $p(p+1)$ and $(p+2)(p-1)$ modulo $5$; both are non-zero only for $p \equiv 2 \pmod 5$. But then $5 \mid p+8$, so the composite member $p(p+8)$ of $E$ is closed by the line $5$.

For the two classes, the same computation for all four positions gives the pattern of survival modulo $5$: $B$ is open only at $p \equiv 4$, $D$ only at $p \equiv 2$, $E$ only at $p \equiv 1$, and $F$ only at $p \equiv 0, 1, 2$. Hence $p \equiv 3$ closes all four and $p \equiv 4$ leaves only $B$; with $p = M+2$ and $M \equiv 3 \pmod 6$ these are $M \equiv 21$ and $M \equiv 27 \pmod{30}$. $\blacksquare$

*Verification.* Over the same $3{,}332$ sectors: $D$ and $E$ are never open together; in the $2{,}992$ sectors whose root pair is not a twin the number of open non-square positions never exceeds $1$; in all $666$ sectors with $M \equiv 21 \pmod{30}$, root twin or not, it is $0$; and in the $666$ with $M \equiv 27 \pmod{30}$ it never exceeds $1$.

**The same census to $M = 10^9$.** Corollary 1a makes the test cheap. Since no two of the six candidate composites differ by $2$, the partner of an exception is never itself an exception, so for $M \gt  36$ a partner is rough exactly when it is prime; and a composite $(M+a)(M+b)$ is rough exactly when $M+a$ and $M+b$ are both prime. Openness is therefore decided by primality alone:
$$A: \ M{+}2, \ (M{+}2)^2{-}2; \qquad\qquad B: \ M{+}2, \ M{+}4, \ (M{+}2)(M{+}4){+}2;$$
$$C: \ M{+}4, \ (M{+}4)^2{-}2; \qquad\qquad D: \ M{+}2, \ M{+}8, \ (M{+}2)(M{+}8){-}2;$$
$$E: \ M{+}2, \ M{+}10, \ (M{+}2)(M{+}10){+}2; \qquad F: \ M{+}4, \ M{+}8, \ (M{+}4)(M{+}8){+}2 .$$
Over all $166{,}666{,}665$ sectors below $10^9$: **$D$ and $E$ are never open together; the number of open non-square positions in a sector whose root pair is not a twin never exceeds one; it is zero in every sector with $M \equiv 21 \pmod{30}$; and it is $\lbrace B\rbrace$ or nothing in every sector with $M \equiv 27 \pmod{30}$.** The counts by decade, with the two sifting dimensions read off the densities:

| decade of $M$ | sectors | $A$ | $C$ | $B$ | $D$ | $E$ | $F$ | sq. $\times \log^2$ | non-sq. $\times \log^3$ | ratio $\times \log$ |
|---|---|---|---|---|---|---|---|---|---|---|
| $10^4\text{--}10^5$ | $1.5\times10^4$ | $655$ | $681$ | $70$ | $46$ | $58$ | $148$ | $9.498$ | $23.658$ | $2.491$ |
| $10^5\text{--}10^6$ | $1.5\times10^5$ | $4{,}466$ | $4{,}487$ | $383$ | $289$ | $291$ | $738$ | $9.525$ | $22.843$ | $2.398$ |
| $10^6\text{--}10^7$ | $1.5\times10^6$ | $32{,}150$ | $32{,}216$ | $2{,}326$ | $1{,}741$ | $1{,}767$ | $4{,}931$ | $9.573$ | $23.940$ | $2.501$ |
| $10^7\text{--}10^8$ | $1.5\times10^7$ | $244{,}729$ | $243{,}890$ | $15{,}391$ | $11{,}176$ | $11{,}708$ | $32{,}167$ | $9.686$ | $24.095$ | $2.488$ |
| $10^8\text{--}10^9$ | $1.5\times10^8$ | $1{,}912{,}716$ | $1{,}910{,}857$ | $106{,}290$ | $76{,}561$ | $81{,}072$ | $222{,}588$ | $9.742$ | $24.249$ | $2.489$ |

The last three columns are the point. They give the density of the square family against $\log^2 M$, the density of the non-square family against $\log^3 M$, and the ratio of the two against $\log M$; since the square positions have dimension $2$ and the non-square ones dimension $3$, the first two should tend to constants and the third should be constant as well. All three do: the first settles near $9.7$ after climbing slowly, the second near $24.2$, and the third is $2.49$ across four consecutive decades, varying by under half a per cent. **The dimension count of Corollary 1e is therefore measured, not only derived.** In the last decade the non-square exceptions occupy $0.324$% of sectors, so a single open non-square cell forces a twin in $99.68$% of them.

One asymmetry inside the family is worth recording: $F$ is about twice as common as $B$ — the ratio is $2.09$ in the last decade and $2.12$ in the one before — although the two carry the same linear condition in strength, a prime pair at gap $4$ and at gap $2$ having the same singular series. The difference is entirely in the partner: the prime factors of $Q_B = (M+3)^2+1$ must be $1 \bmod 4$, those of $Q_F = (M+6)^2-2$ must be $\pm 1 \bmod 8$, and the two densities differ by that factor.

**How rare the non-square exceptions are, and in what sense this can be proved.** The four non-square positions are sifted in dimension **three**, not two. The composite member of each is a product of two linear forms in $M$ and so forbids two residues modulo every line $r$; the partner is an irreducible quadratic and forbids two more or none. Writing $\left(\tfrac{\cdot}{r}\right)$ for the Legendre symbol, the partners are
$$Q_B = (M+3)^2+1, \quad Q_D = (M+5)^2-11, \quad Q_E = (M+6)^2-14, \quad Q_F = (M+6)^2-2,$$
so the number of residues of $M$ that the line $r$ forbids is
$$3+\left(\tfrac{-1}{r}\right), \quad 3+\left(\tfrac{11}{r}\right), \quad 3+\left(\tfrac{14}{r}\right), \quad 3+\left(\tfrac{2}{r}\right)$$
respectively, each of mean $3$ since the characters are non-principal. This extends the computation of Appendix B.1, which gives dimension $2$ for $A, C$ and dimension $3$ for $D, E, F$, to the remaining position $B$.

Let $U(y)$ be the density of residue classes of $M$ in which at least one of $B, D, E, F$ survives every line $r \le y$. Then $U(y) \asymp (\log y)^{-3}$, and computing it exactly by inclusion–exclusion over the four positions gives

| lines up to $y$ | $23$ | $97$ | $199$ | $499$ | $997$ | $4{,}999$ | $19{,}997$ |
|---|---|---|---|---|---|---|---|
| classes free of all four | $79.57$% | $91.43$% | $94.41$% | $96.40$% | $97.32$% | $98.55$% | $99.07$% |
| $U(y)(\log y)^2$ | $2.01$ | $1.79$ | $1.57$ | $1.39$ | $1.28$ | $1.05$ | $0.91$ |
| $U(y)(\log y)^3$ | $6.30$ | $8.20$ | $8.29$ | $8.64$ | $8.84$ | $8.96$ | $9.02$ |

The third row settles the order: the second row falls throughout, the third steadies near $9$.

> **Corollary 1e.** The number of $M \le X$ with $M \equiv 3 \pmod 6$ whose sector carries an open non-square exception is $o(X)$.

*Proof.* Fix $y$. Every line $r \le y$ is active in a sector with $M \gt  y$, so an open non-square exception there survives all of them, and its residue class of $M$ lies in the exceptional set counted by $U(y)$. That set is a union of classes modulo a fixed modulus, so the density of such $M$ up to $X$ tends to at most $U(y)$ as $X \to \infty$. Letting $y \to \infty$ afterwards and using $U(y) \to 0$ gives the claim. $\blacksquare$

The order of the two limits matters: the modulus of the class decomposition grows with $y$, so one may not substitute $y = M$ and read off a rate. The statement gives vanishing density and no rate, and it says nothing about whether any particular sector has an open cell.

**A statement about the partners that the literature does supply.** Writing $M = 6t+3$, each of the six partners becomes a quadratic in $t$:

| type | partner as a quadratic in $t$ | discriminant |
|---|---|---|
| $A$ | $36t^2+60t+23$ | $288$ |
| $B$ | $36t^2+72t+37$ | $-144$ |
| $C$ | $36t^2+84t+47$ | $288$ |
| $D$ | $36t^2+96t+53$ | $1584$ |
| $E$ | $36t^2+108t+67$ | $2016$ |
| $F$ | $36t^2+108t+79$ | $288$ |

None of the discriminants is a perfect square, so all six are irreducible over $\mathbf{Z}$; the leading coefficient is positive; and none has a fixed prime divisor, since $36$ is divisible by $2$ and by $3$, leaving the constant term — odd and prime to $3$ in every row — while for $p \gt  3$ the reduction stays a genuine quadratic and so has at most two roots. (Checked directly for every prime up to $73$, and the greatest common divisor of the first sixty values is $1$ in each row.) Iwaniec [6] proves that an irreducible quadratic with positive leading coefficient and no fixed prime divisor takes values with at most two prime factors infinitely often, and Lemke Oliver [7] gives the form with the values also square-free. Hence:

> **Remark.** For each of the six types separately, there are infinitely many $t$ at which that partner is square-free with at most two prime factors.

Three limits should be read with it, and they are what keep this a remark. It is a statement about **each partner separately**: six infinite sets of $t$, which need not meet, whereas an open cell needs conditions at one and the same $t$. It does not separate "prime" from "product of two primes", which is the distinction an exception turns on. And it says nothing about the composite member, whose openness needs $M+a$ and $M+b$ both prime. It is a correct application of a published theorem to the objects of §2.2, and no more than that.

*This is a change of bookkeeping, not of strength.* At most two square cells are discarded, so $C_M^{\circ} \ge C_M - 2$ and the criterion still amounts to $T_M \ge C_M - 2$, which is Corollary 1. What it adds is that the loss is now located exactly — two square positions and one other — and that the proof needs no scan of residue classes. The gain in the two classes of the second clause is real, and it covers two fifths of all sectors.

**And what it does not buy.** $C_M$ exceeds the twin count of the sector by at most six. Any lower bound on $C_M$ is therefore a lower bound on twins, and (3.2) is an exact reformulation rather than a route. We record it because it is the sharpest form the framework has produced of the twin criterion, not because it weakens the problem.

## Appendix B — Routes that were tried and closed

Each of the four accounts below was in the body of §2 in an earlier version. They are collected here so that §2 reads as a sequence of results, and kept in full because a route closed by measurement or by proof is worth more written down than left to be attempted again. In each case the conclusion, and its status as proof or as measurement, is stated in the corresponding stub in §2.

### B.1 Blocks of consecutive periods, and why lengthening the block does not help

Section 2.3 bounds the exceptions over one period of $35$ sectors. Consecutive periods are coupled in the same way that consecutive sectors are, so the same question can be asked of a block of $L$ periods — $35L$ sectors — and the answer moves. Write $B_L$ for the maximum of $\sum_i |S_{M_i} \cap E_{M_i}|$ over such a block under the twinless hypothesis, so that $B_1 = 31$ is the content of §2.3 and

$$\sum_i C_{M_i} \gt  B_L \implies \text{a twin in the block}.$$

**How $B_L$ is computed, and a trap that is worth naming.** The natural procedure — enumerate the maximal configurations of each residue class and test each for a fixed prime divisor — is *not* sound for this purpose. A residue class whose maximum is $m$ also carries configurations of size $m-1$, $m-2$ and so on, obtained by deleting cells; deleting a cell removes conditions and can only make admissibility easier. Those sub-configurations are never enumerated, so "every configuration at level $\ell$ dies" establishes nothing about level $\ell$. The sound procedure reverses the order: fix a residue for each prime $q$, switch the line $q$ on *inside* the transfer recursion, and read off the maximum. That maximum is by construction the largest admissible configuration at those residues, and the maximisation over residues is $B_L$. It is also faster by orders of magnitude.

**Values.** By that procedure, maximising over the residues of every prime up to the stated bound:

$$B_1 = 31, \qquad B_3 = 67, \qquad B_5 = 100, \qquad B_7 = 138, \qquad B_9 = 163.$$

The first three are certain: $B_1$ is §2.3; $B_3$ and $B_5$ are stable under every prime tested and $B_5$ was obtained twice, once by the sound procedure and once by exhaustive enumeration with an independent admissibility test, which agree. $B_7$ and $B_9$ are stable across twelve and eight consecutive primes respectively but were computed with pruning, so they are lower bounds with strong stability rather than certified maxima.

The extremal configuration at $L=3$ carries $66$ linear and $67$ quadratic conditions — $133$ polynomials of total degree $200$ — and every prime $q \le 200$ leaves it an admissible residue, so §2.3's conclusion transfers: no finite set of lines lowers $67$ either. Two features of the optimum are worth recording. First, it does *not* preserve the single-window maximum in the middle: the three windows contribute $20, 26, 21$, so the block optimum spends $31 - 26 = 5$ of the central window's capacity to gain elsewhere. Second, the killing is concentrated: across every level from $144$ down to $138$ at $L = 7$, the primes $29$ and $37$ account for about ninety per cent of the eliminated configurations, the remainder falling to $43$, $53$, $71$, $73$, $79$ and $97$.

In requirement per sector, $(B_L+1)/35L$ reads $0.914$, $0.648$, $0.577$, $0.567$, $0.521$. It falls, and the next paragraph says why, and how far.

**The quadratic shadow, and the order of $B_L$.** Each exceptional cell carries, besides its linear primality conditions, the condition that the *other* member of the cell survive. Those partners are

$$Q_A = (M+2)^2-2, \quad Q_C = (M+4)^2-2, \quad Q_D = (M+5)^2-11, \quad Q_E = (M+6)^2-14, \quad Q_F = (M+6)^2-2,$$

so each type forbids, modulo a prime $q \gt  17$, a number of residue classes that is exactly

$$\omega_A = \omega_C = 2+\chi_2(q), \qquad \omega_D = 3+\chi_{11}(q), \qquad \omega_E = 3+\chi_{14}(q), \qquad \omega_F = 3+\chi_2(q),$$

with $\chi_d(q)$ the Legendre symbol. The linear conditions supply one forbidden class for $A$ and $C$ and two for $D$, $E$ and $F$; the partner supplies two more exactly when the relevant $d$ is a quadratic residue. Since the quadratic characters are non-principal, each $\omega$ has mean value $2$ for $A$ and $C$ and $3$ for $D$, $E$ and $F$.

*Propositions 2 to 5 below continue the numbering of the parent set; Propositions 2 to 5 belong to the sibling parts.*

> **Proposition 2.** Let a block of $N = 35L$ consecutive sectors carry an admissible configuration of exceptional cells under the twinless hypothesis, and for $X \in \lbrace A,C,D,E,F\rbrace$ let $I_X$ be the set of sector indices carrying a cell of type $X$. Then
> $\displaystyle |I_A|, |I_C| \ll \frac{N}{\log^2 N}, \qquad |I_D|, |I_E|, |I_F| \ll \frac{N}{\log^3 N},$
> and consequently
> $\displaystyle B_L \ll \frac{L}{\log^2 L}.$

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

**This is a computation, not a new tool, and it should be read as one.** Reading the sieve dimension off the number of roots of the defining polynomials modulo each prime is the standard definition of dimension — the condition $\sum_{q \lt  s}(\log q)/f(q) = \kappa\log s + O(1)$ of Halberstam and Richert [5] — and the passage from a dimension-$\kappa$ sifting density to an upper bound of order $N/(\log N)^{\kappa}$ is the standard Selberg estimate; see [2] for the higher-dimensional theory and [5] for the sieve itself. The twin problem in this language is the case $\rho(q) = 2$, dimension $2$. What is particular to the present setting is only the input: that the exceptional cells of Theorem 1 have the five partners above, so that the quadratic characters $\chi_2$, $\chi_{11}$ and $\chi_{14}$ appear and split the five types into dimensions $2,2,3,3,3$. The conclusion then follows by quoting the standard machinery, and we claim nothing for the machinery.

*Two remarks on the shape of this.* The bound is an **upper-bound sieve only**, and upper bounds in a fixed dimension are the direction in which sieve methods have no parity obstruction; nothing here bears on the lower-bound side. And the two-sector types are smaller than the one-sector types by a full logarithm, so in a long block almost every exception is of type $A$ or $C$ — a block that is longer is structurally *simpler*, not more complicated.

The first consequence is the one that matters here: **the density of exceptions tends to zero**, so the requirement per sector is not bounded below by any positive constant.

**And the bound is numerically empty over every computable range.** Taking $\rho^{*}(D) \sim D/\log D$ for the largest admissible set in an interval of diameter $D$, the crude form $B_L \le 2\rho^{*}(210L)-1$ gives, per sector, $2.22$ at $L=1$, $1.59$ at $L=9$, $1.06$ at $L=401$, $0.82$ at $L=10^4$ and $0.51$ at $L=10^8$: it does not fall below $1$ until $L \approx 400$ and does not reach $1/2$ until $L \approx 10^8$. The measured values are far below it everywhere in range, so the observed decrease is not this bound taking effect. Nor do the data identify the exponent: over $1 \le L \le 101$ the quantity $B_L\log^2(210L)/(210L)$ reads $4.22, 4.42, 4.61, 4.99, 4.91, 5.80, 6.68, 7.37$ — rising, not settling — while $B_L\log(210L)/(210L)$ reads $0.789, 0.685, 0.663, 0.685, 0.651, 0.691, 0.720, 0.740$. On this range $\log D$ varies only from $5.3$ to $10.0$, and the two laws are not separated by it.

**What the whole calculation does not buy, stated exactly.** Since $B_L = o(L)$, the criterion no longer asks for a survivor every sector or every second sector: it suffices to prove $\sum_i C_{M_i} \ge \varepsilon L$ for any fixed $\varepsilon \gt  0$, that is, that a positive proportion of sectors contains at least one open cell. Measured at $M_0 = 448{,}353$, the survivor total is $366{,}120$, $1{,}100{,}106$ and $3{,}304{,}035$ over $L = 1, 3, 9$ — that is $10{,}461$, $10{,}477$ and $10{,}489$ per sector, flat — so the inequality holds by a factor of $11{,}810$, $16{,}419$ and $20{,}270$, widening with $L$. The survivor total is linear in $L$ with a large constant; its logarithm is $\log M_0$, not $\log L$, so no amount of lengthening changes its shape.

> **The reduction is therefore real and it is not a route.** What is now required of the survivor side is not a rate of growth but an *existence* statement: one open cell in a positive proportion of sectors. By Theorem 1 an open cell is a twin pair unless it sits at one of six named places, and [P9, §2.3] measures that discrepancy at $0$, $1$ and $3$ over three full periods. So "prove $\sum_i C_{M_i} \ge \varepsilon L$" is "prove that a positive proportion of sectors contains a twin", and shrinking the right-hand side from $32$ to $O(L/\log^2 L)$ changes the number on the right while leaving the missing ingredient on the left exactly as it was.

---

### B.2 The square-phase mean, and the end of the "poor window" question

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

> **The square-phase mean has the exact expression (3.3); numerically it tracks the generic density prediction closely, the two differing by about $1$% or less from $p = 29$ onward in the sample above.** So the exact quantity is available in closed form, and on the tested range it shows no bias at the level of the mean — which replaces the earlier control experiment with a computation, though not with a proof that the two agree in the limit. Individual windows are of course far from the mean — $T_{53}^- = 2$ against $\mu_{\mathrm{sq}} = 5.43$ — but the scatter is governed by the correlation function of [P3, Thm 4], not by any property of squares.

---

### B.3 Two constructions that do not help

**A window balanced across a bundle of lines.** One can design the window instead of inheriting it. For every line of a bundle $p_{\min} \le p \le p_{\max}$ to make exactly $2r+1$ strikes about a common centre $A$ divisible by all of them, the half-width $H$ must satisfy $2rp_{\max} \le H \lt  2(r+1)p_{\min}$, so such a window exists iff
$$\frac{p_{\max}}{p_{\min}} \lt  1 + \frac1r.$$
For $r = 1$ that is $p_{\max} \lt  2p_{\min}$ — the lines $11,13,17,19$ with $H = 40$ give three strikes each — and for $r = 2$ it is $p_{\max} \lt  1.5 p_{\min}$. Moreover the side strikes of different lines never coincide as long as $r \lt  p_{\min}$, so the bundle meets only at $A$.

*Why it changes nothing.* Take $p = 1009$, $q = 1013$, $r = 52$, so each makes $105$ strikes in one window, and slide the window along the common multiples $A_t = pq(2t+1)$. The incidence census of those $105$ positions against the lines $3, 5, 7$ is $48, 24, 12, 8, 6, 4, 2, 1$ — identical in every window over $t = 0,\dots,11$, and identical to the census of the odd numbers modulo $210$. Stronger: the **word** itself, the sequence of incidence patterns across the $105$ positions, is a cyclic rotation of the first window's word in every one of $20$ windows tested. The whole object is one word of length $105$ and a rotation, because $105$ consecutive positions cover every residue modulo $105$ exactly once. The construction promised to separate the *count* of overlaps from their *arrangement*; the measurement says there is nothing to separate, since the arrangement is the same word shifted.

**Ownership and the cofactor.** Writing a strike in a sector $[P^2,Q^2)$ as $N = pm$, it is new for $p$ exactly when $\mathrm{spf}(m) \ge p$, and the higher lines that return to it are exactly the primes $q$ with $p \lt  q \le P$ and $q \mid m$. Two consequences are clean: if $q \gt  p$ shares a new point of $p$ then $p^2q \lt  Q^2$, and conversely $P^2 \le p^2q \lt  Q^2$ makes $p^2q$ a guaranteed shared point. And if $p^3 \ge Q^2$ then $m \lt  Q^2/p \le p^2$ while $m$ has no factor below $p$, so $m$ is prime: in that layer every new strike is a product of exactly two primes (verified with no exception in the sectors $101\to103$, $499\to503$, $997\to1009$).

*Why this too changes nothing.* The condition $p^2q_1q_2\cdots \lt  Q^2$ is **not** a bound on interaction depth, and the derived layers $Q^{1/2}, Q^{2/5}, \dots$ do not exist: $10387 = 13\cdot17\cdot47$ sits inside $[101^2,103^2)$ and $1009091 = 97\cdot101\cdot103$ inside $[997^2,1009^2)$. More to the point, even in the clean layer the question "is this strike new?" becomes "is the cofactor prime?", and for smaller $p$ it becomes "is the cofactor free of prime factors below $p$?" — which is Buchstab's decomposition in the vocabulary of lines. The numbers say the same: of the raw strikes of the clean layer, the new ones are $29$ of $73$, $1158$ of $4756$ and $1492$ of $7938$ in those three sectors — 40, 24 and 19 per cent and falling. Even where no higher line can return, most strikes are still repeats from below.

---

### B.4 Smoothing the window with the classical kernels

Proposition 1 is stated for a sharp window, and a sharp window pays a boundary error of order $1$ per residue class. Replacing the window by a Fejér kernel removes most of that error, and moving the kernel as well removes more. **The smoothing itself is classical**, and so is the order it gains; what is recorded below is an exact discrepancy formula for the single kernel, a bound for the moving one, and a mirror law for the sector index that the quadratic trajectory of [P2, §4.5] supplies. The point of the subsection, though, is the measurement that follows: it says how far this smoothing reaches inside the hierarchy of §2.9, and it does not reach the part that decides the answer.

**A mirror law for the sector index.** Fix an odd modulus $d$ and let $\rho(d)$ be the number of residues it forbids ($2^i$ when $d$ is a product of $i$ lines). Writing $N_d(s)$ for the number of those residues met inside the single sector $I_s = [a_s, a_{s+1})$, put $e_d(s) = N_d(s) - \rho(d)L_s/d$.

> **Proposition 3.** $e_d(s+d) = e_d(s)$; and for $0 \le s \le d-2$,
> $\displaystyle e_d(d-2-s)  =  -\ e_d(s), \qquad\text{with}\qquad e_d(d-1) = 0 .$

*Proof.* Periodicity is $a_{s+d} \equiv a_s \pmod d$, which is (4.4) of [P2, §4.5]. For the reflection, the two facts needed are
$$a_{d-2-s} \equiv a_{s+1} \pmod d, \qquad L_s + L_{d-2-s} = 12d .$$
The first says that — the mirror sector begins, modulo $d$, exactly where $I_s$ ends — while $L_s + L_{d-2-s} = 12(s+1)+12(d-1-s) = 12d$, so the two sectors together cover exactly twelve full periods of $d$ and their errors must cancel. The sector $s = d-1$ has length $12d$ on its own, whence $e_d(d-1) = 0$. $\blacksquare$

*Verification.* Zero failures over the whole cycle for $d = 5, 7, 11, 13, 35, 55, 77$ and $385$, including the two ingredients of the proof checked separately. **So the word of phase errors along a cycle reads $e_0, e_1, \dots, -e_1, -e_0, 0$: it is odd about its own centre.**

**The triangular weight, and an exact discrepancy formula.** Replace the indicator of a window by the triangular weight of half-width $H$,
$$w_H(u)  =  \max\Big(1-\frac{\lvert u\rvert}{H},\ 0\Big),$$
the Cesàro weight, which is the Fejér kernel on $\mathbb{Z}/d\mathbb{Z}$: $H\ w_H$ is the self-convolution of the indicator of $\lbrace 0,\dots,H-1\rbrace$, so its transform is $\lvert \widehat{\mathbf 1}\rvert^2 \ge 0$ and decays like $h^{-2}$ rather than $h^{-1}$. The weight and that representation are standard in exactly this setting; see [1], where sieve functions are averaged over unions of residue classes in a short interval with the same weight.

> **Proposition 4.** Write $H = qd + s$ with $0 \le s \lt d$. Then
> $\displaystyle \max_{b \bmod d}\ \Big\lvert \sum_{n \equiv b \ (d)} w_H(n) - \frac{H}{d} \Big\rvert  =  \frac{s(d-s)}{dH}  \le  \frac{d}{4H}. \qquad\text{(3.7)}$
> with the maximum attained at $b = 0$.

*Proof.* Let $c_j$ be the number of $n \lt H$ in the class $j \pmod d$ and $c_j = H/d + \delta_j$. The weighted count is $H/d + H^{-1}\sum_j \delta_j\delta_{j-b}$. Exactly $s$ of the classes have $c_j = q+1$ and the rest have $c_j = q$, and those $s$ classes form a cyclic interval $A$, so $\delta_j = \mathbf 1_A(j) - s/d$ and
$$\sum_j \delta_j\delta_{j-b}  =  \lvert A \cap (A+b)\rvert - \frac{s^2}{d}.$$
This is largest at $b = 0$, where $\lvert A\cap A\rvert = s$ and the value is $s - s^2/d = s(d-s)/d$; and $s(d-s)/d \le d/4$, with equality only when $s = d/2$ — so for the odd moduli of this paper the second inequality in (3.7) is always strict. $\blacksquare$

**Where this sits.** Smoothing by a Fejér kernel, and the resulting order $O(d/H)$, are classical: [6, Ex. 24.2.1.1(d)] asks for the pointwise estimate $0 \le \Delta_N(x) \le \min\lbrace N, 1/(4N\lVert x\rVert^2)\rbrace$, with the constant $\tfrac14$ arising the same way, from $\sin \pi x \ge 2\lVert x\rVert$. That estimate is not (3.6), though. The left side of (3.7) is an *average* of the kernel over a subgroup of frequencies, $d^{-1}\sum_{h\ne0} e(-hb/d)\Delta_H(h/d)$, not a pointwise value of it; applying the pointwise bound term by term and summing recovers the order but overshoots $d/(4H)$ by a factor of $2.93$, $3.25$ and $3.29$ at $d = 11, 101, 1001$, stable in $H$. **The equality in (3.7) is the part we have not found stated anywhere**, and it explains the near-sharpness of $d/(4H)$ without any measurement: the ratio of the two sides is $4s(d-s)/d^2$, which for odd $d$ is largest at $s = (d\pm1)/2$ and equals $(d^2-1)/d^2$.

**Moving the window as well: a double tent.** Now slide the centre linearly, $c_t = c_0 + t$, and weight the times themselves by a second triangle $q_T(t) = T^{-1}(1-\lvert t\rvert/T)$.

> **Proposition 5.** With that weighting,
> $\displaystyle \lvert E_{d,b}\rvert  \le  \frac{d^4+10d^2-11}{45\ d\ H\ T^2}  \ll  \frac{d^3}{45\ H\ T^2},$
> using the exact identity $\sum_{h=1}^{d-1}\csc^4(\pi h/d) = (d^4+10d^2-11)/45$.

*Proof.* Each triangle contributes the square of a Dirichlet kernel to the Fourier expansion of the error, giving $d^{-1}\sum_{h\ne 0} \lvert D_H(h)\rvert^2 H^{-1}\lvert D_T(h)\rvert^2T^{-2}$; bounding $\lvert D_N(h)\rvert \le \csc(\pi h/d)$ and summing by the identity gives the statement. $\blacksquare$

*The identity is classical*, one of a family of finite cosecant power sums going back to Euler; see [3] for the $\csc^4$ case and its higher analogues. The bound holds with worst ratio $0.8958$ over all $(d,H,T,b)$ we tested. **Taking $H \asymp T \asymp r$ gives $\lvert E\rvert \ll (d/r)^3$, so every modulus $d = o(r)$ loses its phase error without a full cycle modulo $d$ and without any primorial.**

**A remark on the case $H = T$.** There the Fourier multiplier of the two-stage weight is $\lvert D_N(h)\rvert^4/N^3 = \Delta_N(h/d)^2/N$ — the square of the Fejér kernel, which up to normalisation is the **Jackson kernel** of approximation theory. So at equal parameters the construction is a Jackson-type smoothing on the Fourier side; the spatial weight itself is a convolution of two triangles, not a Jackson kernel, and the two should not be confused.

**The exponent is sharp, and the construction has a name.** Expanding $E_{d,b}$ over the non-zero frequencies and keeping a single Fourier coefficient gives a lower bound for $\max_b \lvert E_{d,b}\rvert$; at $H = T = (d-1)/2$ one has $\lvert D_H(1)\rvert \asymp d$, so that lower bound and $d^3/(HT^2)$ are both of order $1$, and no smaller power of $d$ can hold uniformly in $H$ and $T$. **This settles the exponent $3$, not the sharpness of the constant $1/45$.** Measured at that choice, $\max_b\lvert E_{d,b}\rvert$ against the bound is $0.225/0.237$, $0.191/0.203$ and $0.181/0.193$ at $d = 11, 23, 37$ — a ratio near $0.94$, stable. The two-stage device is **iterated Fejér smoothing on $\mathbb{Z}/d\mathbb{Z}$**: the moving centre turns the time average into a second convolution on the same cyclic group, which is why the two Fejér multipliers multiply. Both the sharpness argument and the name are due to a respondent to a question of mine on MathOverflow; the numbers here are my own check of them.

Proposition 3 is what makes the second of these usable across sectors rather than inside one: the moving centre samples consecutive sectors, and their errors are odd about a common centre, so the sliding average is not merely a smoothing but a cancellation.

**Why the certificate survives smoothing.** Since $w_H(u) = H^{-1}\sum_{h=1}^{H}\mathbf 1_{\lbrace \lvert u\rvert \lt h\rbrace}$ and $q_T \ge 0$, a smoothed Bonferroni value is a positive average of sharp ones. So if the smoothed $\mathcal{L}_k$ exceeds $2$, some sharp window in the family has $L_k \gt 2$, and by Proposition 1 that window holds at least three open cells — inside the same sector, so Theorem 1 and Corollary 1 still apply. **Smoothing changes the estimate, not the target.**

**What the smoothing buys, measured.** Applying Proposition 4 to the single tent and Proposition 5 to the double one, with the fixed choices $H = L/4$ and $H = T = L/8$ centred at the sector midpoint:

| $M$ | sharp $L_7$ | tent $L_7$ | double tent $L_7$ | sharp $L_9$ | tent $L_9$ | double tent $L_9$ |
|------|------------|-----------|------------------|------------|-----------|------------------|
| $10{,}005$ | $-93$ | $-75.0$ | $-43.2$ | $502$ | $120.6$ | $59.4$ |
| $20{,}001$ | $-1{,}236$ | $-286.0$ | $-145.6$ | $779$ | $216.4$ | $110.5$ |
| $50{,}001$ | $-7{,}494$ | $-1{,}653.5$ | $-791.2$ | $1{,}567$ | $395.7$ | $199.2$ |

The gain on $L_7$ is a factor of about nine at $M = 50{,}001$. **It is nevertheless not enough: the sign does not change, and the order required stays where Proposition 1 put it.** Since the kernels are the classical ones and the exponent is sharp, this is not a failure of the particular smoothing chosen — it is as far as smoothing of this kind goes.

**One further route, closed by an equivalence.** Instead of smoothing line by line, one may smooth the survivor mask itself: with $A \subseteq \mathbb{Z}/Q\mathbb{Z}$ the set of cells surviving every line up to $P$, ask for
$$\Big\lvert \sum_t q_T(t)\sum_u w_H(u)\ \mathbf 1_A(c_t+u) - H\frac{\lvert A\rvert}{Q} \Big\rvert  \lt  H\frac{\lvert A\rvert}{Q}$$
for every centre $c$, with $H$ and $T$ polynomial in $P$ rather than in the primorial $Q$. The primorial does drop out — the least $H = T$ for which this holds is $2, 3, 5, 7, 10$ at $P = 7, 11, 13, 17, 19$, against $Q = 35$ up to $1{,}616{,}615$ — but the reason is not a new mechanism:

| $P$ | $Q$ | least $H = T$ | largest gap $g$ in $A$ |
|------|-----------|------------|---------------------------------------------|
| 7 | 35 | 2 | 5 |
| 11 | 385 | 3 | 7 |
| 13 | 5,005 | 5 | 11 |
| 17 | 85,085 | 7 | 18 |
| 19 | 1,616,615 | 10 | 25 |

**In every case $2H$ is the largest gap, to within one**, and necessarily so: the smoothed count is positive at every centre exactly when every window of length $2H$ meets $A$, which is the definition of Jacobsthal's function on this residue system. So establishing that inequality with $H$ polynomial in $P$ *is* a bound on $h(k)$, an open problem for over fifty years whose best bound comes from the linear sieve rather than from Fourier analysis. The route is recorded as closed; it is a restatement, not a reduction. It is also weaker than what §2.1 needs, which is not one survivor at some centre but three at a prescribed one.

**Our reading of why is a matter of where the mass sits.** Proposition 5 controls a modulus $d$ only while $d \ll r$. Splitting each $S_i$ by whether the product $d = p_1\cdots p_i$ of its subset falls below $r$:

| $M$ | $r$ | $S_1$ | $S_2$ | $S_3$ | $S_4$ | $S_5\text{--}S_7$ |
|------|------|-------|-------|-------|-------|-----------|
| $20{,}001$ | $3{,}333$ | $88.5$% | $40.1$% | $5.6$% | $0$% | $0$% |
| $50{,}001$ | $8{,}333$ | $90.0$% | $44.7$% | $8.7$% | $0.2$% | $0$% |

**Smoothing reaches almost all of $S_1$ and none of $S_5$ and beyond.** The arithmetic is immediate: for $p_1\cdots p_i \lt r$ the primes must average $r^{1/i}$, which at $i = 4$ and $r = 8{,}333$ means all four drawn from $\lbrace 5,7,11,13\rbrace$ — one subset — and at $i = 5$ means none at all. Since $S_1$ is the term that died at $M = 21$ and the terms that decide the sign of $L_7$ are $S_4$ through $S_7$, **the smoothing controls exactly the part that never needed controlling.** We record this as a closed route on that reading: the boundary error does not appear to be what makes the sign negative, and since the exponent of the moving kernel is sharp we do not expect a different window shape to change it.

---

**No progress toward the twin-prime conjecture is claimed, and no new bound.** Priority is not claimed for any result.


---

## References

The eleven papers of this set are cited as [P1] to [P11], and the numbered entries below are the external works. The two kinds never share a number: a bracket with a P is a companion paper, a bare number is a reference in the list below. This paper imports only the definitions and statements of the companion papers, never their proofs.

1. G. Coppola and M. Laporta, *Sieve functions in arithmetic bands*, Hardy–Ramanujan J. **39** (2016), 21–37; arXiv:1503.07502.
2. H. G. Diamond and H. Halberstam, *A higher-dimensional sieve method*, Cambridge Tracts in Mathematics **177**, Cambridge University Press, 2008.
3. S. B. Ekhad, appendix to *Human and automated approaches for finite trigonometric sums*, arXiv:2204.08228 — Proposition Ton_2 and its higher analogues.
4. J. M. Flagg, *Primes between squares — commentary on Appendix 8 of Laws of Form*, arXiv:2511.05603 (2025) — cited for Lemma 1A only.
5. H. Halberstam and H.-E. Richert, *Sieve Methods*, Academic Press, 1974.
6. H. Iwaniec, *Almost-primes represented by quadratic polynomials*, Invent. Math. **47** (1978), 171–188.
7. R. J. Lemke Oliver, *Almost-primes represented by quadratic polynomials*, Acta Arith. **151** (2012), 241–261.
8. G. Morpurgo, *On a stricter twin primes conjecture, and on the Polignac's conjecture in general*, arXiv:2210.15487 (2022; revised 2023). — *A preprint, not peer reviewed; a heuristic prediction with numerical comparison, containing no theorems. Cited as contemporaneous independent work using the same coordinates.*
9. T. T. K. Nguyen, *Finite-window noncovering on primorial wheels: higher-order CRT bounds and shift correlations*, Preprints.org (2026), doi:10.20944/preprints202608.1299.v1. — *A preprint, not peer reviewed; cited as contemporaneous independent work reaching the same finite-window diagnosis from the Goldbach side.*
10. A. Schinzel and W. Sierpiński, *Sur certaines hypothèses concernant les nombres premiers*, Acta Arith. **4** (1958), 185–208; erratum, ibid. **5** (1959), 259.
