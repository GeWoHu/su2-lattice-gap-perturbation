# YM-05 — Adjudication of hostile referee objections (R3')

Date: 2026-11-05. Referee trail:
- `REFEREE_R3PRIME.md` (minimax-m3.1-flash): **REJECTED**, 3 blocking objections.
- `REFEREE_R3PRIME_ALT.md` (mistral-large-4-1t): **APPROVED**, no blocking objections,
  6 verification notes, independent scratch enumeration of the admissible
  `(u, ū)` cases (`code/referee_scratch_alt.py`).

Split verdict → mathematical adjudication (proof draft §3A/§3B, now in
`R3PRIME_PROOF.md`):

## A1 — "V_j ⊗ V_j* endpoint structure; single symmetric block is a faulty model"
Compatible descriptions, not competing ones. `overline{ψ_n}|_{link ℓ}` is a
homogeneous polynomial of degree `2j` in `Ū`-entries (conjugate matrix
coefficients of `ρ_j = Sym^{2j}`): one symmetric block in the Weingarten
sense. The `V_j ⊗ V_j*` language describes how its indices contract with
*fixed* vertex intertwiners — inputs, not summed over. Annihilation acts
inside the link integral before endpoint contraction: an `ε`-pair on two
symmetric-block slots is the zero tensor on symmetric inputs, so no
endpoint incidence can resurrect it. The Peter–Weyl formulation (§3A)
removes the modeling question entirely: `ψ_n` is a matrix coefficient of
`⊗_ℓ ρ_{j_ℓ}` of the compact group `G^L` by construction. **Resolved.**

## A2 — "orientation ε-closures discarded; (2,0)/(1,1) equivalence unproved"
At the FUNCTION level the distinction disappears: `χ_{1/2}(U^{-1}) = Tr U^{-1}
= Tr U` on SU(2) (eigenvalues `e^{±iθ}`), and by cyclicity of trace,
reversing one link's traversal in a closed loop leaves `χ(U_C)` unchanged.
So the `(1,1)` and `(2,0)` overlap readings are the SAME integrand; the
`(1,1)` slot decomposition is a bookkeeping gauge. In the Peter–Weyl
formulation, reversed-orientation slots are dual matrix coefficients of the
same irreps (`V* ≅ V` via `ε`), so `ε`-closures change incidence
bookkeeping but not which irreps occur. **Resolved.**

## A3 — "necessity only; no construction; table may not exhaust endpoint contractions"
Necessity: Peter–Weyl orthogonality on `G^L` (§3A). Exhaustivity: the
link-by-link decomposition of `F = χ_q χ_p` is COMPLETE and
multiplicity-free by Schur–Weyl (`V ⊗ V = ρ_1 ⊕ ρ_0`); there are no other
summands, hence no other channels — this is exactly the "no higher-spin
chain terms" content. Realizability: Appendix B explicitly computes both
surviving projectors (`c_0² = 1/4`, `c_1² = 3/4`, both nonzero);
`verify_r3prime.py` checks weights, energies, and content tables in exact
arithmetic; `verify_intertwiners.py` certifies multiplicity one.
Referee B independently enumerated realizable `(u,ū)` cases and confirmed
the table. **Resolved.**

## Residual
Referee B's cosmetic note (appendix proof text writes `χ₁(p)` where the
frozen convention is `χ_{1/2}`) is a pre-existing typesetting inconsistency
in Appendix A notation for the *closed chain*, to be harmonized in the
amendment wording; it does not affect any computation (the regression
anchors use `χ_{1/2}` throughout).

## Disposition
All three blocking objections have mathematical resolutions in §3A/§3B;
the revised draft is submitted for a rebuttal re-review (see
`REFEREE_R3PRIME_REREVIEW.md`).
