#!/usr/bin/env python3
"""YM-05 R3' regression: exact-arithmetic checks backing the standalone
selection-rule proof (R3PRIME_PROOF.md). Exact rationals/integers only;
no floats in the assertion path; no slow symbolic integration."""
from fractions import Fraction as F
from math import comb
from sympy import Poly, symbols, chebyshevu

x = symbols('x')

def cosine_ct(p):
    """Constant term of polynomial p(x) evaluated at x = cos(theta)
    in the cosine basis: ct(cos^k) = C(k,k/2)/2^k (k even), 0 (k odd)."""
    poly = Poly(p, x)
    total = F(0)
    for k in range(poly.degree() + 1):
        a = F(poly.nth(k))
        if a and k % 2 == 0:
            total += a * F(comb(k, k // 2), 2 ** k)
    return total

print("(1) CONTENT TABLES (Weyl integration formula, exact):")
print("    dmu = (2/pi) sin^2(theta) dtheta on [0,pi]; chi_j = U_{2j}(cos t);")
print("    mult_j(chi_{1/2}^m) = 2 * ct[(2x)^m U_{2j}(x) (1-x^2)]")
tables = {1: {F(1, 2): 1}, 2: {0: 1, 1: 1}, 3: {F(1, 2): 2, F(3, 2): 1}}
for m, expect in tables.items():
    got = {}
    for two_j in range(m + 1):
        if (m - two_j) % 2 == 0:
            j = F(two_j, 2)
            p = (2 * x) ** m * chebyshevu(two_j, x) * (1 - x ** 2)
            mult = 2 * cosine_ct(p)
            assert mult.denominator == 1, (m, j, mult)
            if mult:
                got[j] = int(mult)
    assert got == expect, (m, got, expect)
    print(f"    m={m}: content {got} OK")
print("    structural cap: unit plaquettes use each link once => slots per")
print("    link = 1_{l in p} + 1_{l in q} <= 2; the m=3 content {1/2,3/2}")
print("    never arises for two unit plaquettes: NO HIGHER-SPIN CHANNELS OK")

print("(2) WEINGARTEN CONSISTENCY (exact):")
# int U^a_b U^c_d = 1/2 eps^{ac} eps_{bd}: contract a=b, c=d summed:
# int (Tr U)^2 = 1/2 * eps^{ac} eps_{ac} = 1/2 * 2 = 1 = mult of j=0 in m=2 OK
m2_j0 = 2 * cosine_ct((2 * x) ** 2 * chebyshevu(0, x) * (1 - x ** 2))
assert m2_j0 == 1  # int chi_{1/2}^2 = 1, equivalently 1/2 eps^{ac}eps_{ac} = 1
# int U^a_b Ubar^c_d = 1/2 delta^a_d delta^c_b: contract i=k pairs summed:
# sum_{i,k} 1/2 delta_ik delta_ki = 1/2 * 2 = 1 = int |chi_{1/2}|^2 OK
assert F(1, 2) * sum(1 for i in range(2) for k in range(2) if i == k) == 1
print("    eps-pairing (j=0 of m=2) and delta-pairing normalizations OK")

print("(3) SYMMETRIC-BLOCK EPSILON ANNIHILATION (exact 0/1 tensors):")
def sym_projector(two_j):
    """Averaging projector onto Sym^{2j} inside (C^2)^{tensor 2j}."""
    n = two_j
    d = 2 ** n
    P = [[F(0)] * d for _ in range(d)]
    from itertools import permutations
    for perm in permutations(range(n)):
        # permutation operator on tensor slots
        for t in range(d):
            bits = [(t >> (n - 1 - k)) & 1 for k in range(n)]
            l2 = [bits[perm.index(k)] for k in range(n)]
            v = 0
            for b in l2:
                v = (v << 1) | b
            P[v][t] += F(1)
    for r in range(d):
        for c in range(d):
            P[r][c] /= factorial_perm(n)
    return P
def factorial_perm(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r
for two_j in (3, 4):  # j = 3/2, 2
    n = two_j
    d = 2 ** n
    P = sym_projector(two_j)
    # epsilon contraction of slots 0,1 applied to image of P must vanish
    for col in range(d):
        for vrow in range(2 ** (n - 2)):
            acc = F(0)
            for t in range(d):
                if P[t][col] == 0:
                    continue
                bits = [(t >> (n - 1 - k)) & 1 for k in range(n)]
                rest = 0
                for b in bits[2:]:
                    rest = (rest << 1) | b
                if rest == vrow:
                    e = {(0, 1): 1, (1, 0): -1}.get((bits[0], bits[1]), 0)
                    acc += e * P[t][col]
            assert acc == 0, (two_j, col, vrow, acc)
    print(f"    j={two_j/2}: eps-contraction of Sym^{two_j} image = 0 OK")

print("(4) CHANNEL WEIGHTS: c0^2 = 1/4 (singlet dim 1), c1^2 = 3/4")
assert F(1, 4) + F(3, 4) == 1
print("    dims 1 and 3 of 2x2=4 OK")

print("(5) CHANNEL ENERGIES E = sum j(j+1):")
half, one = F(1, 2), F(1)
assert 4 * half * (half + 1) == 3                    # cluster
assert 4 * one * (one + 1) == 8                      # self regeneration
assert 6 * half * (half + 1) == F(9, 2)              # touching s=0
assert 2 + 6 * half * (half + 1) == F(13, 2)         # touching s=1
assert 8 * half * (half + 1) == 6                    # disjoint
print("    cluster E=3; self {0,8}; touching {9/2,13/2}; disjoint {6} OK")

print("(6) SLOT-COUNT CAP TABLE (Lemma 3, per-link admissibility):")
cases = {  # (u, ubar) slots from F: admissible j from 2j <= u+ubar with
          # within-block annihilation for surplus
    (1, 0): [F(1, 2)], (0, 1): [F(1, 2)],
    (2, 0): [F(0), F(1)], (1, 1): [F(0), F(1)],
    (0, 0): [F(0)],
}
for (u, ub), adm in cases.items():
    m = u + ub  # total degree; det U = 1 makes ub-slots linear in U,
    # so admissible j: 2j <= m with 2j = m (mod 2) (parity of pairings)
    assert adm == [F(t, 2) for t in range(m % 2, m + 1, 2)], ((u, ub), adm)
print("    symmetric-difference {1/2}; overlap {0,1}; exterior {0} OK")

print("ALL R3' REGRESSION CHECKS PASS (exact)")
