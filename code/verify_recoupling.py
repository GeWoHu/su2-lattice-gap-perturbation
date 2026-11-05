"""Exact YM-03.6 two-plaquette recoupling check."""
from sympy import S, sqrt, Rational, simplify
from sympy.physics.wigner import wigner_6j
h=S(1)/2; channels=(S(0),S(1)); d={s:2*s+1 for s in channels}
F={(s,t):simplify(sqrt(d[s]*d[t])*wigner_6j(h,h,s,h,h,t)) for s in channels for t in channels}
Fmat=[[F[s,t] for t in channels] for s in channels]
assert Fmat==[[-Rational(1,2),sqrt(3)/2],[sqrt(3)/2,Rational(1,2)]]
assert all(simplify(sum(F[s,t]*F[t,u] for t in channels)-(1 if s==u else 0))==0 for s in channels for u in channels)
# theta_s=d_s; four fundamental normalizations give 1/4
A2={s:simplify(d[s]/4) for s in channels}
# Haar 2x2 Weingarten values and epsilon/CG projector trace
Wg_id,Wg_swap=Rational(1,3),-Rational(1,6)
assert (Wg_id,Wg_swap)==(Rational(1,3),-Rational(1,6))
B2={s:simplify(d[s]/4) for s in channels}
assert A2==B2 and simplify(sum(A2.values())-1)==0
v=simplify(-Rational(2,3)*A2[0]-Rational(2,7)*A2[1])
print("F =",Fmat); print("Wg(id), Wg(swap) =",Wg_id,Wg_swap)
print("Method A c_s^2 =",A2); print("Method B c_s^2 =",B2)
print("A == B:",A2==B2); print("norm sum =",simplify(sum(A2.values()))); print("v =",v)
assert v==-Rational(8,21)
