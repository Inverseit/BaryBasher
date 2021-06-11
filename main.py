from barybasher.Objects.Point import Point
from barybasher.Objects.Line import Line
from barybasher.Objects.Triangle import Triangle
from barybasher.Objects.Circle import Circle
import barybasher.core as core




# AB = ABC.getLine("AB")
# AC = ABC.getLine("AC")

# # print(n)

# I = ABC.getPoint("I")

# ABI = Circle(points=(A, B, I))
# CBI = Circle(points=(C, B, I))

# r = ABI.radicalAxisWith(CBI)
# IB =  Line(points=(I, B))
# print(r == IB)

# print(ABI.contains(A))


ABC = Triangle(core.a, core.b, core.c)
A, B, C = ABC.getVertices()
K = ABC.getPoint("symmedian")
# n = ABC.getTangent("B")
# m = ABC.getTangent("C")
n, m = Line(points=(A,B)), Line(points=(B,C))
S = n.intersectWith(m)
print(S)


# def is_collinear(p, q, r):
#     res = core.sympy.Matrix([r.getAsList(), p.getAsList(), q.getAsList()]).det().equals(core.sympy.S.Zero)
#     if res:
#         print(f"{p}, {q}, {r} are collinear")
#     return res

# print(is_collinear(K, S, A))

# J = ABC.getPoint("I_A")


