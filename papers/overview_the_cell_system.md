# The Cell System

## An overview: a coordinate system for the odd sieve — what it proves, what it measures, and where it stops

---

### Abstract

This is a research announcement for six short papers built on one coordinate system for the odd integers. It contains **no proofs**; every statement carries a reference to the paper where it is proved, verified or measured, and every statement is labelled with which of those three it is.

The primitive object is the **line** $L_m(k) = m(m+2k)$, the odd multiples of $m$ from $m^2$ onward. The line $L_3$ has step $6$ and so leaves exactly two odd numbers between consecutive strikes; it is therefore treated not as the first sieving line but as the **coordinate grid**, and the odd integers compress into cells $C_b = (6b-1, 6b+1)$. Against this fixed periodic structure the odd squares slide as a **moving window**, widening by $8$ at each step.

Several quantities usually carried as estimates become identities in these coordinates: the increments of $\lfloor 2j^2/n\rfloor$ have an exact histogram with no error term; the four-state divisor census of the sieve transports exactly and dissolves into two Mertens products; the survivor masks form a martingale on the full cycle with an exact energy identity; the deviations of a whole sequence of sectors reduce to a single sum over primes; and a fixed set of lines leaves a known positive number of fresh gaps each time its cycle returns.

The framework then stops, and it stops in the same place every time. We state that stopping point in the form the construction itself produces: writing $C$ for the surviving cells of a window, $R$ for the composite endpoints inside them and $S$ for the cells with both endpoints composite, one has $T = C - R + S$ exactly for the twin count, hence
$$2(R-C)  =  \sum (-1)^{\Omega(n)}$$
over the endpoints of the surviving cells. The inequality one wants, $R \lt  C$, is therefore precisely the statement that a Liouville sum over the sifted set is negative. **The parity problem is not an obstacle imported from sieve theory; it is what the construction reduces to on its own.**

**No progress toward the twin-prime conjecture is claimed, and no new bound.**

---

## In brief

*Five paragraphs, no tags and no references, for a reader meeting this for the first time. Everything here is restated with citations further down.*

**The object.** Write the odd numbers coprime to $3$ in pairs, $C_j = (6j-1,\ 6j+1)$, and call each pair a **cell**. For an odd $m$, the **line** $L_m$ is the set of odd multiples of $m$ from $m^2$ onward — it begins at $m^2$ because every smaller multiple already lies on a smaller line. A line of prime $p$ meets the cells in exactly two positions, $j \equiv \pm 6^{-1} \pmod p$, so it removes two of every $p$ cells and no line can ever remove both members of one cell. A cell survives all lines up to $z$ when neither member has a prime factor below $z$; a twin pair is a cell that survives all of them.

**What the coordinates buy.** Three things that are usually estimates become exact here. Over one period the surviving cells number $\prod_{5 \le q \le z}(q-2)$, with a closed generating function tracking which rail each line strikes. Inside the interval between consecutive prime squares, a surviving cell is a twin **automatically**, since any composite below $Q^2$ carries a factor below $Q$ and no prime lies between $P$ and $Q$; and the newly born line closes at most one cell of that interval. Within such an interval there are exactly six positions at which a cell can be open without being a twin, and they are given explicitly.

**The cut that makes everything exact.** Sieve only up to $z$ with $z^3$ above the top of the window. Then every surviving endpoint is prime or a product of exactly two primes above $z$, and each composite one is owed exactly one strike, by its smaller factor. Writing $C$ for the surviving cells, $R$ for the composite endpoints inside them and $S$ for the cells with both members composite, the twin count is $T = C - R + S$ — an identity with no error term. Advancing the cut can only lower $R - C$, so a crossing into $R \lt  C$ never reverses.

**Where it stops.** Every criterion in this work reduces to the single inequality $R \lt  C$. Since each surviving endpoint has $\Omega \in \lbrace 1,2\rbrace$, that inequality is *identical* to the statement that $\sum(-1)^{\Omega(n)}$ over the surviving endpoints is negative — a Liouville sum over a sifted set, which is the parity obstruction in its exact form. Equivalently, and with no symbols: **what must be proved is that more than half of the numbers in $(P^2,Q^2)$ with no small prime factor are prime, for every $P$ and not merely on average.** That is a statement about primes in a short interval, not about the sieve, and nothing in these coordinates supplies it.

**What is claimed.** A coordinate system in which several classical quantities are identities rather than approximations; a set of exact local laws inside the interval between prime squares; and a derivation, from inside the construction, of the precise form of the obstruction that stops it. No progress toward the twin prime conjecture, and no new bound. Where a route was tried and closed, the measurement that closed it is recorded, so that it is not tried again.

---

## How to read this

Every statement below is tagged:

| tag | meaning |
|-----|---------------------------------------------------------------------|
| **P** | **proved**, with a complete proof in the cited paper |
| **V** | **verified** exactly on a stated finite range; a complete symbolic proof is *not* supplied |
| **M** | **measured**; a numerical finding with its controls, not a theorem and not asymptotic |

The six papers, and their dependence:

| | title | depends on |
|-----|---------------------------------------------|------------------------|
| **0** | *An exact histogram for a quadratic staircase* | — (contains no primes) |
| **I** | *Cells and lines* | — |
| **II** | *The inheritance law on the cycle* | I |
| **III** | *From cycle to window* | 0, I, II |
| **IV** | *The twin criterion in cell coordinates* | 0, I, II, III |
| **V** | *Where the framework stops* | 0, I, II, III, IV |

Papers 0, I and II are independent of one another. **Paper 0 is the only one a reader with no interest in primes can read on its own**, and it is self-contained. Papers IV and V split by weight of evidence rather than by topic: **IV carries the exact statements — every one an identity, a cap or an explicit list — while V carries the obstruction and the measurements.** Each statement below is tagged, in IV as everywhere else, so that the few measured claims inside IV are not read as theorems.

---

## 1. The coordinates

**The line.** $L_m(k) = m(m+2k) = (m+k)^2-k^2$, the odd multiples of $m$ from $m^2$ onward. Beginning at $m^2$ makes each line responsible exactly for what no smaller line covers.

**P — [I, Thm 1].** $L_m$ contributes a position that no smaller line already covers **if and only if** $m$ is prime.

**The cell.** $L_3$ has step $6$; between consecutive strikes lie exactly two odd numbers. Hence the grid $C_b = (6b-1, 6b+1)$, in which a twin pair is a cell both of whose members survive.

**P — [I, Thm 2] (the cell map).** With $p = 6a+\sigma$,
$$p(6b+\varepsilon)  =  6 (pb+a\varepsilon) + \sigma\varepsilon,$$
so $L_p$ sends the two members of $C_b$ into the cells $pb-a$ and $pb+a$: two positions symmetric about $pb$ at distance $2a$. **Consequence worth stating separately: the mirror symmetry of a line's fingerprint is not a property of the line. It is inherited from the cell and transported by multiplication.**

**P — [I, Thm 3].** A line closes exactly the two cell positions $j \equiv \pm 6^{-1} \pmod p$, always distinct. So exactly two of every $p$ cells lose a member, one per rail — the factor $(p-2)$ of the sieve product, read as geometry rather than density. In the centre coordinate $x = 6b$ the same law reads $x \equiv \pm1 \pmod p$, with no modular inverse.

**P — [I, Cor 3] (a gap around a coincidence).** The $2^k$ ways $k$ lines can split across a cell are the square roots of $1$ modulo their product $P$, and every such cell sits at distance at least $\sqrt{P+1}$ from the point where the $k$ lines meet on $L_3$. So a heavy coincidence has a large fan-out and pushes it far away — the two effects oppose each other.

**P — [I, Cor 4] (the diamond coordinates).** With $S = a+b$ and $D = a-b$: every line is a level set of $S-D$, the squares are the single axis $D=0$, a line's birth is where its diagonal meets that axis, and the fingerprint law — the alternating gaps $2a,\ p-2a$ with which a line meets the cell axis — is the projection of that one straight line. *(The map is a bijection, so nothing is compressed by it; it is the multiplication table rotated through $45^\circ$.)*

**P — [I, §3.7].** At a square front the additive coordinate of a product changes from a **difference** of the two factors' distances to a **sum** of them, according to whether the factors straddle the square or both exceed it:
$$6t = m(e-d)-de+\lbrace 0,2\rbrace  \quad\text{(straddling)}, \qquad 6t = m(u+v)+uv+\lbrace 0,2\rbrace  \quad\text{(both above)}.$$

---

## 2. The window: an exact histogram, with no error term

For odd $n$ put $W_j = \lfloor 2(j+1)^2/n\rfloor - \lfloor 2j^2/n\rfloor$. In the application $W_j = H_j-2$, where $H_j$ is the number of strikes of a line between consecutive odd squares.

**P — [I, Thms 4, 5] (the window in its own coordinates).** Anchor the sector at a twin-candidate pair, $n = 6a$, $W_a = [(n-1)^2,(n+1)^2]$. Then it is exactly the interval of cell indices $c_0, \dots, c_0+N-1$ with $c_0 = 6a^2-2a+1$ and $N = 4a-1$, and every line is two arithmetic progressions on it. **Its midpoint cell is $(n^2-1, n^2+1)$ with $n^2-1 = (n-1)(n+1)$, so the midpoint is NEVER a twin** — the complement of the six exception positions, which say which cells can be open without being twins.

**P — [I, Thms 6, 7] (the shared index).** Run each layer's two lines on the shared strike number $k = 6j+t$. Then $t = k-6j$ is invariant under the passage to the next window, and two laws are exact in it. **The pair's two members are $4n+4t$ apart against a window of width $4n$, so only the newly born pair has both members inside — every older pair has already opened wider than the window and crosses it in two disjoint passes, family-7 first** ([I, Thm 6]; the two $t$-ranges never overlap, checked over every layer with $a\lt 200$). And **the role of a strike is decided by $t \bmod 3$ alone** — upper rail, lower rail, or wasted on $L_3$ — which gives the one-third waste as a consequence of the coordinate instead of a count ([I, Thm 7]; measured 33.32/33.32/33.36 per cent at $a=1667$).

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

**P — [II, Cor 3].** Hence any weight depending on the *count* of prime factors is computable exactly on the cycle. **P — [II, Cor 4]** repairs the one thing Cor 1 cannot carry — dependence on the *sizes* of the factors — by binning, at polynomial rather than exponential cost.

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

**P — [IV, Cor 2] (the dichotomy, and five classes in which it is free).** The six positions are exact quadratics in the sector index, so their state modulo a line is a function of one residue class and the scan over the $35$ classes is a **proof, not a sample**. The lines $5$ and $7$ alone cut six open positions to three, with only four maximal patterns, and no larger line lowers that; but each of $A,D,E$ needs $M+2$ prime and each of $C,F$ needs $M+4$, and all four maximal patterns meet both groups. Hence **no twin at $(M+2,M+4)$ forces $|S_M \cap E_M| \le 2$, so $C_M \ge 3$ already forces a twin** — three open cells rather than seven. Verified over $3{,}332$ sectors with zero violations. In **five** classes $M \equiv 3, 51, 141, 153, 201 \pmod{210}$ the two lines close all six, so every open cell is a twin and the requirement drops to $C_M \ge 1$: measured over $713$ such sectors, $444{,}958$ open cells and **zero** non-twins, against $155$ non-twin survivors in the ordinary sectors below $3{,}000$ alone. The restriction costs nothing — survivor density in the five classes against all others is $0.934 / 0.997 / 1.000$ at $M \lt 4000 / 12000 / 30000$ — and it is an instance of the **W-trick** [V, §8.7].

**P — [IV, §3.3] (the exception budget over a full period, and the limit of local arguments).** Sectors tile, so a prime forced at the top of one is forced near the bottom of the next. Over a full period of $35$ sectors the per-phase caps sum to $5\cdot0+20\cdot1+10\cdot2 = 40$; three adjacent pairs cannot both attain their caps, giving $37$; and admitting $11,13,17$ and scanning all $2431$ alignments gives $\sum_i |S_{M_i}\cap E_{M_i}| \le 31$ under the twinless hypothesis, attained in $9$ alignments. **That ceiling is not lowered by any finite set of lines, and this is a theorem rather than a report of failed attempts.** The $9$ extremal alignments carry $28$ maximal configurations; adding the quadratic conditions on each cell's partner member kills $27$ of them by a fixed prime divisor. The survivor sits at $M_0 \equiv 448353 \pmod{510510}$ with $59$ irreducible polynomials of total degree $90$, is admissible at every prime, and by the Chinese remainder theorem survives any finite list of further lines. The birth order of the lines adds nothing either: a collision would need two offsets differing by $1$ or $3$, and every offset is even. **So the escapee's survival is equivalent to simultaneous primality in the setting of Schinzel's Hypothesis H** — killing it would contradict that prediction rather than weaken the twin problem.

**P/M — [IV, §3.4] (blocks of periods, and the order of the ceiling).** The same question over $L$ consecutive periods gives $B_1 = 31$, $B_3 = 67$, $B_5 = 100$, $B_7 = 138$, $B_9 = 163$ — the first three certain, the last two stable lower bounds — so the requirement per sector falls $0.914, 0.648, 0.577, 0.567, 0.521$. The reason is the **quadratic shadow**: each exception type forbids $2+\chi_2(q)$ classes for $A, C$ and $3+\chi_{11}(q)$, $3+\chi_{14}(q)$, $3+\chi_2(q)$ for $D, E, F$, so the five index sets are sifted in dimensions $2,2,3,3,3$ and $B_L \ll L/\log^2 L$ (Proposition 1). *(The dimension count and the Selberg upper bound are standard; what is particular here is the input — the five partners of Theorem 4 and the characters they carry.)* Two consequences: the density of hiding places tends to zero, and the two-sector types are rarer than the one-sector types by a full logarithm, so a long block **simplifies**. *(And it is not a route: since $B_L = o(L)$ the criterion asks only that a positive proportion of sectors hold one open cell — which by Theorem 4 is a twin up to six named places. The requirement became an existence statement, not a growth rate, and the framework supplies neither. Measured, the survivor total is flat at about $10{,}470$ per sector and exceeds $B_L$ by a factor rising through $11{,}810$, $16{,}419$, $20{,}270$.)*

**P — [IV, Thm 10] (a row reads primality off originality).** Everything on the row of $p$ before $p^2$ is inherited; past it, **$p(p+2j)$ is owned by no smaller line exactly when $p+2j$ is prime**, for $p+2j \lt  p^2$ (1,782,933 checks, no failure). So a row carries one bit of primality per cell up to $p^2$, and the twin condition is "originality survives one step past the diagonal" — the tested cell being $(p+1)^2-1$, which is [I, Thm 5] read along the row rather than across the window. **Exact, geometric, and the twin conjecture verbatim: writing $\sigma(p)$ for the smallest line owning $p(p+2)$, a twin is $\sigma(p) = \infty$.** The suggestion it invites — that if twins were finite each new diagonal point would need a claimant below $\sqrt p$ — does not survive measurement: the claimant is at most 13 in 63.6% of 6,835 cases and at most 100 in 89.9%.

**P — [IV, Thm 5, Cor 2] (one kill per window).** In its own first window $[p^2,(p+2)^2)$ a new line kills **at most one** gap-2 pair, because the grid $L_3$ has already disposed of the other four candidates; and the case of one holds exactly when two primality conditions coincide ($p+2$ prime and $p(p+2)+2$ prime, for $p \equiv 5 \bmod 6$). Verified against the direct count for every prime below $4000$. **So the pair count before the line enters IS the twin count of the window, up to a characterised error of $0$ or $1$** — which is also the cleanest demonstration in the programme that these criteria are reformulations, not reductions.

**P — [IV, Thms 6, 7] (the bridge, and the only law that knows about squares).** Consecutive square windows do not abut: exactly one pair slot falls between them, the pair $((m+2)^2-2, (m+2)^2)$. It obeys a fourth transport law $B' = (q-2-\chi_q(2))B$ with $\chi_q(2)$ the Legendre symbol, so the fingerprint is $(M,S,T,B) \mapsto (qM, (q-1)S, (q-2)T, (q-2-\chi_q(2))B)$ — four degrees, and only the fourth knows the window is anchored at a square. It gives the exact identity $\sum_{i\lt M} T_{m+2i} = 2(m+M)T - B$, and $B/T$ converges to $2.5622$ with **$\prod(1-\chi_q(2)/q) \to 1/L(1,\chi_8)$, $L(1,\chi_8) = \log(1+\sqrt2)/\sqrt2$.** The square geometry enters through a Dirichlet $L$-value.

**P/M — [IV, §3.7].** The average over **all** square phases has an exact closed form, [IV, (3.3)] [**P**]; numerically it tracks the generic density prediction to within about $1$% from $p=29$ on in the tested sample [**M**]. The question whether square-anchored windows are systematically poor is thereby closed as an identity rather than an experiment; the scatter is governed by the correlation function below, not by any property of squares.

**P — [II, Thm 4] (the correlation ladder).** The autocorrelation of the surviving-pair indicator transports exactly: $C_{\mathrm{new}}(h) = K_q(h) C_{\mathrm{old}}(h)$ with $K_q(h) = q-2, q-3, q-4$ according as $h \equiv 0, \pm1$, or otherwise mod $q$ — the ladder descending in ones because a line forbids **two consecutive** classes. Hence $C(h) = 0$ unless $3 \mid h$, which is the effect of the grid isolated. **Corollary: no single number closes the second moment** — the entry of a line multiplies $C(h)$ by a factor depending on $h \bmod q$, so a variance cannot inherit, and the minimal closing object is the function $C(h)$. The general form $N_{\mathrm{new}}(H) = (q-\nu_q(H))N_{\mathrm{old}}(H)$ is the singular series of the Hardy–Littlewood $k$-tuple conjecture for the pattern $H$.

**P — [IV, App. B].** The closing budget $\tau = T-U+Q$ is the exact minimum cover of the distance-$6$ graph. *(An auxiliary model: its object is a prime pair $(p,p+6)$, not a twin pair, and Paper IV places it in an appendix for that reason.)*

**P — [IV, Thms 11, 12, Cor 6] (inheritance across sectors).** For any fixed line set with $Q = \prod p_i$ and $S = \prod(p_i-2)$:
$$B(M+6Q) = B(M) + 12S,$$
exactly — a fixed set of old lines never catches the window. A later line closes at most two of the twelve copies of any surviving class, and **at most one** whenever $d_q = \min(\Delta_q, q-\Delta_q) \gt  11$ with $\Delta_q \equiv (3Q)^{-1} \pmod q$; and the lines able to close two are finite in number, none exceeding $33Q+1$.


**M — the one branch that could have opened, and did not.** The $t \bmod 3$ schedule is asymmetric: a layer hits the upper rail with both members at $t\equiv0$ but the lower rail at opposite residues. Over 1,000 windows the difference between cells closed only above and only below has mean $-1.03$ with sd $20.05$, $t = -1.62$, positive in 47 per cent. **No effect** — and that was the only place in the construction from which a twin-side consequence could have followed.

**P — [IV, Thms 15, 16] (the four outer tracks).** The four cells nearest the window's ends become four tracks as $a$ runs, every member a quadratic $36a^2+Ba+C$. A prime can own a track only where the discriminant is a quadratic residue (Thm 15; 4,209 factor checks, no violation), which makes the tracks **unequal**: Bateman–Horn constants $3.230$, $5.797$, $8.739$, $11.324$ against a generic cell's $12C_2 = 7.922$, so densities $0.41$, $0.73$, $1.10$, $1.43$ — **the fourth track is $3.5\times$ richer in twins than the first, because eleven never divides either of its members while five divides both of the first's.** Predicted against measured at $a = 12$–$30$k: $0.0059/0.0062$, $0.0105/0.0100$, $0.0158/0.0156$, $0.0205/0.0214$.

**P — and the sharp form.** Eligibility for one track admits $3/4$ of primes and for all four exactly $1/4$ — both infinite. But **simultaneous double duty inside one window admits exactly nine primes, $\lbrace 5,7,11,13,19,37,73,89,97\rbrace$, so every $r\gt 97$ closes at most one of the four** (Thm 16; two of the six pairs are outright impossible because the differences are $4$, $6$, $8$). **Restoring the shared variable collapses an infinite set to a finite one — the sharpest local statement in the series after [IV, Cor 6].**

**P — [I, Cor 1] (which forbidden position a twin row can occupy).** Of the two positions a line closes, $-1$ is never occupied by a twin pair and $+1$ only at the line's own birth index: $+1$ is birth first and closure thereafter, $-1$ closure always. Verified over 428 primes against every twin pair below 20,000, zero exceptions. The point of stating it is that the birth index is a permanent exception to any law written over residue classes.

**P — [I, Cor 2] (a diamond centre needs a third row).** For distinct twin pairs $C_a, C_b$ none of the four primes $6a\pm1$, $6b\pm1$ reaches the centre $C_{6ab}$; zero strikes over 6,320 ordered pairs. Arithmetically small — a prime does not divide another prime — but the phase reading says why: multiplying by the phase $+1$ cannot move an admissible phase onto a forbidden one.

**M — [II, Cor 1] (the third channel).** Marking separately the strike a line spends on the grid of 3 gives $\prod((q-3)+u+v+w)$, refining Theorem 2 without changing any cell count; for $\lbrace5,7\rbrace$ the 15 open cells split $8+6+1$. Measured over 234,237 cells, the channel carries no information about which open cells are twin pairs — every conditional rate within 3% of the base.

**M — [II, Cor 2] (the same test one layer up).** The centre of the diamond of $C_a, C_b$ is the cell of index $6ab$, whose phase is the product of the two phases, so the gates $\pm1$ decide again; exactly $(p-3)^2+1$ of the $(p-2)^2$ open phase pairs keep the centre open. Conditional and residue-only, and the birth index is an exception — at $p=5$ it accounts for all 49 failures among 11,175 pairs of twin indices.

**M — [IV, Prop 2] (a window synchronised with its lines).** The primes dividing $p+1$ complete whole cycles inside $(p^2,(p+2)^2)$, so their census there is four exact identities with no edge term. It is not about twins — 273 non-twin values of $p$ satisfy it too — and not a reduction: the surviving fraction 0.3502 is the ordinary sieve value 0.3506.

**M — [IV, Prop 3] (the three mirror channels).** Reflecting the window about $(p+1)^2$ exchanges the two Legendre intervals it is glued from; a single line can close both cells of a mirror pair only through $p(p+2)$, $(p+1)^2$ or $(p+1)^2+1$. The first channel is empty exactly for a twin, the second is the synchronised set, the third is not empty in general (375 and 657 lines at $p = 5741, 10007$). And the reflection settles nothing: the halves carry equal survivor counts every time while the twin counts differ.

**M — [IV, §3.8] (two constructions that do not help).** A window can be designed so every line of a bundle makes the same number of strikes — possible iff $p_{\max}/p_{\min} \lt  1+1/r$ — but sliding it leaves the incidence census identical in every window (48, 24, 12, 8, 6, 4, 2, 1) and the word itself only rotated, so the arrangement is not a degree of freedom separate from the count. And the ownership route (a strike $N=pm$ is new for $p$ iff $\mathrm{spf}(m)\ge p$; $p^3\ge Q^2$ forces the cofactor prime) ends at Buchstab's decomposition: even in that clean layer only 40, 24 and 19 per cent of raw strikes are new.

**P/M — [IV, §3.9] (a proved lower bound on the survivor count).** Writing $m(d)$ for the number of lines striking a cell and $S_i = \sum_d \binom{m(d)}{i}$, the odd Bonferroni truncation $C_M \ge S_0 - S_1 + \cdots - S_{2\ell+1}$ holds for every $\ell$ [**P**], and is **exact** once the order reaches $\max_d m(d)$ [**P**]. This is the first proved lower bound on $C_M$ in the series; every earlier value was a direct count. Measured [**M**]: order three is exact to $M = 21$, order five to $141$, order seven to $381$; and $\max_d m(d) = 9, 10, 11, 12, 13$ at $M = 10^3, 10^4, 5\cdot10^4, 2\cdot10^5, 10^6$, so the order needed grows like $\log\log M$ against $\pi(10^6) = 78{,}498$ lines. **What it does not buy:** a theorem needs uniform control of $S_1,\dots,S_j$ for $j \asymp \log\log M$, sums over $j$-tuples of primes of the shape that makes $S_1$ diverge.

**M — [V, §3.5] (the resources are not the obstruction).** Give the lines the same count of residue classes but choose them greedily instead of at $\pm 6^{-1}$: the window is covered **completely** at $m = 101, 499, 1009, 2001, 4001, 10007, 20011, 50021, 100003$ — zero survivors against $8, 13, 27, 50, 70, 161, 263, 571, 995$ for the true classes, with $9{,}591$ lines and $66{,}669$ cells at the top. So no argument about size, count, capacity, step or window length can work, since it would prove the greedy case too.

**P/M — [IV, §3.11] (smoothing the window, and where it does not reach).** Three exact statements [**P**]: the sector-index errors are odd about their own centre, $e_d(d-2-s) = -e_d(s)$ with $e_d(d-1) = 0$; a Fejér window of half-width $H$ has, writing $H = qd+s$, discrepancy **exactly** $s(d-s)/(dH) \le d/(4H)$, attained at $b = 0$; and sliding it linearly under a second triangle in time gives $\ll d^3/(HT^2)$, with a sharp exponent.

**Almost all of this is classical and cited as such** — the Cesàro weight and its self-convolution form in this arithmetic setting [IV, ref. 2], the pointwise Fejér estimate carrying the same constant [IV, ref. 6], the $\csc^4$ sum [IV, ref. 4], and, at $H = T$, the Fourier multiplier as a Jackson kernel up to normalisation. **The one thing not located anywhere is the exact discrepancy formula**; note that the pointwise estimate summed over frequencies overshoots $d/(4H)$ by a factor near $3.3$, so it does not give it.

Since a triangle is a positive average of sharp windows, a smoothed bound above $2$ still certifies three real survivors in the sector. Measured [**M**]: the gain on $L_7$ is a factor of nine at $M = 50{,}001$ ($-7{,}494 \to -791$), and the sign still does not change. **On our reading the route is closed by where the mass sits:** the share of $S_i$ with $d \lt r$ is $90$%, $45$%, $9$%, $0.2$%, $0$% for $i = 1,\dots,5$, so the smoothing controls the term that died at $M = 21$ and none of the terms that decide the sign. **And smoothing the survivor mask as a whole is closed by an equivalence:** the primorial drops out of the condition, but the least admissible half-width turns out to be half the largest gap in the survivor set, so the statement one would have to prove is a bound on Jacobsthal's function — a restatement, not a reduction, and weaker than the three survivors at a prescribed centre that [IV, §3.1] needs.

**Placement — [IV, §3.10].** The finite-window diagnosis was reached independently, and stated almost identically, by Nguyen (Preprints.org, 2026) in the Goldbach setting: symmetric pairs about a multiple of a primorial, so fixed sum where ours is fixed difference. The correspondence is term by term — with one point of care he raised himself: his conservative avoiding set $U(C)$ and his terminal set $T(C)$ differ by endpoint-prime exceptions, and they coincide here only because the window sits above $M^2$ while every line is at most $M$. The Bonferroni evaluation above is imported from there, and the two measurements above were not made there. Cited as contemporaneous independent work; it is a preprint, not peer reviewed, and claims no Goldbach theorem.

**P — [IV, Prop 5], and this one is a proof of NON-obstruction, which is worth more than another measurement.** The nine-prime constraint is sharp for one line and empty for four. Assign a distinct prime above any bound to each track, take a root of each, and combine by the Chinese remainder theorem: the moduli are coprime, so the shared variable costs nothing. Explicitly, $101 \mid T_1^-$, $103 \mid T_2^-$, $107 \mid T_3^-$, $113 \mid T_4^-$ give $a \equiv 107{,}106{,}110 \pmod{125{,}782{,}673}$; adjoining $5 \mid q+2$ (so the centre is not a twin either) gives $q \equiv 2{,}906{,}724{,}773 \pmod{3{,}773{,}480{,}190}$, coprime residue and modulus, so Dirichlet supplies infinitely many primes $q$ along it. **Along that progression $q$ is prime, $q+2$ composite, and all four named cells closed — permanently and by construction. Hence no FIXED number of named cells can force a twin; an argument of this shape can only bite when the number of cells grows with the window.**

**P/V — [IV, §6] (the gate belt).** Change the unit from the sector to the belt between consecutive prime gates $q^2$ and $r^2$. It holds exactly $(r^2-q^2)/6-1$ cells and grows like $qg$ (Thm 13), while the line born at its left end can strike only $\lfloor 2g/3\rfloor$ of them — **independent of $q$**, so for a twin gap it touches **one** cell however large $q$ is [**IV** — Verified Law 14, proved under $g^2\lt 2q$, a hypothesis stronger than RH supplies, and verified on 17,981 belts]. Measured, that line closes nothing at all in $71$% of belts below $q=1000$ and $77$% between $1000$ and $5000$, with a maximum of $3$ ever. **The monotone version is false** — in the belt $31\to37$ the closures are $17{:}1$, $19{:}3$, $23{:}2$, $29{:}3$, so a newer line beats two older ones; the weakness is collective, not line by line.

**M — [IV, §6.5], the negative half.** Giving every odd $s$ coprime to 3 the power of an independent line and ignoring all overlap gives a deterministic ceiling per age layer ([IV, Prop 4]). Summed over the full pyramid down to $s=5$ it **exceeds** the belt: $3.1\times$, $3.5\times$, $5.3\times$ at $q = 499$, $997$, $10007$, passing the belt already at the second layer, and growing like $\tfrac23\log q$ (the sum runs over all $s$ coprime to $6$, not over primes). **So the recent lines are not capacity-limited, and the missing ingredient is the forced overlap — which is $\prod(1-2/q)$, a statement about the cycle.**

**M — [V, App. C.2.3], and why they do not close it.** At $M = 2319$ the law leaves exactly $1{,}620$ open cells, six distinct lines are needed to erase one family — and $339$ lines reach the sector, supplying a $6.0\times$ oversupply. The $157$ survivors spread over $97$ of the $135$ families at a rate indistinguishable from independent chance. **The constraint binds one line at a time and dissolves in aggregate.**

---

## 6. Where it stops, stated from inside

Fix a window and sieve by every line up to $z$ with $z^3$ above the top of the window. Then **every surviving endpoint is either prime or a product of exactly two primes**, and each such semiprime has a **unique** responsible line, its smaller factor. Writing $C$ for the surviving cells, $R$ for the composite endpoints inside them and $S$ for the cells with both endpoints composite:

**P — [V, Thms 1, 2, 4].** After the cut, every surviving endpoint is prime or a product of exactly two primes (Thm 1), each with a unique responsible line (Thm 2), and $T = C - R + S$ exactly (Thm 4). Therefore

$$\boxed{ 2(R-C)  =  \sum_{\text{endpoints of surviving cells}} (-1)^{\Omega(n)} }$$

**(V, Theorem 6.)** So $R \lt  C$ — the inequality one wants — is precisely the statement that a **Liouville sum over the sifted set is negative**.

**Two further findings, both negative and both stated as such.**

- **[V, Thm 3] (the deficit cannot rise).** Advancing the cut changes $R-C$ by $-\sum(k-1)$ over the cells just closed, where $k$ counts the strikes they still owed; so the deficit is non-increasing and a crossing never reverses. Verified at all 169 cuts for $P=1009$ and all 304 for $P=2003$. Read with the line that follows it: at the final cut $R-C = -T$, so "a crossing exists" is the same statement as "a twin exists", and only the non-reversal is new.
- **[V, Thm 5] (overlap as a resource).** Splitting the pairs of future lines into those piling on one member ($A$) and those splitting across the cell ($B$) gives the unconditional bound $T \ge C-R+\tfrac23A+\tfrac19B$, with both coefficients extremal in that shape. It is the one place in this work where the estimates needed run the other way — an upper bound for $R$, lower bounds for $A$ and $B$ — and the free model puts the critical cut exponent at $0.50681$ against $0.60653$ for $R\lt C$ alone. Measurement then shows the model overstates $A$ (ratios $0.18$–$0.90$, rising as the exponent falls), so the honest threshold is near $0.54$.
- **[V, §2.3] (the covariance form, and the sharpest statement of the wall).** A four-state tally of the surviving cells gives $T/C = (1-u)(1-v) + \kappa$, with $u, v$ the composite rates on the two rails and $\kappa$ their covariance; twins vanish exactly when $\kappa$ reaches its Frechet floor $-(1-u)(1-v)$, and the Buchstab masses at $u_B = 3$ realise that state exactly. Measured over 793 sectors, $\kappa$ sits at $+0.00005$ of the floor and collapses by an order of magnitude per range. So the missing statement is about a correlation between the rails, not a density and not a sieve.
- **[V, Thm 7].** The classical Buchstab upper bound for the composite part equals **exactly twice** the corresponding lower-bound sieve function throughout the relevant range. Any purely sieve-theoretic attempt therefore loses a clean factor of two, uniformly in every parameter — and [V, §3.3] locates why Chen's switching principle cannot repair it: it is aimed at the region where the sieve is vacuous, whereas the twin deficit lives where the sieve works.
- **[V, §3.2].** The two natural parameter constraints are incompatible: $R \lt  C$ requires the cut variable below $2e^\gamma = 3.5621$ (more than half the rough numbers prime), while a positive lower bound in dimension two requires $s \gt  \beta_2 = 4.2664$. At the cut this framework actually uses, $u = 3$, the first requirement is closed-form and elementary: the prime proportion tends to $1/(1+\log 2) = 0.5906$, so $R/C \to 0.8188$, and the measured $R/C$ climbs $0.7038 \to 0.7575$ over $X = 10^6 \dots 4\times10^9$ with the whole distance accounted for by the secondary term of the prime number theorem. *(Stated there as a diagnostic, not a criterion — the criterion is [V, Thm 5].)*

**M — [V, App. C.1] (five routes through the line geometry, closed by measurement).** The same question put to the lines rather than to the sieve, in one explicit window ($M_0 = 448{,}353$, $z = 5857$, $R = 1{,}049{,}024$ cells surviving the cut, of which $T = 366{,}120$ are twins). Prime gaps carry no bias across twenty-nine gap classes, with a $q$-binned control flat to four decimals. The capacity of the lines above the cut does not bound the output but **equals** it — $857{,}712$ against $H = 857{,}695$, a difference of seventeen — which is [V, Thm 2] read as a statement about capacity. The two members of a cell are independent to three parts in a thousand, with the sign of the deviation changing between windows. The two small factors of a doubly-composite cell are independent at $z = -0.26$. And the exact Bézout relation $as-pb=1$ that every such cell carries is **local**: no two consecutive cells are Farey neighbours and nothing telescopes to the ends of the window. Two by-products: the region in which the sieve is vacuous holds $59.4$ per cent of the composite endpoints, which is the number [V, §3.3] states only qualitatively; and the weaker requirement recorded in [V, §2.3] is *identically* $T \gt 0$, so it is not a weaker route but the conclusion itself.

**P/M — [V, §8.6] (the singular series, and a withdrawn order).** The correlation product is the Hardy–Littlewood series of the quadruple $\lbrace -1,1,6h-1,6h+1\rbrace$ normalised by the square of the twin constant, $\mathfrak{S} = 24C_2^2 S_B(h)$, and its mean is exactly $1$ (two proofs). An earlier draft fitted the error over $H \le 4\times10^5$, got a coefficient near $0.85$ that drifted, and reported $O(\log H)$; extending to $H = 37{,}182{,}145$ shows the drift was the curvature of a quadratic, and **$O(\log H)$ is withdrawn**. The consequence is that the two logarithms cancel and the sub-Poisson dispersion is a genuine limit rather than a vanishing correction. **A drifting coefficient is a wrong model, not a noisy one.**

**M — [V, §8.7] (the narrowest form of the requirement).** One does not need to kill the escapee: $\sum_i C_{M_i} \ge 32$ suffices, since the thirty-second survivor has no room inside $E$. Measured, that sum is $1{,}337$ at $k=1$ and $196{,}948$ at $k=1000$, flat in $B_k\log^2 M_0/M_0$ from $k=20$ onward. **Exceeded by a factor of six thousand and still unproved** — and lengthening the window does not help, since a constant multiple of the length buys nothing against $\beta_2$; only a power of $M_0$ would.

**M — [V, §8].** Two test cases, chosen because their answers are known independently: Jacobsthal's function, and almost-primes between squares. In both, the framework reproduces the correct shape and supplies no bound. The failures share one form, and we state it as the framework's defining property rather than as a sequence of accidents.

---

## 7. The pattern

Every exact law in this work is exact **because it forgets something**. The exact cycle laws transport survival state and multiplicative depth; what they do not retain is **ownership** — which line struck a position, and when. Those are different quantities, and [II, §2.5] separates them explicitly. After the depth cut of [V, §2.1] the whole remaining distinction between prime and composite is $\Omega(n) = 1$ against $\Omega(n) = 2$, and that is the quantity none of the laws carry.

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
