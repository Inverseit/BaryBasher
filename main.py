from barybasher.Objects.Point import Point
from barybasher.Objects.Line import Line
from barybasher.Objects.Triangle import Triangle
import barybasher.core as core




# AB = ABC.getLine("AB")
# AC = ABC.getLine("AC")

# # print(n)

ABC = Triangle(core.a, core.b, core.c)
A, B, C = ABC.getVertices()
K = ABC.getPoint("symmedian")
n = ABC.getTangent("B")
m = ABC.getTangent("C")

J = ABC.getPoint("I_A")
I = ABC.getPoint("I")


def is_collinear(p, q, r):
    res = core.sympy.Matrix([r.getAsList(), p.getAsList(), q.getAsList()]).det().equals(core.sympy.S.Zero)
    if res:
        print(f"{p}, {q}, {r} are collinear")
    return res

print(is_collinear(J, I, A))
