# YM-04.6 — FINAL VERDICT

**YM-04.6-VERDICT: HUMAN-REVIEW READY**

Terminal referee round (hostile referee, an independent model-based referee
an independent hosted referee session), adjudication recorded in
`evidence/REFEREE_YM046_FINAL2.md`.

## Adjudication trail
| Round | File | Verdict |
|---|---|---|
| Initial | `evidence/REFEREE_YM046.md` | REVISION REQUIRED (Repair 3 rejected: Appendix F exhaustion not proven; 4 new defects) |
| Re-review | `evidence/REFEREE_YM046_REREVIEW.md` | REVISION REQUIRED (Repair 3 accepted-with-nits; defects 1–4 cured; 2 new defects) |
| Final | `evidence/REFEREE_YM046_FINAL.md` | REVISION REQUIRED (parity error in rewritten selection lemma) |
| Terminal | `evidence/REFEREE_YM046_FINAL2.md` | **HUMAN-REVIEW READY** |

## Repairs implemented (all machine-checked)
1. **Coupling repair.** Production dictionary \(\mu=2g^{-6}\);
   \(\Delta_{\rm phys}=\tfrac32 g^2-\tfrac{142}{105}g^{-10}+O(g^{-16})\); relative
   coefficient \(284/315\,g^{-12}\) (`receipts/conversions_exact.txt`).
2. **Band-head uniqueness.** Exact Perron–Frobenius rigidity (off-diagonal
   equality forces \(k=0\)); exact curvature
   \(\lambda_{\max}(A(k))=12-\tfrac43|k|^2+O(|k|^4)\) via characteristic-polynomial
   root series in five directions plus dense grid audit
   (`receipts/bandhead_curvature.txt`, `code/verify_bandhead.py`).
3. **Channel exhaustion (Repair 3).** New vertex singlet lemma (Clebsch–Gordan
   2-/3-valent rules) plus complete exact enumeration of all admissible spin
   assignments per pair geometry (`code/verify_intertwiners.py`,
   `receipts/intertwiner_exhaustion.txt`): self → all-0 (E=0, normalization only)
   and all-1 (E=8); touching → shared spin 0 (E=9/2) and 1 (E=13/2), multiplicity
   1 each, weighted \(\tfrac{1/4}{-3/2}+\tfrac{3/4}{-7/2}=-\tfrac{8}{21}\) exactly;
   disjoint → unique all-½, E=6, value −⅓. Vacuum-channel scope contradiction
   cured: enumeration stated for the unreduced second-order expression; channel (i)
   assigned to the normalization subtraction; channels (ii)–(iv) exhaust the
   reduced operator.
4. **Selection-lemma parity fix.** The false link-level parity inference is
   deleted; the \(\{0,1\}\) overlap restriction is attributed to the Appendix A–B
   recoupling analysis; the standalone exhaustive derivation is declared as open
   item **R3'** (not concealed as a proved lemma).
5. **Spectral separation** in the main proof now derived from vertex rules +
   bipartiteness (no odd loops, 2-valent constancy, theta graphs E≥7, next level
   9/2). Cross-references, Appendix D convention nit, and self-containedness
   (static checksummed supplementary documents) fixed.

## Mechanical self-check (META-01)
`receipts/META01_RECEIPT_YM046.json`: **mechanical_all_pass = True**
(9 artifact hashes, 6 exact-receipt marker checks, archive hash check 3/3,
terminal referee verdict check). Two earlier False receipts were generator bugs
(bool subscripted; dict aggregation; one expected hash transcribed …156a instead
of the fork-time record …156e in `receipts/ym04_source_hashes.txt`); the underlying
archive was always intact.

## Archive integrity
YM-04 sources verified unchanged against fork-time record:
- `ym04/manuscript.tex` c64ead89…287a OK
- `ym04/appendix.tex` ff89940f…ef15 OK
- `ym04/appendix-body.tex` 4d2b0344…156e OK

## Named open items carried into human review
1. **R3'**: standalone exhaustive derivation that the Appendix A–B recoupling
   channels are the only nonvanishing overlap contributions (currently backed by
   the exact full-space operator identity and the complete vertex enumeration).
2. **KSS76 novelty scan**: library-level comparison against
   Kogut–Sinclair–Susskind, Nucl. Phys. B114 (1976) 199
   (DOI 10.1016/0550-3213(76)90586-1). Classification remains **NOVELTY
   UNRESOLVED**; no originality is claimed.

## Scope discipline
Fixed-volume perturbation theory only (\(L\ge5\), \(\mu_0(L)\), \(O_L(\mu^3)\));
no uniform-in-volume claim, no continuum claim. No submission, no journal contact,
no further coefficient research initiated.

## Addendum (2026-11-09, external-review response — Path 1)
An external referee declined the Appendix G exhaustion argument as
human-review grade. Per owner decision (Path 1), the claim hierarchy was
corrected WITHOUT touching any computation: the main theorem is now stated
under an explicit **Assumption R3'** (channel-exhaustion selection rule,
stated before the main theorem in manuscript.tex); Appendix G carries a
status note; README reflects the conditional status. All unconditional
machine-checked content (coefficient identities, band-head curvature and
PF uniqueness, conversion dictionary) is unchanged and re-verified.
Path 2 (full standalone spin-network derivation removing the assumption)
remains an open research option, not undertaken.
