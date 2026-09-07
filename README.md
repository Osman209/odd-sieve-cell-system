# The Cell System

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22085626.svg)](https://doi.org/10.5281/zenodo.22085626)

[**Read the papers online — https://osman209.github.io/odd-sieve-cell-system/**](https://osman209.github.io/odd-sieve-cell-system/)

A coordinate system for the odd sieve: what it proves, what it only measures, and the
point at which it stops — derived from inside the construction rather than quoted.

Eleven papers, one overview and nine verification scripts. **Start with the overview.**

---

## What this is, and what it is not

**No progress toward the twin-prime conjecture is claimed, and no new bound on anything.**
Papers 1 to 4 build the coordinates and the transport laws, and papers 5 to 8 the construction
and what it decides about twin pairs. Papers 9 to 11 exist to establish the opposite of a result —
that the construction reaches the field's known barrier in its own vocabulary, and to say
precisely where.

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
   and cells, developed until it produces Buchstab's decomposition, the Hardy–Littlewood
   singular series and the exact factor-of-two loss `I(s) = 2f₁(s)` *without importing them*
   — and then stops exactly where the field stops. (The sifting limits `β₁`, `β₂` are quoted
   from the literature, not derived here.) That the framework has no blind spot of its own is
   the finding.
2. **The obstruction stated from inside.** Paper 9 derives the barrier in the construction's
   own terms rather than citing it, and papers 10 and 11 measure how much of the difficulty the
   framework can localise before failing to cross it — a set of density `10⁻³`, and still no
   crossing.
3. **Negative results and withdrawn claims, kept.** Appendix B of Paper 11 lists results this
   work produced and then retracted. The rate at which a structure like this manufactures
   plausible but spurious signals is itself among the findings.
4. **Runnable code for every number printed.** No table appears without a script that
   regenerates it, and every script exits non-zero when its claim fails.

**Priority is not claimed for any result in these papers.**

---

## Contents

```
papers/   eleven papers and one overview, plus one standalone preprint in LaTeX and PDF
code/     nine verification scripts, plus the rendering checker and the site build
docs/     the GitHub Pages site: a landing page per paper, with its PDF
```

### `papers/paper_01_quadratic_staircase.md`

**Paper 1. An Exact Histogram for a Quadratic Staircase.** The increments of $\lfloor 2j^2/n\rfloor$, and the local maxima of $2j^2 \bmod n$.

### `papers/paper_02_cells_and_lines.md`

**Paper 2. Cells and Lines.** A coordinate system for the odd sieve.

### `papers/paper_03_inheritance_law_on_the_cycle.md`

**Paper 3. The Inheritance Law on the Cycle.** Exact transport of the divisor census, and of weights, over a sieve cycle.

### `papers/paper_04_from_cycle_to_window.md`

**Paper 4. From Cycle to Window.** What survives when an exact periodic law is evaluated on a short interval.

### `papers/paper_05_gap_alphabet.md`

**Paper 5. The Gap Alphabet.** Which gaps can occur between consecutive odd composites, and where the ladder of proofs stops.

### `papers/paper_06_twin_criterion.md`

**Paper 6. The Twin Criterion: Six Exception Positions.** A single open cell in a sector is a twin pair unless it sits at one of six named places.

### `papers/paper_07_clocks_and_inheritance.md`

**Paper 7. Clocks and Inheritance.** Primality as a zero-test, and the capacity of a single line across sectors.

### `papers/paper_08_belts_and_short_windows.md`

**Paper 8. Belts and Short Windows.** What a line can do between its own square and the next, and the anatomy of the window between consecutive squares.

### `papers/paper_09_the_exact_obstruction.md`

**Paper 9. The Exact Form of the Obstruction.** An identity for the twin count with no error term, and why an ordinary sieve cannot cross it.

### `papers/paper_10_four_tests.md`

**Paper 10. Four Tests of the Cell System.** Jacobsthal, almost-primes between squares, shared cofactors, and collisions.

### `papers/paper_11_what_a_continuation_needs.md`

**Paper 11. What a Continuation Would Have to Supply.** The external ingredient, the limitations, and the routes already closed.

### How to read the citations

Companion papers are cited as `[P1]` to `[P11]`. A bare number in brackets is an entry in that
paper's own reference list, so `[P9]` is always Paper 9 and `[9]` is always the ninth reference of
the paper you are reading. Each paper numbers its own results from one, so `[P6, Thm 1]` is
Theorem 1 of Paper 6 and an unqualified "Theorem 1" is always the paper you are in. Result numbers
changed at version 2.0.0, when the eleven parts stopped sharing one numbering.

### Checking a claim

Every number printed in the papers is regenerated by a script in `code/`, and each script exits
non-zero if the claim it supports fails.

```
python3 code/verify_exception_dichotomy.py         # one script
for f in code/verify_*.py; do python3 "$f"; done   # all nine
python3 audit.py                                   # structure: references, numbering, tables
```

Several of the scripts take `--fast` for a shorter run.

---

## On the use of AI assistance

Large language models were used as tools. The research direction, the questions, the objects
studied, and the responsibility for every claim are the author's. **ChatGPT (OpenAI)** was used for
algebraic derivation and independent checking; **Claude (Anthropic)** for the numerical work, the
scripts in `code/`, review and most of the prose. Where the two disagreed, computation settled it,
and the text records the resolution.

Where a result is reported here it is because a script regenerates it and the script has been read.
That discipline, rather than any assurance about the tools, is what the reader is asked to rely on.
**No statement in these papers rests on the assertion of a model.**

---

## Status

Eleven papers and one overview. Papers 1 to 4 build the coordinates and the transport laws;
papers 5 to 8 are the construction and what it decides about twin pairs; papers 9 to 11 are the
account of where it stops, and are the reason the set exists in this form. Paper 1 is independent
of the rest and can be read on its own.

The open question the work leaves is stated in Paper 11 §2.1, and it is external: the framework
supplies the objects a weighted sieve argument needs, to measured accuracy, and cannot supply the
rigorous lower bound that argument would consume. Nothing here suggests that bound is close.

Corrections, counterexamples and pointers to prior art are all welcome; open an issue. **Being told
that something here is already known is a useful outcome, not an unwelcome one** — the repository's
own conclusion is that most of it is.

---

## Three method rules, learned by getting them wrong

**Match on mechanism, not on vocabulary.** Three experts were identified in turn as the right reader
for Paper 1 — on "three-distance theorem", on "differences of floor functions", on "exact
frequencies" — and all three were wrong the same way: each works on the irrational, aperiodic side,
and this object is rational and periodic. The words matched and the regime did not.

**A drifting coefficient is a wrong model, not a noisy one.** A singular-series average fitted over
a short range gave a coefficient near `0.85` that moved with the fitting window, and was reported as
`O(log H)` with the drift called instability. Two more orders of magnitude showed the drift to be
the curvature of `(log C)²`. The instability was the signal.

**Reviewing the source is not reviewing the page.** Every paper passed several content audits and
would still have been published with hundreds of broken formulas, because no audit had looked at
the rendered page. Two of the failure modes are silent: a stripped `\{` prints mathematics that is
simply wrong, with no error anywhere. And a checker is not the page either — two further modes
appeared on GitHub that this repository's own checker had passed. Both were found by opening the
page and reading it.

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
https://doi.org/10.5281/zenodo.22085627
```

Repository: <https://github.com/Osman209/odd-sieve-cell-system>
ORCID: <https://orcid.org/0009-0004-5912-999X>
