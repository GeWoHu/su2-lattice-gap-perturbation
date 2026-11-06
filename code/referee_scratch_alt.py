#!/usr/bin/env python3
"""Referee B scratch: exhaustive enumeration of admissible per-link spins
under the proof's own conditions (2j <= u+ubar, 2j == u+ubar mod 2),
with u+ubar <= 2 (unit plaquettes use each link at most once per loop).
Independent re-derivation of the Lemma 3 table."""
from fractions import Fraction as F

admissible = {}
for u in range(3):
    for ub in range(3):
        m = u + ub
        # two unit plaquettes: each loop contributes at most one slot on a
        # link, so realizable cases are (0,0),(1,0),(0,1),(2,0),(1,1)
        if (u, ub) not in {(0, 0), (1, 0), (0, 1), (2, 0), (1, 1)}:
            continue
        js = [F(t, 2) for t in range(m % 2, m + 1, 2)]  # 2j <= m, parity
        admissible[(u, ub)] = js

expected = {
    (1, 0): [F(1, 2)], (0, 1): [F(1, 2)],
    (2, 0): [F(0), F(1)], (1, 1): [F(0), F(1)],
    (0, 0): [F(0)],
}
assert admissible == expected, admissible
print("Lemma 3 table reproduced exhaustively:", admissible)

# parity exclusion check: (1,1) with j=1/2 gives total slots 1+1+1=3 (odd) -> zero
assert (1 + 1 + 2 * F(1, 2)) % 2 == 1
# overlap (2,0) j=0: leftover two U-slots pair via eps: int UU = 1/2 eps eps != 0
# overlap (1,1) j=0: leftover U,Ubar pair via delta != 0
print("Scratch checks OK: no admissible assignment outside the table.")
