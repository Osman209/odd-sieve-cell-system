# Paired Almost Primes in Square Windows and in Short Intervals

## Paper 12. A dimension-two sieve on the same window, with certified coefficients, and the exact distance to four factors

---

### Abstract

The window between consecutive squares is the habitat of the whole set, and this part approaches it with a different tool: the Diamond–Halberstam–Richert sieve in dimension two, with Richert's logarithmic weights. Two statements are proved. In every sufficiently large window between consecutive squares there is a pair $(a, a+2)$ with $\Omega(a) \le 5$, $\Omega(a+2) \le 5$ and $\Omega(a) + \Omega(a+2) \le 8$, and the number of such pairs is at least a constant multiple of $m/(\log m)^2$. In an interval of length $X^\theta$ the same argument gives a pair with $\Omega \le 5$ on each side for every $\theta \ge 0.38$, with $\Omega \le 4$ for every $\theta \ge 0.514$, and with $\Omega \le 3$ for every $\theta \ge 0.78$. Read back in the coordinate of the set, the second row says that the window $(m^2, (m+\lceil m^{0.028}\rceil)^2)$ carries a pair with at most four prime factors on each side. The four weight coefficients behind these statements are certified by interval arithmetic. A closing section measures, inside the square window itself, exactly how far the four-factor statement is: the deficit is $0.064861$, it lies almost entirely in the upper sifting function, and 59.1% of it sits above $s = 4.3$. **Nothing here is new sieve theory, and no progress toward the twin-prime conjecture is claimed.**

**Numbering.** This paper is one part of a set that was written as a single document and is now published in parts. Each part numbers its own results from one and is self-contained: a reference of the form [Pn, Thm 1] means Theorem 1 of Paper n, and an unqualified "Theorem 1" always means this paper's own.

**How to read the claims in this paper.** Statements set as Theorems, Propositions and Lemmas are proved, and the proofs are given. Anything described as *measured* is a computation over a stated finite range and is labelled as such where it occurs. The Diamond–Halberstam–Richert theorems and the values of their transition constants are external inputs, taken from [6] and [5] and not reproved here; what is supplied is the verification that their hypotheses hold for these sequences, and rigorous enclosures for the resulting coefficients.

**This part uses no object from the cell system.** No line, no sector, no cell state and no owner appears below. It is placed in this set because it concerns the same window, not because it shares machinery with [P1] to [P11].

**Keywords:** almost primes, square windows, short intervals, dimension-two sieve, Richert weights, interval arithmetic.

**MSC 2020:** 11N35, 11N36, 11N05.

---

## Summary of the results in this part

| Result | What it says | Section |
|---|---|---|
| **Lemma 1** | The exact local count: $A_d = H 2^{\omega(d)}/d + r_d$ with $\lvert r_d\rvert \le 2^{\omega(d)}$, uniform in the position of the interval and independent of its endpoints. | §2 |
| ***The level ceiling*** | The remainder treatment used here caps the level of distribution at the length of the interval. A limitation of the method, not an impossibility. | §3 |
| ***The weight identity*** | $W = \eta S(\mathcal A,z) - \sum_p w_p S(\mathcal A_p,z)$, exact, because the two members of a cell are coprime. | §5 |
| **Proposition 1** | Certified lower bounds for the four weight coefficients: $0.9103678$ in the square window, then $0.0826730$, $0.0070773$ and $0.0499296$ for the three interval statements. | §6 |
| **Lemma 2** | A positive weight forces $\Omega \le r$ on both members and $\Omega(a)+\Omega(a+2) \lt r+1+u$; the integer bound $8$ needs $u = 3$ and is not automatic along the ladder. | §7 |
| **Theorem 1** | Every sufficiently large window between consecutive squares carries $\gg_k m/(\log m)^2$ pairs with $\Omega \le 5$ on each side and $\Omega(a)+\Omega(a+2) \le 8$. | §8 |
| **Theorem 2** | The ladder in $\theta$: pairs with $\Omega \le 5$ each for $\theta \ge 0.38$, with $\Omega \le 4$ for $\theta \ge 0.514$, with $\Omega \le 3$ for $\theta \ge 0.78$. | §8 |
| **Corollary 1** | Back in square-window language: $(m^2,(m+\lceil m^{0.028}\rceil)^2)$ carries a pair with $\Omega \le 4$ on each side, and $(m^2,(m+\lceil m^{0.56}\rceil)^2)$ one with $\Omega \le 3$. | §8 |
| **Proposition 2** | The parameter sets are not claimed optimal; an uncertified search puts the three thresholds near $0.3702$, $0.5117$ and $0.7615$. | §8 |
| ***The deficit*** | At the optimised parameters the four-factor coefficient in the square window is $-0.064861$; the lower sifting function is exhausted to within $0.00208$, so all of the room is in $F_2$. | §9 |
| ***Where it sits*** | The weighted excess of $F_2$ above $1$ is $0.325741$, of which 59.1% lies above $s = 4.3$; the required saving is 19.91% across the whole range and does not transfer to a sub-range. | §9 |

---

## 1. Setting

Throughout, $\Omega(n)$ counts prime factors with multiplicity and $\omega(n)$ counts distinct prime factors, so $\Omega(5^2\cdot 7) = 3$ while $\omega(5^2\cdot 7) = 2$. The symbol $P_j$ means an integer with **at most** $j$ prime factors. All logarithms are natural.

Two shapes of ambient interval are carried at once, and everything below is written so that they are the same computation. The **short interval** is $(X, X + X^\theta]$ with $0 \lt \theta \le 1$. The **square window** is $(m^2, (m+k)^2)$ for a fixed $k \ge 1$; its length is $2km + k^2$, which is of order $X^{1/2}$ with $X = m^2$, so it is the case $\theta = 1/2$. Write $U$ for the top of the interval.

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

We use the Diamond–Halberstam–Richert bounds in the form stated in [5, §4, (19)–(20)]: for a sequence of cardinality $X_{\mathcal A}$, density $g$ and remainders $r_d$, sieved at level $M \ge z$, the number of survivors is at most

$$X_{\mathcal A} V(z)\left\lbrace F_2\left(\frac{\log M}{\log z}\right) + O(\varepsilon(M))\right\rbrace  +  O\left(\sum_{d \lt M,\ d \mid P(z)} 4^{\omega(d)}\lvert r_d\rvert\right)$$

and at least the corresponding expression with $f_2$ in place of $F_2$ and the remainder subtracted, where $\varepsilon(M) = (\log\log M)^2(\log M)^{-1/6} \to 0$. The functions $F_2$ and $f_2$ are the dimension-two sifting functions of [6, §4, Thm 2]; $F_2$ decreases monotonically to $1$ and $f_2$ increases monotonically to $1$. The weights are Richert's [7].

With $D = H(\log U)^{-20}$, Lemma 1 gives the unweighted remainder bound

$$R_0 \ \ll \sum_{d \lt D} 8^{\omega(d)} \ \ll\ D (1+\log D)^{7} \ \ll_k\ \frac{H}{(\log U)^{13}} \ =\ o\left(H V(z)\right), \qquad\text{(3.1)}$$

where the middle step uses $8^{\omega(n)} \le \tau_8(n)$ and the elementary divisor-sum bound. Since $V(z)$ is of order $(\log U)^{-2}$, any logarithmic saving above $9$ would serve; the exponent $20$ is taken for comfort and **is independent of $\theta$**, which matters in §8.

The sieve parameter is

$$s_D = \frac{\log D}{\log z} = \theta w + O\left(\frac{\log\log U}{\log U}\right).$$

**The level cannot be pushed past the interval, by the method used here.** The remainders are estimated in absolute value, and $\lvert r_d\rvert$ is typically of size $1$ rather than smaller, so the sum in (3.1) is of order $D$ from below as well as above. Since $H V(z)$ is of order $H(\log U)^{-2}$, the requirement that the remainder be $o(HV(z))$ already forces $D$ below $H$ by a power of a logarithm, whatever the sieve weights are. That is a limitation of estimating the remainders in absolute value, which is what is done above; it is **not** asserted that no argument exploiting cancellation in a weighted remainder sum could do better.

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
> $\displaystyle C_5(1/2; 16, 3) \ \ge\ 0.9103678, \qquad C_5(0.38; 23.430, 3.376) \ \ge\ 0.0826730,$
> $\displaystyle C_4(0.514; 16.3683, 2.7828) \ \ge\ 0.0070773, \qquad C_3(0.78; 10.028, 2.257) \ \ge\ 0.0499296 .$

The inputs taken from the literature and **not** reproved are: the dimension-two DHR system as stated in [6, §4, Thm 2]; that $F_2$ decreases to $1$ and $f_2$ increases to $1$; that $\alpha_2$ lies in $[5.356, 5.360]$ and $\beta_2$ in $[4.266, 4.268]$; and the displayed enclosure of Euler's constant. The transition constants and the explicit formulas are those of [6] and the book [3].

The certificate computes, with outward-rounded interval arithmetic on a grid of step $0.0005$:

- $\sigma_2$ on $(0,4]$ from the two explicit formulas, and on $(4, 5.360]$ from the integral recursion, enclosing the integrand on each **whole** subinterval;
- $F_2 = 1/\sigma_2$ on $(0, 5.356]$, a range certainly below $\alpha_2$;
- $F_2$ and $f_2$ above that by the two delayed equations, the enclosures coming from monotonicity alone. Since $f_2$ increases, $f_2(t-1)$ lies on $[a,b]$ between $f_2(a-1)$ and $f_2(b-1)$; since $F_2$ decreases, $F_2(t-1)$ lies between $F_2(b-1)$ and $F_2(a-1)$; and the factor $2t$ is integrated exactly, its integral over $[a,b]$ being $b^2 - a^2$. **This is a monotone Riemann enclosure, not a quadrature rule.**

The imprecision in $\alpha_2$ is handled without relying on a decimal place. The function $s^2F_2(s)$ is increasing on the whole range: below $\alpha_2$ because the DHR equation makes $s^{-2}\sigma_2(s)$ decreasing, and above $\alpha_2$ because its derivative is $2s f_2(s-1) \ge 0$. So for an upper bound one may start from $\alpha_2 \le 5.360$ and integrate from $5.356$, and for a lower bound start from $5.356$ and integrate from $5.360$; both are valid wherever $\alpha_2$ lies in the bracket.

The integral is bounded by an upper Riemann sum on $6{,}000$ pieces: the weight $1/t - u$ decreases in $t$ and is taken at the left endpoint, the argument of $F_2$ decreases in $t$ so $F_2$ is taken at the right endpoint, and the grid lookup uses the lower grid point, which is an upper bound because $F_2$ decreases.

*Measured stability.* An independent floating-point computation with the same enclosure structure keeps all four coefficients positive for $\alpha_2$ anywhere in $[5.30, 5.42]$ and $\beta_2$ anywhere up to $4.30$, the worst corner giving $0.0682$, $0.0231$ and $0.0327$ for the three interval coefficients. That rectangle is far wider than the precision of the published constants.

Regenerated by `code/verify_paired_almost_primes.py`, which exits non-zero if any of the four bounds fails.

Proposition 1 supersedes the weaker bound $C \gt 0.4432$ obtained by stopping the sifting functions at $5.3$ and using $F_2 \ge 1$ beyond that point. **The improvement is entirely in the enclosure, not in the mathematics.**

---

## 7. Repeated factors, and what a positive weight forces

Discard every cell for which $p^2 \mid Q(b)$ for some prime $z \le p \lt y$. Each such $p$ has two roots modulo $p^2$, so the number $E$ of discarded cells satisfies

$$E \ \le\ 2\sum_{z \le p \lt y}\left(\frac{H}{p^2} + 1\right) \ \ll\ \frac{H}{z} + y, \qquad\text{(7.1)}$$

and this is $o(HV(z))$ provided $1/u \lt \theta$.

> **Lemma 2.** Let $(a, a+2)$ be a cell surviving the sieve at $z$ and the deletion above, and let $n$ be either member. Then $B(n) \gt \Omega(n) - u$. Consequently a positive weight forces $\Omega(n) \le r$ on **both** members, and $\Omega(a) + \Omega(a+2) \lt r + 1 + u$.

*Proof.* Every prime factor of $n$ is at least $z$, and after the deletion each prime factor below $y$ occurs exactly once. Hence

$$\Omega(n) - \frac{\log n}{\log y} \ =\ \sum_{p \mid n} v_p(n)\left(1 - \frac{\log p}{\log y}\right) \ \le\ B(n),$$

because the omitted summands, those with $p \ge y$, are non-positive. Since $n \lt U = y^u$ this gives $B(n) \gt \Omega(n) - u$. A positive weight means $B(a) + B(a+2) \lt \eta = r+1-u$, and both values of $B$ are non-negative, so each member satisfies $\Omega(n) - u \lt r+1-u$, that is $\Omega(n) \le r$. Adding the two inequalities gives $\Omega(a) + \Omega(a+2) - 2u \lt r+1-u$, so the integer sum is below $r+1+u$. $\blacksquare$

**The sum bound depends on $u$, and this is not a technicality.** The conclusion of Lemma 2 is the strict inequality $\Omega(a)+\Omega(a+2) \lt r+1+u$, so the integer bound it yields is $\lceil r+u\rceil$ when $u$ is not an integer, and $r+u$ when it is. At $r = 5$ and $u = 3$ exactly this reads $\Omega(a)+\Omega(a+2) \le 8$; at $r = 5$ and $u = 3.376$ it reads only $\le 9$. So the bound $8$ accompanies Theorem 1 and **does not** accompany the rows of Theorem 2 whose $u$ exceeds $3$.

Let $W_*$ be the weight sum after the deletion. Every weight is at most $\eta$, so $W_* \ge W - \eta E$, and (5.2), (7.1) and Proposition 1 give $W_* \gt 0$ for every sufficiently large $X$. If $N_+$ is the number of cells of positive weight then $W_* \le \eta N_+$, so $N_+$ is at least a positive constant times $H V(z)$.

---

## 8. The two statements

> **Theorem 1.** Fix $k \ge 1$. There are constants $m_0(k)$ and $c_k \gt 0$ such that for every $m \gt m_0(k)$ the window $(m^2, (m+k)^2)$ contains at least $c_k  m (\log m)^{-2}$ integers $a$ with
> $\displaystyle m^2 \lt a \lt a+2 \lt (m+k)^2, \qquad \Omega(a) \le 5, \quad \Omega(a+2) \le 5, \quad \Omega(a)+\Omega(a+2) \le 8 .$

*Proof.* Take $\theta = 1/2$, $w = 16$, $u = 3$, $r = 5$, so $\eta = 3$. The conditions of §3, §4 and §7 hold: $1/u = 1/3 \lt 1/2$; $\theta - 1/u = 1/6 \gt 1/16 = 1/w$; and $\theta w = 8$ exceeds $\beta_2$. By Proposition 1 the coefficient is at least $0.9103678$, so by (5.2) and §7 the weight sum is positive for all large $m$, and the number of positive-weight cells is at least a constant times $H V(z)$, which is of order $m(\log m)^{-2}$. Lemma 2 with $u = 3$ gives the three factor bounds on those cells. $\blacksquare$

> **Theorem 2.** For every $\theta \ge 0.38$ and every sufficiently large $X$, the interval $(X, X+X^\theta]$ contains at least $c(\theta) X^\theta(\log X)^{-2}$ pairs $(n, n+2)$ with $\Omega(n) \le 5$ and $\Omega(n+2) \le 5$. The same holds with $\Omega \le 4$ on each side for every $\theta \ge 0.514$, and with $\Omega \le 3$ on each side for every $\theta \ge 0.78$.

*Proof.* Take the parameter sets of Proposition 1. For each of them $1/u \lt \theta$, namely $0.29621$, $0.35935$ and $0.44306$ against $0.38$, $0.514$ and $0.78$; and $\theta - 1/u \gt 1/w$, namely $0.08379$, $0.15465$ and $0.33694$ against $0.04268$, $0.06109$ and $0.09972$; and $\theta w \gt \beta_2$, namely $8.9034$, $8.4133$ and $7.8218$. Nothing else in §2 to §7 depends on $\theta$: Lemma 1 does not use the endpoints of the interval, and the exponent $20$ in $D$ was chosen independently of $\theta$. The coefficients are positive by Proposition 1 and the conclusion follows as in Theorem 1. A larger $\theta$ is covered by the same parameters: with $w$ and $u$ fixed, raising $\theta$ raises $f_2(\theta w)$ and lowers $F_2(w(\theta-t))$ at every $t$, so $C$ increases. $\blacksquare$

> **Proposition 2.** The parameter sets of Proposition 1 are not claimed to be optimal. An uncertified numerical search locates the thresholds of the three statements of Theorem 2 near $0.3702$, $0.5117$ and $0.7615$.

The first and third rows are set well above their thresholds, so their certified coefficients carry a wide margin. The middle row is deliberately close to its threshold: at $\theta = 0.514$ the certified coefficient is $0.0070773$, roughly ten times the width of the enclosure, and the certificate no longer returns a positive value below about $\theta = 0.513$. *This is a search result and is labelled as such; it is not a theorem, and the thresholds themselves are not certified.*

> **Corollary 1.** For every sufficiently large $m$ the window $(m^2, (m + \lceil m^{0.028}\rceil)^2)$ contains a pair $(a, a+2)$ with $\Omega(a) \le 4$ and $\Omega(a+2) \le 4$, and the window $(m^2, (m + \lceil m^{0.56}\rceil)^2)$ contains a pair with $\Omega \le 3$ on each member.

*Proof.* Write $k = \lceil m^{\vartheta}\rceil$ and $X = m^2$. The window has length $2mk + k^2 \ge 2m^{1+\vartheta} = 2X^{(1+\vartheta)/2}$, so it contains the interval $(X, X + X^{(1+\vartheta)/2}]$. At $\vartheta = 0.028$ that exponent is $0.514$ and at $\vartheta = 0.56$ it is $0.78$, so Theorem 2 applies to the contained interval. $\blacksquare$

**No new uniformity is needed for Corollary 1**, and this is worth saying because the obvious route — rewriting §2 to §7 with $H$ of order $U^{(1+\vartheta)/2}$ and re-checking every remainder sum — is not necessary. A window that contains an interval of the required length inherits the conclusion from that interval.

**The square-window form is the one to compare against Theorem 1.** At $k$ fixed the method gives five factors on each side; at $k = \lceil m^{0.028}\rceil$ it gives four. That is the whole distance, stated in the coordinate the set uses.

**"Sufficiently large" is part of both theorems.** Neither proof computes $m_0(k)$ or the threshold in $X$, because the $o(1)$ of (5.2) is not made explicit by the DHR theorems as used. A separate and deliberately wasteful construction, replacing the DHR functions by explicit linear sieves in a vector-sieve combination in the manner of [1], does yield an explicit threshold; it is far too large to be closed by any computation, and it is not the subject of this paper.

---

## 9. The distance to four factors in the square window

Theorem 2 gives $\Omega \le 4$ on both members at length $X^{0.514}$, and the square window has length $X^{1/2}$ exactly. The certified gap in the exponent is therefore $0.014$, and the uncertified gap of Proposition 2 about $0.0117$. **Neither is a small increase in length**: $X^{0.014}$ grows without bound, so the two statements are not close in any absolute sense; what is small is the exponent.

In the square-window coordinate of Corollary 1 the same gap reads $k = \lceil m^{0.028}\rceil$ against $k$ fixed. *Measured, with $w$ and $u$ frozen at the values below and only the level raised*: writing the length exponent as $\beta = (1+\vartheta)/2$, the weighted excess $E(\beta)$ falls from $0.321431$ at $\beta = 1/2$ and crosses the deficit at $\beta \approx 0.512874$, that is $\vartheta \approx 0.0258$; allowing the positive term to move with $\beta$ as well gives $\beta \approx 0.512698$ and $\vartheta \approx 0.0254$. At the certified $\beta = 0.514$ the floating-point coefficient is $+0.0125$ and the certificate returns $+0.0071$. **These are numerical crossings of a coefficient, not theorems**: only $\vartheta = 0.028$ carries a certificate.

The gap can also be measured inside the square window. Optimising the parameters at $\theta = 1/2$ for $r = 4$ gives $w = 16.9155$ and $u = 2.8215$, at which

$$(r+1-u)f_2(\theta w) = 2.176408, \qquad 2\int_{1/w}^{1/u}\left(\frac1t - u\right)F_2\left(w(\tfrac12 - t)\right) dt = 2.241269,$$

$$C_4 = 2.176408 - 2.241269 = -0.064861 .$$

*Everything in the rest of this section is measured*: it comes from an uncertified floating-point solution of the DHR system at those parameters, and it diagnoses where the deficit sits. It is not part of any statement proved above.

### 9.1 The lower sifting function is exhausted

$f_2$ at $8.4578$ is $0.999045$, and its supremum is $1$. Replacing it by that supremum saves about $0.00208$ against a deficit of $0.064861$. **No improvement of a lower bound sieve closes this**, and in particular a smaller sifting limit $\beta_2$ does not: $\beta_2$ enters only through $f_2$ at an argument where $f_2$ is already within 0.1% of its limit.

### 9.2 Where the deficit sits

Write the subtracted estimate as $1.915527 + 0.325741$, the first term being what remains if $F_2$ is replaced by its infimum $1$, and the second the excess above that floor. In the variable $s = w(1/2 - t)$ the excess is

$$E_A = \int_A \rho(s)\left(F_2(s) - 1\right) ds, \qquad \rho(s) = \frac{2}{w}\left(\frac{1}{\tfrac12 - s/w} - u\right),$$

with $s$ running over $2.4626$ to $7.4578$. Since $\rho$ increases with $s$, **a unit of improvement is worth more at larger $s$**. The excess distributes as

| $s$ | weighted excess | share |
|---|---|---|
| $2.4626$ to $2.5$ | $0.0001223$ | 0.04% |
| $2.5$ to $3$ | $0.0193100$ | 5.93% |
| $3$ to $4$ | $0.0846521$ | 25.99% |
| $4$ to $4.3$ | $0.0291643$ | 8.95% |
| $4.3$ to $5$ | $0.0682185$ | 20.94% |
| $5$ to $5.3577$ | $0.0340126$ | 10.44% |
| $5.3577$ to $6$ | $0.0466977$ | 14.33% |
| $6$ to $7.4578$ | $0.0435870$ | 13.38% |

so 59.1% of the weighted excess lies **above** $s = 4.3$. The band with the largest single entry is not where most of the excess is; it is merely the widest band.

### 9.3 What an improvement would have to achieve

Suppose an upper bound sieve gives $F^*$ with $F^*(s) - 1 \le (1-\lambda)(F_2(s)-1)$ for $s \ge S$, and $F^* = F_2$ below $S$. The saving is $\lambda$ times the excess above $S$, so the requirement is $\lambda E_{\ge S} \gt 0.064861$:

| improvement from | $E_{\ge S}$ | $\lambda$ required |
|---|---|---|
| $s \ge 2.4626$ (all of it) | $0.325765$ | 19.91% |
| $s \ge 3.0$ | $0.306332$ | 21.17% |
| $s \ge 3.5$ | $0.267942$ | 24.21% |
| $s \ge 4.0$ | $0.221680$ | 29.26% |
| $s \ge 4.3$ | $0.192516$ | 33.69% |
| $s \ge 5.0$ | $0.124297$ | 52.18% |
| $s \ge 5.3577$ | $0.090285$ | 71.84% |

**A percentage quoted for one range does not transfer to another.** The figure 19.91% across the whole range suffices, while the same 19.91% confined to $2.5 \le s \le 4.3$ saves only about $0.0265$. The criterion is on the weighted integral, never on a percentage alone.

### 9.4 Two qualifications

**First, $F_2$ is not a free parameter inside the DHR system.** The pair $(F_2, f_2)$ is the unique solution of the two delayed equations under the boundary condition that both tend to $1$; lowering one while leaving the other alone does not describe any sieve. An improvement must therefore be an **independent upper bound theorem**, proved by some other construction. The saving is then exactly as tabulated, with no offset, because the lower bound theorem that supplies $f_2$ is a separate theorem and is unaffected by it.

**Second, a smaller required percentage does not mean an easier target.** At $s = 7$ the value of $F_2$ is $1.0204$, so removing a quarter of its excess means proving $1.0153$, tightening a bound already close to its absolute floor of $1$; at $s = 3$ the value is $2.9164$ and the room is far larger. The required percentage and the attainable percentage are different questions, and only the first is measured here.

### 9.5 One further sensitivity

Replacing $F_2$ by the constant $1$ at the parameters above turns $C_4$ into $+0.260881$, and re-optimising the parameters afterwards raises it to about $+0.78$. So **the weight structure is not what obstructs the four-factor statement at this level; the upper sifting function is.** This is a sensitivity measurement only. It does not assert that any part of that range is attainable, since $1$ is not an available upper bound for a count.

---

## 10. Placement

What follows is a bounded source review, not a priority search, and no claim of absence from the literature is made.

Dudek and Johnston [4] showed that every interval between consecutive squares contains an integer with at most four prime factors, and Campbell [2] improved this to three, **for every $n \ge 1$ and with no threshold**. Those are statements about a single integer. The statements here are about a pair at distance $2$, which is a different and harder shape, and they are conditional on an unspecified threshold. The two kinds of result are not comparable in either direction.

Wu [8] proved that for each fixed $\theta \gt 0.971$ and all large $x$ the interval $[x, x+x^\theta]$ contains primes $p$ with $\Omega(p+2) \le 2$. That is a far stronger conclusion in a far longer interval: a square window near $x$ has length of order $x^{1/2}$, and $x^{0.971}/x^{1/2} \to \infty$, so his theorem cannot be inserted into these windows, and nothing here implies his conclusion.

---

## 11. What is and is not established

- Theorems 1 and 2 hold for **every** sufficiently large window, not for most windows and not on average. The uniformity comes from Lemma 1.
- The argument uses no unproved hypothesis about the distribution of primes in these windows.
- Neither theorem asserts that either member is prime, and neither asserts anything about four prime factors in the square window.
- "Sufficiently large" is part of both statements. No threshold is computed here, and nothing is claimed about any particular window.
- The parameter sets are not claimed optimal, and the thresholds of Proposition 2 are not certified.
- Everything in §9 is measured, not proved, and the level ceiling of §3 is a limitation of the method used, not an impossibility theorem.

---

## Reproducing

Every number printed above is regenerated by `code/verify_paired_almost_primes.py`, which uses the standard library only and exits non-zero if any of the four coefficients of Proposition 1 fails to be certified positive. Its success means that those four inequalities hold given the literature inputs listed in §6. It does not reprove the DHR theorems, does not verify the thresholds of Proposition 2, and does not examine any particular window. The measurements of §9 are diagnostic and are not asserted by it.

---

---

*The computations and much of the prose in this paper were prepared with AI assistance (ChatGPT, OpenAI; Claude, Anthropic), used for algebraic derivation, for drafting and rewriting code and text, for running the computations, and for auditing the papers against their own scripts. All statements were checked by the author, who is responsible for them; the repository README sets out the division of labour in full.*
---

## References

The papers of this set are cited as [P1] to [P11], and the numbered entries below are the external works. The two kinds never share a number: a bracket with a P is a companion paper, a bare number is a reference in the list below.

1. M. Bordignon, D. R. Johnston and V. Starichkova, *An explicit version of Chen's theorem and the linear sieve*, Int. J. Number Theory **21** (2025), 2497–2572.
2. P. Campbell, *On the existence of integers with at most 3 prime factors between every pair of consecutive squares*, arXiv:2603.10356 (2026).
3. H. G. Diamond and H. Halberstam, *A Higher-Dimensional Sieve Method*, Cambridge Tracts in Mathematics **177**, Cambridge University Press, 2008.
4. A. W. Dudek and D. R. Johnston, *Almost primes between all squares*, J. Number Theory **278** (2026), 726–745.
5. C. S. Franze and P.-H. Kao, *Almost-prime values of reducible polynomials at prime arguments*, arXiv:1812.11280 (2018).
6. P.-H. Kao, *Almost-prime polynomials with prime arguments*, arXiv:1606.03505 (2016).
7. H.-E. Richert, *Selberg's sieve with weights*, Mathematika **16** (1969), 1–22.
8. J. Wu, *Chen's double sieve, Goldbach's conjecture and the twin prime problem*, Acta Arith. **114** (2004), 215–273.
