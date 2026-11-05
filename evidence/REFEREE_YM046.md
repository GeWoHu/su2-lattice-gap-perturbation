# Hostile referee report: YM-04.6

## REPAIR-1 — ACCEPTED-WITH-NITS

The algebra is exact: (g^2/2)(71/105)(2g^-6)^2=(142/105)g^-10, the relative coefficient is 284/315 g^-12, and the mu^3 remainder becomes O_L(g^-16). The abstract, Corollary 1.2, Section 2.2, and Appendix D agree. I found no residual claim that the present Hamiltonian has mu=g^-4; the alternative convention is explicitly qualified. Nit: the sentence in Appendix D about “dropping the g^2/2 prefactor” should identify the resulting Hamiltonian explicitly.

## REPAIR-2 — ACCEPTED-WITH-NITS

For the real-symmetric fibers displayed, lambda_max(B)<=rho(|B|) is valid, and |A(k)|<=A(0) is valid (the proof should say |2 cos k_i+2 cos k_j|<=4). The strict Perron comparison is valid against irreducible A(0). Off-diagonal equality gives |cos(k_i/2)|=1; on [-pi,pi) this forces every k_i=0. The sentence that diagonal equalities themselves force cos k_i=1 is false: absolute diagonal equality also permits both cosines to be -1, though the off-diagonal conditions repair the conclusion.

The curvature -4|k|^2/3 agrees with verify_bandhead.py and the receipt. The lattice discretization and fixed-L O_L(mu^3) argument are adequate. Nit: the proof's phrase “uniformly in k (Section 2.3)” points to a nonexistent subsection.

## REPAIR-3 — REJECTED

The geometric trichotomy is sound for L>=5: two distinct unit plaquettes cannot share two links, and winding identifications do not create a counterexample in this range. The center-parity observation and “three spin-1/2 legs have no singlet” are also correct (1/2 tensor 1/2 tensor 1/2 = 1/2 direct-sum 1/2 direct-sum 3/2).

However, Appendix F does not prove the advertised channel exhaustion. In lem:exhaust1 the local parity restriction only gives spin 0 or 1 on a doubly covered link and spin 1/2 on a singly covered link; it does not by itself classify the allowed vertex intertwiners. In prop:exhaust, the assertion that every mixed 0/1 fusion in the self case leaves an “unpaired intertwiner” is only a verbal local assertion and is not checked at all vertices. The touching-case assertion that shared spin 0 “forces each square's remaining chain to be the chi_1-type invariant” and is then killed by “vacuum exclusion” is not justified: reduced-resolvent exclusion is a statement about the intermediate eigenspace, not a demonstrated vanishing of every resulting product intertwiner. Likewise, the disjoint-case paragraph states the -1/3 value while simultaneously describing it as an E=3 regeneration handled by J; it does not enumerate or project all intertwiners. The cited sym2 lemma addresses a symmetric slot, not this full invariant-space classification. A complete tensor-product/intertwiner calculation (or explicit exact projector computation) is required.

## NEW DEFECTS

1. **Appendix E, lem:headE proof, equality sentence:** “diagonal equalities force cos k_x=cos k_y=cos k_z=1” is false for entrywise absolute equality; only the combined diagonal and off-diagonal conditions force the result.
2. **Appendix E, prop:headexact proof:** “uniformly in k (Section 2.3)” is an invalid internal cross-reference; there is no Section 2.3.
3. **Manuscript Section 3 proof of Theorem main:** the claim that gauge invariance forces equal fluxes around each closed loop and hence that the next flux level is 9/2 is not generally a valid characterization of arbitrary spin-network supports. The needed spectral separation should be proved from link-energy arithmetic plus vertex constraints.
4. **Self-containedness:** Section Scope cites the campaign model specification and literature ledger as accompanying archive materials. Thus the manuscript is not fully self-contained as requested; the scope/novelty claims need to be reproduced in the manuscript or supplied as ordinary supplementary documents with stable contents.

## OVERCLAIM CHECK

The fixed-volume qualification, absence of a continuum claim, and absence of a uniform-in-L claim are stated clearly. Section 9 says exactly NOVELTY UNRESOLVED, records the equivalence test, and says “No originality is claimed here”; no originality overclaim remains. The band-head claim is plausible after Repair 2, but the global coefficient and hence the main theorem still depend on the unproved Appendix-F exhaustion.

**Final assessment:** not suitable for external human review as a repaired theorem manuscript until Repair 3 is supplied and the small cross-reference/self-containedness defects are corrected.

YM-04.6-VERDICT: REVISION REQUIRED
