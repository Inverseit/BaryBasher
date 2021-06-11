from barybasher.Objects.Point import Point
from barybasher.Objects.Line import Line
from barybasher.Objects.Triangle import Triangle
from barybasher.Objects.Circle import Circle
import barybasher.core as core



ABC = Triangle(core.a, core.b, core.c)
A, B, C = ABC.getVertices()
K = ABC.getPoint("symmedian")
n = ABC.getTangent("B")
m = ABC.getTangent("C")
S = n.intersectWith(m)

result = core.is_collinear(K, S, A)
if result:
    print("S lies in AK")

