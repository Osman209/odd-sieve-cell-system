# Coverage

One row per verification script. The column that matters is **the definition used**: three
review passes each found a script passing green against a definition the paper did not
state, so a `COVERS` line naming a *section* is not enough — what has to be written down,
and compared with the paper by eye, is the quantity the script actually computes.

The rule for maintaining this file: **a script may not be added or changed without its row,
and the row must be written from the script, then checked against the paper.** If the two
readings differ, one of them is wrong, and that is the whole point of the exercise.

`--fast` is the range this table records unless stated otherwise; several scripts reach
further under `--full`, and where that matters it is in the range column.

| script | covers | the definition it uses | range executed | tolerance, and why |
|---|---|---|---|---|
| `verify_quadratic_staircase.py` | [P1], all sections | `W_j = ⌊2(j+1)²/n⌋ − ⌊2j²/n⌋` over the first cycle `0 ≤ j ≤ n−1`; local maxima of `2j² mod n` taken **strictly** | odd `n ≤ 20,001` (`--full`: 200,001) | exact — integer identities, no tolerance |
| `verify_central_pair.py` | [P2, §5] | `ℓ(m)` is the least `k ≥ 1` at which the largest divisor of `m(m+2k)` below its square root exceeds `m` | odd `m < 4,000` | exact |
| `verify_new_additions.py` | [P2, §3.5], [P2, §3.6], [P3, §3], [P3, §4], [P6, §2.8], [P9, §2.2] | phase normalised by the **birth index** `c = a` with `p = 6a+σ`, not by `6⁻¹` | primes `< 3,000`, twin rows `< 20,000` | exact. **This is the row the second pass caught**: the paper used to say `6⁻¹`, the script has always used the birth index, and the corollary was false for `p ≡ 1 (mod 6)`. [P2, §3.5] now states the script's convention |
| `verify_four_state_law.py` | [P3, §§2.1–2.4], [P3, §§5.1–5.2] | cycle modulus is `∏q` in the **cell** index, not `6∏q`; `(A,B,C,D)` counted over one full cycle | lines to 19 (`--full`: to 199) | exact in rational arithmetic; the Mertens columns to four printed decimals |
| `verify_bin_generating_function.py` | [P3, §4.3] | **two** markers per bin, `∏((q−2) + u_β + v_β)`; bins are equal blocks of the line list in size order | full cycle of `{5,7,11,13,17,19}`, `M = 1,616,615` | exact, state by state. Also asserts the one-marker form has fewer monomials than there are states — which is why it cannot carry the claim |
| `verify_window_transfer.py` | [P2, §4.3], [P4, §2.1], [P4, §§3.4–3.5], [P6, §2.1] | moving depth: sector `(u², (u+2)²)` with `u ≡ 5 (mod 6)`, sieved by every line `≤ u` | `U ≤ 1,019` (`--full`: 2,039) | exact on counts; `T`, `M` to one printed decimal |
| `verify_l2_stress.py` | [P4, §3.2], [P4, §5.3] | §3: `u ≡ 5 (mod 6)`, window `(u²,(u+2)²)`. §5: **every** integer `u`, window `(u²,(u+1)²)`, and `D_r = strikes − 2X_r/r` with `X_r` the cells of the sectors `u ≥ r` only | `U ≤ 600` (`--full`: 2,400) | the flat ratio is asserted below 0.01 and within a factor 1.5 across `U`; the deterministic term is asserted at ≥ 95% of the old ratio. **This is the row the second pass caught**: the old normalisation `2X/r` charged each line for sectors before its birth |
| `verify_l2_nested.py` | [P4, §5.3] | the **nested** deviation `ε_r(u)` — strikes of `r` on the survivors of the smaller lines — and the `B_r` of [P4, Thm 3] | `U ≤ 600` (default 1,200) | `Σ B_r = T − M` asserted to machine precision; the exponent asserted only to lie in (2,3), because three points do not fix it |
| `verify_restricted_depth.py` | [P4, §5.3] | depth capped at a **fixed** `z = U^{1/2}`, not a per-sector `u^{1/2}` | `U ≤ 2,400` (`--full`: 38,400) | reported, not asserted against any printed row: the row it regenerated has been withdrawn from the paper |
| `verify_deviation_tables.py` | [P4, §4.1], [P9, §3.6], [P9, App. A] | `μ_r` is the mean of `ε_r` over sectors; identity A predicts `−(χ_r/r)Q_{r⁻}` | 1,400 sectors under `--full`, fewer by default | `μ_5` exact at any sector count; the other rows to their printed decimals. The `z`-score row is statistical and is reported, not asserted |
| `verify_gap_alphabet.py` | [P5], all sections | survivors on **one rail**, coprime to every prime from 5 to the depth, runs counted at spacing 6 | depth 97 over `4×10⁷` cells under `--full` | exact counts; the density to six decimals against `∏(1−1/q)` |
| `verify_exception_dichotomy.py` | [P6, §2.2], [P6, §2.3] | the six positions as quadratics in `n` with `M = 6n+3`; the budget maximised over residues, not over enumerated configurations | all 35 classes; all 2,431 alignments | exact — these are exhaustive scans over residue classes, so they are proofs and carry no tolerance. **What it does not emit**: the 28 maximal configurations, the 27 eliminations and the 59 polynomials with an explicit prime bound. [P11, §2.4] should not claim it does |
| `verify_exception_certificate.py` | [P6, §2.3] | a **configuration** is the set of counted cells together with the states those cells force, so two optimal state sequences differing only where no cell is counted are the same configuration — which is why 28 is reported and not the 357,210 optimal sequences; elimination means a prime dividing one polynomial of the system at every residue of `t` | the 9 extremal alignments; primes to 200 | exact. The check is complete because the system has total degree 90, so `q > 90` always leaves a residue |
| `verify_bonferroni_depth.py` | [P6, §2.2], [P6, §2.9] | `m(d)` counts lines striking the cell `d`; `S_i = Σ_d C(m(d), i)` in one pass | every sector below `M = 2,500` | exact; the alternating sum asserted to equal `C_M` at order `max_d m(d)` |
| `verify_coverage_and_exceptions.py` | [P9, §3.5], [P6, App. A], [P6, App. B] | greedy control: same lines, same **number** of classes per line, classes chosen greedily instead of at `±6⁻¹` | `m ≤ 4,001` (`--full`: 100,003) | exact — the greedy run leaves zero survivors, which is a count |
| `verify_smoothed_mask.py` | [P6, App. B.4] | double tent, support `4H−3`; the criterion is a two-sided deviation below the mean, not positivity | `P ≤ 19`, `Q` to 1,616,615 | exact; the implication `4H−3 ≥ g` asserted, the converse only reported |
| `verify_clocks_and_inheritance.py` | [P7, §2], [P7, §3], [P7, App. A] | `φ_q(p) ≡ (q−p)/2 (mod q)`; the distance-6 graph joins **survivors**, and its object is a pair `(p, p+6)`, not a twin | lines to 13, `P = 101` | exact |
| `verify_belts_and_windows.py` | [P8, §2], [P8, §3] | belt `= (r²−q²)/6 − 1` cells between two gates; depth capacity `D_M(p) = max{r : pʳ < (M+2)²}` | `q < 5,000` (`--full`: 200,000) | exact |
| `verify_line_routes.py` | [P9, §3.4] | the five routes in one window at `M₀ = 448,353`, cut at `z = 5857` | the single window | exact on counts; the independence checks are statistical and are reported with their nulls |
| `verify_parity_mean.py` | [P9, §2.3] | mean of `(−1)^Ω` over `z`-rough `n`, and over `z`-rough `n` with `n+2` also rough | `4×10⁷` integers at `10⁸` under `--full` | the three-sigma agreement with `1 − 2/(1+log 2)` is asserted **only under `--full`**, because the published row meets it at exactly three errors |
| `verify_four_tests.py` | [P10, §§2.3–2.5], [P10, §2.8], [P10, §§2.11–2.12], [P10, §2.14] | collisions counted **inside the belt**, `v ≤ H = (N+9)/6` | prime lines below `2×10⁴` | exact. **This is the row the merged pass caught**: [P10, Thm 7] used to be stated for the whole list `S_p` while both its proof and this script use the belt. The theorem now states the restriction |
| `verify_sharing_index.py` | [P10, §2.9] | the floor test is on `s`, where `k = p+2s`; sharing means a common **odd** cofactor in the open window `(k²,(k+2)²)` | odd `p < 150` (default 400) | exact; the 93 disagreements are asserted to be floor-equalities without sharing, all at composite `p+2` |
| `verify_singular_series_order.py` | [P10, §2.6] | `S_B(h)` truncated at `z`, with the tail of `G` closed analytically rather than by a prime bound | `C ≤ 10⁵` (`--full` reaches `3.7×10⁷`) | **a fit, not a certificate.** Exit 0 means the decomposition reproduces; it does not test the asymptotic order, which the paper labels measured |
| `verify_transfer_layers.py` | [P10, §2.5] | the three layers: mean depth, `NN` totals, conditional depth law inside `OO` | `X ≤ 10⁸` (`--full`: 10¹⁰) | layer 1 exact; layers 2 and 3 to their printed decimals. Rows above the cutoff are skipped and **named in the output**, not silently passed |
| `verify_dimension_two_sieve.py` | [P10, §2.5] | its own no-crossing `β = 4.834`, which is the Rosser–Iwaniec value, **not** DHR's 4.2664 | `s ≤ 40`, step `1/4096` | **a record, not support for a printed claim.** The `Ω ≤ 5` statement it was written for is no longer in any paper; the DHR row is labelled UNVERIFIED in its own output |
| `verify_continuation_budget.py` | [P11, App. C.2] | `τ = T − U + Q` on the distance-6 graph; `deg₆` read so that `Σ deg₆ = 2G` | `P ≤ 997` (`--full`: 1,999) | `τ` exact; `S` within one of the printed value; `c_p` to three decimals — a tolerance, and the printed 1.0074 against the computed 1.0079 is inside it |
| `verify_cell_transfer.py` | [P4, §6.1], [P9, §3.2], [P11, App. A] | window-over-cycle ratios by state, at moving depth | `X ≤ 10⁸` | to printed decimals |
| `verify_first_appearance.py` | — | **orphan**: no published table depends on it; kept as a record of the bad-phase sweep | — | — |

*`code/set_doi.py` and `code/build_site.py` and `code/build_pdfs.sh` are build tools, not verifications, and carry no row.*

## What this table does not do

It does not prove that a script is right, and it does not replace reading one. It makes the
one failure that has recurred visible: a definition in the middle column that a reader of
the paper would not recognise. Three of the rows above carry exactly that history, and each
is marked.

Two gaps remain and are recorded rather than papered over:

- **[P6, §2.3]'s certificate — now closed.** `verify_exception_dichotomy.py` reaches the
  ceiling of 31 and the surviving alignment; `verify_exception_certificate.py` supplies the
  rest, and writing it corrected the paper twice: the eliminating primes are 19, 23 and 31
  but the split of the 27 among them depends on the order they are tried, and three primes
  leave the survivor exactly one residue, not two.
- **[P9, §2.2]'s mean of `(−1)^Ω` over rough `n`.** The `4×10⁷` factorisations are inside
  `verify_parity_mean.py --full` and out of reach of a default run, so a default run does
  not check that row.
