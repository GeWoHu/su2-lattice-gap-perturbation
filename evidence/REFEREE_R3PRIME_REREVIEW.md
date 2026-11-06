# YM-05 R3' Rebuttal Re-review

Date: 2026-11-05. Inputs: `R3PRIME_PROOF.md` (revised, §§3A–3B), `evidence/REFEREE_R3PRIME.md` (original REJECT), `evidence/REFEREE_R3PRIME_ADJUDICATION.md`, and frozen `ym046/appendix-body.tex` (Lemma `lem:sym2`, `lem:valence`, Appendix B weights).

Method: hostile, function-level Peter–Weyl re-derivation; no credit for rhetoric.

## Objection 1 — Link model: V_j ⊗ V_j* endpoint structure and slot count

**RESOLVED (with one wording correction).**

Under the frozen convention (gauge-invariant spin-network states with vertex singlets), a link of flux j contributes the matrix coefficient D^j(U) of ρ_j = Sym^{2j}; its row and column indices are the two endpoint tensors V_j* and V_j. The space of functions of one link variable with fixed endpoint spins is V_j* ⊗ V_j, and the state ψ_n lies in the coefficient space of the *external* tensor product ⊗_ℓ(ρ_{j_ℓ} ⊠ ρ_{j_ℓ}*), i.e. a vector (not literally "a matrix coefficient") in the coefficient space of the external representation. Vertex intertwiners are the contractions that make this object gauge invariant. So the author's §3A statement is representation-theoretically sound, and the original objection — that a bare symmetric block ignores the endpoint block and its incidence — no longer applies: the incidence is carried by the coefficient's row/column index pair and by the fixed vertex intertwiners.

Bidegree bookkeeping is also correct: in ⟨ψ_n, F⟩ = ∫ overline{ψ_n} F, overline{ψ_n} contributes 2j ℧-slots (one degree-2j symmetric block) on link ℓ, while F contributes u U-slots and ū Ū-slots. Thus the (1,0)/(0,1), (2,0)/(1,1), (0,0) slot counts in Lemma 1 are the correct bidegrees; the revision correctly abandons the endpoint-incidence bookkeeping instead of trying to patch it.

Correction (non-blocking): ψ_n is a vector in the coefficient space, possibly in a multiplicity space; "is a matrix coefficient" should be read as "is supported in the coefficient space of that external representation", which is all the orthogonality argument needs.

## Objection 2 — Orientation reversal and ε-closures

**RESOLVED (with a required rephrasing of A2).**

At the function level the orientation issue genuinely disappears, and the author's key identity is correct for the frozen group: on SU(2), Tr U^{-1} = Tr U (eigenvalues e^{±iθ}), hence χ(U_C) = χ(U_C^{-1}) for any closed loop C, so the *value* of a plaquette character does not depend on the choice of orientation of that plaquette. Consequently the two overlap readings ("both traversals alike" and "opposite") give literally the same integrand, and the ε-closures inserted by U^{-1} = εŪε^{-1} are already encoded in the equality of the two functions. No incidence-level analysis is required for this obstruction.

Required rephrasing (non-blocking, but the current sentence is literally false): cyclicity of trace does not permit reversing "one link" inside a trace; an oriented closed loop has a single global orientation, so the operation that is available is reversal of the *whole* loop, and the valid statement is Tr(U_C^{-1}) = Tr(U_C) for SU(2) (which is an SU(2)-specific identity, not a general trace-cyclicity statement). With that rephrasing, the argument stands.

## Objection 3 — Necessity, exhaustivity over legal endpoint contractions, and realizability

**Realizability: RESOLVED.** Appendix B gives the explicit F-move amplitudes c_0 = 1/2, c_1 = √3/2 (squared 1/4, 3/4), both nonzero; `lem:valence` gives multiplicity-one vertex intertwiners for the two touching assignments (s, 1/2, 1/2), s = 0,1; the self and disjoint assignments are the standard singlet/triplet networks with unique invariants; `verify_intertwiners.py` checks the finite assignment enumeration. The frozen Appendix B weights are exactly as cited, and the frozen energy arithmetic (0, 8, 9/2, 13/2, 6) is unaffected. The requirement that every listed channel be *constructed* is met, not merely asserted.

**Necessity/exhaustivity: UNRESOLVED as written.** The substantive gap is not rhetorical: §3A's linkwise "Schur–Weyl" step is stated in a type-inconsistent way, and the inference drawn from it is not valid without additional analysis that is absent from the revision.

1. In the product-group Peter–Weyl basis (the one appropriate to Haar measure ∏ dU_ℓ), a matrix coefficient D^{1/2} is of external type (1/2,1/2), and D^j is of type (j,j). The draft instead uses the *diagonal* (conjugation) decomposition V ⊗ V = ρ_1 ⊕ ρ_0, which is a different action and is not orthogonal for the product Haar measure. These two typings must not be mixed.

2. Consequently, the content of two matrix entries on the same link is NOT "V ⊗ V = ρ_1 ⊕ ρ_0" with two channels. In external typing,
   (V*⊗V) ⊗ (V*⊗V) = (ρ_1⊠ρ_1) ⊕ (ρ_1⊠ρ_0) ⊕ (ρ_0⊠ρ_1) ⊕ (ρ_0⊠ρ_0),
   i.e. four channels, because the row pair and the column pair are CG-decomposed independently. The draft lists only the two diagonal types (k,k), k = 0,1. The two crossed types (1,0) and (0,1) are omitted — and they are exactly the "other endpoint-incidence patterns" that Objection 3 demanded be enumerated and excluded, not merely ignored.

3. The draft's key inference — "Peter–Weyl orthogonality forces j_ℓ = k_ℓ link by link" — therefore does not follow from what is written. As stated, F is not a sum of coefficients of ⊗_ℓ ρ_{k_ℓ} with k_ℓ ∈ {0,1} on the overlap, so the claimed link-by-link forcing is unsupported.

The gap is repairable, and the repair does not change the table, but it must be supplied (the minimal repair is stated below). In external typing, ψ_n has type (j_ℓ,j_ℓ) on every link, so the crossed overlap channels (1,0),(0,1) can never match it; the diagonal channels match only j_ℓ = 1 (type (1,1)) and j_ℓ = 0 (type (0,0)). On a symmetric-difference link F has type (1/2,1/2) and ψ_n type (j,j), forcing j = 1/2; on an exterior link F is type (0,0), forcing j = 0. This yields exactly the frozen table, and the (0,0) channel is genuinely nonzero (the antisymmetric row/column contraction is a constant, whereas the (1,1) channel carries the spin-1 content), consistent with c_0² = 1/4. Thus the conclusion is very likely correct, but the revision as submitted does not contain the argument that establishes it.

(Also noted: the draft's phrase that a one-entry link "carries one U-entry = coefficient of ρ_{1/2}" and that an exterior link "contributes ρ_0" are shorthand for the external types (1/2,1/2) and (0,0); the corrected typing must be stated explicitly in the same paragraph as the orthogonality inference, otherwise the inference is again unlicensed.)

## Residual gaps and frozen-statement check

- Frozen statement (§1): if ⟨n|V|p⟩ ≠ 0 then j_ℓ = 1/2 on supp(q) Δ supp(p), j_ℓ ∈ {0,1} on the overlap, j_ℓ = 0 outside, with the contents exhaustive and no higher-spin chain terms. The revision's corrected external typing reproduces exactly this table, and the vertex-level enumeration (self {0,1}; touching {s=0,1} with six 1/2; disjoint eight 1/2) with multiplicities one and the energies 0, 8, 9/2, 13/2, 6 is unchanged and independently checkable against `appendix-body.tex`.
- The original "three slots (odd)" sentence is correctly identified as a counting error under |p⟩ = χ_{1/2}(U_p) (one fundamental slot per traversed link); the correction to "two slots on the overlap" is right, and the present bidegree analysis is the missing justification for it.
- No finite-lattice exception was found: the reasoning is per-link and lattice-independent; the L ≥ 5 geometric trichotomy is untouched.
- Remaining defect (blocking as written, minimal fix): the linkwise decomposition of F in §3A must be restated in external (row,column) typing with all four overlap channels displayed, followed by the observation that ψ_n is of type (j,j) on every link, so only the diagonal channels can contribute. Until that is in the proof, the exhaustivity claim over legal endpoint-contraction patterns is not proved by §3A, and the original blocking Objection 3 survives in modified form. The remaining two blocking objections are genuinely resolved by §§3A–3B.

## Verdict

REJECTED
