# PRIMARY SOURCE LEDGER — YM-04.5 Historical Hunt
## Theorem Under Trial
SU(2) Kogut-Susskind Hamiltonian LGT on T³_L, dimensionless H(μ) = Σ_links C₂(l) + μ Σ_p (2 - ReTr U_p), C₂ = electric Casimir with eigenvalue j(j+1), ReTr = UNNORMALIZED fundamental trace, product Haar probability measure, gauge-invariant L², L≥5, fixed volume: spectral gap Δ(μ,L) = 3 - (71/105) μ² + O(μ³), μ→0+, band head at k=0 uniform one-plaquette mode, coefficient L-independent; L=4 has 48 extra winding-loop E=3 states.

Dictionary to standard KS: H_KS = (g²/2)Σ E² - (1/2g⁴)Σ_p(Tr U_p + h.c.), energies in units g²/2, μ = 2g⁻⁶.

## Target Coefficient
Canonical published-form targets (all exactly equivalent, see NORMALIZATION_CROSSWALK.md):
- T1 dimensionless: c₂ = -71/105.
- T2 physical: Δ_phys = (3/2)g² - (142/105)g⁻¹⁰.
- T3 relative: Δ_phys = (3/2)g²·(1 - (284/315)g⁻¹²).
A source counts as prior art ONLY if its operator, object (3+1d one-glueball gap at k=0), and dimension match after conversion.

## Source Examination Log

---
### SOURCE 1: Kogut–Sinclair–Susskind, Nucl. Phys. B114 (1976) 199 — "A Quantitative Approach to Low-Energy Quantum Chromodynamics" (INSPIRE record 3785, texkey Kogut:1976zr)
**Status**: ACCESS-INCOMPLETE (kill-condition source; adjudication deferred, NOT resolved to KNOWN)
**Access Method**: INSPIRE API metadata (title/journal confirmed); ScienceDirect article page via Tavily extract (captcha wall); r.jina.ai proxy (captcha "Are you a robot?"); Wayback Machine API for both DOI and PII URLs → NO archived snapshots; libgen.gl search → 0 rows; Anna's Archive → connection failure; INSPIRE documents list → empty (no PDF on record).
**Full Text Obtained**: NO
**Obstacles**: Elsevier paywall + captcha bot wall; zero web-archive coverage of the article URL; no open repository copy.
**Formulas Found**: None directly. Object match confirmed from bibliographic record: this paper's object IS the 3+1d one-plaquette glueball in analytic strong-coupling expansion (the closest known object-match to our theorem in the literature).
**Converted Coefficient**: not determinable without text.
**Match/No-Match**: UNKNOWN — kill condition armed: if their printed second-order gap converts to T2 = -(142/105)g⁻¹⁰, classification flips to KNOWN.
**Page/Equation References**: pp. 199–236 (full article); specific equation not verifiable from abstract-level access.

---
### SOURCE 2: Kogut–Susskind, Phys. Rev. D 11 (1975) 395 — Hamiltonian formulation
**Status**: ACCESS-INCOMPLETE
**Access Method**: INSPIRE metadata; APS page paywalled; no open PDF found; no Wayback snapshot for the DOI landing.
**Full Text Obtained**: NO
**Obstacles**: APS paywall; preprint (FERMILAB-PUB series) not located in open repositories during window.
**Formulas Found**: Foundational operator definition only (the H we freeze is theirs).
**Converted Coefficient**: n/a
**Match/No-Match**: Defines the model; second-order gap formula not extractable.
**Page/Equation References**: PRD 11 395 (1975).

---
### SOURCE 3: Kogut, Rev. Mod. Phys. 51 (1979) 659 — review
**Status**: ACCESS-INCOMPLETE
**Access Method**: Wayback availability API → no snapshot; APS paywall.
**Full Text Obtained**: NO
**Obstacles**: paywall, no archive.
**Formulas Found**: None verifiable.
**Converted Coefficient**: n/a
**Match/No-Match**: UNKNOWN.
**Page/Equation References**: RMP 51 659 (1979).

---
### SOURCE 4: Creutz, "Quarks, Gluons and Lattices" (1983) — Hamiltonian strong-coupling chapter
**Status**: EXAMINED (full text)
**Access Method**: Full PDF obtained locally (creutz_quarks_gluons_lattices.pdf, 11.9 MB), converted to text (creutz_qgl.txt, ~11k lines), keyword-scanned: glueball, strong coupling, Hamiltonian, flux, perturbation, plaquette excitation, 71/105.
**Full Text Obtained**: YES
**Obstacles**: OCR noise (some glyphs corrupted); no formula index.
**Formulas Found**: Hamiltonian formulation and Gauss-law counting (pp. ~106–107 of the printed text): "When g_H is large, the electric term dominates… The potential or magnetic term in the Hamiltonian then acts as a perturbation which excites links into intermediate states involving higher representations. The first correction involves the excitation of the links around a single plaquette into the fundamental representation. For further details we refer the reader to the review by Kogut (1979)."
**Converted Coefficient**: No numeric second-order glueball coefficient printed in the examined passages; the book delegates details to Kogut (1979).
**Match/No-Match**: NO MATCH (method-level match only). Creutz describes exactly our expansion scheme but publishes no coefficient that could equal -71/105.
**Page/Equation References**: Hamiltonian-approach section, ch. 5 area, pp. 106–107 as printed; zero hits for "71/105" in full-text scan.

---
### SOURCE 5: Creutz, "From Bosons to Glueballs" (2023, World Scientific)
**Status**: ACCESS-INCOMPLETE
**Access Method**: arXiv API title search → no entry (book, not preprinted).
**Full Text Obtained**: NO
**Obstacles**: commercial book; no open edition.
**Formulas Found**: none.
**Converted Coefficient**: n/a
**Match/No-Match**: UNKNOWN.
**Page/Equation References**: n/a

---
### SOURCE 6: Montvay–Münster, "Quantum Fields on a Lattice" (Cambridge, 1994)
**Status**: ACCESS-INCOMPLETE
**Access Method**: Internet Archive catalog search → item `quantumfieldsonl0000istv` exists but is loan-restricted (no full-text search hit returned via petabox scrape during window).
**Full Text Obtained**: NO
**Obstacles**: controlled digital lending.
**Formulas Found**: none verifiable.
**Converted Coefficient**: n/a
**Match/No-Match**: UNKNOWN.
**Page/Equation References**: n/a

---
### SOURCE 7: Rothe, "Lattice Gauge Theories: An Introduction" 2nd ed.
**Status**: ACCESS-INCOMPLETE
**Access Method**: Internet Archive advancedsearch → no matching item (only an unrelated arXiv record returned).
**Full Text Obtained**: NO
**Obstacles**: no open copy.
**Formulas Found**: none.
**Converted Coefficient**: n/a
**Match/No-Match**: UNKNOWN.
**Page/Equation References**: n/a

---
### SOURCE 8: Drouffe–Zuber, Phys. Rep. 102 (1983) 1
**Status**: ACCESS-INCOMPLETE
**Access Method**: paywalled Elsevier; no archive snapshot.
**Full Text Obtained**: NO
**Obstacles**: paywall.
**Formulas Found**: none.
**Converted Coefficient**: n/a
**Match/No-Match**: UNKNOWN.
**Page/Equation References**: n/a

---
### SOURCE 9: Morningstar notes (ym04/ledger/sc_morningstar.txt) — 2+1d static potential
**Status**: EXAMINED (full text, prior campaign)
**Access Method**: archived lecture notes from YM-04 novelty audit.
**Full Text Obtained**: YES
**Obstacles**: none.
**Formulas Found**: x = 4/g⁴; E_m = 4C_F = 3; vacuum E_vac = -x²N_plaq/3 (their Eq. 36); channel classes (a) -1/3, (b) -1/6, (c) -3/14.
**Converted Coefficient**: channel values match ours class-by-class; their object is the 2+1d static q-q̄ line energy.
**Match/No-Match**: CHANNEL-LEVEL MATCH, OBJECT MISMATCH. 2+1d multiplicities give -131/105, not -71/105 (exact derived analogue). Not prior art against the 3+1d value.
**Page/Equation References**: Eq. (36) and channel discussion.

---
### SOURCE 10: Morningstar–Creutz 2+1d glueball papers; Morningstar PRD 1990s
**Status**: EXAMINED (prior campaign, Euclidean Monte Carlo)
**Access Method**: YM-04 novelty audit evidence.
**Full Text Obtained**: partial (abstracts + methods).
**Obstacles**: numerical papers, no analytic coefficient tables.
**Formulas Found**: Euclidean mass fits in β, not μ-expansion coefficients.
**Converted Coefficient**: not comparable without re-expansion; raw comparison forbidden (different expansion variable).
**Match/No-Match**: NO MATCH (method and object differ).
**Page/Equation References**: n/a

---
### SOURCE 11: Post-2020 quantum-simulation / coupled-cluster / Schrieffer–Wolff works
**Status**: EXAMINED (search sweep)
**Access Method**: arXiv API sweeps: glueball+strong-coupling+Hamiltonian (2 hits), coupled-cluster+Hamiltonian LGT, quant-ph+strong-coupling glueball (0 hits), citations sweeps.
**Full Text Obtained**: abstract-level for all; full text for hep-lat/9805011 (Schütte–Weihong–Hamer coupled cluster, 2+1d SU(2)).
**Obstacles**: none; the modern literature is 2+1d or Euclidean.
**Formulas Found**: hep-lat/9805011 uses the Kogut–Susskind Hamiltonian H = (1/2a)(Σg²E² - (2/g²)V) in 2+1d, coupled-cluster to 6th order, compares to 18th/28th-order strong-coupling series (Hamer–Oitmaa–Zheng, PRD 45 (1992) 4652). Pavel (hep-lat/0912.5465, 1611.06542) uses a derivative expansion in λ = g^{-2/3} — different expansion variable entirely.
**Converted Coefficient**: 2+1d series coefficients are dimension-incompatible with the 3+1d target (multiplicity argument, Crosswalk §2d).
**Match/No-Match**: NO MATCH. No post-2020 work reproduces a 3+1d one-glueball gap coefficient in μ = 2g⁻⁶ form.
**Page/Equation References**: hep-lat/9805011 §2 (their H definition); refs [1]–[9] scanned.

---
### SOURCE 12: INSPIRE citation graph around B114 (records 3785, 199845)
**Status**: EXAMINED
**Access Method**: INSPIRE API citations.recid:3785.
**Full Text Obtained**: metadata only.
**Obstacles**: INSPIRE citation coverage for 1970s nuclear-phys records is sparse: citations.recid:3785 returned total 0 (known incomplete graph — NOT evidence of no citations).
**Formulas Found**: none.
**Converted Coefficient**: n/a
**Match/No-Match**: inconclusive by construction.
**Page/Equation References**: record 199845 = Decker–Sinclair, "Strong Coupling Expansion for the Mass Gap in SU(2) Lattice Gauge Theory with Mixed Action" (1984) — object is the Euclidean mixed-action mass gap, not the Hamiltonian glueball band head.

---
### SOURCE 13: Google Books / Internet Archive textbook snippet search
**Status**: ACCESS-INCOMPLETE
**Access Method**: Google Books API v1 queries for "71/105" glueball, "142/105" lattice, glueball+second-order+strong-coupling.
**Full Text Obtained**: NO (API returned totalItems=None — snippet search unavailable for these queries from this host).
**Obstacles**: Google Books API snippet coverage; no preview search fallback available in window.
**Formulas Found**: none.
**Converted Coefficient**: n/a
**Match/No-Match**: UNKNOWN.
**Page/Equation References**: n/a

---

## EQUIVALENCE FINDINGS
1. One full-text source (Creutz 1983) describes our exact expansion scheme and publishes NO second-order coefficient — method prior art, not result prior art.
2. One full-text source (Morningstar notes) matches our recoupling channel VALUES exactly but in 2+1d and for a different object; exact 2+1d analogue coefficient is -131/105 ≠ -71/105.
3. The unique object-match candidate in the literature is KSS76 (B114 199): 3+1d analytic strong-coupling glueball, second order. Its full text is paywalled with zero archived copies → ACCESS-INCOMPLETE. Kill condition remains armed; absence of access is NOT evidence of novelty.
4. No examined source prints T1/T2/T3. No source prints "71/105" in any scanned full text.
5. The method (degenerate quantum-mechanical perturbation theory on the KS Hamiltonian, strong-coupling basis) is textbook-standard; the specific assembled coefficient for the 3+1d gap at second order, with the L≥5 band-head statement, was not found published in any full text obtained.

## FINAL VERDICT (historical hunt)
NOVELTY UNRESOLVED, leaning INCREMENTAL.
- Correctness of the coefficient is independently machine-anchored; the historical question cannot be closed to KNOWN or NOVELTY SUPPORTED because the single object-matched primary source (KSS76) is ACCESS-INCOMPLETE after five distinct access routes.
- Probability judgment (explicit): a competent 1976 practitioner COULD have derived the same number; whether KSS76 printed it is unknown. Classifying as KNOWN would overclaim; classifying as NOVELTY SUPPORTED would overclaim in the other direction.
- The presentation package (exact rational bookkeeping, L≥5 band-head theorem, L=4 winding-sector exception) is more rigorous than typical for the genre and is the defensible contribution if the coefficient itself turns out to be printed somewhere in the 1975–1983 literature.

---

## ADDENDUM — Independent rerun on NVIDIA NIM MiniMax M3.1 Flash (2026-11-05 11:00 CST)
Provider note: first attempt (run 983238dc) died on a provider 429 with zero output; retry (run 61d46061) completed the work and wrote ledger/HUNT_RERUN_MINIMAX.md but its completion delivery failed (empty result). Work product verified on disk; findings merged here.

New access routes attempted by the rerun (beyond the parent's five): CERN Document Server (web + API), NASA ADS record 1976NuPh..B114..199K, OSTI.gov discovery + PDF download (OSTI record 1968748 — downloaded, text-searched, NON-QUALIFYING: the "71/105" occurrence there is bibliographic numbering, not a coefficient), Springer/JHEP-style routes, SciSpace PDF route (bot page), Internet Archive search-inside (401/403 controlled lending), Google Books snippet/API.

Rerun conclusion (independent of the parent's): **HUNT-CLASS: NOVELTY UNRESOLVED**. KSS76 remains ACCESS-INCOMPLETE after eleven distinct routes in total; no qualifying full text prints T1/T2/T3; the rerun explicitly refuses both KNOWN and NOVELTY SUPPORTED, consistent with the parent ledger.
