# Independent Referee Report (B) — YM-05, Lemma R3' (second review)

Date: 2026-11-05. Target: `projects/math-research/ym05/R3PRIME_PROOF.md`.
Read-only inputs: `R3PRIME_PROOF.md`, `ym046/appendix-body.tex`,
`ym05/code/verify_r3prime.py`, `ym05/receipts/verify_r3prime.txt`.
Rerun: `verify_r3prime.py` passes (exact); scratch:
`code/referee_scratch_alt.py` reproduces the Lemma 3 table exhaustively.

## Objections

1. (non-blocking) Lemma 1 slot counts and orientation — VERIFIED, no objection.
   `χ(U_C)=Tr` uses each loop link exactly once; reversed traversal gives one
   `Ū`-slot via `U^{-1}=εŪε^{-1}` (valid on SU(2), det = 1). The `ψ̄_n` block
   carries `2j` `Ū`-slots in `Sym^{2j} ⊂ (V_{1/2})^{⊗2j}` — correct, since
   `D^{(j)} = Sym^{2j}` is homogeneous of degree `2j` and symmetric.

2. (non-blocking) Lemma 2 Weingarten factorization — VERIFIED, no objection.
   Product Haar measure factors link-wise. On SU(2) (V self-dual) the
   invariant pairings are δ for mixed U/Ū pairs and ε for same-type pairs;
   a pairing between two slots of the symmetric `ψ_n` block is necessarily
   ε-type and vanishes (`ε^{ac}S_{ac}=0`, lem:sym2, confirmed exactly for
   j=3/2, 2 in the rerun script). Hence all `2j` slots of `ψ_n` must pair to
   F-slots; surplus F-slots (≤ 2) pair among themselves legally. Sound.

3. (non-blocking) Lemma 3 admissibility table — VERIFIED exhaustive.
   Conditions `2j ≤ u+ū` and `2j ≡ u+ū (mod 2)` applied to the only realizable
   slot counts `(0,0),(1,0),(0,1),(2,0),(1,1)` (each unit plaquette uses a
   link at most once) yield exactly `{(1,0),(0,1): 1/2; (2,0),(1,1): 0,1;
   (0,0): 0}`. Independent scratch enumeration confirms no assignment outside
   the table. Self-energy p=q is the (2,0)/(1,1) overlap case — covered.
   Selection is per-link, hence L-independent; no periodic small-L exception.

4. (non-blocking) Theorem content — VERIFIED. Energies {0,8}, {9/2,13/2}, {6}
   and weights 1/4, 3/4 (dims 1,3 of 2×2=4) re-derived exactly in the rerun;
   `½⊗½ = 0⊕1` is multiplicity-free, so multiplicity one holds at link
   level (vertex valence rules are outside this link-level claim and are
   separately machine-checked per the proof).

5. (non-blocking) §2 "three slots (odd)" correction — VERIFIED correct.
   appendix-body.tex (lem:exhaust1 proof, ~line 280) indeed reads "two
   fundamental slots around the closed spin-1 chain of p and one ... of q
   ... three slots (odd)". Under the frozen convention `|p⟩ = χ_{1/2}(U_p)`
   a character contributes ONE slot per link, so the overlap carries two
   slots and the corrected count is right; the lemma statement (overlap
   {0,1}) is consistent with the correction. Residual note: the appendix
   proof text writes `χ₁(p)`, which conflicts with the frozen `χ_{1/2}`
   convention — a cosmetic inconsistency in the old derivation sentence,
   not in the proved statement.

6. (non-blocking) Completeness — no gap found. Brute-force checks are backed
   by the pairing argument, not substituted for it; hypotheses unweakened.
   No admissible intermediate assignment outside the table exists.

## Verdict

APPROVED
