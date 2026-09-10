# Paired Almost Primes in Square Windows and in Short Intervals

## Paper 12. A dimension-two sieve on the same window, with certified coefficients, and a measurement of how far four factors are

---

### Abstract

The window between consecutive squares is the habitat of the whole set, and this part approaches it with a different tool: the Diamond–Halberstam–Richert sieve in dimension two, with Richert's logarithmic weights. Two theorems are proved, with one corollary. In every sufficiently large window between consecutive squares there is a pair $(a, a+2)$ with $\Omega(a) \le 5$, $\Omega(a+2) \le 5$ and $\Omega(a) + \Omega(a+2) \le 8$, and the number of such pairs is at least a constant multiple of $m/(\log m)^2$. In an interval of length $X^\theta$ the same argument gives a pair with $\Omega \le 5$ on each side for every $\theta \ge 0.38$, with $\Omega \le 4$ for every $\theta \ge 0.513$, and with $\Omega \le 3$ for every $\theta \ge 0.78$. Read back in the coordinate of the set, the second row says that the window $(m^2, (m+\lceil m^{0.026}\rceil)^2)$ carries a pair with at most four prime factors on each side. The four weight coefficients behind these statements are certified by interval arithmetic. A closing section measures, inside the square window itself, exactly how far the four-factor statement is: the deficit is $0.064861$, it lies almost entirely in the upper sifting function, and 59.1% of that function's weighted excess above $1$ sits above $s = 4.3$. **Nothing here is new sieve theory, and no progress toward the twin-prime conjecture is claimed.** The published results on this pair carry fewer prime factors than Theorem 1 does — Chen's theorem already gives $\gg X(\log X)^{-2}$ pairs below $X$ with $\Omega(n)+\Omega(n+2) \le 3$, and every sufficiently large square window is known to contain a single integer with $\Omega \le 2$ — and §10 sets out those comparisons. What is not in those results is that **every** such window carries a pair.

**Numbering.** This paper is one part of a set that was written as a single document and is now published in parts. Each part numbers its own results from one and is self-contained: a reference of the form [Pn, Thm 1] means Theorem 1 of Paper n, and an unqualified "Theorem 1" always means this paper's own.

**How to read the claims in this paper.** Statements set as Theorems, Propositions and Lemmas are proved, and the proofs are given. Anything described as *measured* is a computation over a stated finite range and is labelled as such where it occurs. The Diamond–Halberstam–Richert theorems and the values of their transition constants are external inputs, taken from [17] and [12] and not reproved here; what is supplied is the verification that their hypotheses hold for these sequences, and rigorous enclosures for the resulting coefficients.

**This part uses no object from the cell system.** No line, no sector, no cell state and no owner appears below. It is placed in this set because it concerns the same window, not because it shares machinery with [P1] to [P11].

**Keywords:** almost primes, square windows, short intervals, dimension-two sieve, Richert weights, interval arithmetic.

**MSC 2020:** 11N35, 11N36, 11N05.

---

## Summary of the results in this part

| Result | What it says | Section |
|---|---|---|
| **Lemma 1** | The exact local count: $A_d = H 2^{\omega(d)}/d + r_d$ with $\lvert r_d\rvert \le 2^{\omega(d)}$, uniform in the position of the interval and independent of its endpoints. | §2 |
| ***The level*** | The absolute remainder majorant, with $D = H(\log U)^{-20}$, supplies a level with exponent $\theta$. No impossibility is claimed for larger levels. | §3 |
| ***The weight identity*** | $W = \eta S(\mathcal A,z) - \sum_p w_p S(\mathcal A_p,z)$, exact, because the two members of a cell are coprime. | §5 |
| **Proposition 1** | Certified lower bounds for the four weight coefficients: $0.91558$ in the square window, then $0.08793$, $0.00621$ and $0.05351$ for the three interval statements. | §6 |
| **Lemma 2** | $B(n) \ge \Omega(n) - u$, so a positive weight forces $\Omega \le r$ on both members and $\Omega(a)+\Omega(a+2) \lt r+1+u$; the integer bound $8$ needs $u = 3$ and is not automatic along the ladder. | §7 |
| **Theorem 1** | Every sufficiently large window between consecutive squares carries $\gg_k m/(\log m)^2$ pairs with $\Omega \le 5$ on each side and $\Omega(a)+\Omega(a+2) \le 8$. | §8 |
| **Theorem 2** | The ladder in $\theta$: pairs with $\Omega \le 5$ each for $\theta \ge 0.38$, with $\Omega \le 4$ for $\theta \ge 0.513$, with $\Omega \le 3$ for $\theta \ge 0.78$. | §8 |
| **Corollary 1** | Back in square-window language: $(m^2,(m+\lceil m^{0.026}\rceil)^2)$ carries a pair with $\Omega \le 4$ on each side, and $(m^2,(m+\lceil m^{0.56}\rceil)^2)$ one with $\Omega \le 3$. | §8 |
| ***Observation*** | The parameter sets are not claimed optimal; an uncertified search puts the three thresholds near $0.3702$, $0.5117$ and $0.7615$. | §8 |
| ***The deficit*** | At the optimised parameters the four-factor coefficient in the square window is $-0.064861$; the lower sifting function is exhausted to within $0.002081$, so nearly all of the room is in $F_2$. | §9 |
| ***Where it sits*** | The weighted excess of $F_2$ above $1$ is $0.325757$, of which 59.1% lies above $s = 4.3$; the required saving is 19.91% across the whole range and does not transfer to a sub-range. | §9 |

---

## 1. Setting

Throughout, $\Omega(n)$ counts prime factors with multiplicity and $\omega(n)$ counts distinct prime factors, so $\Omega(5^2\cdot 7) = 3$ while $\omega(5^2\cdot 7) = 2$. The symbol $P_j$ means an integer with **at most** $j$ prime factors. All logarithms are natural.

Two shapes of ambient interval are carried at once, and everything below is written so that they are the same computation. The **short interval** is $(X, X + X^\theta]$ with $0 \lt \theta \le 1$. The **square window** is $(m^2, (m+k)^2)$; its length is $2km + k^2$, so with $X = m^2$ and $k$ fixed it is of order $X^{1/2}$, the case $\theta = 1/2$. Theorem 1 keeps $k$ fixed. Corollary 1 lets $k$ grow with $m$, and then the length exponent is $(1+\vartheta)/2$ where $k = \lceil m^\vartheta\rceil$; nothing else changes. Write $U$ for the top of the interval.

We look only for pairs of the shape $(6b-1, 6b+1)$. This is a restriction — the pair $(9,11)$ has few factors and is not of that shape — but it costs nothing here, because what is being proved is existence, and a pair found inside a subclass is a pair. Put

$$\mathcal B = \lbrace  b \in \mathbb{Z} : \text{both } 6b-1 \text{ and } 6b+1 \text{ lie in the interval}  \rbrace, \qquad H = \lvert \mathcal B\rvert .$$

Then $H = X^\theta/6 + O(1)$, and in the square-window case $H = km/3 + O_k(1)$.

Three cut-offs are used, governed by two free parameters $w$ and $u$:

$$z = U^{1/w}, \qquad y = U^{1/u}, \qquad D = \frac{H}{(\log U)^{20}},$$

together with

$$P(z) = \prod_{5 \le p \lt z} p, \qquad V(z) = \prod_{5 \le p \lt z}\left(1 - \frac{2}{p}\right).$$

The primes $2$ and $3$ are absent from $P(z)$ and from $V(z)$: the form $6b \pm 1$ excludes them already, and any change of variable must preserve that.

---

## 2. The sifting sequence and its local count

Put $Q(b) = (6b-1)(6b+1)$ and let $\mathcal A = \lbrace Q(b) : b \in \mathcal B \rbrace$, indexed by $b$. For squarefree $d$ coprime to $6$ set

$$A_d = \mathrm{card}\lbrace  b \in \mathcal B : d \mid Q(b)  \rbrace.$$

> **Lemma 1.** For every squarefree $d$ coprime to $6$,
> $\displaystyle A_d = H g(d) + r_d, \qquad g(d) = \frac{2^{\omega(d)}}{d}, \qquad \lvert r_d\rvert \le 2^{\omega(d)} .$

*Proof.* For each prime $p \ge 5$ the congruence $Q(b) \equiv 0 \pmod p$ has exactly two roots, the solutions of $6b \equiv 1$ and $6b \equiv -1$; they are distinct because $p \nmid 2$. By the Chinese remainder theorem $d$ has $2^{\omega(d)}$ roots. The set $\mathcal B$ is an interval of consecutive integers, so each residue class modulo $d$ meets it in $H/d$ elements with absolute error at most $1$. Summing over the $2^{\omega(d)}$ classes gives the statement. $\blacksquare$

Two features of Lemma 1 are used later and are worth naming now. It is **uniform in the position of the interval**, so no averaging over windows enters anywhere; and it **does not use the endpoints**, so the square window and the general short interval are governed by the same estimate. This is why §8 can prove both statements from one apparatus.

---

## 3. Sieve inputs, dimension, and the level

The local density $g(p) = 2/p$ satisfies the dimension-two hypothesis. Mertens' estimates give the required uniform product bound

$$\prod_{v_1 \le p \lt v_2}\left(1 - g(p)\right)^{-1} \ \le\ \left(\frac{\log v_2}{\log v_1}\right)^{2}\left(1 + \frac{A}{\log v_1}\right)$$

for a suitable constant $A$, together with $V(z)$ of order $(\log z)^{-2}$, hence of order $(\log U)^{-2}$.

We use the Diamond–Halberstam–Richert bounds in the form stated in [12, §4, (19)–(20)]: for a sequence of cardinality $X_{\mathcal A}$, density $g$ and remainders $r_d$, sieved at level $M \ge z$, the number of survivors is at most

$$X_{\mathcal A} V(z)\left\lbrace F_2\left(\frac{\log M}{\log z}\right) + O(\varepsilon(M))\right\rbrace  +  O\left(\sum_{d \lt M,\ d \mid P(z)} 4^{\omega(d)}\lvert r_d\rvert\right)$$

and at least the corresponding expression with $f_2$ in place of $F_2$ and the remainder subtracted, where $\varepsilon(M) = (\log\log M)^2(\log M)^{-1/6} \to 0$. The functions $F_2$ and $f_2$ are the dimension-two sifting functions of [17, §4, Thm 2]; $F_2$ decreases monotonically to $1$ and $f_2$ increases monotonically to $1$. The weights are Richert's [20].

With $D = H(\log U)^{-20}$, Lemma 1 gives the unweighted remainder bound

$$R_0 \ \ll \sum_{d \lt D} 8^{\omega(d)} \ \ll\ D (1+\log D)^{7} \ \ll\ \frac{H}{(\log U)^{13}} \ =\ o\left(H V(z)\right), \qquad\text{(3.1)}$$

where the middle step uses $8^{\omega(n)} \le \tau_8(n)$ and the elementary divisor-sum bound. Since $V(z)$ is of order $(\log U)^{-2}$, any logarithmic saving above $9$ would serve; the exponent $20$ is taken for comfort and **is independent of $\theta$**, which matters in §8.

The sieve parameter is

$$s_D = \frac{\log D}{\log z} = \theta w + O\left(\frac{\log\log U}{\log U}\right).$$

**On the level.** The absolute remainder majorant used here is the one in (3.1), of size $O(D(1+\log D)^7)$, and taking $D = H(\log U)^{-20}$ makes it $o(HV(z))$. This supplies a level with exponent $\theta$. It does **not** establish an impossibility result for larger levels, or for differently weighted remainder sums in which cancellation is exploited; nothing below needs one.

---

## 4. Subsums cut by a middle prime

Let $S(\mathcal A, z)$ count the $b \in \mathcal B$ with $\gcd(Q(b), P(z)) = 1$, and for $z \le p \lt y$ let $S(\mathcal A_p, z)$ count those that also satisfy $p \mid Q(b)$. Since $p$ does not divide $P(z)$ it is coprime to every modulus $d \mid P(z)$, and Lemma 1 applied to $pd$ gives

$$\mathrm{card}\lbrace  b \in \mathcal B : pd \mid Q(b) \rbrace = \frac{2H}{p} g(d) + r_{pd}.$$

So the cut sequence has cardinality $2H/p$ and **the same density $g$** on the sifting primes, and the upper bound of §3 applies at level $D/p$. That level is admissible uniformly because $(D/y)/z$ is of order $U^{\theta - 1/u - 1/w}(\log U)^{-20}$, which tends to infinity whenever $\theta - 1/u \gt 1/w$.

The total weighted remainder carries **no factor for the number of primes $p$**. In the product $pd$ every prime factor of $d$ is below $z$, so $p$ is the unique prime factor of $pd$ that is at least $z$, and the map $(p,d) \mapsto pd$ is injective on these sums. Together with $4^{\omega(d)}\lvert r_{pd}\rvert \le 2\cdot 8^{\omega(d)} = \tfrac14 8^{\omega(pd)}$ this gives

$$R_1 = \sum_{z \le p \lt y}\ \sum_{d \lt D/p,\ d\mid P(z)} 4^{\omega(d)}\lvert r_{pd}\rvert \ \ll\ D(1+\log D)^7 = o\left(HV(z)\right). \qquad\text{(4.1)}$$

The bound (4.1) is what makes the sum over $p$ harmless, and it is the reason the interval statements of §8 cost nothing extra in the remainder. The relative errors $\varepsilon(D/p)$ are uniformly $o(1)$ because $\log(D/p)$ is of order $\log U$ throughout, and their weighted sum is $o(1)$ because $\sum_{z \le p \lt y} 1/p = O(1)$.

---

## 5. The weight, and the coefficient it produces

Put

$$w_p = 1 - \frac{\log p}{\log y}, \qquad B(n) = \sum_{\substack{z \le p \lt y \cr  p \mid n}} w_p, \qquad \mathrm{wt}(b) = \eta - B(6b-1) - B(6b+1),$$

with $\eta = r + 1 - u$.

The two members of a cell are coprime: their greatest common divisor divides $2$ and both are odd. Hence no prime is counted twice between them, and

$$W \ :=\ \sum_{\substack{b \in \mathcal B \cr  (Q(b),P(z))=1}} \mathrm{wt}(b) \ =\ \eta S(\mathcal A, z)  -  \sum_{z \le p \lt y} w_p S(\mathcal A_p, z). \qquad\text{(5.1)}$$

The identity (5.1) is exact. Applying the lower bound of §3 to the first term and the upper bound of §4 to the second, then passing from the sum over primes to an integral by partial summation in $t = \log p/\log U$, gives

$$W \ \ge\ H V(z)\lbrace C + o(1) \rbrace, \qquad\text{(5.2)}$$

$$C = C_r(\theta; w, u) = (r+1-u) f_2(\theta w)  -  2\int_{1/w}^{1/u}\left(\frac{1}{t} - u\right) F_2\left(w(\theta - t)\right) dt .$$

The factor $2$ in front of the integral is the two roots of $Q$ modulo $p$. **No second factor of $2$ is inserted for the two members of the cell**: that is carried by those roots already.

For the square window the choice $w = 16$, $u = 3$ gives $\theta w = 8$ and the upper-function argument $8 - 16t$, which is the classical shape.

---

## 6. Certified values of the coefficient

> **Proposition 1.** With the inputs listed below,
> $\displaystyle C_5(1/2; 16, 3) \ \ge\ 0.91558, \qquad C_5(0.38; 23.430, 3.376) \ \ge\ 0.08793,$
> $\displaystyle C_4(0.513; 16.42405, 2.79166) \ \ge\ 0.00621, \qquad C_3(0.78; 10.028, 2.257) \ \ge\ 0.05351 .$

The inputs taken from the literature and **not** reproved are: the dimension-two DHR system as stated in [17, §4, Thm 2]; that $F_2$ decreases to $1$ and $f_2$ increases to $1$; that $\alpha_2$ lies in $[5.3576, 5.3578]$ and $\beta_2$ in $[4.2662, 4.2665]$ — these are the five printed digits of the values $\alpha_2 = 5.3577\ldots$ and $\beta_2 = 4.2664\ldots$ given in [17], rounded outward; and the displayed enclosure of Euler's constant. The transition constants and the explicit formulas are those of [17] and the book [9].

The certificate computes, with outward-rounded interval arithmetic on a grid of step $0.0002$:

- $\sigma_2$ on $(0,4]$ from the two explicit formulas, and on $(4, 5.3578]$ from the integral recursion, enclosing the integrand on each **whole** subinterval. The integrand there needs $\sigma_2(t-2)$ only for $t-2 \le 3.3578$, where the explicit formula applies;
- $F_2 = 1/\sigma_2$ on $(0, 5.3576]$, a range certainly below $\alpha_2$;
- $F_2$ and $f_2$ above that by the two delayed equations, the enclosures coming from monotonicity alone. Since $f_2$ increases, $f_2(t-1)$ lies on $[a,b]$ between $f_2(a-1)$ and $f_2(b-1)$; since $F_2$ decreases, $F_2(t-1)$ lies between $F_2(b-1)$ and $F_2(a-1)$; and the factor $2t$ is integrated exactly, its integral over $[a,b]$ being $b^2 - a^2$. **This is a monotone Riemann enclosure, not a quadrature rule.**

The imprecision in $\alpha_2$ is handled without relying on a decimal place. The function $s^2F_2(s)$ is increasing on the whole range: below $\alpha_2$ because the DHR equation makes $s^{-2}\sigma_2(s)$ decreasing, and above $\alpha_2$ because its derivative is $2s f_2(s-1) \ge 0$. Write $a = 5.3576$ and $b = 5.3578$. Monotonicity of $F_2$ gives $b^2F_2(b) \le b^2F_2(a)$, and monotonicity of $s^2F_2(s)$ gives $b^2F_2(b) \ge a^2F_2(a)$. Those two are the starting values used at $b$, and both integrals run from $b$. This is valid wherever $\alpha_2$ lies in the bracket, and needs no further digit of it.

The endpoints $1/w$ and $1/u$ are not exact decimals, so they are enclosed and the partition covers $[1/w, 1/u]$ from the outside; over-covering is safe because the integrand is non-negative. The integral is then bounded by an upper Riemann sum on $20{,}000$ pieces: the weight $1/t - u$ decreases in $t$ and is taken at the left end of each piece, the argument of $F_2$ decreases in $t$ so $F_2$ is taken at the right end, and the grid lookup uses the lower grid node, which is an upper bound because $F_2$ decreases. The script asserts the four displayed bounds, not merely that each coefficient is positive.

Regenerated by `code/verify_paired_almost_primes.py`, which exits non-zero if any of the four bounds fails.

*A two-point sensitivity test of the implementation.* An independent floating-point solution of the same system, run at $(\alpha_2,\beta_2) = (5.3550, 4.2680)$ and at $(5.3600, 4.2650)$ — displacements twenty-five times the width of the $\alpha_2$ bracket and ten times that of the $\beta_2$ bracket — returns $0.91517$, $0.08838$, $0.00658$, $0.05368$ at the first and $0.91780$, $0.08963$, $0.00761$, $0.05464$ at the second. This checks that the computation does not turn on the fourth or fifth digit of either constant. It is **not** a proof of uniformity over the rectangle between them, and changing a transition constant in a floating-point solve does not by itself produce valid sifting functions. Regenerated by `code/verify_square_window_deficit.py`.

An enclosure that stops the sifting functions at $5.3$ and uses $F_2 \ge 1$ above that point returns less than half of the first of these four numbers. What removes that loss is the march of the two delayed equations described above, so **the improvement is entirely in the enclosure, not in the mathematics**: the coefficients themselves are what they always were.

---

## 7. Repeated factors, and what a positive weight forces

Discard every cell for which $p^2 \mid Q(b)$ for some prime $z \le p \lt y$. Each such $p$ has two roots modulo $p^2$, so the number $E$ of discarded cells satisfies

$$E \ \le\ 2\sum_{z \le p \lt y}\left(\frac{H}{p^2} + 1\right) \ \ll\ \frac{H}{z} + y, \qquad\text{(7.1)}$$

and this is $o(HV(z))$ provided $1/u \lt \theta$.

> **Lemma 2.** Let $(a, a+2)$ be a cell surviving the sieve at $z$ and the deletion above, and let $n$ be either member. Then $B(n) \ge \Omega(n) - u$. Consequently a positive weight forces $\Omega(n) \le r$ on **both** members, and $\Omega(a) + \Omega(a+2) \lt r + 1 + u$.

*Proof.* Every prime factor of $n$ is at least $z$, and after the deletion each prime factor below $y$ occurs exactly once. Hence

$$\Omega(n) - \frac{\log n}{\log y} \ =\ \sum_{p \mid n} v_p(n)\left(1 - \frac{\log p}{\log y}\right) \ \le\ B(n),$$

because the omitted summands, those with $p \ge y$, are non-positive. Since $n \le U = y^u$ — the interval is closed at its upper end, so a member may equal $U$ — this gives $B(n) \ge \Omega(n) - u$. A positive weight means $B(a) + B(a+2) \lt \eta = r+1-u$, and both values of $B$ are non-negative, so each member satisfies $\Omega(n) - u \lt r+1-u$, that is $\Omega(n) \le r$. Adding the two inequalities gives $\Omega(a) + \Omega(a+2) - 2u \lt r+1-u$, so the integer sum is below $r+1+u$. The strictness at both steps comes from the weight, not from the size of $n$. $\blacksquare$

**The sum bound depends on $u$, and this is not a technicality.** The conclusion of Lemma 2 is the strict inequality $\Omega(a)+\Omega(a+2) \lt r+1+u$, so the integer bound it yields is $\lceil r+u\rceil$ when $u$ is not an integer, and $r+u$ when it is. At $r = 5$ and $u = 3$ exactly this reads $\Omega(a)+\Omega(a+2) \le 8$; at $r = 5$ and $u = 3.376$ it reads only $\le 9$. So the bound $8$ accompanies Theorem 1 and **does not** accompany the rows of Theorem 2 whose $u$ exceeds $3$.

Let $W_*$ be the weight sum after the deletion. Every weight is at most $\eta$, so $W_* \ge W - \eta E$, and (5.2), (7.1) and Proposition 1 give $W_* \gt 0$ for every sufficiently large $X$. If $N_+$ is the number of cells of positive weight then $W_* \le \eta N_+$, so $N_+$ is at least a positive constant times $H V(z)$.

---

## 8. The two statements

> **Theorem 1.** Fix $k \ge 1$. There are constants $m_0(k)$ and $c_k \gt 0$ such that for every $m \gt m_0(k)$ the window $(m^2, (m+k)^2)$ contains at least $c_k  m (\log m)^{-2}$ integers $a$ with
> $\displaystyle m^2 \lt a \lt a+2 \lt (m+k)^2, \qquad \Omega(a) \le 5, \quad \Omega(a+2) \le 5, \quad \Omega(a)+\Omega(a+2) \le 8 .$

*Proof.* Take $\theta = 1/2$, $w = 16$, $u = 3$, $r = 5$, so $\eta = 3$. The conditions of §3, §4 and §7 hold: $1/u = 1/3 \lt 1/2$; $\theta - 1/u = 1/6 \gt 1/16 = 1/w$; and $\theta w = 8$ exceeds $\beta_2$. By Proposition 1 the coefficient is at least $0.91558$, so by (5.2) and §7 the weight sum is positive for all large $m$, and the number of positive-weight cells is at least a constant times $H V(z)$, which is of order $m(\log m)^{-2}$. Lemma 2 with $u = 3$ gives the three factor bounds on those cells. $\blacksquare$

> **Theorem 2.** For every $\theta \ge 0.38$ and every sufficiently large $X$, the interval $(X, X+X^\theta]$ contains at least $c(\theta) X^\theta(\log X)^{-2}$ pairs $(n, n+2)$ with $\Omega(n) \le 5$ and $\Omega(n+2) \le 5$. The same holds with $\Omega \le 4$ on each side for every $\theta \ge 0.513$, and with $\Omega \le 3$ on each side for every $\theta \ge 0.78$.

*Proof.* Take the parameter sets of Proposition 1. For each of them $1/u \lt \theta$, namely $0.29621$, $0.35821$ and $0.44306$ against $0.38$, $0.513$ and $0.78$; and $\theta - 1/u \gt 1/w$, namely $0.08379$, $0.15479$ and $0.33694$ against $0.04268$, $0.06089$ and $0.09972$; and $\theta w \gt \beta_2$, namely $8.9034$, $8.4255$ and $7.8218$. Nothing else in §2 to §7 depends on $\theta$: Lemma 1 does not use the endpoints of the interval, and the exponent $20$ in $D$ was chosen independently of $\theta$. The coefficients are positive by Proposition 1 and the conclusion follows as in Theorem 1. A larger $\theta$ is covered by the same parameters: with $w$ and $u$ fixed, raising $\theta$ raises $f_2(\theta w)$ and lowers $F_2(w(\theta-t))$ at every $t$, so $C$ increases. $\blacksquare$

> **Observation.** The parameter sets of Proposition 1 are not claimed to be optimal. An uncertified numerical search locates the thresholds of the three statements of Theorem 2 near $0.3702$, $0.5117$ and $0.7615$. This is a numerical observation and not a proposition, and it is used in no proof.

The first and third rows are set well above their thresholds, so their certified coefficients carry a wide margin. The middle row is deliberately close to its threshold: at $\theta = 0.513$ the certified lower bound is $0.00621$ against a floating-point value of $0.007134$, a difference of about $0.0009$. The certificate still returns a positive value a little below $0.513$; any strictly positive certified bound would serve mathematically, and $0.513$ is chosen only to keep the conclusion several times clear of that difference. *This is a search result and is labelled as such; it is not a theorem, and the thresholds themselves are not certified.*

> **Corollary 1.** For every sufficiently large $m$ the window $(m^2, (m + \lceil m^{0.026}\rceil)^2)$ contains a pair $(a, a+2)$ with $\Omega(a) \le 4$ and $\Omega(a+2) \le 4$, and the window $(m^2, (m + \lceil m^{0.56}\rceil)^2)$ contains a pair with $\Omega \le 3$ on each member.

*Proof.* Write $k = \lceil m^{\vartheta}\rceil$ and $X = m^2$. The window has length $2mk + k^2 \ge 2m^{1+\vartheta} = 2X^{(1+\vartheta)/2}$, so it contains the interval $(X, X + X^{(1+\vartheta)/2}]$. At $\vartheta = 0.026$ that exponent is $0.513$ and at $\vartheta = 0.56$ it is $0.78$, so Theorem 2 applies to the contained interval. $\blacksquare$

**No new uniformity is needed for Corollary 1**, and this is worth saying because the obvious route — rewriting §2 to §7 with $H$ of order $U^{(1+\vartheta)/2}$ and re-checking every remainder sum — is not necessary. A window that contains an interval of the required length inherits the conclusion from that interval.

**The square-window form is the one to compare against Theorem 1.** At $k$ fixed the method gives five factors on each side; at $k = \lceil m^{0.026}\rceil$ it gives four. That is the whole distance, stated in the coordinate the set uses.

**"Sufficiently large" is part of both theorems.** Neither proof computes $m_0(k)$ or the threshold in $X$, because the $o(1)$ of (5.2) is not made explicit by the DHR theorems as used. A separate and deliberately wasteful construction, replacing the DHR functions by explicit linear sieves in a vector-sieve combination in the manner of [4], does yield an explicit threshold; it is far too large to be closed by any computation, and it is not the subject of this paper.

---

## 9. The distance to four factors in the square window

Theorem 2 gives $\Omega \le 4$ on both members at length $X^{0.513}$, and the square window has length $X^{1/2}$ exactly. The certified gap in the exponent is therefore $0.013$, and the uncertified gap of the Observation in §8 about $0.0117$. **Neither is a small increase in length**: $X^{0.013}$ grows without bound, so the two statements are not close in any absolute sense; what is small is the exponent.

In the square-window coordinate of Corollary 1 the same gap reads $k = \lceil m^{0.026}\rceil$ against $k$ fixed. *Measured, with $w$ and $u$ frozen at the values below and only the level raised*: writing the length exponent as $\beta = (1+\vartheta)/2$, the weighted excess $E(\beta)$ falls from $0.325757$ at $\beta = 1/2$ and crosses the deficit at $\beta \approx 0.512719$, that is $\vartheta \approx 0.0254$; allowing the positive term to move with $\beta$ as well gives $\beta \approx 0.512544$ and $\vartheta \approx 0.0251$. At $\beta = 0.513$, and at the parameters $w = 16.42405$, $u = 2.79166$ of that row rather than the frozen pair used for the two crossings, the floating-point coefficient is $+0.007134$ and the certificate returns $+0.00621$. **These are numerical crossings of a coefficient, not theorems**: only $\vartheta = 0.026$ carries a certificate.

The gap can also be measured inside the square window. Optimising the parameters at $\theta = 1/2$ for $r = 4$ gives $w = 16.9155$ and $u = 2.8215$, at which

$$(r+1-u)f_2(\theta w) = 2.176419, \qquad 2\int_{1/w}^{1/u}\left(\frac1t - u\right)F_2\left(w(\tfrac12 - t)\right) dt = 2.241279,$$

$$C_4 = 2.176419 - 2.241279 = -0.064861 .$$

*Everything in the rest of this section is measured*: it comes from an uncertified floating-point solution of the DHR system at those parameters, and it diagnoses where the deficit sits. It is not part of any statement proved above.

### 9.1 The lower sifting function is exhausted

$f_2$ at $8.45775$ is $0.999045$, and its supremum is $1$. Replacing it by that supremum saves about $0.002081$ against a deficit of $0.064861$. **No improvement acting through $f_2$ closes this**, whatever its source: the whole of the positive term is already within 0.1% of the largest value it could ever take.

### 9.2 Where the deficit sits

Write the subtracted estimate as $1.915523 + 0.325757$, the first term being what remains if $F_2$ is replaced by its infimum $1$, and the second the excess above that floor. In the variable $s = w(1/2 - t)$ the excess is

$$E_A = \int_A \rho(s)\left(F_2(s) - 1\right) ds, \qquad \rho(s) = \frac{2}{w}\left(\frac{1}{\tfrac12 - s/w} - u\right),$$

with $s$ running over $2.4625$ to $7.4578$. Since $\rho$ increases with $s$, **a unit of improvement in $F_2$ is worth more at larger $s$** — while the excess still available above a threshold shrinks as the threshold rises, which is why the percentages in §9.3 grow with $S$ even though the weight does. The excess distributes as

| $s$ | weighted excess | share |
|---|---|---|
| $2.4625$ to $2.5$ | $0.0001226$ | 0.04% |
| $2.5$ to $3$ | $0.0193128$ | 5.93% |
| $3$ to $4$ | $0.0846569$ | 25.99% |
| $4$ to $4.3$ | $0.0291653$ | 8.95% |
| $4.3$ to $5$ | $0.0682214$ | 20.94% |
| $5$ to $5.3577$ | $0.0340129$ | 10.44% |
| $5.3577$ to $6$ | $0.0466945$ | 14.33% |
| $6$ to $7.4578$ | $0.0435701$ | 13.38% |

so 59.1% of the weighted excess lies **above** $s = 4.3$. The band carrying the largest single entry, from $s = 3$ to $s = 4$, is not where most of the excess is.

### 9.3 What an improvement would have to achieve

Suppose an upper bound sieve gives $F^*$ with $F^*(s) - 1 \le (1-\lambda)(F_2(s)-1)$ for $s \ge S$, and $F^* = F_2$ below $S$. The saving is then at least $\lambda$ times the excess above $S$, so it is enough that $\lambda E_{\ge S} \gt 0.064861$. Such an $F^*$ would also have to be an upper bound applicable to the same restricted sequences, with remainders that can still be summed at level $D/p$:

| improvement from | $E_{\ge S}$ | $\lambda$ required |
|---|---|---|
| $s \ge 2.4625$ (all of it) | $0.325757$ | 19.91% |
| $s \ge 3.0$ | $0.306321$ | 21.17% |
| $s \ge 3.5$ | $0.267929$ | 24.21% |
| $s \ge 4.0$ | $0.221664$ | 29.26% |
| $s \ge 4.3$ | $0.192499$ | 33.69% |
| $s \ge 5.0$ | $0.124278$ | 52.19% |
| $s \ge 5.3577$ | $0.090265$ | 71.86% |

**A percentage quoted for one range does not transfer to another.** The figure 19.91% across the whole range suffices, while the same 19.91% confined to $2.5 \le s \le 4.3$ saves only about $0.0265$. The criterion is on the weighted integral, never on a percentage alone.

### 9.4 Two qualifications

**First, $F_2$ is not a free parameter inside the DHR system.** The pair $(F_2, f_2)$ is the unique solution of the two delayed equations under the boundary condition that both tend to $1$; lowering one while leaving the other alone does not describe any sieve. An improvement must therefore be an **independent upper bound theorem**, proved by some other construction. The saving is then exactly as tabulated, with no offset, because the lower bound theorem that supplies $f_2$ is a separate theorem and is unaffected by it.

**Second, a smaller required percentage does not mean an easier target.** At $s = 7$ the value of $F_2$ is $1.0204$, so removing a quarter of its excess means proving $1.0153$, tightening a bound already close to its absolute floor of $1$; at $s = 3$ the value is $2.9164$ and the room is far larger. The required percentage and the attainable percentage are different questions, and only the first is measured here.

### 9.5 One further sensitivity

Replacing $F_2$ by the constant $1$ at the parameters above turns $C_4$ into $+0.260896$, and re-optimising the parameters afterwards raises it further. So at these parameters the obstruction is carried by the upper sifting function and not by the size of the positive term. This is a sensitivity measurement only. It does not assert that any part of that range is attainable, since $1$ is not an available upper bound for a count.

---

## 10. Placement

What follows is a bounded source review, not a priority search, and no claim of priority or of absence from the literature is made. **Every published result quoted below is stronger than the ones here in the count of prime factors.** This section says so plainly, identifies where each difference comes from, and states the one thing that is left.

### 10.1 The pair, over the whole range

The record for the pair is Chen's [7]: infinitely many primes $p$ with $\Omega(p+2) \le 2$, and quantitatively $\gg X(\log X)^{-2}$ such $p$ below $X$. That is not a positive density — the primes themselves have density zero — but it is the same order as the count in Theorem 1. In the notation of the almost-prime tuple literature this is $r_2 = 3$, that is, $\Omega(n) + \Omega(n+2) \le 3$ for $\gg X(\log X)^{-2}$ values of $n \le X$, against the $\le 8$ of Theorem 1. The constant in front has been improved repeatedly and is still moving, so none is quoted here.

Selberg's weighted sieve [21] came first and is of a different shape: for $X$ large, the number of $n \le X$ such that one of $n$ and $n+2$ has at most two prime factors and the other at most three is $\gg X(\log X)^{-2}$. It is the split that is its content; in the total it is superseded by Chen. Bombieri's asymptotic sieve [3] gives asymptotic formulas for $\sum_{n \le X}\Lambda_k(n)\Lambda(n+2)$, again over the whole range, and Debouzy [8] localises the smaller factor under the Elliott–Halberstam conjecture. Goldston, Graham, Pintz and Yıldırım [13] prove that the gap between consecutive integers with exactly two prime factors is at most $6$ infinitely often.

**The order of the count is the same, and this should be stated.** Summing the count of Theorem 1 over the windows below $X$ gives $\gg \sum_{m \le \sqrt X} m(\log m)^{-2}$, which is again of order $X(\log X)^{-2}$. Theorem 1 therefore produces no more pairs than [7] or [21] do, and produces them with more prime factors.

The line on almost-prime $k$-tuples that grew out of [21] — Heath-Brown [15], Ho and Tsang [16], Maynard [19], Lewulis [18], Bin Chen [6] — improves the constants $r_k$ for $k \ge 3$ and **does not touch $k = 2$**; Balasubramanian and Srivastav [2] sharpen the constant inside Selberg's own inequality. Evans [11] proves asymptotic formulas for correlations of numbers with exactly two prime factors, valid for almost all shifts $h$ in a range, by the circle method rather than by a sieve — because, as stated there, integers with exactly two prime factors cannot be counted by sieve methods on account of the parity problem, even under the Elliott–Halberstam conjecture.

### 10.2 The single integer, in the same window

On the single-integer side the window is better understood than it is for the pair. Wu [22] proves that $(x - x^{101/232}, x]$ contains a $P_2$ for large $x$, and $101/232 = 0.4353\ldots$, so that interval is **shorter** than a square window near $x$: taking $x = (m+1)^2$, its length $(m+1)^{202/232}$ is below $2m+1$ for large $m$. Hence every sufficiently large window between consecutive squares contains an integer with $\Omega \le 2$.

Against that, Dudek and Johnston [10] showed that every such window contains an integer with at most four prime factors and Campbell [5] improved this to three, **for every $n \ge 1$ and with no threshold**: those are the price of an explicit statement valid in every window, not only in the large ones. Theorem 1 is on the other side of that trade — asymptotic, not explicit — and it is about a pair.

**Corollary 1 is the pair analogue of a move already in print.** Dudek and Johnston [10] close their introduction by noting that their approach should give an integer with at most three prime factors in $(n^3, (n+1)^3)$, and one with at most two in $(n^4, (n+1)^4)$. Lengthening the window to lower the factor count is therefore not new here; what §8 supplies is the same move for a pair at distance $2$, with the exponent measured rather than assumed.

### 10.3 The short-interval lines, and where they stop

There is a line carrying Chen's theorem into short intervals, begun by Ross at $\theta \ge 0.98$ and lowered in steps to $0.97$ through work of Wu, Salerno and Vitolo, Cai and Lu, and Cai; [22] is one of those steps. Each produces a **prime** $p$ in $[x, x+x^\theta]$ with $\Omega(p+2) \le 2$ — a far stronger conclusion in a far longer interval, since $x^{0.97}/x^{1/2} \to \infty$.

The bounded-gap machinery is capped in the same way. Alweiss and Luo [1] carry the Maynard–Tao result into intervals $[x - x^\delta, x]$ for every $\delta \ge 0.525$, and $0.525$ is where it stops because that is the Baker–Harman–Pintz range in which a prime is known to exist at all. The third row of Theorem 2, at $\theta = 0.78$, lies above that ceiling: in an interval of that length [1] gives two genuine primes at bounded distance, and the only thing the present statement adds there is that the distance is exactly $2$.

### 10.4 What is left, and a remark from the same corner of the subject

A count of $\gg X(\log X)^{-2}$ pairs below $X$ does not say that any particular window contains one: a global count is compatible with the pairs clustering, and none of the results in §10.1 locates them. Theorem 1 says that **every** sufficiently large window between consecutive squares contains a pair with $\Omega \le 5$ on each member, with no exceptional windows. That is the only axis on which the statements here are not dominated, and nothing else is claimed.

It is worth recording that the limit measured in §9 is recognised from the other direction as well. Campbell [5] remarks that reaching $\Omega \le 2$ for the single integer lies beyond his framework, that weighted sieves have a natural limitation in that direction — the extremal example in Chapter 5 of Greaves [14] — and that results producing $2$-almost primes in related problems have needed a more flexible input, such as Iwaniec's form of the error term in the linear sieve, which admits bilinear estimates. §9 measures the same wall on the pair side and puts a number on it.

---

## 11. What is and is not established

- Theorems 1 and 2 hold for **every** sufficiently large window, not for most windows and not on average. The uniformity comes from Lemma 1.
- The argument uses no unproved hypothesis about the distribution of primes in these windows.
- The published results on the pair carry fewer prime factors — $\Omega(n)+\Omega(n+2) \le 3$ by Chen — and the count is of the same order; and on the single-integer side every large square window is known to contain an integer with $\Omega \le 2$. §10 states all of this. The only claim made here is the absence of exceptional windows for a pair.
- Nothing here asserts that either member is prime. Nothing here asserts four prime factors on both members of a pair in a square window with $k$ fixed; Corollary 1 reaches four only once $k$ is allowed to grow.
- "Sufficiently large" is part of both statements. No threshold is computed here, and nothing is claimed about any particular window.
- The parameter sets are not claimed optimal, and the thresholds in the Observation of §8 are not certified.
- Everything in §9 is measured, not proved. §3 supplies a level with exponent $\theta$ and claims no impossibility for larger levels.

---

## Reproducing

Two scripts, and they are of different kinds.

`code/verify_paired_almost_primes.py` is the interval certificate. It uses the standard library only and exits non-zero if any of the four coefficients of Proposition 1 fails to be certified positive. Its success means that those four inequalities hold given the literature inputs listed in §6. It does not reprove the DHR theorems, does not verify the thresholds of the Observation in §8, and does not examine any particular window.

`code/verify_square_window_deficit.py` regenerates every measurement quoted in §9 — the deficit, its split into floor and excess, the band table, the table of required savings, the sensitivity of §9.5 and the two crossings in the window-length exponent — together with the stability check of §6, all from floating-point solutions of the same system. It is **not** an enclosure, and the certificate above does not depend on it.

The only numbers in this paper stated without a script are the three thresholds of the Observation in §8, which are labelled there as an uncertified search and are used in no proof.

---

---

*The computations and much of the prose in this paper were prepared with AI assistance (ChatGPT, OpenAI; Claude, Anthropic), used for algebraic derivation, for drafting and rewriting code and text, for running the computations, and for auditing the papers against their own scripts. All statements were checked by the author, who is responsible for them; the repository README sets out the division of labour in full.*
---

## References

The papers of this set are cited as [P1] to [P11], and the numbered entries below are the external works. The two kinds never share a number: a bracket with a P is a companion paper, a bare number is a reference in the list below.

1. R. Alweiss and S. Luo, *Bounded gaps between primes in short intervals*, Res. Number Theory **4** (2018), art. 15.
2. R. Balasubramanian and P. Srivastav, *On Selberg's approximation to the twin prime problem*, arXiv:1504.04347 (2015).
3. E. Bombieri, *On twin almost primes*, Acta Arith. **28** (1975), 177–193; corrigendum, ibid. **28** (1976), 457–461.
4. M. Bordignon, D. R. Johnston and V. Starichkova, *An explicit version of Chen's theorem and the linear sieve*, Int. J. Number Theory **21** (2025), 2497–2572.
5. P. J. Campbell, *On the existence of integers with at most 3 prime factors between every pair of consecutive squares*, arXiv:2603.10356 (2026).
6. B. Chen, *Small gaps between almost-twin primes*, Forum Math. (2025); see also *On almost-prime $k$-tuples*, Int. J. Number Theory **20** (2024), 1525–1544.
7. J.-R. Chen, *On the representation of a large even integer as the sum of a prime and a product of at most two primes*, Sci. Sinica **16** (1973), 157–176.
8. N. Debouzy, *Twins almost prime under an Elliott–Halberstam conjecture*, arXiv:1907.06393 (2019).
9. H. G. Diamond and H. Halberstam, *A Higher-Dimensional Sieve Method*, Cambridge Tracts in Mathematics **177**, Cambridge University Press, 2008.
10. A. W. Dudek and D. R. Johnston, *Almost primes between all squares*, J. Number Theory **278** (2026), 726–745.
11. N. Evans, *Correlations of almost primes*, Math. Proc. Cambridge Philos. Soc. **174** (2023), 301–344.
12. C. S. Franze and P.-H. Kao, *Almost-prime values of reducible polynomials at prime arguments*, arXiv:1812.11280 (2018).
13. D. A. Goldston, S. W. Graham, J. Pintz and C. Y. Yıldırım, *Small gaps between products of two primes*, Proc. London Math. Soc. (3) **98** (2009), 741–774.
14. G. Greaves, *Sieves in Number Theory*, Ergebnisse der Mathematik und ihrer Grenzgebiete (3) **43**, Springer, 2001.
15. D. R. Heath-Brown, *Almost-prime $k$-tuples*, Mathematika **44** (1997), 245–266.
16. K.-H. Ho and K.-M. Tsang, *On almost prime $k$-tuples*, J. Number Theory **120** (2006), 33–46.
17. P.-H. Kao, *Almost-prime polynomials with prime arguments*, arXiv:1606.03505 (2016).
18. P. Lewulis, *Variants of the Selberg sieve and almost prime $k$-tuples*, Q. J. Math. **74** (2023), 327–363.
19. J. Maynard, *3-tuples have at most 7 prime factors infinitely often*, Math. Proc. Cambridge Philos. Soc. **155** (2013), 443–457.
20. H.-E. Richert, *Selberg's sieve with weights*, Mathematika **16** (1969), 1–22.
21. A. Selberg, *Lectures on Sieves*, Collected Papers, Volume II, Springer, 1991, 65–247.
22. J. Wu, *Almost primes in short intervals*, Sci. China Math. **53** (2010), 2511–2524; and *Chen's double sieve, Goldbach's conjecture and the twin prime problem*, Acta Arith. **114** (2004), 215–273.
