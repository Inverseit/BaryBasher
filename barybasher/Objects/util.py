from .Point import Point
from .Line import Line
from .Circle import Circle
import barybasher.core as core
sympy = core.sympy
sympify = core.sympify

def midpoint(p, q):
    px, py, pz = p.get_normalized_dict().values()
    qx, qy, qz = q.get_normalized_dict().values()
    mx, my, mz = list(map(sympify, ((px+qx)/2, (py+qy)/2, (pz+qz)/2)))
    dens = list(map(lambda i: i.as_numer_denom(), (mx, my, mz)))
    if dens[0][1].equals(dens[1][1]) and dens[0][1].equals(dens[2][1]):
        t = dens[0][0], dens[1][0], dens[2][0]
        mx, my, mz = tuple(map(sympify, t))
    return Point(mx, my, mz)


def intersection_of_lines(l1, l2):
    require_line(l1)
    require_line(l2)
    return sympy.linsolve(
        [l1.get_equation(), l2.get_equation(), x - 1], (x, y, z))


def is_collinear(p, q, r):
    res = sympy.Matrix(
        [r.getAsList(), p.getAsList(), q.getAsList()]).det().equals(sympy.S.Zero)
    return res
