# The Inheritance Law on the Cycle

## II. Exact transport of the divisor census, and of weights, over a sieve cycle

---

### Abstract

Working in the cell coordinates of Paper I, we study the fixed periodic structure of the odd sieve — no window, no squares. Labelling each cell by the survival state of its two members gives a four-state system whose update under the entry of a new line is linear; we show that it has a conserved quantity and therefore a closed solution, in which the whole state dissolves into the two Mertens products $\prod(1-1/q)$ and $\prod(1-2/q)$ (Theorem 1).

The four counts are a *census*, however, not a simulator: we give a two-cell counterexample showing that the final state does not determine the history, so no automaton on the four states can run the process forward. Exactness and blindness turn out to be the same property here — the linear update closes precisely because it forgets which line owns each strike.

The law then **refines**. Tracking, in addition, the *inheritance depth* of each cell — the number of old lines dividing either member — the transport remains exact, in a finite state space of size $O(\pi(z))$, with closed generating function $\prod_q\big((q-2)+xu+xv\big)$ (Theorem 2). Consequently $\sum f(\Omega_{\le z})$ is computable exactly on the cycle for an arbitrary $f$, nonlinear truncations included (Corollary 1).

That is still not enough for Richert's logarithmic weight, which depends on the *sizes* of the factors and not only on their number; we exhibit the gap explicitly. The repair is to mark each line by the bin of its size, and it closes: the refined product transports the joint per-bin census exactly (Corollary 2), at a cost polynomial in $\pi(z)$ for fixed resolution, and eight bins reproduce Richert's weight to $0.4$%.

Finally we record a second exact structure on the same cycle: assigning each integer to its smallest striking line partitions the strip into **disjoint** ownership layers, so the survivor count is a plain difference with no inclusion–exclusion (Theorem 3) — and we show precisely what this costs, namely that the repaired sum returns the sieve product and nothing more.

**Everything here is exact on the full cycle.** The passage to a short window is the subject of Paper III, and it is where the losses are.

**Keywords:** sieve of dimension two, Mertens products, weighted sieves, Richert weights, generating functions.

**MSC 2020:** 11N35, 11N05, 11Y16.

---

## 1. Setting

We use the coordinates of Paper I without change. $L_p(k) = p(p+2k)$ is the line of $p$, beginning at $p^2$; $L_3$ is the coordinate grid, and the odd integers compress to cells $C_b = (6b-1,\ 6b+1)$. Two facts from Paper I are used throughout and nothing else is:

- **[I, Thm 2] (the cell map).** With $p = 6a+\sigma$, one has $p(6b+\varepsilon) = 6(pb + a\varepsilon) + \sigma\varepsilon$, so the line $p$ sends the two members of $C_b$ into the cells $pb-a$ and $pb+a$. In cell coordinates each branch steps by $p$, not by $6p$.
- **[I, Thm 3].** The two positions a line closes are $j \equiv \pm 6^{-1} \pmod p$, and they are always distinct; so **exactly two** of every $p$ cells lose a member, one on each rail.

The second is the only input the whole of §2–§4 needs. Everything below is a consequence of "of the $p$ copies of any cell, exactly two are struck, one per rail."

Throughout, $z$ is the sieve depth, the cycle modulus in the cell index is $\prod_{5\le q\le z} q$ (**not** $6\prod q$ — an off-by-a-factor that is easy to make), and $\Omega_{\le z}$ denotes the number of lines up to $z$ dividing either member of a cell, i.e. the inheritance depth.

---


## 2. The four-state law and its closed solution

### 2.1 The update

Counting cells of each type over a full cycle, the entry of line $p$ gives
$$A' = (p-2)A, \quad B' = A + (p-1)B, \quad C' = A + (p-1)C, \quad D' = B + C + pD. \tag{2.1}$$

*Reason.* Of the $p$ copies of an $NN$ cell, one has its lower member struck and one its upper, so $p-2$ remain and two migrate. In $NO$ one member is already dead, so only the live member can be hit and one copy migrates to $OO$. $OO$ is invariant.

*Verification* (exact rational arithmetic; the cycle modulus in the cell index is $\prod q$, **not** $6\prod q$):

| lines | $M$ | $(A,B,C,D)$ | predicted |
|---|---|---|---|
| $\lbrace 5\rbrace$ | 5 | $(3,1,1,0)$ | — |
| $\lbrace 5,7\rbrace$ | 35 | $(15,9,9,2)$ | ✓ |
| $\lbrace 5,7,11\rbrace$ | 385 | $(135,105,105,40)$ | ✓ |
| $\lbrace 5,7,11,13\rbrace$ | 5,005 | $(1485,1395,1395,730)$ | ✓ |

The full cycle state — which grows like $\prod q$ — is thus carried by four integers.

### 2.2 Theorem 1 (conserved quantity and closed solution)

Write $a = A/M$ and so on.

> **Theorem 1.** The quantity $a+b$ is form-invariant, $(a+b)' = (1-1/p)(a+b)$, and consequently
> $$\boxed{(a,b,c,d) = \big(P_2,   P_1-P_2,   P_1-P_2,   1-2P_1+P_2\big)} \tag{2.2}$$
> where $P_1 = \prod_{5\le q\le P}(1-1/q)$ and $P_2 = \prod_{5\le q\le P}(1-2/q)$.

*Proof.* From (2.1) in normalised form,
$$a'+b' = \Big(1-\tfrac2p\Big)a + \Big(1-\tfrac1p\Big)b + \tfrac{a}{p} = a\Big(1-\tfrac2p+\tfrac1p\Big) + \Big(1-\tfrac1p\Big)b = \Big(1-\tfrac1p\Big)(a+b).$$
Since $a+b = 1$ initially, $a+b = P_1$. Also $a' = (1-2/p)a$ with $a=1$ initially gives $a = P_2$. Symmetry gives $b=c$, and $a+b+c+d=1$ supplies $d$. $\blacksquare$

*Verification.* All three identities hold with zero error in exact rational arithmetic for every $p$ from $5$ to $199$.

| $p$ | $a$ | $b$ | $a+b$ | $P_1$ | $P_2$ |
|---|---|---|---|---|---|
| 7 | 0.428571 | 0.257143 | 0.685714 | 0.685714 | 0.428571 |
| 31 | 0.186275 | 0.272282 | 0.458556 | 0.458556 | 0.186275 |
| 199 | 0.085574 | 0.226109 | 0.311684 | 0.311684 | 0.085574 |

### 2.3 Asymptotics

Removing the factors at $2$ and $3$ (whose product is $1/3$) from Mertens' theorem [1],
$$P_1 \sim \frac{C}{\log P}, \quad C = 3e^{-\gamma} = 1.6843785; \qquad P_2 \sim \frac{K}{\log^2 P}, \quad K = 12 C_2 e^{-2\gamma} = 2.4972872. \tag{2.3}$$

*Verification.* Iterating (2.1) to $P = 2\times10^8$: $a\log^2 P \to 2.497274$; and $(1-d)\log P \to 3.37227$ against the predicted $2C = 3.3687569$.

### 2.4 Structural reading

$$\frac{b}{a} \sim \frac{C}{K}\log P = 0.6744833 \log P. \tag{2.4}$$

Fully alive cells — the twin candidates — die like $1/\log^2 P$, whereas half-dead cells die only like $1/\log P$. The flow is always $NN \to NO/ON \to OO$, and the surviving population becomes overwhelmingly $OO$.

**Methodological remark.** Although (2.1) arises from the cell model alone, it dissolves completely into the two classical Mertens products and contains no new quantity. We record it as a fact about the law, not as a disappointment: it is the reason the law is *exact* rather than approximate.

### 2.5 The law is a census, not a simulator

Theorem 1 transports the four counts exactly, and it is easy to read more into that than it says. It does not say that the four states carry enough information to run the process, and they do not.

**The counterexample is two cells.** Take
$$C_4 = (23,\ 25), \qquad C_8 = (47,\ 49).$$
Both end in the same state — one member survives, the other is composite — so both are counted in the same class by Theorem 1 at every depth beyond $7$. But their histories differ: $25 = 5^2$ is struck the moment $L_5$ enters, whereas $49 = 7^2$ is still **alive** at that stage and dies only when $L_7$ enters. So two cells with identical final states occupy different states at an intermediate depth, and the final label does not determine which.

**Consequence, stated as a limitation.** No automaton on the four states reproduces the history of individual cells. To recover that history one needs at least the *owner* (or death stage) of each dead member, which is strictly more information than the final state. **Inheritance depth is different information:** it records how many old lines divide either member, not which line killed a member first and not when that happened. Theorem 2 restores the depth distribution, which is enough for the weighted censuses of §§3–4, but it does **not** turn the four-state census into a history simulator. Ownership is introduced separately in §5.

**And it locates a second reading of the same fact.** The four-state law is exact *because* it forgets: a linear update on four numbers can only exist if the update is independent of everything the four numbers do not record. Owner labels and spatial history are precisely what have to be forgotten for the four-number law to close. So exactness and blindness are two sides of the same compression here — which is the pattern this framework repeats, and the reason Paper III has something to measure at all.

## 3. Theorem 2: the refined law, with generating function

Theorem 1 records how many cells occupy each state. One may ask for more: the distribution of **inheritance depth** across states, where the depth $j$ of a cell is the number of old lines dividing either of its members. This refinement also closes, and in closed form.

> **Theorem 2.** Let $N_{s,j}$ count the cells in state $s$ with inheritance depth $j$. Then the entry of a line $p$ gives
> $$NN_j  \to  (p-2)NN_j + NO_{j+1} + ON_{j+1},$$
> $$NO_j  \to  (p-2)NO_j + NO_{j+1} + OO_{j+1}, \qquad ON \text{ likewise},$$
> $$OO_j  \to  (p-2)OO_j + 2 OO_{j+1}. \tag{3.1}$$
> Equivalently, marking a strike by $x$ and the two rails by $u$ and $v$, the full census is read off from
> $$\boxed{ \prod_{5\le q\le z}\big((q-2) + xu + xv\big). } \tag{3.2}$$

*Proof.* Of the $p$ copies of any cell, exactly two are struck — one on each rail — by [I, Thm 3]. A copy that is struck acquires one further dividing line, hence depth $j+1$; the other $p-2$ copies retain depth $j$. Reading off which rails are affected in each state gives (3.1), and (3.2) is the generating-function form of the same statement, one factor per line. $\blacksquare$

*Verification.* Zero error at $p = 7, 11, 13, 17, 19$, over full cycles up to $M = 1{,}616{,}615$ cells. For the lines up to 19, expanding (3.2) gives
$$NN = 378675 = \prod(q-2),$$
$$NO = ON = 325980x + 106299x^2 + 17000x^3 + 1425x^4 + 60x^5 + x^6,$$
$$OO = 212598x^2 + 102000x^3 + 19950x^4 + 1800x^5 + 62x^6,$$
each matching the direct census exactly. Setting $x = 1$ recovers Theorem 1.

**Two consequences.**

1. **The state space is finite at every depth**, since $j \le \pi(z)$. One does not need to track a continuous weight; the full distribution of depth is a vector of length $O(\pi(z))$, and it transports exactly.

2. **Hence any weight of the form $w = f(\Omega_{\le z})$ is computable exactly on the cycle, for an arbitrary $f$ — including a truncation such as $\max(0, \cdot )$.** Nonlinearity is harmless once one carries the distribution rather than its mean. The restriction to be kept in mind is that $x$ marks *that* a line struck and not *which*: a weight depending on the sizes of the factors is not of this form. We return to both points in §4.

**A negative control worth recording.** The obvious cheaper refinement — binning cells by the *value* of a log-weight into a fixed number of bins — does **not** close: prediction error $0$%, $24$%, $14$%, $10$% at $p = 7, 11, 13, 17$. The exactness depends on refining by a quantity that changes by exactly one under a strike, which the depth $j$ does and a binned weight does not.

---



## 4. Weights on the cycle

### 4.1 What Theorem 2 gives, and what it does not

Weighted sieves attach to each surviving element a weight depending on its factorisation, and deduce an almost-prime from the positivity of the weighted sum. The weight that powers the current explicit results between consecutive squares and cubes (see [V, §7.6] for those) is Richert's [2]:
$$w(a)  =  \lambda  -  \sum_{\substack{p \mid a \cr  z\le p<y}}\Big(1 - \frac{\log p}{\log y}\Big), \qquad \lambda = k+1-k_2,$$
with $z = X^{1/k_1}$ and $y = X^{1/k_2}$; the mechanism is that $w(a) > 0$ forces $\Omega(a) \le k$, so a positive lower bound for $\sum w(a)$ over the sifted set produces an almost-prime. (The constant is $\lambda$, not $1$; with $\lambda = 1$ the weight detects $\Omega \le k_2$ instead.) It is a nonlinear function of the factorisation and, through $\log p/\log y$, of the *sizes* of the factors.

It is tempting to conclude that the framework cannot carry such a weight, since its objects are binary or counts. **That conclusion is half false, and Theorem 2 says which half.** The refined law transports the *full distribution* of inheritance depth, in a finite state space of size $O(\pi(z))$, exactly. Consequently:

> **Corollary 1.** On the full cycle, $\sum_{\text{cells}} f(\Omega_{\le z})$ is computable exactly for an arbitrary function $f$, including a truncation $\max(0,\cdot)$, by reading the coefficients of (3.2).

**So nonlinearity is harmless once one carries the distribution rather than its mean.** The earlier obstruction we recorded — that a truncation cannot be tracked — was an artefact of following only the four totals.

**But $\Omega$ alone is not enough for Richert.** The weight above is not a function of $\Omega_{\le z}$: through $\log p/\log y$ it depends on the *sizes* of the prime factors, whereas the marker $x$ in (3.2) records only *that* a line struck, never which. Four numbers with the same count make the gap concrete: $143,\ 2167,\ 2483,\ 323$ each have exactly two prime factors in $(10,200)$, and their weights at $y = 200$ are $-0.0633,\ 0.4497,\ 0.4754,\ 0.0905$.

### 4.2 Why binning by the *value* of the weight does not work

The cheap repair is to bin cells by the value of a log-weight into a fixed number of bins and carry the bin counts. It does **not** close: prediction error $0$%, $24$%, $14$%, $10$% at $p = 7, 11, 13, 17$. The reason is that a cell's actual weight inside a bin is unknown at the moment $\log p$ is added, so the update is not determined by the state. Exactness needs a refinement by a quantity that changes by **exactly one** under a strike — which the depth does and a binned weight does not. The correct repair therefore refines the *line*, not the *weight*.


### 4.3 Refining the generating function by the size of the line

The obstruction identified in §4.1 is that the marker $x$ in (3.2) records *that* a line struck and never *which*. The repair is to mark by size.

> **Corollary 2.** Let $\beta$ assign to each line a bin. Then on the full cycle
> $$\prod_{5\le q\le z}\big((q-2) + x_{\beta(q)}u + x_{\beta(q)}v\big) \tag{4.1}$$
> transports the **joint distribution of the per-bin strike counts on each rail**, exactly.

*Proof.* Identical to Theorem 2. Of the $p$ copies of any cell exactly two are struck, one on each rail; the only change is that the marker attached to the striking line is $x_{\beta(q)}$ rather than $x$. $\blacksquare$

*Verification.* Full cycle for the lines $5,\dots,19$ ($M = 1{,}616{,}615$ cells): the census predicted by (4.1) agrees with the direct census in **every** state, at $B = 2$ ($90$ states) and $B = 3$ ($180$ states), with no error.

**The cost is polynomial, not exponential.** The state space has size $\prod_b \binom{n_b+2}{2}$, where $n_b$ is the number of lines in bin $b$ — a polynomial of degree $2B$ in $\pi(z)$:

| $z$ | lines | depth only (Thm 2) | $B=2$ | $B=4$ | $B=8$ | unrefined joint, $2^{\pi(z)}$ |
|---|---|---|---|---|---|---|
| 1,000 | 166 | 167 | $1.9\times10^{6}$ | $9.1\times10^{9}$ | $3.3\times10^{15}$ | $\approx10^{50}$ |
| 20,000 | 2,260 | 2,261 | $5.0\times10^{9}$ | $8.2\times10^{15}$ | $6.5\times10^{26}$ | $\approx10^{680}$ |

**And the resolution Richert's weight requires is modest.** Measured on $4\times10^{6}$ cells with $X = 2.4\times10^{7}$ and the parameters $k=3$, $k_1 = 8$, $k_2 = 3.17$ (so $z = 8.4$, $y = 212.9$, $\lambda = 0.83$, and $43$ lines in the weight range), comparing $\sum\max(0,w)$ computed from the binned counts against the exact value:

| bins $B$ | 1 (depth only) | 2 | 4 | 8 | 16 |
|---|---|---|---|---|---|
| relative error | $+40.5$% | $+8.2$% | $+2.0$% | $+0.39$% | $+0.10$% |

The $+40.5$% in the first column is exactly the error of ignoring the sizes, i.e. the gap left by Corollary 1; eight bins close it to $0.4$%.

$$\boxed{ \text{The } \textit{factor-size} \text{ deficit is removable: exact at every resolution, polynomial in } \pi(z),\ 0.4\text{ per cent} \text{ at } B=8. }$$



## 5. Ownership layers

This section changes the bookkeeping object. Sections 2–4 count **cells** and therefore carry the two-rail factor $1-2/q$. Here we assign an owner to each **individual odd integer**, so the corresponding one-point density is $1-1/q$. The ownership decomposition is exact on a full CRT cycle and removes inclusion–exclusion by construction.

### 5.1 Ownership, and disjoint layers

Assign to each odd $n$ its **owner**, the smallest line striking it:
$$O(n) = \min\lbrace q : q \mid n,  q \ne n\rbrace , \qquad O(n) = N \text{ if none.}$$

Thus $O(25) = O(35) = 5$, $O(45) = 3$, $O(49) = 7$, and $O(105) = 3$ — priority resolves every overlap, so $105$ belongs to $3$ alone although $5$ and $7$ also divide it.

> **Theorem 3.** Let $S_{<q}$ denote the survivors of all lines below $q$. Then the ownership layers
> $$E_q  =  q \cdot S_{<q}, \qquad \text{taken from } q^2 \text{ onward},$$
> are pairwise disjoint, and consequently
> $$\mathrm{card}S(I)  =  \mathrm{card}I  -  \sum_q \mathrm{card}E_q(I) \tag{5.1}$$
> **with no inclusion–exclusion corrections.**

*Proof.* If $n$ has owner $q$ then $n = q r$ with $r$ divisible by no line below $q$, i.e. $r \in S_{<q}$; and $n \ge q^2$ since $r \ge q$. Conversely any $q r$ with $r \in S_{<q}$ and $q r \ge q^2$ has least prime factor $q$. So $E_q$ is exactly $\lbrace n : O(n) = q\rbrace$, and distinct owners give disjoint sets. $\blacksquare$

*Verification.* $E_5 = \lbrace 25, 35, 55, 65, 85, 95, 115, 125, \dots\rbrace$ and $E_7 = \lbrace 49, 77, 91, 119, 133, 161, 203, 217, \dots\rbrace$ agree exactly, term by term, with $\lbrace n : O(n) = 5\rbrace$ and $\lbrace n : O(n) = 7\rbrace$.

**A genuine structural gain, and a precise accounting of what it costs.** The $2^{\pi(z)}$ intersection terms vanish by construction — the difficulty does not disappear, it moves: evaluating $\mathrm{card}E_q(I)$ requires knowing how many earlier survivors the layer copies, i.e. the *shape* of $S_{<q}$. **Each layer is a scaled copy of the previous survivor strip**, which is the same statement as the observation that all lines read a common word on a common strip.



### 5.2 Why disjointness repairs the union bound but not the estimate

The layering of §5.1 was reached by asking a specific question: **the union bound over lines fails because it double-counts, so does the failure disappear once the layers are genuinely disjoint?** The answer is instructive, and worth recording because the first half of it is a real gain.

**The union bound.** Each line $q$ strikes at most a fraction $1/q$ of an interval, so the naive bound on the struck fraction is $\sum_q 1/q$. Over odd $q \le z$ this diverges like $\log\log z$ and exceeds $1$ almost immediately — for a window of $100$ cells it is already spent by the fourth line ($40+29+18+15 = 102$). **This failure is caused entirely by double-counting: a number divisible by both $3$ and $5$ is charged twice.**

**The layered count.** By Theorem 3 the layers are disjoint, so no position is charged twice. On a full CRT cycle the struck fraction is exactly $\sum_q |E_q|/|I|$; on a shorter interval the same disjoint identity holds for counts, but the simple product formula below acquires boundary dependence. Comparing the full-cycle densities:

| $z$ | union bound $\sum_q 1/q$ | layered bound $\sum_q \lvert E_q\rvert/\lvert I\rvert$ | survivors |
|---|---|---|---|
| 13 | 0.844 | 0.616 | 0.384 |
| 101 | **1.313** | 0.762 | 0.238 |
| 997 | **1.698** | 0.838 | 0.162 |
| $10^6$ | **2.264** | **0.919** | 0.081 |

$$\boxed{ \text{The layered bound is below } 1 \text{ for every } z, \text{ however many lines are summed.} }$$

**So the summation failure is genuinely repaired: disjointness is exactly the property the union bound lacked.**

**But on the full cycle the repaired sum returns the sieve product and nothing more.** Since each residue class occurs exactly once in every $q$ copies, $|E_q| = \frac{1}{q}|S_{<q}|$ on the full CRT cycle; the layer sizes already contain the product of everything below, and

$$\sum_{q\le z} \frac{|E_q|}{|I|}  =  1 - \prod_{q\le z}\Big(1-\frac1q\Big), \qquad\text{hence}\qquad \frac{|S|}{|I|} = \prod_{q\le z}\Big(1-\frac1q\Big). \tag{5.2}$$

*Verification.* Measured layer fractions in $(P^2, 9P^2)$ at $P = 997$: $|E_3| = 0.3333$, $|E_5| = 0.1333$, $|E_7| = 0.0762$ — matching $1/3$, $2/15$, $8/105$ exactly, and identically at $P = 101$ and $P = 499$.

**The interference did not disappear; it moved.** It is no longer in the intersections — it is inside the size of each layer. Three routes therefore reach the same place:

| route | result |
|---|---|
| naive union bound | diverges |
| **disjoint layers** | $\prod(1-1/q)$ |
| inclusion–exclusion | $\prod(1-1/q)$ |

**The layered form is the cleanest of the three and the only one whose bound never exceeds $1$, but it is not stronger.** Evaluating $|E_q(I)|$ requires $|S_{<q}|$ on the interval $I/q$ — the same problem one level down. That recursion is Legendre's, and its shape and its limitations are classical.



---

## 6. The correlation ladder: transport of the second moment

Sections 2–4 transport counts. This section transports *pairs of counts*, and the outcome settles a question the earlier sections leave open: what is the smallest object that closes under the entry of a new line, if one wants variances and not only means.

### 6.1 The pair indicator and its autocorrelation

Index gap-2 pairs by $x$, the pair being $(2x+1, 2x+3)$, and set $A(x) = 1$ when both members survive the line set, $0$ otherwise. $A$ is periodic with period $M = \prod q$, and $\sum_x A(x) = T = \prod(q-2)$. Define the autocorrelation
$$C(h)  =  \sum_{x \bmod M} A(x) A(x+h).$$

> **Theorem 4.** Under the entry of a line $q$,
> $$C_{\mathrm{new}}(h)  =  K_q(h) C_{\mathrm{old}}(h), \qquad K_q(h) = \begin{cases} q-2, & h \equiv 0 \pmod q,\cr  q-3, & h \equiv \pm1 \pmod q,\cr  q-4, & \text{otherwise,}\end{cases}$$
> and hence $C_Q(h) = \prod_{q \in Q} K_q(h)$ outright, with no cycle of length $M$ ever being built.

*Proof.* For a single line $q$, the pair at $x$ dies exactly when $2x+1 \equiv 0$ or $2x+3 \equiv 0$, i.e. when $x \in \lbrace c, c-1\rbrace$ with $c \equiv -1/2 \pmod q$ — **two consecutive classes**, and that is what makes the ladder descend in steps of one. For the pairs at $x$ and at $x+h$ both to survive, $x$ must avoid
$$\lbrace c,\ c-1\rbrace  \cup \lbrace c-h,\ c-1-h\rbrace ,$$
a union of size $2$, $3$ or $4$ according as $h \equiv 0$, $h \equiv \pm1$, or otherwise modulo $q$. Multiplicativity across the lines is the Chinese remainder theorem. $\blacksquare$

*Verification.* Compared with the definition over the full cycle for the line sets $\lbrace 3,5\rbrace$, $\lbrace 3,5,7\rbrace$, $\lbrace 3,5,7,11\rbrace$ and $\lbrace 3,5,7,11,13\rbrace$ — periods up to $M = 15{,}015$ — at every $h$ from $0$ to $39$: exact in every case. For the last set, $C(0),\dots,C(8) = 1485, 0, 0, 189, 0, 0, 504, 0, 0$.

**A corollary visible in that data.** $K_3(h) = 0$ whenever $h \not\equiv 0 \pmod 3$, because $L_3$ leaves a single class modulo $3$. Hence
$$C(h) = 0 \quad\text{unless}\quad 3 \mid h,$$
and the surviving pairs live on a sublattice. This is the effect of the grid line isolated in its cleanest form.

The five rungs of the ladder now all have meanings: $q$ counts cells, $q-1$ single survivors (§2), $q-2$ one pair, $q-3$ two pairs at distance $\pm1$, and $q-4$ two pairs in general position.

### 6.2 Why no single number closes the second moment

For a window of $L$ consecutive pair slots placed at $s$, write $N_s(L) = \sum_{j<L} A(s+j)$. Averaging over $s$ gives the mean $LT/M$ and, exactly,
$$\mathrm{Var}(N_L)  =  \frac{LT + 2\sum_{h=1}^{L-1}(L-h) C(h)}{M}  -  \Big(\frac{LT}{M}\Big)^{2}, \tag{6.1}$$
with no sampling and no independence assumption anywhere.

> **Corollary 3.** There is no function $f$ with $\mathrm{Var}' = f(\mathrm{Var}, q)$.

*Proof.* By Theorem 4 the entry of $q$ multiplies $C(h)$ by a factor depending on $h \bmod q$. Two line sets with the same variance but different distributions of $C(h)$ across the residue classes of $h$ therefore acquire different variances. $\blacksquare$

*Verification.* The variance of the deviations across square-anchored windows, for the line sets $\lbrace 3\rbrace$, $\lbrace 3,5\rbrace$, $\lbrace 3,5,7\rbrace$, $\lbrace 3,5,7,11\rbrace$, is $0.0741$, $0.1689$, $1.1316$, $2.2880$ — successive ratios $2.28$, $6.70$, $2.02$, with no pattern, as Corollary 3 requires.

**So the minimal object that closes the second moment is the function $C(h)$, not a number.** The four-state census of §2 is exact because a single window count is a linear functional of $A$; a variance is a quadratic one, and quadratic functionals need the correlation itself.

### 6.3 The general pattern, and what it is

Nothing above used $h$ being a single displacement. For any finite pattern of displacements $H$, the same argument gives
$$N_{\mathrm{new}}(H)  =  \big(q - \nu_q(H)\big) N_{\mathrm{old}}(H),$$
where $\nu_q(H)$ is the number of distinct residues modulo $q$ that the pattern forbids. Theorem 4 is the case $|H| = 2$ and §2 the case $|H| = 1$.

**This should be named for what it is.** The resulting product $\prod_q (1 - \nu_q(H)/q)$, suitably normalised, is the singular series of the Hardy–Littlewood $k$-tuple conjecture for the pattern $H$ [1, Ch. 1]. The transport law is therefore not a new object; what §6.1 adds is that the framework produces it by a direct combinatorial count on the cycle, with the ladder $q-2, q-3, q-4$ read off from the geometry of two consecutive forbidden classes rather than assembled from local densities.

**And the limitation is the same as everywhere in this paper.** These laws describe the distribution over *all* phases of the cycle. They say nothing about any one designated phase, and a designated phase is what an application needs.

---

## 7. What is exact here, and what is not

**Exact on the cycle, with proof:** the four-state update and its closed solution (Theorem 1); the refined law and its generating function (Theorem 2); arbitrary weights in $\Omega_{\le z}$ (Corollary 1); the refinement by line size at any resolution (Corollary 2); the disjointness of the ownership layers and the resulting inclusion–exclusion-free count (Theorem 3).

**Measured, not proved:** the cost table and the bin-resolution table of §4.3, which are computations rather than theorems, and the $24$% negative control of §4.2.

**Not addressed here at all:** every theorem above is exact over a full cycle of length $\prod q$. Applications need a window of length $\asymp z^2$. Paper III measures that transfer separately. On the tested windows, soft depth weights transfer very accurately, while the sharp depth-zero indicator shows the familiar deficit near $0.80$. Those are window measurements, not consequences of the exact cycle identities proved here.

**No new bound and no improvement to any known result is claimed.** The survivor density $\prod(1-2/q)$ is the classical $V(z)$ of a sieve of dimension $\kappa = 2$; Theorem 1 dissolves into Mertens products and contains no new constant; Theorem 3 is the least-prime-factor decomposition, and the recursion of §5.2 is Legendre's. What is offered is that several quantities usually carried as estimates are, in these coordinates, identities — and, in the case of weights, that the identity survives a refinement fine enough to be useful.

---


---

## References

The companion papers are cited as [0], [I], [III], [IV].

1. J. Friedlander and H. Iwaniec, *Opera de Cribro*, AMS Colloquium Publications **57**, 2010. — *the Mertens products of §2.3 and the standard form of the weighted sieve against which Corollary 2 is compared.*
2. H.-E. Richert, *Selberg's sieve with weights*, Mathematika **16** (1969), 1–22. — *the weight $w(a)$ discussed in §4; it depends on the sizes of the prime factors, which is precisely what Corollary 1 does not transport and Corollary 2 repairs.*
