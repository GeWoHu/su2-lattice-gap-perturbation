# YM-04 exact-verification code

All scripts: Python 3 + SymPy, exact rational arithmetic only, no floats in
any assertion, no numerical fitting. Runtimes on this host: anchors ~2 min,
identity ~3 min, census ~1 min.

| script | verifies |
|---|---|
| `verify_anchors.py` | `\|ReTr U_p\|^2 = 1` (Weyl + Weingarten dual methods), `\langle p\|V\|\Omega\rangle = -1`, first-order block `= 0`, regeneration amplitudes, touching `c_0^2=1/4, c_1^2=3/4`, `v=-8/21`, YM-03.6 formula `24v+127/15 = -71/105` |
| `verify_identity.py` | builds the exact 12-regular touching adjacency `A` at `L=5` (`n=375`) over `\mathbb Q`; proves the operator identity `M_2 = (1/3+v)A + cI` entry-by-entry including the `J`-cancellation; `2\times2` vacuum-mixing consistency `\langle u|\tfrac13 J|u\rangle = |\mathcal P|/3`; `c_2 = -71/105` |
| `verify_recoupling.py` | `c_0^2, c_1^2` by 6j calculus and Weingarten integration, dual exact methods |
| `verify_adjacency.py` | touching-degree census (12) and `\lambda_{\max}(A)=12` at `k=0` |
| `verify_census.py` | `L=4` exceptional census: 192 plaquettes + 48 winding loops = 240; winding touching count 16 |

Provenance: extracted from the YM-03.6/03.7/03.8 campaign computations
(`../ym036`, `../ym037`, `../ym038`, preserved unchanged) and re-run
end-to-end at YM-04 launch; all checks pass. The manuscript and appendix do
not depend on these scripts for correctness -- they re-derive every step
analytically -- the scripts are the independent machine audit.
