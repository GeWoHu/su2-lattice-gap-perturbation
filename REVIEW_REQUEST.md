# Review Request — Questions for Mathematical Physicists

This is a fixed-volume preprint released for expert review. We are
specifically asking for criticism, not endorsement. Please open a GitHub
Issue for any finding, however small.

1. **Is the SU(2) recoupling and channel-exhaustion argument complete,
   particularly R3'?**
   Appendix F (`appendix-body.tex`, Lemma `lem:valence`, Proposition
   `prop:exhaust`) enumerates intermediate states via vertex singlet rules
   plus a complete finite enumeration. The formerly open standalone
   derivation (R3') is now supplied as **Appendix G** (Peter–Weyl external
   typing, four-channel overlap decomposition, crossed-channel
   annihilation), internally proved and model-reviewed but **not human
   peer reviewed**: please audit Appendix G directly — accept it, or find
   the counterexample the model reviewers missed.

2. **Are the degenerate perturbation and vacuum-mixing calculations
   correct?**
   Main text Section 3 and Appendix E: isolation of the `E = 3` cluster,
   the reduced-resolvent expansion, and the vacuum-subtraction/normalization
   treatment (the `+|P|/3` double-counting adjudication in
   `code/verify_identity.py`).

3. **Is the coefficient consistent with historical strong-coupling
   literature after normalization conversion?**
   Our dictionary is `mu = 2 g^-6` (Appendix D). After conversion the
   second-order term is `-(142/105) g^-10` with relative coefficient
   `284/315`. Does this match — or contradict — known strong-coupling
   expansions (Kogut–Susskind reviews, Creutz, Monte Carlo literature)?

4. **Is the `L >= 5` restriction sufficient?**
   The geometric trichotomy (Lemma `lem:exhaust2`) and winding exclusions
   are stated for `L >= 5`; the `L = 4` winding exception is separated
   explicitly. Is anything else hiding at small volume?

5. **Is this result mathematically substantive or primarily pedagogical?**
   Given the exactness of the verification but the fixed-volume scope and
   the unresolved novelty question (Kogut–Sinclair–Susskind, *Nucl. Phys.*
   **B114** (1976) 199–236), how should this be positioned?

## Ground rules for reviewers

- The novelty classification is **UNRESOLVED**; no originality is claimed.
- No continuum or uniform-in-volume claim is made or implied.
- The preparation-stage referee process was model-based (disclosed in
  `evidence/`); it is not human peer review.
- Every numeric claim has an exact-arithmetic script behind it
  (`code/`, `receipts/`).

## The single load-bearing item (updated 2026-11-09)
Everything conditional in this paper rests on **Assumption R3'** — the
channel-exhaustion selection rule stated before the main theorem, with the
claimed proof in Appendix G. Human auditors should attack Appendix G first:
the Peter–Weyl external typing, the four-channel decomposition
`(0,0)⊕(0,1)⊕(1,0)⊕(1,1)`, and the crossed-channel annihilation against the
diagonal `(j,j)` type. If Appendix G survives audit, Assumption R3' is
discharged and the main theorem becomes unconditional within the stated
fixed-volume scope. If it fails, the unconditional residue is precisely the
machine-checked truncated second-order expression with coefficient −71/105
over the Appendices A–B channels, plus the band-head and dictionary results.
