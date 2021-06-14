from barybasher.Objects.Point import Point
from barybasher.Objects.Line import Line
from barybasher.Objects.Triangle import Triangle
from barybasher.Objects.Circle import Circle
import barybasher.core as core
import barybasher.Objects.util as util


ABC = Triangle(core.a, core.b, core.c)
A, B, C = ABC.getVertices()
w = ABC.get_circumcircle()
M = util.midpoint(A, B)
I_C = ABC.getPoint("I_C") # Вневписанка C
AK = Line(points=(A, I_C)) # Внешняя биссектриса
K = w.intersectionNotEqualTo(AK, A)[0] 

ser_per = ABC.get_perpendicular_bisector("CA")
I = ABC.getPoint("I")
A_bisect = Line(points=(A, I))
P = ser_per.intersectWith(A_bisect)
print(P)



# t = Circle(points=(A, K, M))

# print(t)
t2 = Circle(points=(A, M, P))
# print(t2)

# print(core.sympify(t.equation - t2.equation))

# print(t2.contains(P))
print(t2.contains(K))





# K = ABC.getPoint("symmedian")
# m = ABC.getTangent("C")
# S = n.intersectWith(m)

# result = core.is_collinear(K, S, A)
# if result:
#     print("S lies in AK")

