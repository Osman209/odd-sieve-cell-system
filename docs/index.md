# The Cell System

**A coordinate system for the odd sieve — what it proves, what it measures, and where it stops.**

Seven documents on the elementary sieve of the odd numbers. **Every paper has a typeset PDF** alongside the web version. Papers I–IV build a construction
and prove what it decides; Paper V derives the point at which it stops *from inside the
construction* rather than quoting it.

**No progress toward the twin-prime conjecture is claimed, and no new bound on anything.**
Priority is not claimed for any result here. Every headline result reached already lives
somewhere in the literature, and each paper names the source.

[Repository](https://github.com/Osman209/odd-sieve-cell-system) ·
[The author's other work: Prime Number Studies](https://osman209.github.io/prime-number-studies/)

---

## The papers

### [Overview — a coordinate system for the odd sieve](overview_the_cell_system.md) · [PDF](overview_the_cell_system.pdf)

**Start here.** The whole set in one pass: every result stated once, with its status —
proved, proved-under-hypothesis, or measured — attached to it.

### [Paper 0 — an exact histogram for a quadratic staircase](paper_0_quadratic_staircase.md) · [PDF](paper_0_quadratic_staircase.pdf)

The odd one out: **it concerns no prime numbers at all.** For odd `n`, the increments
`⌊2(j+1)²/n⌋ − ⌊2j²/n⌋` take only the values `0,…,4`, and their five multiplicities are
given exactly by `⌊(n+7)/8⌋` — with no error term, which is the surprise. A companion
theorem counts the local maxima of `2j² mod n`, and turns on four residues whose squares
always sum to `84`.

The standalone preprint, typeset in LaTeX rather than converted: [PDF](quadratic_staircase.pdf).

### [Paper I — cells and lines](paper_I_cells_and_lines.md) · [PDF](paper_I_cells_and_lines.pdf)

The coordinates. Each odd prime is a line, the numbers `6m ± 1` are a cell, and the window
between consecutive prime squares is where every line that matters is already present.
Includes the central-factor theorem and a section on which statements are restatements
rather than results.

### [Paper II — the inheritance law on the cycle](paper_II_inheritance_law_on_the_cycle.md) · [PDF](paper_II_inheritance_law_on_the_cycle.pdf)

Exact transport: adding a sieve line multiplies the cycle and the census transports with no
error at all. A refined form tracks the full depth distribution through a finite-state
generating function and reproduces Richert's weight to `0.4%`.

### [Paper III — from cycle to window](paper_III_from_cycle_to_window.md) · [PDF](paper_III_from_cycle_to_window.pdf)

What survives the move from an exact periodic law to a short interval. Soft weights transfer
almost exactly; sharp indicators do not. The distinction is measured, not asserted.

### [Paper IV — the twin criterion](paper_IV_twin_criterion.md) · [PDF](paper_IV_twin_criterion.pdf)

What the framework proves outright: the six exceptional positions, the belt between
consecutive prime squares, and what a newborn line can remove on its first window.

### [Paper V — where the framework stops](paper_V_where_the_framework_stops.md) · [PDF](paper_V_where_the_framework_stops.pdf)

The obstruction, derived rather than quoted. Two test cases are followed to their end and
both land on the same wall. The transfer is measured in three layers; the two-dimensional
Buchstab factor `e^{2γ}/4` is confirmed to three decimals at `X = 10¹⁰`; and the quantity a
weighted sieve argument evaluates transfers with a relative error of `0.36%`, so the
computation is not the obstruction. A claim withdrawn during the work is recorded in place
rather than quietly replaced.

---

## What the work offers instead of a new result

**A construction followed honestly to its end.** It produces Buchstab's identity, the
Hardy–Littlewood singular series and the sifting limit `β₁ = 2` without importing any of
them, and then stops exactly where the field stops. **That the framework has no blind spot
of its own is the finding.**

**Negative results and withdrawn claims, kept.** Appendix B of Paper V lists results this
work produced and then retracted. How readily a structure like this manufactures plausible
but spurious signals is itself among the findings.

**Runnable code for every number printed.** Four scripts in the repository regenerate every
table, and each exits non-zero when the claim it supports fails.

---

Corrections, counterexamples and pointers to prior art are welcome —
[open an issue](https://github.com/Osman209/odd-sieve-cell-system/issues).
Being told that something here is already known is a useful outcome, not an unwelcome one.

Text CC BY 4.0 · code MIT · ORCID [0009-0004-5912-999X](https://orcid.org/0009-0004-5912-999X)
