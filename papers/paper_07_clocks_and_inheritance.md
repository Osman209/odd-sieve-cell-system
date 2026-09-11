# Clocks and Inheritance

## Paper 7. Primality as a zero-test, and the capacity of a single line across sectors

---

### Abstract

The same window read in two further units. In the clock unit each line carries a phase that slides by a fixed law as the window moves, primality becomes the statement that no clock reads zero, and a row reads primality off originality: a surviving cofactor is prime. In the inheritance unit the sector law transports exactly from one sector to the next, the capacity of one new line on one family is computed in closed form, and the lines that can ever be exceptional are shown to be finite in number. Each statement is exact; none of them binds. **No progress toward the twin-prime conjecture is claimed.**

**Numbering.** This paper is one part of a set that was written as a single document and is now published in parts. Each part numbers its own results from one and is self-contained: a reference of the form [Pn, Thm 1] means Theorem 1 of Paper n, and an unqualified "Theorem 1" always means this paper's own. Result numbers therefore differ from those of the earlier seven-document releases, where the whole set shared the numbering of the single document.

**How to read the claims in this paper.** Statements set as Theorems, Propositions and Corollaries are proved, and the proofs are given. One result in the set is labelled **Verified Law**: it is proved under a stated hypothesis and verified numerically outside it. Anything described as *measured* is a computation over a stated finite range and is labelled as such where it occurs.

**Keywords:** twin primes, sieve cycles, inheritance, cell coordinates.

**MSC 2020:** 11N35, 11N05, 11A41.

---

## Summary of the results in this part

**§2 — Clocks, and primality as a zero-test**

| Result | What it says | Section |
|-------------|----------------------------------------------------|---------|
| **Theorem 1** | The shift law $\phi_q(p+2) = \phi_q(p) - 1 \pmod q$ for every old line. | §2.1 |
| **Corollary 1** | $p$ is composite **iff** some old clock reads $0$ at its birth. | §2.1 |
| **Corollary 2** | The clock of $L_3$ cycles $2 \to 1 \to 0$, so its two non-zero states are exactly the two rails. | §2.1 |
| **Theorem 2** | Surviving cofactors are prime, for $p \ge 11$ and $p \lt t \le 9p$. | §2.2 |
| **Theorem 3** | A row reads primality off originality — a recoding of trial division, not a new test. | §2.3 |

**§3 — Inheritance across sectors, and the capacity of one line**

| Result | What it says | Section |
|---------------|--------------------------------------------------|---------|
| **Theorem 4** | The sector inheritance law $B(M + 6Q) = B(M) + 12S$. | §3.1 |
| **Proposition 1** | A window synchronised with its lines: the primes dividing $p+1$ give four **exact** identities with no edge term. Not twin-specific, and not a reduction. | §3.1 |
| **Theorem 5** | The capacity of one new line on one family, through $\Delta_q \equiv (3Q)^{-1} \pmod q$. | §3.2 |
| **Proposition 2** | The three mirror channels: the first is empty exactly for a twin, the second is the synchronised set, the third is not empty in general. | §3.2 |
| **Corollary 3** | The lines that can close two copies of a family are finite in number. | §3.3 |

**Appendix A — an auxiliary exact model**

| Result | What it says | Section |
|---------------|--------------------------------------------------|---------|
| **Theorems A1–A3, Corollary A1** | The minimum deletion cover $\tau = T-U+Q$ of the distance-$6$ graph, its propagation laws and its tail compression. **Its object is a prime pair $(p,p+6)$, not a twin pair**, and the appendix says so before anything else. | App. A |

---

## 1. Setting

We use Papers [P1] and [P2]–[P4] as follows. Paper [P9]–[P11] is a companion rather than a source: it is cited where the obstruction it derives explains why a cut is placed where it is, and nothing else is imported from it.

- **[P1]** supplies the window combinatorics: the increments $W_j$ of $\lfloor 2j^2/p\rfloor$, their uniform bound and their exact histogram.
- **[P2]** supplies the coordinates: the line $L_p(k) = p(p+2k)$ beginning at $p^2$, the grid $L_3$, the cells $C_b = (6b-1, 6b+1)$, and the square window with its $+8$ growth.
- **[P3]** supplies the exact cycle laws: the four-state law, its refinement by inheritance depth, arbitrary weights in $\Omega_{\le z}$, the refinement by line size, and the disjoint ownership layers.
- **[P4]** studies the transfer to a window of length $\asymp z^2$. On the tested windows, linear depth weights measure $1.0000$ to the reported precision, the tested soft truncations remain close to $1$, and the sharp depth-zero indicator is the exceptional endpoint with ratio near $0.80$. These are measurements, not an exact window theorem.

A word on the last point, since it is what makes this paper's organisation possible. The indicator of depth zero is the condition "both members of the cell survive" — that is, the twin condition. Thus, in the tested family, the largest transfer loss occurs precisely at the depth-zero indicator, the quantity that becomes a primality/twin condition inside the moving square window.

---

## 2. Clocks, and primality as a zero-test

### 2.1 Theorem 1 (the shift law) and primality

> **Theorem 1.** $\phi_q(p+2) = \phi_q(p) - 1 \pmod q$ for every old line $q$; and when $p$ itself becomes an old line, $\phi_p(p+2) = p-1$.

*Proof.* Substituting $p+2$ for $p$ in [P4, (2.2)] subtracts $1$. For the second, $\phi_p(p+2) = (p-(p+2))/2 = -1 \equiv p-1$. $\blacksquare$

*Verification.* Zero failures among $4{,}983$ instances, and zero for the insertion rule.

Hence, writing $\Phi(n) = (\phi_3, \phi_5, \phi_7,\dots)$, the transition $n \mapsto n+2$ acts as
$$\Phi  \longmapsto  \Phi - 1,$$
each component on its own circle, and the whole system evolves by three small numbers:
$$\text{step } +4, \qquad \text{first square gap } +8, \qquad \text{all clocks } -1,$$
with one clock inserted at $p-1$ whenever $p$ is prime. The system is *shift, zero-test, insert*; nothing is rebuilt.

> **Corollary 1.** $p$ is composite if and only if some old clock reads $0$ at its birth. Equivalently, **a prime is a step at which no clock lands on zero.**

*Verification.* Zero failures over all odd $p \lt  2000$.

> **Corollary 2.** The clock of $L_3$ cycles $2 \to 1 \to 0$, so the two non-zero states are exactly the cell $(6a-1, 6a+1)$. **The cell, taken as a definition in [P2, §3.1], is a consequence.**

### 2.2 Theorem 2 (surviving cofactors are prime)

> **Theorem 2.** For $p \ge 11$ and $p \lt  t \le 9p$, a cofactor $t$ surviving all lines below $p$ is prime.

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

The "new" cofactors are exactly $13,17,19,23,\dots,97$, all prime, as Theorem 2 requires.

### 2.3 The general form: a row reads primality off originality

Theorem 2 is the case that arises inside one sector. Read along the whole row of $p$ it has a general form, and the general form is worth stating because it makes the twin condition geometric.

Call a cell of the row **original** if no line below $p$ owns it. Everything before $p^2$ is inherited — a strike $p m$ with $m \lt  p$ carries the smallest prime factor of $m$, which is below $p$ — so $p^2$ is the first original cell on the row. Past it:

> **Theorem 3.** For $p$ prime and $p \le p+2j \lt  p^2$,
> $\displaystyle p (p+2j) \ \text{ is original with respect to the lines below } p \quad\Longleftrightarrow\quad p+2j \ \text{ is prime}.$

*Proof.* Suppose $p+2j$ is composite. Being below $p^2$, its least prime factor is below $p$:
$$p+2j = rs \quad\text{with}\quad r \le \sqrt{p+2j} \lt p,$$
so the line $r$ already owns the cell. If $p+2j$ is prime it has no factor below $p$ at all, and $p$ itself begins at $p^2$. $\blacksquare$

*Verification.* Zero failures over $1{,}782{,}933$ instances: every prime $p \lt  400$ and every $j$ with $p+2j \lt  p^2$.

**So a row is a reader.** The row of $p$ carries, in the originality of its cells, the primality of every odd number from $p$ up to $p^2$ — one bit per cell, with no change to the definition of a prime. Two consequences are worth recording.

**First, the twin condition becomes a two-step statement at the diagonal.** The cells at $p^2$ and $p(p+2)$ are the first two on the row past the inherited region, and by Theorem 3
$$(p, p+2)\ \text{is a twin pair} \quad\Longleftrightarrow\quad \text{originality survives one step past } p^2 .$$
Writing $\mathsf O$ for original and $\mathsf I$ for inherited, the row crosses the diagonal as $\dots\mathsf I \mid \mathsf O \mathsf O\dots$ at a twin and $\dots\mathsf I\mid \mathsf O \mathsf I\dots$ otherwise: at $p=23$, $529$ is original but $575 = 23\cdot 5^2$ is not, and $(23,25)$ is not a twin.

**Second, the shadow lies on a curve already in the series.** The tested cell is
$$p (p+2)  =  (p+1)^2 - 1,$$
so every twin test sits one unit below an even square: $35 = 36-1$, $143 = 144-1$, $323 = 324-1$, $899 = 900-1$. **That is [P2, Thm 5] read along the row instead of across the window** — the cell $(n^2-1,\ n^2+1)$ with $n = p+1$, whose lower member $(n-1)(n+1)$ is composite by construction. The two statements are the same fact.

**And the reformulation is exact, which is precisely why it is not progress.** Writing $\sigma(p)$ for the smallest line **below $p$** owning $p(p+2)$ — the line $L_p$ itself always owns it, since $p(p+2) \gt  p^2$ — one has $\sigma(p) = \mathrm{spf}(p+2) \le \sqrt{p+2}$ when $p+2$ is composite, and $\sigma(p) = \infty$ exactly when $(p,p+2)$ is a twin. Proving $\sigma(p) = \infty$ infinitely often is proving the twin conjecture, in the same words. What the row picture adds is a suggestion — that if twins were finite, every new diagonal point would need its shadow claimed by some line below $\sqrt p$ — and the suggestion does not survive measurement: over $6{,}835$ composite cases with $p \lt  200{,}000$ the claimant is at most $13$ in $63.6$% of them and at most $100$ in $89.9$%, the counts being $5$: $2248$, $7$: $1125$, $11$: $557$, $13$: $415$, $17$: $303$. **The $\sqrt p$ bound is nowhere near tight; the shadows are claimed by the smallest lines, not by a delicate conspiracy of many.**

---

## 3. Inheritance across sectors, and the capacity of a single line

Section 2 treats one sector at a time. This section treats the *sequence* of sectors, indexing them by $M = 9, 15, 21, \dots$ — the odd multiples of $3$ — with the sector $(M^2, (M+6)^2)$ carrying $A(M) = 2M+6$ cells. Three exact laws come out, all sharper than the average statement "line $q$ removes $2/q$ of what remains", because each is a statement about a *named* gap rather than about a count.

### 3.1 Theorem 4: the sector inheritance law

Fix any finite set of lines $p_1 \lt  \dots \lt  p_r$ above $3$, and put
$$Q = \prod_i p_i, \qquad S = \prod_i (p_i - 2),$$
so that $S$ cells survive that set in each cycle of $Q$ consecutive cells. Let $B(M)$ be the number of cells of the sector at $M$ that survive those lines.

> **Theorem 4.** $B(M + 6Q)  =  B(M)  +  12 S.$

*Proof.* Two facts. First, the sector grows by exactly $12Q$ cells: $A(M+6Q) - A(M) = 12Q$. Second — and this is what makes the law exact rather than approximate — the **phase is preserved**: the sector at $M$ begins near cell $M^2/6$, and
$$\frac{(M+6Q)^2}{6} - \frac{M^2}{6}  =  2MQ + 6Q^2  \equiv  0 \pmod Q .$$
So the first $A(M)$ cells of the later sector repeat the earlier sector's pattern exactly, and the tail of $12Q$ new cells is precisely twelve complete cycles, each leaving $S$ survivors. $\blacksquare$

*Verification.* Exact at every $M$ tested, for each of the three sets: $\lbrace 5\rbrace$ ($Q=5$, $S=3$, increment $36$); $\lbrace 5,7\rbrace$ ($Q=35$, $S=15$, increment $180$); $\lbrace 5,7,11\rbrace$ ($Q=385$, $S=135$, increment $1620$).

**What it says.** A *fixed* set of old lines never catches up with the window. Each time its cycle returns to the same phase, the sector has grown, and a known positive number $12S$ of fresh open cells appears. Only lines born after the set was fixed can close them.


**A window whose lines are synchronised with it.** Theorem 4 moves along the cycle. The opposite situation — a window whose length is a whole number of periods of the lines acting on it — also occurs, and there the counts are identities rather than estimates. Fix $p \equiv 5 \pmod 6$, put $C = (p+1)^2$ and index the interval $(p^2,(p+2)^2)$ by the cells $X_d = (C+6d-1,\ C+6d+1)$ for $-(2m-1) \le d \le 2m-1$ where $p+1 = 6m$, so the interval holds $N = 4m-1$ cells. A line $r \ge 5$ completes a whole number of its cycles inside the strip if and only if $r \mid 4m$, and since $r$ is odd and larger than $3$ this is $r \mid p+1$.

> **Proposition 1.** Let $S$ be the set of primes $r \ge 5$ dividing $p+1$, put $P = \prod_{r \in S} r$, $A = \prod (r-1)$, $B = \prod (r-2)$, and suppose $m = aP$. Write $N_{\varnothing}$, $N_L$, $N_R$, $N_{LR}$ for the number of cells of the strip untouched by $S$, struck on the left member only, on the right member only, and on both. Then, exactly,
> $\displaystyle N_{\varnothing} = 4aB - 1, \qquad N_{L} = N_{R} = 4a(A-B), \qquad N_{LR} = 4a(P - 2A + B).$

*Proof.* Fix $r \in S$. Since $r \mid p+1$ one has $C = (p+1)^2 \equiv 0 \pmod r$, so the two members of $X_d$ are $6d-1$ and $6d+1$ modulo $r$, and $r$ strikes the left exactly when $d \equiv 6^{-1}$ and the right exactly when $d \equiv -6^{-1}$ — two distinct classes by [P2, Thm 3], leaving $r-2$ classes untouched. The moduli are pairwise coprime, so by the Chinese remainder theorem, among the $P$ classes of $d$ modulo $P$ there are $B$ untouched by every line of $S$, while $\prod_{r}\big((r-2)+1\big) - B = A-B$ are struck on the left and never on the right, the same number on the right, and $P - B - 2(A-B) = P-2A+B$ on both.

The strip runs over $d = -(2m-1),\dots,2m-1$, that is $4m-1 = 4aP-1$ consecutive integers: one short of $4a$ complete periods. Adjoining the single index $d = 2m$, which lies past the right end of the strip, completes them; and $2m = 2aP \equiv 0 \pmod P$, so the class short by one representative is $d \equiv 0 \pmod P$. That class is untouched by every $r \in S$, since its members are $C \mp 1 \equiv \mp 1 \pmod r$. So the whole deficit falls on $N_{\varnothing}$ — the centre cell $d = 0$ is inside the strip and is counted; what is missing is one of the other representatives of its class. $\blacksquare$

*Verification.* At $p = 2309$, where $S = \lbrace 5,7,11\rbrace$, $P = 385$, $a = 1$, $A = 240$, $B = 135$: the strip holds $4aP - 1 = 1539$ cells, one short of the $1540$ that four complete periods of $385$ would give, and the direct census gives $539 + 420 + 420 + 160$, matching the four formulas exactly, and the surviving fraction is $N_{\varnothing}/N = 539/1539 = 0.3502$. The identities were then checked over every $p \equiv 5 \pmod 6$ below $2000$ — $59$ of them twin, $273$ not — with no exception.

*Two things it is not.* It is **not** a statement about twins: primality of $p$ and $p+2$ enters nowhere in the derivation, which needs only $6 \mid p+1$. And it is **not** a reduction: the surviving fraction is $N_{\varnothing}/N = 0.3502$ against $\prod_{r \in S}(1 - 2/r) = 0.3506$ at $p = 2309$, so the drop from $1539$ to $539$ is the ordinary sieve by those three lines and nothing more. What the synchronisation buys is exactness — no edge term — not size.

### 3.2 Theorem 5: the capacity of one new line on one family

Each survivor of the fixed set appears in the new tail exactly twelve times, at cells
$$x,\ x+Q,\ x+2Q,\ \dots,\ x+11Q,$$
which we call a **family**. A new line $q$ closes a cell $c$ when $c \equiv \pm 6^{-1} \pmod q$, so on a family it closes the copies $t$ solving $x + tQ \equiv \pm 6^{-1}$. There are two such $t$ modulo $q$, and their separation does not depend on $x$:

> **Theorem 5.** Put $\Delta_q \equiv (3Q)^{-1} \pmod q$ and $d_q = \min(\Delta_q,\ q - \Delta_q)$. Then a line $q \gt  11$ closes at most two copies of any family, and **at most one** whenever $d_q \gt  11$.

*Proof.* The two solutions differ by $2\cdot 6^{-1} Q^{-1} = (3Q)^{-1}$, whose least absolute representative is $\pm d_q$. Two copies lie in the family only if two values of $t \in \lbrace 0,\dots,11\rbrace$ differ by $d_q$, which needs $d_q \le 11$. $\blacksquare$

*Verification.* For $Q = 385$, brute force over all $x$ and all $q$ from $13$ to $101$ reproduces the predicted capacity with **zero mismatches**. Sample values of $d_q$: $13{:}6$, $17{:}1$, $19{:}5$, $23{:}9$, $31{:}4$, $37{:}14$, $53{:}24$, $83{:}12$, $101{:}39$.

**The reflection of that window, and what a single line can do to it.** The interval $(p^2,(p+2)^2)$ is two consecutive Legendre intervals glued at $C = (p+1)^2$, and the map $d \mapsto -d$ exchanges them. A line respects the reflection $x \mapsto 2C-x$ exactly when it divides $2C$, that is when it belongs to the set $S$ of Proposition 1 — so the synchronised lines are precisely the lines the reflection preserves.

> **Proposition 2.** A single line $q \lt  p$ can strike both cells of a mirror pair $X_d, X_{-d}$ only if $q \mid p(p+2)$, or $q \mid (p+1)^2$, or $q \mid (p+1)^2+1$.

*Proof.* Add the two members in each of the three ways: $L_d + L_{-d} = 2(C-1) = 2p(p+2)$, $L_d + R_{-d} = 2C$, and $R_d + R_{-d} = 2(C+1)$. If $q$ divides both members of a pair it divides their sum, and $q$ is odd. $\blacksquare$

*What the three channels are worth.* The first is empty exactly when $p$ and $p+2$ are both prime, since then $p(p+2)$ has no factor below $p$ — this is the one place in this subsection where the twin hypothesis does any work. The second is the set $S$ itself. The third is not empty in general: the number of **mirror pairs** closed on both sides by a single line is $5, 12, 0, 0, 375, 657, 4$ at $p = 101, 137, 2309, 3299, 5741, 10007, 17789$, the zeros being the accident that $(p+1)^2+1$ is prime there. (It is not a count of lines: at most six primes below $p$ divide one of the three quantities, and Proposition 2 bounds the lines, not the pairs.)

*And the reflection settles nothing about twins, which is the point of recording it.* Measured over the first six of those $p$: the two halves carry exactly equal cell counts and exactly equal survivor counts, every time, while the twin counts differ by $-1, -2, -1, -8, +2, +10$. The symmetry transports the structure perfectly and constrains the one quantity one wants not at all — a symmetry gives structure on a set when it is non-empty, and never gives non-emptiness.

### 3.3 Corollary 3: the exceptional lines are finite in number

> **Corollary 3.** A line $q$ can close two copies of a family only if $q \mid 3Qr \pm 1$ for some $1 \le r \le 11$. Consequently every $q \gt  33Q + 1$ closes **at most one** copy of every family.

*Proof.* The condition $d_q \le 11$ means $\Delta_q \equiv \pm r$ with $r \le 11$, that is
$$3Qr \equiv \pm 1 \pmod q \qquad\text{for some } 1 \le r \le 11;$$ and $0 \lt  3Qr \mp 1 \le 33Q+1$, so $q$ cannot divide it once $q$ exceeds that bound. $\blacksquare$

For $Q = 385$ the threshold is $12{,}706$. This is a genuinely local statement: it names, for each family, a bound on what a *specific* line can do, whereas $2/q$ only bounds a total.


---

## Appendix A — An auxiliary exact model: the distance-6 closing budget

**What this appendix is, and why it is not in the body.** Sections 2 and 3 concerned twins: a surviving cell, whose two members differ by $2$. The present appendix concerns a different graph — survivors joined to survivors at distance $6$ — and the two must not be run together, because the word “gap 6” would otherwise cover both the *letter* $6$ of [P5, §2.1] (a gap of $6$ between consecutive odd composites, which contains a twin) and the *edge* of length $6$ used here. **What an untouched edge exhibits once the remaining lines have acted is a prime pair $(p, p+6)$, not a twin pair.**

Measured, so that the distinction is not left rhetorical: inside $(P^2, 9P^2)$ at $P = 101$ there are $2{,}903$ edges, of which $1{,}865$ survive the remaining lines and $1{,}410$ are genuine gap-$6$ configurations — for instance $(10247,10253)$, $(10337,10343)$, $(10601,10607)$. **None of them is a twin.**

We keep the material because the budget it produces is exact, and because $(p,p+6)$ is open in precisely the same way and for precisely the same reason; but nothing here bears on the twin conjecture directly. It is placed in an appendix for that reason: it is an exact model that Papers 9 to 11 use as a test object, not a step in the twin criterion.

Instead of asking what the lines will close, we ask the dual question: **how many deletions are needed, at minimum, to close every distance-$6$ edge?** If the available deletions fall short, a pair survives.

### A.1 Theorem A1 (the exact minimum cover)

Take survivors as vertices and join $x$ to $x+6$. Let $T$, $U$, $Q$ count the edges, the $3$-term runs and the $4$-term runs (runs, not components: a component on $k$ vertices contributes $\max(0,k-2)$ to $U$ and $\max(0,k-3)$ to $Q$).

> **Theorem A1.** The minimum number of deletions required to destroy every distance-$6$ edge is
> $\displaystyle \tau = T - U + Q.$

*Proof.* By [P5, Thm 3] of [P5, §2.3] every component is a path on at most $4$ vertices. For a path on $v$ vertices the minimum vertex cover has size $\lfloor v/2 \rfloor$, so the cover of a path on $k$ vertices is $\lfloor k/2 \rfloor$. Summing $(k-1)-(k-2)+(k-3)$ over components reproduces $\lfloor k/2\rfloor$ for $k = 2,3,4$ — and **only** for those, since $k=5$ would give $3$ against the true value $2$. The cap of [P5, Thm 3] is thus exactly what makes the identity hold. $\blacksquare$

*Verification* by direct component decomposition:

| lines | component census | min cover | $T-U+Q$ |
|-------|------------------|-----------|------|
| $\lbrace 5,7\rbrace$ | $\lbrace 1{:}4, 2{:}4, 3{:}4, 4{:}6\rbrace$ | 20 | 20 |
| $\lbrace 5,7,11\rbrace$ | $\lbrace 1{:}68, 2{:}56, 3{:}44, 4{:}42\rbrace$ | 184 | 184 |
| $\lbrace 5,7,11,13\rbrace$ | $\lbrace 1{:}1100, 2{:}788, 3{:}524, 4{:}378\rbrace$ | 2068 | 2068 |

**This is an exact combinatorial identity: no independence assumption and no density heuristic enters.**

### A.2 Propagation laws

Let $G = T - D$ count genuine gap-$6$ pairs, $D$ those with a survivor between. *(The twins sit in $D$: the surviving middle differs by $2$ from one of the two endpoints. So $G$ — the object [P11, App. B] targets — is exactly the twin-free part, which is the content of the caution above. Incidentally, measured on all four cycles below, $U = D$ exactly; we do not use this.)*

> **Theorem A2.** On the full cycle, the entry of a new line $r$ gives
> $\displaystyle T' = (r-2)T, \qquad D' = (r-3)D, \qquad G' = (r-2)G + D.$

*Proof.* Of the $r$ copies of a pair, one has its left member struck and one its right, leaving $r-2$. A $D$-configuration has three sensitive positions (both ends and the middle), leaving $r-3$; and the copy whose middle is deleted becomes a genuine gap-$6$. $\blacksquare$

| lines | $V$ | $T$ | $D$ | $G$ |
|-------|-------|-------|-------|-------|
| $\lbrace 5\rbrace$ | 8 | 6 | 4 | 2 |
| $\lbrace 5,7\rbrace$ | 48 | 30 | 16 | 14 |
| $\lbrace 5,7,11\rbrace$ | 480 | 270 | 128 | 142 |
| $\lbrace 5,7,11,13\rbrace$ | 5,760 | 2,970 | 1,280 | 1,690 |

> **Corollary A1.** On the full cycle, $\dfrac{T}{V} = \rho_p = \prod_{5\le s\le p}\dfrac{s-2}{s-1}$ and $\dfrac{D}{T} = \theta_p = \dfrac{2}{3}\prod_{7\le s\le p}\dfrac{s-3}{s-2}$ — **exact identities, not estimates.**

| $p$ | 23 | 53 | 101 | 199 | 499 | 997 |
|------|--------|--------|--------|--------|--------|--------|
| $\rho_p$ | 0.4358 | 0.3607 | 0.3151 | 0.2746 | 0.2367 | 0.2138 |
| $\theta_p$ | 0.3606 | 0.2967 | 0.2588 | 0.2253 | 0.1941 | 0.1753 |

Both tend to zero: distance-$6$ pairs become rarer, yet a growing share of those remaining become genuine gaps.

### A.3 Theorem A3 (tail compression)

Inside $(P^2,9P^2)$, after the lines up to $P$ have acted, every surviving composite has the form $n=qr$ with
$$P\lt q\lt 3P,\qquad q\le r\lt \frac{9P^2}{q}\lt 9P.$$
Indeed three factors above $P$ would give $n\gt P^3\gt 9P^2$ for $P\gt 9$, and the smaller of the two remaining factors is below $3P$. Consequently the number of genuinely new strikes contributed later by a line $q$ with $P\lt q\lt 3P$ is
$$E_P(q)=\pi(9P^2/q)-\pi(q-1)\lt 2(3P-q)+1,$$
so a line approaching $3P$ loses power because the available cofactor interval contracts.

A related compression occurs among the **late lines in the sweep up to $P$ itself**:

> **Theorem A3.** For $P \ge 243$ and $P/3 \lt  q \lt  P$, every new strike of $q$ inside the window has the form $x = qr$ with $r$ **prime**.

*Proof.* The cofactor satisfies $r \lt  9P^2/q \lt  27P$. If $r$ were composite, all its prime factors would be $\ge q$ (it survived the smaller lines), so $r \ge q^2 \gt  P^2/9$. The contradiction holds precisely when $P^2/9 \ge 27P$, i.e. $P \ge 243$. $\blacksquare$

**Finite check around the threshold.** Direct enumeration of new strikes with composite cofactor:

| $P$ | 101 | 151 | 199 | 211 | **241** | 251 | 307 | 499 | 997 |
|-----------|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| anomalies | 26 | 9 | 6 | 5 | **0** | 0 | 0 | 0 | 0 |

The enumeration exhibits anomalies at smaller $P$ and none in the tested cases from $241$ onward; this is consistent with, but stronger numerically than, the proved sufficient threshold $243$. The sharper pointwise condition is $q^3 \gt  9P^2$, i.e. $q \gt  9^{1/3}P^{2/3}$; and the two conditions cross exactly at
$$\frac{P}{3} = 9^{1/3}P^{2/3} \iff \frac{P^3}{27} = 9P^2 \iff P = 243,$$
so $243$ is the point at which the constraint $q \gt  P/3$ becomes the binding one.

---

---

*The computations and much of the prose in this paper were prepared with AI assistance (ChatGPT, OpenAI; Claude, Anthropic), used for algebraic derivation, for drafting and rewriting code and text, for running the computations, and for auditing the papers against their own scripts. All statements were checked by the author, who is responsible for them; the repository README sets out the division of labour in full.*
---

## References

The companion papers of this set are cited as [P1] to [P12]. This paper uses no external reference: everything it quotes is a definition or a statement of a companion paper, never a proof.
