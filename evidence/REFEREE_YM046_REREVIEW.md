# YM-04.6 re-review

## REPAIR-3 — ACCEPTED-WITH-NITS

The repair now supplies the missing local representation-theoretic criterion and a complete finite enumeration.  `verify_intertwiners.py` executes the 16 self assignments and retains exactly all-0 and all-1; the touching case has exactly the two shared-link spins 0 and 1, each with multiplicity one and energies 9/2 and 13/2; the disjoint case has the unique all-1/2 assignment, energy 6.  The stated denominators and weighted touching sum -8/21 are exact and the receipt reproduces the passing assertions.  The two-valent and three-valent Clebsch–Gordan rules justify the multiplicity claim for these support graphs.  The geometric trichotomy is sound for the declared plaquette set and L>=5 (the L=4 winding exception is explicitly separated).  Nit: the proof delegates the finite enumeration to code rather than displaying all vertex tests, but it specifies the finite domains and rules sufficiently for an external reviewer to reproduce it.

## DEFECTS 1–4 — CURED

1. The Appendix E rigidity argument now states the needed off-diagonal equality conditions and correctly uses the half-angle signs on `[-pi,pi)`; the cross-reference is repaired.
2. The Appendix D convention statement is now explicit: a `g^{-4}` symbol belongs to a rescaled Hamiltonian and cannot be substituted into the original dictionary alone.
3. The spectral-separation paragraph in the main proof now gives the vertex-rule/bipartite argument, excludes odd loops, and identifies the next relevant level as 9/2 (with the theta lower bound). This cures the earlier unsupported separation assertion, subject to the usual external check of the finite graph classification.
4. Section 9 states NOVELTY UNRESOLVED, records the exact equivalence test and converted expression, and expressly makes no originality claim. The supplementary documents are described as static checksummed material and the scope/novelty statements are reproduced in the paper.

## NEW DEFECTS

1. **Vacuum-channel scope contradiction (Appendix F, lines 256–258 and Proposition `prop:exhaust`, lines 319–365).** The section defines M2 with R0 on `\mathcal M\ominus` vacuum directions, and says every claim is about that reduced operator. The proposition nevertheless says its intermediate states are exhausted by four channels and includes “(i) the vacuum intermediate,” then counts it in the self enumeration and proof. This is mathematically harmless only if the proposition is explicitly broadened to the unreduced second-order matrix before the vacuum subtraction, or else the vacuum item is removed from the proposition and treated separately in the subsequent normalization calculation. As written, the object being exhausted and the listed set are inconsistent.

2. **Local wording ambiguity (Appendix F, Lemma `lem:exhaust1`, lines 260–283).** The displayed bidegree discussion uses `p_n,q_n` after introducing n as an eigenstate and p,q as plaquettes, without defining these as linkwise U/bar-U counts. The intended parity conclusion is supported by the subsequent finite check, but the notation should be repaired for self-contained human review.

## OVERCLAIM CHECK

The manuscript continues to state fixed-volume perturbation theory only, allows `\mu_0(L)` and `O_L(\mu^3)`, and explicitly disclaims volume-uniform and continuum conclusions. Section 9 says NOVELTY UNRESOLVED, records the conversion/equivalence test, and says no originality is claimed. The updated PDF is present, and the exact intertwiner checker passes. Subject to correcting the vacuum-channel scope contradiction (and preferably the bidegree notation), the package is suitable for external human review.

YM-04.6-VERDICT: REVISION REQUIRED
