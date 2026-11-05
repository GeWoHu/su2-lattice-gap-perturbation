#!/usr/bin/env python3
"""YM-04.6 Repair-3: EXHAUSTIVE exact intertwiner enumeration for Appendix F.
Singlet multiplicities (exact integers, SU(2)):
  2-valent:  m(j1,j2) = 1 iff j1=j2.
  3-valent:  m(j1,j2,j3) = 1 iff triangle(|ji|) and j1+j2+j3 in Z.
Enumerate ALL spin assignments on each pair-geometry support with the
Peter--Weyl parity bounds of lem:exhaust1 (doubly covered link: 0 or 1;
singly covered: 1/2), and list every assignment whose invariant space
(product of vertex multiplicities) is nonzero, with its H_E energy.
"""
from fractions import Fraction as F
H = F(1,2)
def m2(j1,j2): return 1 if j1==j2 else 0
def m3(j1,j2,j3):
    tri = (j3 >= abs(j1-j2)) and (j3 <= j1+j2)
    return 1 if tri and ((j1+j2+j3) % 1 == 0) else 0
# --- self case q=p: 4-cycle, spins {0,1}; vertices pair consecutive links
adm=[]
for s in [(a,b,c,d) for a in (0,1) for b in (0,1) for c in (0,1) for d in (0,1)]:
    dim = m2(s[0],s[1])*m2(s[1],s[2])*m2(s[2],s[3])*m2(s[3],s[0])
    if dim:
        E = sum(x*(x+1) for x in s)
        adm.append((s,dim,E))
print("SELF (q=p): admissible intermediates:")
for s,dim,E in adm: print("  spins",s,"dim",dim,"E =",E)
assert adm == [((0,0,0,0),1,F(0)), ((1,1,1,1),1,F(8))], "mixed 0/1 self fusions must vanish"
# --- touching: shared e0 spin {0,1}; two 3-edge chains at 1/2.
# vertices: 4 two-valent along chains (1/2,1/2) OK; 2 three-valent (e0,1/2,1/2).
print("TOUCHING: admissible intermediates:")
res=[]
for s0 in (0,1):
    dim = m3(F(s0),H,H)**2   # both 3-valent endpoints
    E = s0*(s0+1) + 6*H*(H+1)
    if dim: res.append((s0,dim,E))
    print(f"  shared spin {s0}: dim {dim}, E = {E}, denominator 3-E = {3-E}")
assert res == [(0,1,F(9,2)), (1,1,F(13,2))], "exactly two touching intermediates"
# --- disjoint: two separate 4-cycles, all links singly covered => 1/2
dim = 1
E = 8*H*(H+1)
print(f"DISJOINT: unique intermediate: all 1/2, dim {dim}, E = {E}, denominator 3-E = {3-E}")
assert E == F(6)
# --- channel closure identity (exact): weights from Appendix B
v = F(-8,21)
lhs = (F(1,4)/(3-F(9,2)) + F(3,4)/(3-F(13,2)))
print("touching channel: (1/4)/(-3/2) + (3/4)/(-7/2) =", lhs, "= v = -8/21 OK:", lhs==v)
print("self regeneration: 1/(3-8) =", F(1,3-8), "= -1/5 OK")
print("disjoint: 1/(3-6) =", F(1,-3), "= -1/3 OK")
print("ALL INTERTWINER EXHAUSTION CHECKS PASS (exact integers, complete enumeration)")
