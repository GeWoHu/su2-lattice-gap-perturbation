# YM-04.5 — PRIOR-ART EQUIVALENCE MAP
Phase 2 synthesis (parent-run after hunt-child failure), 2026-11-05 ~10:25 CST.
Frozen object: see FROZEN_THEOREM.md. Kill targets: T1 = -71/105, T2 = -(142/105)g⁻¹⁰, T3 = relative -(284/315)g⁻¹² (NORMALIZATION_CROSSWALK.md).

## Equivalence classes examined

### A. Exact-object candidates (3+1d Hamiltonian one-glueball gap, second order)
| Source | Object match | Operator match | Coefficient found | Status |
|---|---|---|---|---|
| KSS76, NPB B114 (1976) 199 | YES | presumed (KS Hamiltonian) | not readable | ACCESS-INCOMPLETE — sole kill condition |
| KS75, PRD D11 (1975) 395 | partial (foundational; dispersion discussed) | YES | not readable | ACCESS-INCOMPLETE |
| Kogut RMP 51 (1979) 659 | likely (review of the above) | YES | not readable | ACCESS-INCOMPLETE |
| Decker–Sinclair 1984 (INSPIRE 199845) | NO — Euclidean mixed-action mass gap | different action | — | NO MATCH |

### B. Method prior art (same scheme, different or unspecified object)
| Source | Finding |
|---|---|
| Creutz, *Quarks, Gluons and Lattices* (1983), full text | Describes exactly our expansion ("magnetic term acts as a perturbation… first correction… links around a single plaquette into the fundamental representation"), delegates numbers to Kogut 1979. No second-order coefficient printed. Zero "71/105" hits in full-text scan. |
| Morningstar lecture notes (2+1d), full text | Same recoupling channel values (-1/3, -1/6, -3/14), same vacuum -x²N/3; object = static q-q̄ line in 2+1d. Exact 2+1d analogue coefficient -131/105 ≠ -71/105. Channel-level equivalence, dimension/object mismatch. |

### C. Different-expansion neighbors (excluded by Crosswalk §2)
- Hamer–Oitmaa–Zheng PRD 45 (1992) 4652 and ELCE series work: 2+1d, transfer-matrix β-series.
- Coupled-cluster line (Schütte–Weihong–Hamer PRD 55 (1997) 2974; hep-lat/9805011 full text): 2+1d KS Hamiltonian, β variable.
- Pavel hep-lat/0912.5465, 1611.06542: derivative expansion λ=g^{-2/3}, continuum-field variables; no μ² glueball-gap coefficient.
- Euclidean high-order glueball series (10th–28th order): raw comparison forbidden; only a second-order term after re-expansion could touch T3 — none located.

### D. Modern (post-2020) quantum-computation/SW-transform line
arXiv sweeps (glueball × strong-coupling × Hamiltonian; quant-ph × strong-coupling; coupled-cluster × LGT): no 2020+ paper publishes a 3+1d SU(2) one-glueball gap coefficient in μ = 2g⁻⁶ form within the search window. Absence of hits is NOT treated as novelty evidence (mission rule).

## Adjudication
1. **Is -71/105 already published?** UNKNOWN. The only full-text source with object proximity (Morningstar) is 2+1d with a different object and a provably different coefficient. The only object-matched source (KSS76) is unreadable after five access routes (publisher, Wayback, libgen, Anna's Archive, INSPIRE documents). Classification: **NOVELTY UNRESOLVED**.
2. **Would a practitioner regard it as routine?** YES for the method — degenerate perturbation theory in the strong-coupling basis is textbook (Creutz states the recipe outright). The assembled statement (exact rational coefficient + L≥5 band-head theorem + L=4 exception) is more rigorous than the genre standard but mathematically modest.
3. **Kill condition status**: armed, unresolved. If KSS76 (or KS75/RMP79) prints T2/T3, classification flips to KNOWN with no change to correctness.
4. **Do NOT cite as prior art**: 2+1d coefficients (-131/105 family), Euclidean β-series, derivative-expansion results — all fail the operator/object/dimension test.
