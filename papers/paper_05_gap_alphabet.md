# The Gap Alphabet

## Paper 5. Which gaps can occur between consecutive odd composites, and where the ladder of proofs stops

---

### Abstract

Between consecutive odd composites the gap takes only the values $2$, $4$ and $6$, and a gap of $6$ *is* a twin pair. That single observation turns the twin problem into a question about one letter of a three-letter alphabet, and this paper settles everything about that alphabet that can be settled without prime input: the two short gaps occur infinitely often for elementary reasons, the long one is equivalent to the conjecture itself, and the forbidden words of the language are classified. On one rail no five survivors above $5$ lie in arithmetic progression of step $6$, and the run counts obey an exact product formula that caps runs at four. **No progress toward the twin-prime conjecture is claimed.**

**Numbering.** This paper is one part of a set that was written as a single document and is now published in parts. Each part numbers its own results from one and is self-contained: a reference of the form [Pn, Thm 1] means Theorem 1 of Paper n, and an unqualified "Theorem 1" always means this paper's own. Result numbers therefore differ from those of the earlier seven-document releases, where the whole set shared the numbering of the single document.

**How to read the claims in this paper.** Statements set as Theorems, Propositions and Corollaries are proved, and the proofs are given. One result in the set is labelled **Verified Law**: it is proved under a stated hypothesis and verified numerically outside it. Anything described as *measured* is a computation over a stated finite range and is labelled as such where it occurs.

**Keywords:** twin primes, gap alphabet, sieve cycles, cell coordinates.

**MSC 2020:** 11N35, 11N05, 11A41.

---

## Summary of the results in this part

**§2 — The gap alphabet, and the ladder of proofs**

| Result | What it says | Section |
|-------------|----------------------------------------------------|---------|
| **Theorem 1** | The gap between consecutive odd composites takes only the values $2$, $4$ or $6$. | §2.1 |
| **Theorem 2** | Gaps $2$ and $4$ occur infinitely often with no prime input; gap $6$ infinitely often is *equivalent* to the twin conjecture. | §2.2 |
| **Theorem 3** | On one rail, no five survivors above $5$ lie in arithmetic progression of step $6$. | §2.3 |
| **Corollary 1** | The run counts $G_k$ at spacing $6$ obey $G_k = \prod(q-k)$, capping runs at four. | §2.3 |

---

## 1. Setting

This paper is short and takes almost nothing from the others. [P2] supplies the coordinates: the line $L_p(k) = p(p+2k)$ beginning at $p^2$, the grid $L_3$ of step $6$, and the cells $C_b = (6b-1, 6b+1)$. Theorems 1, 2 and 3 use those and nothing more; Theorem 3 needs only that $L_5$ begins at $25$. Corollary 1 is the one place where the cycle enters: the count of runs over a full period is the product law of [P3].

Two companions are cited but not used as sources. [P9] is where the obstruction that stops the ladder is derived, and [P11] is where the routes around it are collected. Neither is needed to read this paper.

**A warning about the word "gap", carried here because this is the paper that fixes the alphabet.** A *gap* below always means the numerical distance between two consecutive odd composites, so the letter $6$ is a twin pair. That is not the same object as an *edge of length $6$* between two survivors, which is a prime pair $(p, p+6)$ and is studied in [P7, App. A]. The two must not be run together: the phrase "gap 6" would otherwise cover both.

---

## 2. The gap alphabet and the ladder of proofs

*Terms used throughout, all as defined in [P2].* A **line** $L_p$ is the odd multiples of $p$ from $p^2$ onward; a **cell** is a pair $C_b = (6b-1,\ 6b+1)$; a **strike** is a member of a cell that lies on some line; a member is a **survivor** of a set of lines if none of them strikes it, and a cell is **open** if both its members survive. A **gap** here always means the numerical distance between two consecutive odd composites, not a count of cells. A **sector** is the interval between consecutive odd squares; a **belt** is the interval between the squares of consecutive primes.

We record first what the framework proves outright about gaps, and then where the ladder of proofs stops.

### 2.1 Theorem 1 (the gap alphabet)

> **Theorem 1.** The gap between consecutive odd composites takes only the values $2$, $4$ or $6$.

*Proof.* Among any three consecutive odd numbers the residues modulo $3$ are a permutation of $\lbrace 0,1,2\rbrace$:
$$n,\ n+2,\ n+4 \ \longrightarrow\ \text{one of them lies on } L_3 .$$
So one of them is divisible by $3$; and every odd multiple of $3$ from $9$ onward lies on $L_3$. Hence beyond $7$ no three consecutive survivors exist, and the gap is capped at $6$. $\blacksquare$

Correspondingly: gap $2$ means no survivor between; gap $4$ means one isolated prime; and **gap $6$ means two adjacent survivors, i.e. a twin pair.** Verified: every gap-$6$ interval contains a twin, zero failures among $2{,}992$ instances below $3\times10^5$.

Measured over $9\times10^8$ gaps up to $2\times10^9$, the three letters occur with frequencies $0.89816$, $0.09475$ and $0.00708$; the maximum observed gap is $6$, first attained at $9$.

Hence an equivalent form of the twin conjecture: **the maximal possible gap is attained infinitely often.** The cap is free and proved; the statement concerns composites, which are the objects the framework actually constructs.

### 2.2 The ladder, and where it stops

> **Theorem 2.** Gap $2$ occurs infinitely often, requiring no prime; gap $4$ occurs infinitely often, requiring one prime.

*Proof.* For gap $2$ take
$$n = 30j+3, \qquad n+2 = 30j+5 .$$
The first lies on $L_3$, the second on $L_5$, both for every $j\ge1$. For gap $4$: let $p \equiv 8 \pmod{15}$ be prime; then $p-2 \equiv 6$ is divisible by $3$ and $p+2 \equiv 10$ by $5$, so $p$ is an isolated survivor, and Dirichlet's theorem supplies infinitely many such $p$. $\blacksquare$

$$\begin{array}{lll}
\text{gap } 2 & \text{zero primes required} & \textbf{proved} \cr 
\text{gap } 4 & \text{one prime (Dirichlet)} & \textbf{proved} \cr 
\text{gap } 6 & \textbf{two primes simultaneously} & \textbf{open}
\end{array}$$

**Dirichlet supplies one prime in an arithmetic progression; nothing supplies two at a prescribed distance.** That is the whole of the remaining distance.

**Why this reciprocal-sum test cannot bridge it.** Summing reciprocals by gap type:

| $N$ | gap 2 | gap 4 | gap 6 |
|------|-------|-------|-------|
| $10^6$ | 2.805 | 0.887 | 0.464 |
| $10^8$ | 4.556 | 1.127 | 0.488 |
| $2\times10^9$ | 5.762 | 1.257 | **0.498** |

Gaps $2$ and $4$ have **divergent** reciprocal sums, and divergence proves infinitude. The two diverge at different rates: almost every odd composite begins a gap of $2$, so that column grows like $\tfrac12\log N$, while the gap-$4$ column counts isolated primes and grows like $\log\log N$. The gap-$6$ sum **converges**, and that is Brun's theorem [1] rather than a reading of the column: every gap-$6$ interval carries a twin pair by Theorem 1, so this sum is dominated by the sum of $1/p$ over twins. The column shows it flattening toward its constant on the tested range. That constant is the analogue of Brun's constant in the present alphabet and not Brun's constant itself: the latter is $\sum_{\text{twins}}\big(1/p + 1/(p+2)\big) = 1.9021605\ldots$, whereas the column above carries one reciprocal per gap-$6$ event. A convergent reciprocal sum cannot distinguish "infinitely many" from "finitely many". Thus this particular divergence-based density test has no route to the twin conclusion.

### 2.3 Runs and the cap at four

> **Theorem 3.** On a single rail, no five survivors with $x \gt  5$ can lie in arithmetic progression with common difference $6$; and $5, 11, 17, 23, 29$ is the only exception.

*Proof.* Since $6 \equiv 1 \pmod 5$, the five terms
$$x, \quad x+6, \quad x+12, \quad x+18, \quad x+24$$
run through all residues modulo $5$, so exactly one of them is divisible by $5$. If that term exceeds $5$ it is an odd multiple of $5$ at least $25$, hence lies on $L_5$ and is struck. The term can fail to be struck only when it equals $5$ itself, which forces $x = 5$. $\blacksquare$

**The exception is real and must be carried in the statement.** For $x = 5$ the run is $5, 11, 17, 23, 29$, and all five are prime; an exhaustive search to $2\times10^5$ finds this and no other. It exists purely because $L_5$ is born at $25$: as a statement about the *residue classes* the argument is exact, and only the birth rule creates the exception.

*Verification.* At sieve depth $97$ over $4\times10^7$ cells of the upper rail $6b+1$, with $b$ running from $0$ and survivors taken to be the members coprime to every prime from $5$ to $97$, the run-length census is $6{,}448{,}150$ of length $1$; $2{,}404{,}092$ of length $2$; $778{,}762$ of length $3$; $211{,}170$ of length $4$; and **none of length $5$ or more.** The range is pinned by the survivor total itself: there are $14{,}437{,}300$ survivors, a density of $0.360932$ against $\prod_{5\le q\le 97}(1-1/q) = 0.360952$. (On the lower rail the same census gives $6{,}448{,}103$, $2{,}403{,}803$, $779{,}340$, $210{,}868$, and under the birth-at-$p^2$ rule that rail carries one run of length five, namely the exception $5, 11, 17, 23, 29$ of Theorem 3. The convention above is therefore part of the statement.) Regenerated by `code/verify_gap_alphabet.py`.

> **Corollary 1.** With $G_k$ the number of **starting positions** of a run of $k$ consecutive survivors at spacing $6$ on one rail — so that a run of length $\ell$ is counted once in each of $G_1,\dots,G_\ell$ — the full-cycle counts satisfy $G_k = \prod_{q}(q-k)$, for $k \lt  \min q$.

*Proof.* A run of $k$ forbids exactly $k$ marks on each ruler, leaving $q-k$. $\blacksquare$

**$G_k$ is not the census of maximal runs, and the two must not be read off one table.** For the lines $\lbrace 5,7\rbrace$ the starts are $24, 15, 8, 3, 0$, matching the product; the *maximal* runs of the same cycle are $2$ of length $1$, $2$ of length $2$, $2$ of length $3$ and $3$ of length $4$. Once $k$ reaches the smallest line the product would turn negative, and the true count is $0$: the formula holds below that point and the cap of Theorem 3 is what happens at it.

*Verification* (direct count over a full cycle of the line set, on one rail; the runs are counted at spacing $6$ in the cell index):

| lines | $k{=}1$ | 2 | 3 | 4 | **5** |
|-------|------|-----|----|----|---|
| $\lbrace 5\rbrace$ | 4 | 3 | 2 | 1 | **0** |
| $\lbrace 5,7\rbrace$ | 24 | 15 | 8 | 3 | **0** |
| $\lbrace 5,7,11\rbrace$ | 240 | 135 | 64 | 21 | **0** |

**The four laws $(q-1),\dots,(q-4)$ are therefore not four phenomena but one ruler with different numbers of marks.**

---

---

*The computations and much of the prose in this paper were prepared with AI assistance (ChatGPT, OpenAI; Claude, Anthropic), used for algebraic derivation, for drafting and rewriting code and text, for running the computations, and for auditing the papers against their own scripts. All statements were checked by the author, who is responsible for them; the repository README sets out the division of labour in full.*
---

## References

The eleven papers of this set are cited as [P1] to [P11], and the numbered entry below is the external work. This paper imports one result from outside the set — the convergence of §2.2 — and nothing else; every other statement it quotes is a definition or a statement of a companion paper, never a proof.

1. V. Brun, *La série 1/5+1/7+1/11+1/13+⋯ où les dénominateurs sont nombres premiers jumeaux est convergente ou finie*, Bull. Sci. Math. **43** (1919), 100–104, 124–128. — *the convergence of the sum over twin pairs, which dominates the gap-6 column of §2.2.*
