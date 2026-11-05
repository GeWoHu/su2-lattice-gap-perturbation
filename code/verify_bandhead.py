#!/usr/bin/env python3
"""YM-04.6 band-head uniqueness verification (Appendix E). EXACT sympy only.
(1) A(0): lambda=12 simple, uniform eigenvector (eigenvals exact).
(2) Generic-direction EXACT curvature: first-order perturbation on the simple
    eigenpair gives the quadratic term u^T A2 u = -(4/3)(a^2+b^2+c^2), isotropic.
    Second-order perturbation is quadratic in Delta A = O(|k|^2), hence O(|k|^4):
    the quadratic term is exact.
(3) Independent cross-check per rational direction: characteristic-polynomial
    root series lambda(t) = 12 + c2 t^2 + c4 t^4 solved exactly; c2 must equal -4/3.
(4) Dense-grid audit: lambda_max < 12 strictly off origin (float, audit only).
"""
import sympy as sp, math
import numpy as np
t,a,b,c = sp.symbols('t a b c', real=True)
def Af(x,y,z):
    return sp.Matrix([
     [2*sp.cos(x)+2*sp.cos(y), 4*sp.cos(y/2)*sp.cos(z/2), 4*sp.cos(x/2)*sp.cos(z/2)],
     [4*sp.cos(y/2)*sp.cos(z/2), 2*sp.cos(x)+2*sp.cos(z), 4*sp.cos(x/2)*sp.cos(y/2)],
     [4*sp.cos(x/2)*sp.cos(z/2), 4*sp.cos(x/2)*sp.cos(y/2), 2*sp.cos(y)+2*sp.cos(z)]])
A0 = Af(0,0,0)
assert A0.eigenvals() == {12:1, 0:2}
u = sp.Matrix([1,1,1])/sp.sqrt(3)
assert (A0*u-12*u).norm() == 0
print("(1) lambda=12 SIMPLE at k=0, uniform eigenvector: OK")
A2 = sp.expand(sp.diff(Af(a*t,b*t,c*t),t,2).subs(t,0)/2)
q = sp.expand((u.T*A2*u)[0])
assert sp.simplify(q+sp.Rational(4,3)*(a**2+b**2+c**2)) == 0
print("(2) EXACT generic-direction curvature = -(4/3)|k|^2, isotropic: OK")
L = sp.Symbol('L')
for dd in [(1,0,0),(1,1,0),(1,1,1),(2,1,3),(1,2,0)]:
    nn = sp.sqrt(sum(x*x for x in dd)); dn = [sp.Rational(x)/nn for x in dd]
    p = sp.series((L*sp.eye(3)-Af(*[x*t for x in dn])).det(), t, 0, 5).removeO()
    L2,L4 = sp.symbols('L2 L4')
    ser = sp.series(p.subs(L, 12+L2*t**2+L4*t**4), t, 0, 5).removeO()
    sol = sp.solve([sp.Eq(ser.coeff(t,2),0), sp.Eq(ser.coeff(t,4),0)],[L2,L4], dict=True)[0]
    assert sp.simplify(sol[L2]+sp.Rational(4,3)) == 0, (dd, sol[L2])
    print(f"(3) charpoly root series dir {dd}: c2 = {sp.simplify(sol[L2])} = -4/3, c4 = {sp.simplify(sol[L4])}: OK")
def lmax(k):
    x,y,z = k
    M = np.array([[2*math.cos(x)+2*math.cos(y), 4*math.cos(y/2)*math.cos(z/2), 4*math.cos(x/2)*math.cos(z/2)],
                   [4*math.cos(y/2)*math.cos(z/2), 2*math.cos(x)+2*math.cos(z), 4*math.cos(x/2)*math.cos(y/2)],
                   [4*math.cos(x/2)*math.cos(z/2), 4*math.cos(x/2)*math.cos(y/2), 2*math.cos(y)+2*math.cos(z)]])
    return float(np.linalg.eigvalsh(M)[-1])
worst=-1.0; N=40
for i in range(-N,N+1):
    for j in range(-N,N+1):
        for m in range(-N,N+1):
            if i==j==m==0: continue
            worst = max(worst, lmax((math.pi*i/N, math.pi*j/N, math.pi*m/N)))
assert worst < 12.0
print(f"(4) dense grid audit max lambda_max off-origin = {worst:.9f} < 12 STRICT: OK")
print("ALL BAND-HEAD UNIQUENESS CHECKS PASS")
