# The Cell System

[**Read the papers online — https://osman209.github.io/odd-sieve-cell-system/**](https://osman209.github.io/odd-sieve-cell-system/)

A coordinate system for the odd sieve: what it proves, what it only measures, and the
point at which it stops — derived from inside the construction rather than quoted.

Seven documents and four verification scripts. **Start with the overview.**

---

## What this is, and what it is not

**No progress toward the twin-prime conjecture is claimed, and no new bound on anything.**
Papers I–IV build a construction and prove what it decides; Paper V exists to establish the
opposite of a result — that the construction reaches the field's known barrier in its own
vocabulary, and to say precisely where.

Every headline result reached here already lives somewhere in the literature. Each paper
names the source. The table below is the map.

| what the papers reach | where it already lives |
|---|---|
| the four-state inheritance law under a new sieve line | the **wheel sieve**, and cycles of gaps in Eratosthenes' sieve |
| the correlation ladder `K_q(h) = q−2, q−3, q−4` and its product | the **Hardy–Littlewood** singular series (1923) for a prime quadruple |
| that this singular series averages to `1` | **Gallagher** (1976); refined by **Montgomery–Soundararajan** |
| the density of survivors of a truncated sieve, as a function of `log x / log z` | **Buchstab's** function `ω` (1937) |
| the recursive two-factor split of a survivor | **Buchstab's identity** |
| the sifting limit at which a lower bound stops being positive | **Selberg** (1949); **Iwaniec** (1971, 1980); **Diamond–Halberstam–Richert** (2008) |
| weights that convert a sieve count into an almost-prime statement | **Kuhn** (1954); **Richert** (1969) |
| `Ω ≤ 3` between consecutive squares | **Campbell** (2026); `Ω ≤ 2` asymptotically is **Chen** (1975) |
| almost all intervals `[n², (n+1)²]` contain the expected number of primes | **Bazzanella** (2000, 2011), by zero-density estimates |
| the largest gap in the coprime cycle | **Jacobsthal's** function; **Iwaniec** (1978), **Maier–Pomerance** (1990) |
| the parity obstruction the construction runs into | **Selberg's** parity argument (1949) |

**What the repository offers instead of a new result:**

1. **A construction followed honestly to its end.** An elementary coordinate system of lines
   and cells, developed until it produces Buchstab's identity, the singular series and the
   sifting limit `β₁ = 2` *without importing them* — and then stops exactly where the field
   stops. That the framework has no blind spot of its own is the finding.
2. **The obstruction stated from inside.** Paper V derives the barrier in the construction's
   own terms rather than citing it, and measures how much of the difficulty the framework
   can localise before failing to cross it — a set of density `10⁻³`, and still no crossing.
3. **Negative results and withdrawn claims, kept.** Appendix B of Paper V lists results this
   work produced and then retracted. The rate at which a structure like this manufactures
   plausible but spurious signals is itself among the findings.
4. **Runnable code for every number printed.** No table appears without a script that
   regenerates it, and every script exits non-zero when its claim fails.

**Priority is not claimed for any result in these papers.**

---

## Contents

```
papers/   seven documents, plus one standalone preprint in LaTeX and PDF
code/     four verification scripts, plus the rendering checker
docs/     the GitHub Pages site: a web page and a typeset PDF for every paper
```

### `papers/overview_the_cell_system.md`

**Start here.** The whole set in one pass — every result stated once, with its status
(proved, proved-under-hypothesis, or measured) attached. Eight sections: the coordinates,
the window, the cycle, the transfer, what the framework decides, where it stops, the
pattern the work keeps arriving at, and what an external ingredient would have to supply.

### `papers/paper_0_quadratic_staircase.md`

The odd one out: **it concerns no prime numbers at all.** For odd `n`, the increments
`W_j = ⌊2(j+1)²/n⌋ − ⌊2j²/n⌋` take only the values `0,…,4`, and their five multiplicities
are given exactly by `A = ⌊(n+7)/8⌋` — with no error term, which is the surprise, since a
probabilistic model of the same count returns the same answer and would normally carry one.
A companion theorem counts the interior local maxima of `2j² mod n`: exactly `2A` for every
odd `n ≥ 51`. Its proof turns on the four values `8x mod n` at the quarter points being
`±1, ±3, ±5, ±7` in some order, so that their squares always sum to `84`.

The paper states plainly how it differs from the objects it resembles. Replacing `j²` by `j`
gives the characteristic **Sturmian** word, but the analogy is one of form only: this word is
periodic, has five letters, and its factor complexity and imbalance are measured and reported
against the Sturmian values to show exactly how far the resemblance fails.

Also available as a standalone preprint: [`quadratic_staircase.tex`](papers/quadratic_staircase.tex), [`quadratic_staircase.pdf`](papers/quadratic_staircase.pdf).

### `papers/paper_I_cells_and_lines.md`

The coordinates. Each odd prime `p` is a line `L_p(k) = p² + 2pk`; the numbers `6m ± 1` form
a cell; the window between consecutive prime squares is where every line that matters is
already present. Includes the central-factor theorem — for odd `m` the two divisors nearest
`√m` are reached in exactly `a + b + 2` steps — with its handover corollary, and a section
saying which of these statements are restatements rather than results.

### `papers/paper_II_inheritance_law_on_the_cycle.md`

Exact transport. Adding a line `q` multiplies the cycle by `q`, and the census transports with
no error at all. The refined version tracks the full distribution of inheritance depth through
a finite-state generating function, and a size-binned refinement reproduces Richert's weight
to `0.4%`. §6 gives the correlation ladder that the singular series of Paper V is built from.

### `papers/paper_III_from_cycle_to_window.md`

What survives the move from an exact periodic law to a short interval. Soft weights transfer
almost exactly; sharp indicators do not. The distinction is measured rather than asserted, and
it governs everything in Paper V §7.6.

### `papers/paper_IV_twin_criterion.md`

What the framework proves outright: the six exceptional positions, the belt between consecutive
prime squares, the birth of a line and what it can remove on its first window. One statement
(Verified Law 17) is proved under a stated hypothesis and verified numerically beyond it, and
is labelled that way wherever it appears.

### `papers/paper_V_where_the_framework_stops.md`

The obstruction, derived rather than quoted. Two test cases are followed to their end — squares
and almost-primes, and Jacobsthal's function — and both land on the same wall. §7.6 measures the
transfer in three layers: the mean is exact; the state totals move by the two-dimensional
Buchstab factor `e^{2γ}/4`, confirmed to three decimals at `X = 10¹⁰`; the shape carries a
residual that saturates. It then shows that the quantity a weighted sieve argument actually
evaluates transfers with a relative error of `0.36%`, so the computation is not the obstruction
by a wide margin.

The section also records a correction made during the work: an earlier draft reported the error
in a singular-series average as `O(log H)`, and extending the computation to the seventh
primorial showed that to be the curvature of a quadratic seen over too short a range. The claim
is withdrawn in place rather than quietly replaced.

---

## Reproducibility

Every number in the papers is regenerated by a script in `code/`. Each exits non-zero when the
claim it supports does not hold, and each accepts `--force-fail` to exercise that gate.

```
pip install numpy scipy sympy

python3 code/verify_central_pair.py                          # Paper I §5 — the central factor
python3 code/verify_cell_transfer.py                         # Paper III §6, Paper V §6.5, Appendix B
python3 code/verify_transfer_layers.py --fast                # Paper V §7.6 — the three transfer layers
python3 code/verify_singular_series_order.py --hm 1616615    # Paper V §7.6 — checksum at Q₆
```

Full runs:

```
python3 code/verify_transfer_layers.py           # to X = 10⁹,  ~10 min
python3 code/verify_transfer_layers.py --deep    # adds X = 10¹⁰, ~35 min
python3 code/verify_singular_series_order.py     # to Q₇ = 37,182,145, ~2 min
```

`verify_singular_series_order.py` uses a segmented sieve so that it reaches the seventh primorial
inside ordinary memory. Its header documents one thing worth reading before reproducing anything:
the subtracted expectation is of size `C`, so an unclosed tail in the prime bound is amplified by
`C` — two runs differing only in that bound disagreed by `0.1` at `C = 1.6×10⁶`, which is larger
than several of the effects being measured. The script closes that tail analytically, and a
reproduction that does not will not match.

### Rebuilding the PDFs

`code/build_pdfs.sh` regenerates `docs/*.pdf` from `papers/*.md` with pandoc and pdflatex,
using `code/pdf_header.tex`. The same source serves both outputs: `\lbrace`, `\rbrace` and
`\cr` are valid in KaTeX and in LaTeX alike. Run the rendering checker first — a math span
whose closing `$` is preceded by a space renders correctly on GitHub and is invisible to
pandoc, which is how the first conversion attempt failed.

```
sh code/build_pdfs.sh
```

### The rendering checker

`code/check_github_math.js` is not a mathematical check. It extracts every formula, applies
GitHub's escape-stripping, renders it through KaTeX, and inspects the **output** for the two
failures that raise no error: a lost subscript, and a brace that has silently vanished. It also
refuses macros GitHub's deployment rejects, and requires a constant pipe count per table block.

```
npm install katex && node code/check_github_math.js papers/*.md README.md
```

It should report exactly **one** problem: a false positive in Paper 0, verified by rendering.
The checker exists because the papers in this repository failed on 741 counts the first time it
was run against them, in five separate modes, every one of which had bitten before.

---

## Three method rules this work exists to illustrate

All three were learned by getting them wrong first, during this work.

**Match on mechanism, never on vocabulary.** Three expert readers were identified in turn as the
right person to ask about Paper 0 — one on "three-distance theorem", one on "differences of floor
functions", one on "exact frequencies" — and all three were wrong in the same way: each works on
the *irrational, aperiodic* side, and this object is rational and periodic. The words matched and
the regime did not. The same failure at a larger scale would be to call a construction new because
its notation is.

**A drifting coefficient is a wrong model, not a noisy one.** A singular-series average was fitted
over a short range, produced a coefficient near `0.85` that moved with the fitting window, and was
reported as `O(log H)` with the drift described as instability. Extending the range by two orders
of magnitude showed the drift to be the curvature of `(log C)²`. The instability *was* the signal;
it was read as noise.

**Reviewing the source is not reviewing the page.** Every paper here passed several content audits
and would still have been published with hundreds of broken formulas, because no audit had looked
at the rendered page. Two of the failure modes are silent: a stripped `\{` prints mathematics that
is simply wrong, with no error box anywhere.

---

## On the use of AI assistance

The verification scripts in `code/`, and much of the prose in `papers/`, were written with the
assistance of **Claude (Anthropic)**, used as a working collaborator: drafting and rewriting code,
running the computations, drafting and editing text, searching the literature, and auditing the
papers against their own scripts.

The research direction, the questions asked, the decisions about what to publish and what to
withdraw, and the final responsibility for every claim are the author's.

Several corrections recorded in these papers were found by that auditing, and several were errors
the assistant had itself introduced on an earlier pass and found on a later one — including the
withdrawn `O(log H)` claim above, and a numerical reconciliation in §7.6 that compared an
asymptotic limit against a finite-scale measurement as though they were the same quantity. Where
a result is reported here, it is because a script regenerates it and the script has been read.

---

## Status

Seven documents. Papers I–IV are the construction and what it decides; Paper V is the account of
where it stops, and is the reason the set exists in this form. Paper 0 is independent of the rest
and can be read on its own.

The open question the work leaves is stated in Paper V §8.1, and it is external: the framework
supplies the objects a weighted sieve argument needs, to measured accuracy, and cannot supply the
rigorous lower bound that argument would consume. Nothing here suggests that bound is close.

Corrections, counterexamples and pointers to prior art are all welcome; open an issue. **Being told
that something here is already known is a useful outcome, not an unwelcome one** — the repository's
own conclusion is that most of it is.

---

## Related work

The author's other line of work — the division table, the Weil quadratic form, the Li–Sekatskii
coefficients and the numerical study of the zeta zeros — is in a separate repository:
**[prime-number-studies](https://github.com/Osman209/prime-number-studies)**
([site](https://osman209.github.io/prime-number-studies/), DOI [10.5281/zenodo.21638887](https://doi.org/10.5281/zenodo.21638887)).
The two programmes are independent; nothing here depends on anything there.

---

## License

- Text, papers and figures: **CC BY 4.0** — see `LICENSE-CONTENT`.
- Code: **MIT** — see `LICENSE`.

## Citation

```
Osman, M. (2026). The Cell System: a coordinate system for the odd sieve —
what it proves, what it measures, and where it stops. Zenodo.
```

Repository: <https://github.com/Osman209/odd-sieve-cell-system>
ORCID: <https://orcid.org/0009-0004-5912-999X>
