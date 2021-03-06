from barybasher.Objects.Point import Point
from barybasher.Objects.Line import Line
from barybasher.Objects.Triangle import Triangle
from barybasher.Objects.Circle import Circle
import barybasher.core as core
from util import intersection

ABC = Triangle(core.a, core.b, core.c)
A, B, C = ABC.getVertices()
tangentB = ABC.getTangent("B")
tangentC = ABC.getTangent("C")
L = intersection(tangentC,tangentB) #updated interface of intersection
K = ABC.getPoint("K") # Symmedian point
A_symmedian = Line(points=[A, K])
assert(A_symmedian.contains(L)) #resolves to true
print("Lemma is true")


