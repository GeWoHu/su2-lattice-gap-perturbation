# SU(2) Lattice Gauge Theory: Exact Second-Order Strong-Coupling Gap Expansion on the Three-Torus

## Status: PREPRINT FOR EXPERT REVIEW — NOT PEER REVIEWED

This repository publishes a fixed-volume mathematical physics computation
for **transparent, independent human review**. It is a review release,
**not** a claim of discovery and **not** a completed, peer-accepted proof.
Independent model-based (AI) verification was used during preparation;
that is **not** human peer review.

## Reported result (fixed finite volume, `L >= 5`)

Dimensionless form (production normalization dictionary):

```
Delta(mu, L) = 3 - (71/105) * mu^2 + o_L(mu^2)
```

Physical normalization (`mu = 2 g^-6`):

```
Delta_phys = (3/2) g^2 - (142/105) g^-10 + O(g^-16)
```

with relative second-order coefficient `284/315 · g^-12`. All coefficient
identities are verified in exact rational arithmetic (see
[Reproducibility](#reproducibility)); the coefficient is **not** described
as a certified new theorem.

## What is open

1. **R3' — internally proved (2026-11-06); human review still requested.**
   The standalone exhaustive derivation of the channel-exhaustion selection
   rule is now supplied as **Appendix G**: Peter–Weyl external typing, the
   complete four-channel overlap decomposition `(0,0)⊕(0,1)⊕(1,0)⊕(1,1)`,
   crossed-channel annihilation against the diagonal `(j,j)` type, and the
   full admissibility argument — independent of the full-space operator
   identity (which remains as a cross-check). A slot-counting erratum in
   the earlier derivation sentence is disclosed transparently in an
   Appendix F footnote; the selection-rule *statement* is unchanged.
   Independent model-based adversarial review (two hostile audits, two
   re-review rounds, split verdict adjudicated line by line) is preserved
   in `evidence/REFEREE_R3PRIME*.md`. **Model-based review is not human
   peer review**; the appendix is explicitly offered for human audit, and
   the prior obligation trail remains in
   `evidence/REFEREE_YM046_FINAL2.md`.
2. **Novelty: UNRESOLVED.** Pending a library-level comparison with
   Kogut–Sinclair–Susskind, *Nuclear Physics* **B114** (1976) 199–236
   ([DOI](https://doi.org/10.1016/0550-3213(76)90586-1)). The recorded
   equivalence test is in `supplementary/`. No originality is claimed.
3. **Scope.** Fixed finite lattices `T_L^3`, `L >= 5` only. This is **not**
   a statement about the continuum Yang–Mills mass-gap problem; no
   continuum limit and no uniform-in-`L` claim is made.

## Contents

- [`manuscript.pdf`](manuscript.pdf) / [`manuscript.tex`](manuscript.tex) —
  the paper; [`appendix-body.tex`](appendix-body.tex) — appendices A–G.
- [`code/`](code/) — exact verification scripts (Python, `sympy`/`fractions`,
  no floats in the assertion path).
- [`receipts/`](receipts/) — machine receipts for each check, including the
  consolidated mechanical self-check
  [`receipts/META01_RECEIPT_YM046.json`](receipts/META01_RECEIPT_YM046.json).
- [`evidence/`](evidence/) — full independent-referee adjudication trails
  (`REFEREE_YM046*`: four rounds on the original release; `REFEREE_R3PRIME*`:
  four rounds on the Appendix G amendment, split verdict adjudicated;
  all model-based, disclosed as such).
- [`supplementary/`](supplementary/) — prior-art equivalence test and
  primary-source access log.
- [`FINAL_VERDICT.md`](FINAL_VERDICT.md) — preparation-stage verdict and
  repair history.
- [`REVIEW_REQUEST.md`](REVIEW_REQUEST.md) — specific questions for
  mathematical physicists.
- [`MANIFEST.sha256`](MANIFEST.sha256) — artifact integrity.

## Reproducibility

```
python3 code/verify_anchors.py        # normalization engine + YM-03.6 anchor
python3 code/verify_identity.py       # operator identity M2 = (1/3+v)A + cI (full space, L=5)
python3 code/verify_census.py         # adjacency census + coefficient identities
python3 code/verify_bandhead.py       # Perron rigidity + exact curvature -4/3
python3 code/verify_intertwiners.py   # complete channel-exhaustion enumeration
python3 code/verify_r3prime.py        # R3' content tables, Weingarten, annihilation
sha256sum -c MANIFEST.sha256          # artifact integrity
```

Requirements: Python 3 with `sympy`. The manuscript compiles with
`tectonic manuscript.tex` (standard LaTeX packages only).

## Reviewing

Please open a **GitHub Issue** for any technical comment or correction —
errors of any size are welcome. See `REVIEW_REQUEST.md` for the five
specific questions this release most wants answered.

## License

Text and documentation: CC0 1.0 ([LICENSE-CC0](LICENSE-CC0)).
Verification code: MIT ([LICENSE-MIT](LICENSE-MIT)).
No third-party figures or data are included; cited literature remains the
property of its authors (cited, not reproduced).
