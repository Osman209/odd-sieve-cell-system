# The Cell System

## An overview: a coordinate system for the odd sieve — what it proves, what it measures, and where it stops

---

### Abstract

This is a research announcement for six short papers built on one coordinate system for the odd integers. It contains **no proofs**; every statement carries a reference to the paper where it is proved, verified or measured, and every statement is labelled with which of those three it is.

The primitive object is the **line** $L_m(k) = m(m+2k)$, the odd multiples of $m$ from $m^2$ onward. The line $L_3$ has step $6$ and so leaves exactly two odd numbers between consecutive strikes; it is therefore treated not as the first sieving line but as the **coordinate grid**, and the odd integers compress into cells $C_b = (6b-1, 6b+1)$. Against this fixed periodic structure the odd squares slide as a **moving window**, widening by $8$ at each step.

Several quantities usually carried as estimates become identities in these coordinates: the increments of $\lfloor 2j^2/n\rfloor$ have an exact histogram with no error term; the four-state divisor census of the sieve transports exactly and dissolves into two Mertens products; the survivor masks form a martingale on the full cycle with an exact energy identity; the deviations of a whole sequence of sectors reduce to a single sum over primes; and a fixed set of lines leaves a known positive number of fresh gaps each time its cycle returns.

The framework then stops, and it stops in the same place every time. We state that stopping point in the form the construction itself produces: writing $C$ for the surviving cells of a window, $R$ for the composite endpoints inside them and $S$ for the cells with both endpoints composite, one has $T = C - R + S$ exactly for the twin count, hence
$$2(R-C)  =  \sum (-1)^{\Omega(n)}$$
over the endpoints of the surviving cells. The inequality one wants, $R < C$, is therefore precisely the statement that a Liouville sum over the sifted set is negative. **The parity problem is not an obstacle imported from sieve theory; it is what the construction reduces to on its own.**

**No progress toward the twin prime conjecture is claimed, and no new bound.**

---

## How to read this

Every statement below is tagged:

| tag | meaning |
|---|---|
| **P** | **proved**, with a complete proof in the cited paper |
| **V** | **verified** exactly on a stated finite range; a complete symbolic proof is *not* supplied |
| **M** | **measured**; a numerical finding with its controls, not a theorem and not asymptotic |

The six papers, and their dependence:

| | title | depends on |
|---|---|---|
| **0** | *An exact histogram for a quadratic staircase* | — (contains no primes) |
| **I** | *Cells and lines* | — |
| **II** | *The inheritance law on the cycle* | I |
| **III** | *From cycle to window* | 0, I, II |
| **IV** | *The twin criterion in cell coordinates* | 0, I, II, III |
| **V** | *Where the framework stops* | 0, I, II, III, IV |

Papers 0, I and II are independent of one another. **Paper 0 is the only one a reader with no interest in primes can read on its own**, and it is self-contained. Papers IV and V split by genre rather than by topic: **IV contains only theorems, V only measurements and the account of the stopping point.**

---

## 1. The coordinates

**The line.** $L_m(k) = m(m+2k) = (m+k)^2-k^2$, the odd multiples of $m$ from $m^2$ onward. Beginning at $m^2$ makes each line responsible exactly for what no smaller line covers.

**P — [I, Thm 1].** $L_m$ contributes a position that no smaller line already covers **if and only if** $m$ is prime.

**The cell.** $L_3$ has step $6$; between consecutive strikes lie exactly two odd numbers. Hence the grid $C_b = (6b-1, 6b+1)$, in which a twin pair is a cell both of whose members survive.

**P — [I, Thm 2] (the cell map).** With $p = 6a+\sigma$,
$$p(6b+\varepsilon)  =  6 (pb+a\varepsilon) + \sigma\varepsilon,$$
so $L_p$ sends the two members of $C_b$ into the cells $pb-a$ and $pb+a$: two positions symmetric about $pb$ at distance $2a$. **Consequence worth stating separately: the mirror symmetry of a line's fingerprint is not a property of the line. It is inherited from the cell and transported by multiplication.**

**P — [I, Thm 3].** A line closes exactly the two cell positions $j \equiv \pm 6^{-1} \pmod p$, always distinct. So exactly two of every $p$ cells lose a member, one per rail — the factor $(p-2)$ of the sieve product, read as geometry rather than density. In the centre coordinate $x = 6b$ the same law reads $x \equiv \pm1 \pmod p$, with no modular inverse.

**P — [I, Cor 1] (the diamond coordinates).** With $S = a+b$ and $D = a-b$: every line is a level set of $S-D$, the squares are the single axis $D=0$, a line's birth is where its diagonal meets that axis, and the fingerprint law — the alternating gaps $2a,\ p-2a$ with which a line meets the cell axis — is the projection of that one straight line. *(The map is a bijection, so nothing is compressed by it; it is the multiplication table rotated through $45^\circ$.)*

**P — [I, §3.7].** At a square front the additive coordinate of a product changes from a **difference** of the two factors' distances to a **sum** of them, according to whether the factors straddle the square or both exceed it:
$$6t = m(e-d)-de+\lbrace 0,2\rbrace  \quad\text{(straddling)}, \qquad 6t = m(u+v)+uv+\lbrace 0,2\rbrace  \quad\text{(both above)}.$$

---

## 2. The window: an exact histogram, with no error term

For odd $n$ put $W_j = \lfloor 2(j+1)^2/n\rfloor - \lfloor 2j^2/n\rfloor$. In the application $W_j = H_j-2$, where $H_j$ is the number of strikes of a line between consecutive odd squares.

**P — [I, Thms 4, 5] (the window in its own coordinates).** Anchor the sector at a twin-candidate pair, $n = 6a$, $W_a = [(n-1)^2,(n+1)^2]$. Then it is exactly the interval of cell indices $c_0, \dots, c_0+N-1$ with $c_0 = 6a^2-2a+1$ and $N = 4a-1$, and every line is two arithmetic progressions on it. **Its midpoint cell is $(n^2-1, n^2+1)$ with $n^2-1 = (n-1)(n+1)$, so the midpoint is NEVER a twin** — the complement of the six exception positions, which say which cells can be open without being twins.

**P — [I, Thms 6, 7] (the shared index).** Run each layer's two lines on the shared strike number $k = 6j+t$. Then $t = k-6j$ is invariant under the passage to the next window, and two laws are exact in it. **The pair's two members are $4n+4t$ apart against a window of width $4n$, so only the newly born pair has both members inside — every older pair has already opened wider than the window and crosses it in two disjoint passes, family-7 first** ([I, Thm 6]; the two $t$-ranges never overlap, checked over every layer with $a<200$). And **the role of a strike is decided by $t \bmod 3$ alone** — upper rail, lower rail, or wasted on $L_3$ — which gives the one-third waste as a consequence of the coordinate instead of a count ([I, Thm 7]; measured 33.32/33.32/33.36 per cent at $a=1667$).

**M — [I, §4.3], and it is the cleanest form of a fact that recurs throughout.** A line whose modulus reaches $N$ cannot wrap inside the window, so its whole budget is two. At $a = 1667$: the **857** lines below $N$ close **6,500** cells, the **370** lines above it close **20**. And within the small group, the four smallest lines do $80$% of the work while every line above $n/2$ together closes one cell. **The large lines are not weak because they are large, but because the window is shorter than their period — and the threshold is neither $\sqrt n$ nor $n/2$ but the window's own length.**

**P — [0, Thm 1].** $W_j \in \lbrace 0,1,2,3,4\rbrace$ for every odd $n$ and every $j$ in the first cycle. **A square sector contains between two and six strikes of any line, however large — not $O(p)$.**

**P — [0, Thm 2].** With $A = \lfloor (n+7)/8\rfloor$,
$$\mathrm{card}\lbrace W{=}0\rbrace  = \mathrm{card}\lbrace W{=}4\rbrace  = A, \quad \mathrm{card}\lbrace W{=}2\rbrace  = 2A-1, \quad \mathrm{card}\lbrace W{=}1\rbrace  = \mathrm{card}\lbrace W{=}3\rbrace  = \tfrac{n+1}{2}-2A.$$
Verified with zero exceptions for every odd $n \le 200{,}001$.

**Why this is the paper's best result.** A probabilistic model of the same count returns the same answer; sums of this shape normally carry an error of size $\sqrt n\log n$ or $n^{1/3}$. None appears. **The reason is that the intervals tile and the tiling is exact — and the residues $2j^2 \bmod n$ never enter the proof.**

**P — [0, Thms 3, 4].** A symmetric pair of sectors compresses to a single element $d \in \lbrace 0,1,2\rbrace$, and the pair census satisfies $N_2 = N_0+1$: again one integer governs everything.

**P — [0, Thm 5].** The companion statement, and the one that does concern the residues: for odd $n \ge 51$ the sequence $2j^2 \bmod n$ has exactly $2A$ interior local maxima. Computation extends this to every odd $n$ except $3,5,7,9,49$.

*The proof of Theorem 5 turns on three moves and one coincidence: a palindrome symmetry; a transition count replacing the two conditions defining a maximum by one; the observation that the relevant **pairs** of intervals tile once separated by parity; and the fact that the four residues $8x \bmod n$ which arise are always $\pm1,\pm3,\pm5,\pm7$ in some order, so their squares always sum to $84$.*

---

## 3. The cycle: exact transport

**P — [II, Thm 1] (the four-state law).** The census of cells by state $(NN, NO, ON, OO)$ transports exactly under the entry of a new line, and has the closed solution
$$(a,b,c,d) = \big(P_2,\ P_1-P_2,\ P_1-P_2,\ 1-2P_1+P_2\big),$$
with $P_1 = \prod(1-1/q)$ and $P_2 = \prod(1-2/q)$. **The full cycle state — which grows like $\prod q$ — is carried by four integers.**

*And it dissolves completely into the two classical Mertens products, containing no new quantity. We record that as the reason the law is exact rather than approximate.*

**P — [II, Thm 2] (the refined law).** The joint distribution of state and **inheritance depth** also transports exactly, and is read off from the generating function
$$\prod_{5\le q\le z}\big((q-2)+xu+xv\big).$$

**P — [II, Cor 1].** Hence any weight depending on the *count* of prime factors is computable exactly on the cycle. **P — [II, Cor 2]** repairs the one thing Cor 1 cannot carry — dependence on the *sizes* of the factors — by binning, at polynomial rather than exponential cost.

**A limitation stated in the same breath — [II, §2.5].** The four-state law is a **census, not a simulator**. The cells $C_4 = (23,25)$ and $C_8 = (47,49)$ end in the same state, yet $25$ dies when $L_5$ enters while $49$ is still alive until $L_7$ does. No automaton on the four states reproduces the history. **The law is exact precisely because it forgets: a linear update on four numbers can exist only if it is independent of everything those four numbers do not record. Exactness and blindness are two sides of one compression.**

---

## 4. From cycle to window

**P — [III, Thms 1, 2].** An old line appears to a new one as a **periodic ruler** with phase $\phi_q(p) \equiv (q-p)/2 \pmod q$; and for $q \ge 7$, within the first cycle, a square sector is shorter than the ruler's period, so the local question is presence or absence rather than counting. *(Both hypotheses are necessary and both are stated: outside the first cycle a block can hold two marks, and $q=5$ can meet a block of length $6$ twice.)*

**P — [III, Thm 3].** The iterated deviations of a whole sequence of sectors telescope into a **single sum over primes**:
$$2^{\pi(U)} \text{ intersections}  \longrightarrow  \text{one sum}.$$
This is the first point in the framework at which stacking the lines does not blow up.

**P — [III, Thm 4] (martingale).** On the full CRT cycle the normalised survivor masks have orthogonal differences and total energy exactly $1/P_z-1$. **So the primorial is present as a period, but the size of the $L^2$ error does not carry it.**

**M — [III, §3.2].** At moving depth the measured ratio is $T/M \approx 0.80$, stable across three orders of magnitude. At moving depth the sieve variable is $s = 2$ exactly, the scale at which a Buchstab-type correction is expected; the value $0.80$ itself is a measurement.

**V — [III, §4].** A mean law carrying a Legendre symbol, and a square-cycle cancellation identity summing to $-(2/r)$ over a cycle. Both agree with every exact enumeration reported; complete symbolic proofs are not supplied.

**M — [III, §5].** The decisive $L^2$ question. On the tested range the data grow like $U^{3.16}$ against a target base scale $U^2$. **This is evidence against the desired bound at accessible scales, not an asymptotic refutation.**

**M — [III, §6].** The transfer curve. Linear depth weights transfer at ratio $1.0000$ to the reported precision; the truncations $\max(0,1-j/t)$ stay within about $3.2$% of $1$ for tested $t\ge2$; and at $t \le 1$ — exactly the indicator $[j=0]$, which **is** the twin condition in the moving window — the ratio drops to $\approx 0.80$.

A second measurement in the same section replaces the weight by a *pattern*: the cycle law $N_{\mathrm{new}}(H) = (q-\nu_q(H))N_{\mathrm{old}}(H)$ of [II, §6.3] is tested for admissible patterns of up to five cells — a condition on ten integers at once — and transfers at $J/L = 1.0000$ to within the statistical error at $u = 3$ and $u = 4$ ([III, Prop. 2]). **So the two together locate the loss: it is entirely in the one-point density, which carries the Buchstab correction at $s=2$, and not in the correlations built on top of it.**

$$\boxed{ \text{The transfer fails in the one-point density and holds in the correlations, for every pattern tested.} }$$

---

## 5. What the framework decides

**P — [IV, Thm 1] (the gap alphabet).** The gap between consecutive odd composites is only $2$, $4$ or $6$; and **gap $6$ means a twin pair**. So an equivalent form of the twin conjecture: *the maximal possible gap is attained infinitely often.* The cap is free and proved.

**P — [IV, Thm 2] (the ladder).** Gap $2$ occurs infinitely often requiring no prime; gap $4$ occurs infinitely often requiring one prime, by Dirichlet. Gap $6$ needs **two primes simultaneously** and is open. *Dirichlet supplies one prime in a progression; nothing supplies two at a prescribed distance. That is the whole of the remaining distance.*

**P — [IV, Thm 3, Cor 1].** No five survivors at spacing $6$ on one rail beyond the single exception $5,11,17,23,29$; and the full-cycle run counts are $G_k = \prod(q-k)$ — *four laws that are not four phenomena but one ruler with different numbers of marks.*

**P — [IV, Thm 4] (six exception positions).** Switch on every line $p \le M$ in the sector $(M^2,(M+6)^2)$. Then **at most six** cells can be open without being a twin pair, and their positions are explicit:
$$E_M  =  \underbrace{\Big\lbrace \tfrac{2M}{3},\ M+1,\ \tfrac{5M}{3}+2,\ 2M+3\Big\rbrace }_{\text{only if } M+2 \text{ prime}} \cup \underbrace{\Big\lbrace \tfrac{4M}{3}+2,\ 2M+5\Big\rbrace }_{\text{only if } M+4 \text{ prime}} .$$
Verified with zero violations over $3{,}332$ sectors. **This replaces "the lines must leave at least seven gaps" by "they must leave one gap that is not at one of six named places"** — and the six are fixed by the geometry of the square, not chosen by the lines. It is the sharpest form of the twin criterion the framework has produced. *(It is not a route: $C_M$ exceeds the twin count by at most six, so any lower bound on $C_M$ is a lower bound on twins.)*

**P — [IV, Thm 13] (a row reads primality off originality).** Everything on the row of $p$ before $p^2$ is inherited; past it, **$p(p+2j)$ is owned by no smaller line exactly when $p+2j$ is prime**, for $p+2j < p^2$ (1,782,933 checks, no failure). So a row carries one bit of primality per cell up to $p^2$, and the twin condition is "originality survives one step past the diagonal" — the tested cell being $(p+1)^2-1$, which is [I, Thm 5] read along the row rather than across the window. **Exact, geometric, and the twin conjecture verbatim: writing $\sigma(p)$ for the smallest line owning $p(p+2)$, a twin is $\sigma(p) = \infty$.** The suggestion it invites — that if twins were finite each new diagonal point would need a claimant below $\sqrt p$ — does not survive measurement: the claimant is at most 13 in 63.6% of 6,835 cases and at most 100 in 89.9%.

**P — [IV, Thm 5, Cor 2] (one kill per window).** In its own first window $[p^2,(p+2)^2)$ a new line kills **at most one** gap-2 pair, because the grid $L_3$ has already disposed of the other four candidates; and the case of one holds exactly when two primality conditions coincide ($p+2$ prime and $p(p+2)+2$ prime, for $p \equiv 5 \bmod 6$). Verified against the direct count for every prime below $4000$. **So the pair count before the line enters IS the twin count of the window, up to a characterised error of $0$ or $1$** — which is also the cleanest demonstration in the programme that these criteria are reformulations, not reductions.

**P — [IV, Thms 6, 7] (the bridge, and the only law that knows about squares).** Consecutive square windows do not abut: exactly one pair slot falls between them, the pair $((m+2)^2-2, (m+2)^2)$. It obeys a fourth transport law $B' = (q-2-\chi_q(2))B$ with $\chi_q(2)$ the Legendre symbol, so the fingerprint is $(M,S,T,B) \mapsto (qM, (q-1)S, (q-2)T, (q-2-\chi_q(2))B)$ — four degrees, and only the fourth knows the window is anchored at a square. It gives the exact identity $\sum_{i<M} T_{m+2i} = 2(m+M)T - B$, and $B/T$ converges to $2.5622$ with **$\prod(1-\chi_q(2)/q) \to 1/L(1,\chi_8)$, $L(1,\chi_8) = \log(1+\sqrt2)/\sqrt2$.** The square geometry enters through a Dirichlet $L$-value.

**P/M — [IV, §3.7].** The average over **all** square phases has an exact closed form, [IV, (3.4)] [**P**]; numerically it tracks the generic density prediction to within about $1$% from $p=29$ on in the tested sample [**M**]. The question whether square-anchored windows are systematically poor is thereby closed as an identity rather than an experiment; the scatter is governed by the correlation function below, not by any property of squares.

**P — [II, Thm 4] (the correlation ladder).** The autocorrelation of the surviving-pair indicator transports exactly: $C_{\mathrm{new}}(h) = K_q(h) C_{\mathrm{old}}(h)$ with $K_q(h) = q-2, q-3, q-4$ according as $h \equiv 0, \pm1$, or otherwise mod $q$ — the ladder descending in ones because a line forbids **two consecutive** classes. Hence $C(h) = 0$ unless $3 \mid h$, which is the effect of the grid isolated. **Corollary: no single number closes the second moment** — the entry of a line multiplies $C(h)$ by a factor depending on $h \bmod q$, so a variance cannot inherit, and the minimal closing object is the function $C(h)$. The general form $N_{\mathrm{new}}(H) = (q-\nu_q(H))N_{\mathrm{old}}(H)$ is the singular series of the Hardy–Littlewood $k$-tuple conjecture for the pattern $H$.

**P — [IV, Thm 8].** The closing budget $\tau = T-U+Q$ is the exact minimum cover of the distance-$6$ graph.

**P — [IV, Thms 14, 15, Cor 6] (inheritance across sectors).** For any fixed line set with $Q = \prod p_i$ and $S = \prod(p_i-2)$:
$$B(M+6Q) = B(M) + 12S,$$
exactly — a fixed set of old lines never catches the window. A later line closes at most two of the twelve copies of any surviving class, and **at most one** whenever $d_q = \min(\Delta_q, q-\Delta_q) > 11$ with $\Delta_q \equiv (3Q)^{-1} \pmod q$; and the lines able to close two are finite in number, none exceeding $33Q+1$.




**M — the one branch that could have opened, and did not.** The $t \bmod 3$ schedule is asymmetric: a layer hits the upper rail with both members at $t\equiv0$ but the lower rail at opposite residues. Over 1,000 windows the difference between cells closed only above and only below has mean $-1.03$ with sd $20.05$, $t = -1.62$, positive in 47 per cent. **No effect** — and that was the only place in the construction from which a twin-side consequence could have followed.

**P — [IV, Thms 18, 19] (the four outer tracks).** The four cells nearest the window's ends become four tracks as $a$ runs, every member a quadratic $36a^2+Ba+C$. A prime can own a track only where the discriminant is a quadratic residue (Thm 18; 4,209 factor checks, no violation), which makes the tracks **unequal**: Bateman–Horn constants $3.230$, $5.797$, $8.739$, $11.324$ against a generic cell's $12C_2 = 7.922$, so densities $0.41$, $0.73$, $1.10$, $1.43$ — **the fourth track is $3.5\times$ richer in twins than the first, because eleven never divides either of its members while five divides both of the first's.** Predicted against measured at $a = 12$–$30$k: $0.0059/0.0062$, $0.0105/0.0100$, $0.0158/0.0156$, $0.0205/0.0214$.

**P — and the sharp form.** Eligibility for one track admits $3/4$ of primes and for all four exactly $1/4$ — both infinite. But **simultaneous double duty inside one window admits exactly nine primes, $\lbrace 5,7,11,13,19,37,73,89,97\rbrace$, so every $r>97$ closes at most one of the four** (Thm 19; two of the six pairs are outright impossible because the differences are $4$, $6$, $8$). **Restoring the shared variable collapses an infinite set to a finite one — the sharpest local statement in the series after [IV, Cor 6].**

**P — [IV, Prop 2], and this one is a proof of NON-obstruction, which is worth more than another measurement.** The nine-prime constraint is sharp for one line and empty for four. Assign a distinct prime above any bound to each track, take a root of each, and combine by the Chinese remainder theorem: the moduli are coprime, so the shared variable costs nothing. Explicitly, $101 \mid A^-$, $103 \mid B^-$, $107 \mid C^-$, $113 \mid D^-$ give $a \equiv 107{,}106{,}110 \pmod{125{,}782{,}673}$; adjoining $5 \mid q+2$ (so the centre is not a twin either) gives $q \equiv 2{,}906{,}724{,}773 \pmod{3{,}773{,}480{,}190}$, coprime residue and modulus, so Dirichlet supplies infinitely many primes $q$ along it. **Along that progression $q$ is prime, $q+2$ composite, and all four named cells closed — permanently and by construction. Hence no FIXED number of named cells can force a twin; an argument of this shape can only bite when the number of cells grows with the window.**

**P/V — [IV, §7] (the gate belt).** Change the unit from the sector to the belt between consecutive prime gates $q^2$ and $r^2$. It holds exactly $(r^2-q^2)/6-1$ cells and grows like $qg$ (Thm 16), while the line born at its left end can strike only $\lfloor 2g/3\rfloor$ of them — **independent of $q$**, so for a twin gap it touches **one** cell however large $q$ is [**IV** — Verified Law 17, proved under $g^2<2q$, a hypothesis stronger than RH supplies, and verified on 17,981 belts]. Measured, that line closes nothing at all in $71$% of belts below $q=1000$ and $77$% between $1000$ and $5000$, with a maximum of $3$ ever. **The monotone version is false** — in the belt $31\to37$ the closures are $17{:}1$, $19{:}3$, $23{:}2$, $29{:}3$, so a newer line beats two older ones; the weakness is collective, not line by line.

**M — [IV, §7.5], the negative half.** Giving every odd $s$ coprime to 3 the power of an independent line and ignoring all overlap gives a deterministic ceiling per age layer (Prop 1). Summed over the full pyramid down to $s=5$ it **exceeds** the belt: $3.1\times$, $3.5\times$, $5.3\times$ at $q = 499$, $997$, $10007$, passing the belt already at the second layer, and growing like $\tfrac23\log q$ (the sum runs over all $s$ coprime to $6$, not over primes). **So the recent lines are not capacity-limited, and the missing ingredient is the forced overlap — which is $\prod(1-2/q)$, a statement about the cycle.**

**M — [V, §5], and why they do not close it.** At $M = 2319$ the law leaves exactly $1{,}620$ open cells, six distinct lines are needed to erase one family — and $339$ lines reach the sector, supplying a $6.0\times$ oversupply. The $157$ survivors spread over $97$ of the $135$ families at a rate indistinguishable from independent chance. **The constraint binds one line at a time and dissolves in aggregate.**

---

## 6. Where it stops, stated from inside

Fix a window and sieve by every line up to $z$ with $z^3$ above the top of the window. Then **every surviving endpoint is either prime or a product of exactly two primes**, and each such semiprime has a **unique** responsible line, its smaller factor. Writing $C$ for the surviving cells, $R$ for the composite endpoints inside them and $S$ for the cells with both endpoints composite:

**P — [V, Thms 1–3].** After the cut, every surviving endpoint is prime or a product of exactly two primes (Thm 1), each with a unique responsible line (Thm 2), and $T = C - R + S$ exactly (Thm 3). Therefore

$$\boxed{ 2(R-C)  =  \sum_{\text{endpoints of surviving cells}} (-1)^{\Omega(n)} }$$

**(V, Theorem 4.)** So $R < C$ — the inequality one wants — is precisely the statement that a **Liouville sum over the sifted set is negative**.

**Two further findings, both negative and both stated as such.**

- **[V, Thm 5].** The classical Buchstab upper bound for the composite part equals **exactly twice** the corresponding lower-bound sieve function throughout the relevant range. Any purely sieve-theoretic attempt therefore loses a clean factor of two, uniformly in every parameter — and [V, §6.6] locates why Chen's switching principle cannot repair it: it is aimed at the region where the sieve is vacuous, whereas the twin deficit lives where the sieve works.
- **[V, §6.5].** The two natural parameter constraints are incompatible: $R < C$ requires the cut variable below $2e^\gamma = 3.5621$ (more than half the rough numbers prime), while a positive lower bound in dimension two requires $s > \beta_2 = 4.2664$. At the cut this framework actually uses, $u = 3$, the first requirement is closed-form and elementary: the prime proportion tends to $1/(1+\log 2) = 0.5906$, so $R/C \to 0.8188$, and the measured $R/C$ climbs $0.7038 \to 0.7575$ over $X = 10^6 \dots 4\times10^9$ with the whole distance accounted for by the secondary term of the prime number theorem. *(Stated there as a diagnostic, not a criterion — the criterion is [V, Thm 5].)*

**M — [V, §7].** Two test cases, chosen because their answers are known independently: Jacobsthal's function, and almost-primes between squares. In both, the framework reproduces the correct shape and supplies no bound. The failures share one form, and we state it as the framework's defining property rather than as a sequence of accidents.

---

## 7. The pattern

Every exact law in this work is exact **because it forgets something**. The exact cycle laws transport survival state and multiplicative depth; what they do not retain is **ownership** — which line struck a position, and when. Those are different quantities, and [II, §2.5] separates them explicitly. After the depth cut of [V, §6.1] the whole remaining distinction between prime and composite is $\Omega(n) = 1$ against $\Omega(n) = 2$, and that is the quantity none of the laws carry.

- The four-state law closes because it forgets ownership.
- The generating function closes because it counts strikes and not their sizes.
- The martingale is orthogonal because the CRT coordinates are independent.
- The sector inheritance law is exact because the phase is preserved.

And the twin condition is a statement about exactly the discarded coordinate: **both endpoints with total $\Omega(n) = 1$, not $2$** — total multiplicative depth, not the inheritance depth of [II, Thm 2], which the laws do carry. That is why lengthening the window does not help — the layers are the same in any window; why changing coordinates does not help — rotating the multiplication table does not change $\Omega$; and why symmetry does not help — $j^2 = (-j)^2$, so the layer is unchanged.

$$\boxed{ \text{The framework describes motion between the multiplicative layers completely, and does not describe the layer.} }$$

---

## 8. What an external ingredient would have to supply

Not a better bound on the number of strikes, nor a sharper local constraint — the framework has produced several of those and they were absorbed. What is needed is an input that distinguishes $\Omega = 1$ from $\Omega = 2$ inside the sifted set. In the published literature the only machinery that has moved that barrier over the integers is the work on correlations of multiplicative functions in the Matomäki–Radziwiłł–Tao line, and the identity of §6 is a Liouville sum, so it is stated in exactly the language that machinery speaks. We record that as the natural next reading, not as a plan.

---

## References

The six papers: **[0]** *An exact histogram for a quadratic staircase*; **[I]** *Cells and lines*; **[II]** *The inheritance law on the cycle*; **[III]** *From cycle to window*; **[IV]** *The twin criterion in cell coordinates*; **[V]** *Where the framework stops*. Full reference lists are in the individual papers; the works most used are Friedlander–Iwaniec, *Opera de Cribro* (2010); Harman, *Prime-Detecting Sieves* (2007); Richert, *Selberg's sieve with weights* (1969); Diamond–Halberstam, *A higher-dimensional sieve method* (2008); and Polymath, *Variants of the Selberg sieve* (2014).

Verification code accompanies every claim tagged **V** or **M**.
