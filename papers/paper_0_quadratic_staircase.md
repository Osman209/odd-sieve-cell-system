# An Exact Histogram for a Quadratic Staircase

## 0. The increments of $\lfloor 2j^2/n\rfloor$, and the local maxima of $2j^2 \bmod n$

---

### Abstract

For odd $n$ let
$$W_j  =  \left\lfloor \frac{2(j+1)^2}{n}\right\rfloor - \left\lfloor \frac{2j^2}{n}\right\rfloor , \qquad j = 0,1,\dots,n-1 .$$

We prove that $W_j \in \lbrace 0,1,2,3,4\rbrace$ for every odd $n$ and every $j$ in this range, and that the five values occur with multiplicities determined by the single integer $A = \lfloor (n+7)/8\rfloor$:
$$\mathrm{card}\lbrace W{=}0\rbrace  =  \mathrm{card}\lbrace W{=}4\rbrace  =  A, \qquad \mathrm{card}\lbrace W{=}2\rbrace  =  2A-1,$$
$$\mathrm{card}\lbrace W{=}1\rbrace  =  \mathrm{card}\lbrace W{=}3\rbrace  =  \tfrac{n+1}{2} - 2A .$$

The proof is a tiling argument and carries **no error term**. This is worth emphasising: a probabilistic model of the same count, assuming $2j^2 \bmod n$ equidistributed, returns the same answer, and sums of this shape normally carry an error of size $\sqrt n \log n$ or $n^{1/3}$. None appears, and the residues $2j^2 \bmod n$ never enter the argument.

The same tiling, read geometrically, also **locates** the increments and not only counts them (Theorem 2b): $\lfloor 2j^2/n\rfloor$ is the ceiling quantisation of the concave parabola $x(n-2x)/n$, the value $W_j = 0$ occurs exactly at the floors of its ascending level crossings and $W_j = 2$ exactly at the descending ones, and the two families are separated by the peak at $n/4$. A mirror relation then reduces the descending list to the ascending one plus one bit per level.

A companion compression is proved for the symmetric pairs (Theorems 3 and 4): a pair collapses to a single element of $\lbrace 0,1,2\rbrace$, and its census is again governed by one integer.

We then prove the corresponding statement about the residues themselves, which the histogram deliberately avoids: for odd $n \ge 51$ the sequence $2j^2 \bmod n$ has exactly $2A$ interior local maxima (Theorem 5). The proof combines a palindrome symmetry, a transition count that replaces the two conditions defining a maximum by one, the observation that the relevant *pairs* of intervals tile once separated by parity, and a small arithmetic coincidence: the four residues $8x \bmod n$ that arise are always $\pm1, \pm3, \pm5, \pm7$ in some order, so their squares always sum to $84$.

Nothing in this paper concerns prime numbers.

**How to read the claims in this paper.** Statements set as Theorems, Propositions and Corollaries are proved, and the proofs are given. Everything else falls into two kinds, and we try to keep them apart. A *measurement* is a computation over a stated finite range; it is labelled with that range, and it supports a claim about that range only. A *reading* is our own judgement about what a measurement or a proof appears to mean, and we mark it as ours rather than stating it as established. In this paper the proportion is heavily weighted to the first kind: everything but the sample tables is proved.

**Keywords:** floor function, quadratic residues, exact multiplicities, three-distance theorem, equidistribution.

**MSC 2020:** 11B57, 11A07, 11K31.

---

## 1. The object

Throughout, $n \ge 3$ is odd and $j$ runs over $0,1,\dots,n-1$. Set
$$F(x) = \left\lfloor \frac{2x^2}{n}\right\rfloor, \qquad W_j = F(j+1)-F(j), \qquad r_j = 2j^2 \bmod n .$$

$F$ is a staircase under the parabola $2x^2/n$; $W_j$ is its increment, and $r_j$ is the residue left over. The two are linked by $2j^2 = nF(j) + r_j$, but — and this is the point of §3 — the histogram of $W$ can be determined without ever computing an $r_j$.

Two elementary remarks fix the scale. The total rise is
$$\sum_{j=0}^{n-1} W_j = F(n)-F(0) = 2n,$$
so the mean increment is exactly $2$; and $W_j$ counts the multiples of $n$ in the interval
$$I_j = \big(2j^2,\ 2(j+1)^2\big], \qquad |I_j| = 4j+2 . \qquad\text{(1.1)}$$

The intervals $I_0, I_1, \dots$ tile $(0,\infty)$. That is the only structural fact the histogram needs.

---

## 2. Theorem 1: the range

> **Theorem 1.** For every odd $n$ and every $0 \le j \le n-1$,
> $$W_j \in \lbrace 0,1,2,3,4\rbrace .$$

*Proof.* The two arguments of the floor differ by
$$\frac{2(j+1)^2}{n}-\frac{2j^2}{n}  =  \frac{4j+2}{n},$$
which is positive and, for $j \le n-1$, strictly less than $4$. A difference of floors of two reals differing by less than $4$ lies in $\lbrace 0,1,2,3,4\rbrace$. $\blacksquare$

*Verification.* Zero violations over every odd $n \le 20{,}001$.

The restriction $j \le n-1$ is real: for $j$ in the range $[rn, (r+1)n)$ the same computation gives $W_j \in \lbrace 4r, \dots, 4r+4\rbrace$, so the bound moves up in steps of four. Everything below concerns $0 \le j \le n-1$, which we call the **first cycle**.

Two further symmetries, both immediate from (1.1), will be used:
$$W_j + W_{n-1-j} = 4, \qquad W_{(n-1)/2} = 2. \qquad\text{(2.1)}$$

---

## 3. Theorem 2: the exact multiplicities

> **Theorem 2.** Let $n \ge 3$ be odd and $A = \lfloor (n+7)/8\rfloor$. Over the first cycle,
> $$\mathrm{card}\lbrace W{=}0\rbrace  =  \mathrm{card}\lbrace W{=}4\rbrace  =  A, \qquad \mathrm{card}\lbrace W{=}2\rbrace  =  2A-1,$$
> $$\mathrm{card}\lbrace W{=}1\rbrace  =  \mathrm{card}\lbrace W{=}3\rbrace  =  \frac{n+1}{2}-2A,$$
> and no other value occurs.

| $n$ | $(N_0,N_1,N_2,N_3,N_4)$ | $A$ |
|--------|------|------|
| 11 | $(2, 2, 3, 2, 2)$ | 2 |
| 101 | $(13, 25, 25, 25, 13)$ | 13 |
| 1,009 | $(127, 251, 253, 251, 127)$ | 127 |
| 19,997 | $(2500, 4999, 4999, 4999, 2500)$ | 2500 |

*Verification.* Zero exceptions for every odd $n \le 200{,}001$.

*Proof.* By (1.1), $W_j$ counts the multiples of $n$ in $I_j$, an interval of length exactly $4j+2$. Hence:

- if $4j+2 \lt  n$, the interval is shorter than $n$ and holds **at most one** multiple, so $W_j \in \lbrace 0,1\rbrace$;
- if $4j+2 \ge n$, it is at least as long and holds **at least one**, so $W_j \ge 1$.

**The count of zeros.** Consequently $W_j = 0$ forces $j \lt  m := \lfloor (n+1)/4\rfloor$. On that range the intervals $I_0,\dots,I_{m-1}$ tile $(0, 2m^2]$ exactly and each holds at most one multiple, so the number of *occupied* intervals equals the number of multiples in the range, namely $\lfloor 2m^2/n\rfloor$. Therefore
$$N_0  =  m - \left\lfloor \frac{2m^2}{n}\right\rfloor. \qquad\text{(3.1)}$$

Write $n = 8t+r$ with $r \in \lbrace 1,3,5,7\rbrace$; then $m = 2t+\varepsilon$ with $\varepsilon = 0,1,1,2$ respectively. We claim the quotient in (3.1) is $q = t+\varepsilon-1$:

| $r$ | $m$ | $q$ | $2m^2-nq$ | check |
|------|------|------|------|--------|
| 1 | $2t$ | $t-1$ | $7t+1$ | $\lt  8t+1$ ✓ |
| 3 | $2t+1$ | $t$ | $5t+2$ | $\lt  8t+3$ ✓ |
| 5 | $2t+1$ | $t$ | $3t+2$ | $\lt  8t+5$ ✓ |
| 7 | $2t+2$ | $t+1$ | $t+1$ | $\lt  8t+7$ ✓ |

Each remainder is a positive linear function of $t$ strictly below $n$, so the quotient is as claimed and
$$N_0 = (2t+\varepsilon)-(t+\varepsilon-1) = t+1 = \left\lfloor \frac{n+7}{8}\right\rfloor = A. \qquad\text{(3.2)}$$

**The remaining four.** Put $H = (n-1)/2$. For $0 \le j \lt  H$ the interval $I_j$ has length $4j+2 \lt  2n$, so $W_j \in \lbrace 0,1,2\rbrace$. These $H$ intervals tile $(0, 2H^2]$, which contains
$$\left\lfloor \frac{2H^2}{n}\right\rfloor = H-1$$
multiples of $n$. Writing $N_i^- = \mathrm{card}\lbrace 0 \le j \lt  H : W_j = i\rbrace$, we have $N_0^- = A$ together with
$$N_0^- + N_1^- + N_2^- = H, \qquad N_1^- + 2N_2^- = H-1,$$
and subtracting gives $N_2^- = A-1$. The central index $j = H$ has $W_H = 2$ by (2.1). Finally the symmetry $W_j + W_{n-1-j} = 4$ pairs $W{=}0$ with $W{=}4$ and $W{=}1$ with $W{=}3$, while $W{=}2$ pairs with itself. Therefore
$$N_4 = N_0 = A, \qquad N_2 = 2(A-1)+1 = 2A-1,$$
and the remaining $n - (N_0+N_2+N_4)$ indices split equally:
$$N_1 = N_3 = \frac{n+1}{2}-2A. \qquad \blacksquare$$

### 3.1 Why the count has no error term

A probabilistic model, assuming $2j^2 \bmod n$ equidistributed, estimates $N_0$ by
$$\sum_{j \lt  (n-2)/4} \frac{n-4j-2}{n}  \approx  \frac n8,$$
the correct answer, with deviation never exceeding $0.889$ for odd $n \le 20{,}001$. Sums of this shape normally carry an error of size $\sqrt n \log n$ (character sums) or $n^{1/3}$ (lattice points).

**The reason none appears here is that the indicators are not independent: the intervals tile, and the tiling is exact.** The residues $2j^2 \bmod n$ never enter the argument. Theorem 5 is the statement about those residues, and it is a good deal harder.

---

### 3.2 Theorem 2b: where the increments are, not only how many

Theorem 2 counts the five values. They can also be *located*, in closed form, and the argument is the tiling of §1 read geometrically rather than arithmetically.

Set
$$D_j  =  j - \left\lfloor \frac{2j^2}{n}\right\rfloor, \qquad\text{so that}\qquad D_{j+1}-D_j  =  1 - W_j .$$
Because $j$ is an integer, $D_j = \lceil f(j)\rceil$ with
$$f(x)  =  x - \frac{2x^2}{n}  =  \frac{x(n-2x)}{n},$$
a concave parabola with its peak at $x = n/4$. So $D$ is the ceiling quantisation of a parabola, $W_j = 0$ means $D$ rises, $W_j = 1$ that it is flat, and $W_j = 2$ that it falls.

> **Theorem 2b.** Let $H = (n-1)/2$ and $A = \lfloor (n+7)/8\rfloor$ as before, and for $1 \le m \le A$ put
> $$\alpha_m  =  \left\lfloor \frac{n-\sqrt{n^2-8n(m-1)}}{4}\right\rfloor, \qquad \beta_m  =  \left\lceil \frac{n+\sqrt{n^2-8n(m-1)}}{4}\right\rceil - 1 .$$
> Then, for $0 \le j \lt H$,
> $$W_j = 0 \iff j = \alpha_m \text{ for some } 1 \le m \le A, \qquad W_j = 2 \iff j = \beta_m \text{ for some } 2 \le m \le A,$$
> and $W_j = 1$ at every other index of that range. Moreover
> $$\max_j D_j = A,$$
> and the two families are separated by the peak: every $\alpha_m \lt n/4$ and every $\beta_m + 1 \gt n/4$.

*Proof.* $f(j+1)-f(j) = (n-4j-2)/n$ has absolute value less than $1$ throughout $0 \le j \lt H$, so the ceiling can move by at most one step and $D$ is unimodal: it rises while $j \lt n/4$ and falls after, giving the separation and leaving only $W \in \lbrace 0,1,2\rbrace$ on this range. A rise into level $m$ happens at the last integer before $f$ crosses the value $m-1$ upward, and a fall out of it at the last integer before $f$ crosses $m-1$ downward; solving $f(x) = m-1$ gives the two roots
$$x_m^{\pm}  =  \frac{n \pm \sqrt{n^2-8n(m-1)}}{4},$$
whence the stated floor and ceiling. The peak value of $f$ on the integers is $(n^2-1)/(8n)$, since $n$ is odd and the nearest integer to $n/4$ is at distance $1/4$; its ceiling is $A$. $\blacksquare$

*Verification.* Zero mismatches for $1{,}429$ odd $n$ up to $20{,}001$, and the count $\lvert\lbrace \alpha_m\rbrace\rvert = A$ recovers $N_0 = A$ of Theorem 2 for every odd $n \le 20{,}001$. The separation at the peak has zero violations for odd $n \lt 4{,}000$.

**A mirror that halves the data.** The two roots satisfy $x_m^- + x_m^+ = n/2 = H + \tfrac12$, and after the floor and the ceiling this becomes
$$\beta_m  =  H - \alpha_m - \varepsilon_m, \qquad\text{where}\qquad \varepsilon_m = \begin{cases} 0, & \lbrace x_m^-\rbrace \lt \tfrac12,\\[2pt] 1, & \lbrace x_m^-\rbrace \ge \tfrac12,\end{cases}$$
verified with zero mismatches over $20{,}508$ pairs $(n,m)$ with $n \lt 1{,}500$. So the descending half needs no separate list: the ascending positions $\alpha_m$ and one bit per level determine everything, and the palindrome $W_j + W_{n-1-j} = 4$ of (2.1) then determines the whole word.

**What this does not give.** The crossing set $\mathcal A_n = \lbrace \alpha_m \rbrace$ is a compression of the word, not an arithmetic invariant of it. Measured against a control with the same real crossing positions but randomised fractional parts — same parabola, same density everywhere, no arithmetic — the distribution of $\mathcal A_n \bmod q$ is not more structured than the control but slightly less: over odd $n \in (10^3, 2\cdot10^4)$ the $\chi^2$ statistics are $10.5, 14.5, 24.3, 48.7, 51.5, 68.6$ at $q = 7, 11, 13, 17, 19, 23$ against control means $9.1, 20.3, 28.7, 50.3, 56.0, 80.8$, the true value lying below the control in five cases of six. **The small departure from equidistribution is a consequence of the shape of the parabola — the crossings crowd near $0$ and thin towards the peak — and not of any relation between $n$ and $q$.** This is recorded because the closed form invites the opposite guess.

---

## 4. Theorems 3 and 4: pairs

Index the symmetric pairs $\lbrace j, n-1-j\rbrace$ by $R = 1,3,\dots,n-2$.

> **Theorem 3.** With
> $$d_n(R) = \left\lfloor \tfrac12 + \frac{(R+2)^2}{2n}\right\rfloor - \left\lfloor \tfrac12 + \frac{R^2}{2n}\right\rfloor,$$
> one has $d_n(R) \in \lbrace 0,1,2\rbrace$, and the corresponding pair of increments is $(W_L, W_R) = (2-d,\ 2+d)$.

*Proof.* The two arguments of the floor differ by
$$\frac{(R+2)^2-R^2}{2n} = \frac{2(R+1)}{n},$$
which for $1 \le R \le n-2$ lies strictly between $0$ and $2$; hence the difference of floors is $0$, $1$ or $2$. Substituting the pair parametrisation into the definition of $W$ gives $W_R = 2+d_n(R)$, and (2.1) then gives $W_L = 2-d_n(R)$. $\blacksquare$

*Verification.* Zero failures over every odd $n \lt  600$ and every odd $R$ with $1 \le R \le n-2$.

> **Theorem 4.** Let $N_d = \mathrm{card}\lbrace R : d_n(R) = d\rbrace$. Then $N_2 = N_0+1$.

*Proof.* There are $(n-1)/2$ odd values $R = 1,3,\dots,n-2$, and the definition of $d_n(R)$ telescopes along them:
$$\sum_R d_n(R) = \left\lfloor \tfrac12 + \frac{n^2}{2n}\right\rfloor - \left\lfloor \tfrac12 + \frac{1}{2n}\right\rfloor = \frac{n+1}{2}.$$
Hence
$$N_0+N_1+N_2 = \frac{n-1}{2}, \qquad N_1+2N_2 = \frac{n+1}{2},$$
and subtracting gives $N_2-N_0 = 1$. $\blacksquare$

*Verification.* Zero failures over all odd $n \lt  2000$.

| $n$ | $N_0$ | $N_1$ | $N_2$ |
|------|------|------|------|
| 11 | 1 | 2 | 2 |
| 13 | 1 | 3 | 2 |
| 31 | 3 | 8 | 4 |
| 101 | 12 | 25 | 13 |
| 499 | 62 | 124 | 63 |

As in Theorem 2, the whole census is governed by one integer.

---

## 5. Theorem 5: the number of local maxima of $2j^2 \bmod n$

Theorem 2 counts the values of $W$. The companion question concerns their *arrangement*, and its sharpest form is the number of local maxima of the residue sequence itself.

> **Theorem 5.** Let $n \ge 51$ be odd and $A = \lfloor (n+7)/8\rfloor$. Then $r_j = 2j^2 \bmod n$, $j = 0,\dots,n-1$, has exactly $2A$ interior local maxima.

*Range of the statement.* The proof below needs $n \ge 51$, where the interval structure of Step 4 is in its generic configuration. Computation shows the conclusion is in fact true for **every** odd $n$ except five: $n = 3, 5, 7, 9, 49$. Checked exhaustively for all odd $n \le 200{,}001$.

Throughout put
$$\varepsilon_j = [\, r_{j+1} \lt  r_j \,], \qquad q_j = \left\lfloor \frac{4j+2}{n}\right\rfloor, \qquad H = \frac{n-1}{2},$$
$$\Phi(x) = \left\lfloor \frac{2x^2}{n}\right\rfloor + \left\lfloor \frac{2(x-1)^2}{n}\right\rfloor,$$
so that $\varepsilon_j = W_j - q_j$, and $j$ is a local maximum exactly when $\varepsilon_{j-1} = 0$ and $\varepsilon_j = 1$.

### 5.1 Step 1: the palindrome

Since $2(n-j)^2 \equiv 2j^2$, we have $r_j = r_{n-j}$ for $1 \le j \le n-1$. Maxima therefore occur in mirror pairs $j \leftrightarrow n-j$, with no fixed point because $n$ is odd. Also $r_{H+1} = r_{n-H-1} = r_H$, so
$$\varepsilon_0 = 0 \quad (\text{since } r_1 = 2 \gt  0 = r_0), \qquad \varepsilon_H = 0,$$
and no maximum straddles the middle. Hence the total is twice the number of maxima in $1 \le j \le H$.

### 5.2 Step 2: maxima are exactly the mixed pairs

In any $0$–$1$ word the numbers of ascents and descents differ by the boundary values; applied to $\varepsilon_0,\dots,\varepsilon_H$ with both ends $0$, the two are equal. Therefore
$$\mathrm{card}\lbrace j \le H : \varepsilon_{j-1}=0,\ \varepsilon_j=1\rbrace  = \tfrac12 \mathrm{card}\lbrace j \le H : \varepsilon_{j-1} \ne \varepsilon_j\rbrace ,$$
and combining with Step 1:
$$\boxed{ \mathrm{card}\lbrace \text{local maxima}\rbrace   =  \mathrm{card}\lbrace  1 \le j \le H  :  \varepsilon_{j-1} \ne \varepsilon_j \rbrace . }$$

### 5.3 Step 3: a mixed pair is one condition on one interval

Since $\varepsilon_{j-1}+\varepsilon_j = (W_{j-1}+W_j) - (q_{j-1}+q_j)$, the pair at $j$ is mixed if and only if
$$P_j := \big(2(j-1)^2,\ 2(j+1)^2\big] \quad\text{contains exactly } q_{j-1}+q_j+1 \text{ multiples of } n.$$
$P_j$ has length exactly $8j$. No residue occurs in this condition.

### 5.4 Step 4: the pair intervals tile, by parity

Consecutive $P_j$ overlap, but each parity subfamily tiles exactly:
$$P_{2s+1} = \big(8s^2,\ 8(s+1)^2\big], \qquad P_{2s} = \big(2(2s-1)^2,\ 2(2s+1)^2\big],$$
of lengths $8(2s+1)$ and $16s$. Since $8j \lt  4n$ on $j \le H$, each $P_j$ carries $L_j$ or $L_j+1$ multiples with $L_j = \lfloor 8j/n\rfloor \in \lbrace 0,1,2,3\rbrace$, and over any block of consecutive $j$ of one parity the total telescopes. Set $\mathrm{off}_j = (q_{j-1}+q_j)-L_j$; then $j$ is mixed iff $P_j$ carries the **larger** count when $\mathrm{off}_j = 0$, the **smaller** when $\mathrm{off}_j = -1$.

Both $L_j$ and $\mathrm{off}_j$ are explicit step functions of $j$, with jumps only at
$$1 \lt  \ell_1 = \left\lceil \tfrac n8\right\rceil \le \beta_1 = \left\lceil \tfrac{n-2}4\right\rceil \le \ell_2 = \left\lceil \tfrac n4\right\rceil$$
$$\le \beta_2 = \left\lceil \tfrac{n+2}4\right\rceil \lt  \ell_3 = \left\lceil \tfrac{3n}8\right\rceil \lt  H \lt  H+1,$$
giving **seven** intervals with $(L,\mathrm{off}) = (0,0),(1,-1),(1,0),(2,-1),(2,0),(3,-1),(3,0)$ in order. The last is the single point $j = H$, where $4H+2 = 2n$ forces $q_H = 2$. Combining the two parities, an interval $[\alpha,\beta)$ has $\beta-\alpha$ tiles whose multiples total $\Phi(\beta)-\Phi(\alpha)$, independently of which parity starts it. Its contribution to the mixed count is $G-LC$ if $\mathrm{off}=0$ and $(L+1)C-G$ if $\mathrm{off}=-1$, with $G = \Phi(\beta)-\Phi(\alpha)$ and $C = \beta-\alpha$.

Summing the seven intervals and telescoping the $\Phi$'s (note $\Phi(1)=0$):
$$\mathrm{card}(\text{mixed}) = 2\big[\Phi(\ell_1)-\Phi(\beta_1)+\Phi(\ell_2)-\Phi(\beta_2)+\Phi(\ell_3)-\Phi(H)\big] + \Phi(H+1) + \Sigma_C, \qquad\text{(5.1)}$$
$$\Sigma_C = 2(\beta_1-\ell_1)-(\ell_2-\beta_1)+3(\beta_2-\ell_2)-2(\ell_3-\beta_2)+4(H-\ell_3)-3.$$

*Verification of (5.1).* Zero failures against the direct count for every odd $9 \le n \le 20{,}001$.

### 5.5 Step 5: evaluating the seven $\Phi$'s

Two are immediate: $\Phi(H+1) = n-1$ and $\Phi(H) = n-5$. Three more are linear; writing $n = 8t+r$ with $r \in \lbrace 1,3,5,7\rbrace$,
$$-\Phi(\beta_1)+\Phi(\ell_2)-\Phi(\beta_2) = -2t + c_r, \qquad c_r = 3, -1, 1, -3 .$$
The remaining two are the content, and they are handled together.

> **Lemma.** For odd $n = 8t+r \ge 51$,
> $$\Phi\big(\lceil n/8\rceil\big) + \Phi\big(\lceil 3n/8\rceil\big) = \frac{5n-k_r}{8}, \qquad k_r = 13, 7, 25, 19 \ \text{ for } r = 1,3,5,7 .$$

*Proof.* Put $m = \lceil 3r/8\rceil \in \lbrace 1,2,2,3\rbrace$, so $\lceil n/8\rceil = t+1$ and $\lceil 3n/8\rceil = 3t+m$; the four arguments are $x \in \lbrace t,\ t+1,\ 3t+m-1,\ 3t+m\rbrace$. Because $8t \equiv -r \pmod n$,
$$8x \equiv e_x \pmod n, \qquad e_x = -r,\ 8-r,\ 8m-8-3r,\ 8m-3r,$$
and **in every one of the four cases $\lbrace |e_x|\rbrace$ is a permutation of $\lbrace 1,3,5,7\rbrace$** — for instance $r=1,m=1$ gives $(-1,7,-3,5)$ and $r=7,m=3$ gives $(-7,1,-5,3)$. Since $32 \cdot 2x^2 = (8x)^2$,
$$32\big(2x^2 \bmod n\big) \equiv e_x^2 \pmod n, \qquad \sum_x e_x^2 = 1+9+25+49 = 84 .$$
Writing $32(2x^2 \bmod n) = e_x^2 + a_x n$ with $a_x \in [0,32)$ determined by $e_x^2 + a_x n \equiv 0 \pmod{32}$, a check of the sixteen classes $n \bmod 32$ gives $\sum_x a_x = 80-4r$ in every case, whence
$$\sum_x \big(2x^2 \bmod n\big) = \frac{84+(80-4r)n}{32} = \frac{(20-r)n+21}{8}.$$
On the other hand $\sum_x 2x^2 = 40t^2+(24m-8)t+(4m^2-4m+4)$ exactly, and dividing the difference by $n = 8t+r$ gives $5t+s_r$ with $s_r = -1,1,0,2$, which is $(5n-k_r)/8$. $\blacksquare$

*Verification of the Lemma.* Zero failures for every odd $n \le 300{,}001$ apart from $n = 3,5,7,9,17,25,49$, where the interval structure of Step 4 degenerates.

### 5.6 Step 6: assembly

Substituting $\ell_1 = t+1$, $\beta_1 = 2t+\lceil\frac{r-2}{4}\rceil$, $\ell_2 = 2t+\lceil\frac r4\rceil$, $\beta_2 = 2t+\lceil\frac{r+2}{4}\rceil$, $\ell_3 = 3t+m$, $H = 4t+\frac{r-1}{2}$ into (5.1) together with the Lemma gives, in each of the four residue classes,
$$\mathrm{card}(\text{mixed})  =  2t+2  =  2A. \qquad \blacksquare$$

| $n$ | $8t+1$ | $8t+3$ | $8t+5$ | $8t+7$ |
|------|------|------|------|------|
| $\mathrm{card}(\text{mixed})$ | $2t+2$ | $2t+2$ | $2t+2$ | $2t+2$ |

### 5.7 Remark: what made it work

A local maximum is *two* consecutive conditions, while Theorem 2 counts $j$ satisfying *one*; and while the intervals $I_j$ tile, consecutive $P_j$ overlap. The apparent obstruction dissolves in two moves. Steps 2 and 3 convert the two conditions into one — a condition on the count of multiples in the single interval $P_j$ — and Step 4 observes that the $P_j$ tile perfectly once separated by parity. The elementary weight $\sum_j \varepsilon_j = (n-1)/2$, which follows from $\gcd(4,n)=1$ because the increments $(4j+2) \bmod n$ then run over every residue, is thereby joined by a second weight, of pairs rather than of single terms, and the same tiling carries both.

The one place where genuine arithmetic enters is the Lemma, and it enters through a small coincidence worth naming: the four numbers $8x \bmod n$ attached to $\lceil n/8\rceil$ and $\lceil 3n/8\rceil$ are, up to sign, always $1,3,5,7$ — so their squares always sum to $84$, whatever $n$ is.

---

## 6. Placement

Since $r_j = 2j^2 \bmod n$ is $n\lbrace j^2\alpha\rbrace$ with $\alpha = 2/n$ **rational**, the natural comparisons are these.

**The linear analogue.** For $\lbrace j\alpha\rbrace$ the three-distance theorem of Sós, Świerczkowski and Surányi [1] states that the gaps between consecutive points take at most three values. Theorems 2 and 4 are of that flavour — a small fixed set of values with exactly determined multiplicities — but the object is quadratic and the statement is about the increments of the associated staircase rather than about gaps. We do not claim the three-distance theorem as a template; the resemblance is one of shape.

**The quadratic literature runs the other way.** For irrational $\alpha$ the fine-scale statistics of $\lbrace j^2\alpha\rbrace$ — pair correlation and spacings — are known only for almost every $\alpha$ and only as limiting laws; see Heath-Brown [2]. That is a statement about a *continuum* of $\alpha$ and about a limiting distribution. A theorem of the present kind — a finite set of values with explicit multiplicities and no error term — is possible only because the orbit here is finite and periodic.

**The nearest relative** is the literature on spacings of quadratic residues modulo $q$, for instance Kurlberg [3]. The results there are again distributional; Theorems 2, 4 and 5 are exact identities for a single explicit sequence.

We are not aware of the multiplicities of Theorem 2, the pair census of Theorem 4, or the count of Theorem 5 in the literature, and would be glad to be corrected.

---

## Appendix A — Sample data

**The increments $W_j$, $n = 7$:** $0, 1, 1, 2, 3, 3, 4$. Here $A = \lfloor 14/8\rfloor = 1$, and Theorem 2 predicts $\mathrm{card}\lbrace 0\rbrace =\mathrm{card}\lbrace 4\rbrace =1$, $\mathrm{card}\lbrace 2\rbrace =2A-1=1$, $\mathrm{card}\lbrace 1\rbrace =\mathrm{card}\lbrace 3\rbrace =(n+1)/2-2A=2$ — exactly what the list shows. (Note that $n=7$ is one of the five small exceptions to Theorem 5; the histogram of Theorem 2 has no exceptions at all.)

**The residues $r_j = 2j^2 \bmod 17$:** $0, 2, 8, 1, 15, 16, 4, 13, 9, 9, 13, 4, 16, 15, 1, 8, 2$. Interior local maxima at $j = 2,5,7,10,12,15$ — six of them, and $2A = 2\lfloor 24/8\rfloor = 6$.

**The seven intervals of Step 4, $n = 101$** ($t = 12$, $r = 5$, $H = 50$): the boundaries are
$$1,\quad \ell_1 = 13,\quad \beta_1 = 25,\quad \ell_2 = 26,\quad \beta_2 = 26,\quad \ell_3 = 38,\quad H = 50,\quad H+1 = 51,$$
so the fourth interval $[\ell_2,\beta_2)$ is empty here and five of the seven carry indices, with $(L,\mathrm{off}) = (0,0)$ on $[1,13)$, $(1,-1)$ on $[13,25)$, $(1,0)$ at $j=25$, $(2,0)$ on $[26,38)$, $(3,-1)$ on $[38,50)$ and $(3,0)$ at $j=50$.

## Appendix B — Note on method

Two details were found by failure rather than by design and are recorded so that a reader reconstructing the argument does not lose time on them.

**The constant $2$ in the increment.** In the application from which this paper was extracted, the increment appears as $H_j = 2+W_j$; dropping the additive constant breaks the formula in $57$ of $78$ tested cases. It is an artefact of that application, not of the staircase, but it is easy to mislay.

**The seventh interval.** A first version of (5.1) used six intervals and failed for essentially every $n$. The omission is the single point $j = H$, where $4H+2 = 2n$ forces $q_H = 2$ rather than $1$; with it restored the identity holds with zero failures on the whole tested range.

---

*The computations and much of the prose in this paper were prepared with AI assistance (Claude, Anthropic), used for drafting and rewriting code and text, running the computations, searching the literature, and auditing the paper against its own scripts. The research direction, the questions asked, the decisions about what to publish and what to withdraw, and the responsibility for every claim are the author's. The full note is in the repository README.*

---

## References

1. V. T. Sós, *On the distribution mod 1 of the sequence $n\alpha$*, Ann. Univ. Sci. Budapest, Eötvös Sect. Math. **1** (1958), 127–134.
2. D. R. Heath-Brown, *Pair correlation for fractional parts of $\alpha n^2$*, Math. Proc. Cambridge Philos. Soc. **148** (2010), 385–407.
3. P. Kurlberg, *The distribution of spacings between quadratic residues, II*, Israel J. Math. **120** (2000), part A, 205–224.
