import sympy
# from sympy import sympify

a, b, c = sympy.symbols('a,b,c')
x, y, z = sympy.symbols('x,y,z')

xyz = sympy.symbols('x,y,z')
abc = sympy.symbols('a,b,c')
uvw = sympy.symbols('u,v,w')

def sympify(*argv):
    return sympy.sympify(*argv)

def version():
    return "0.0.1"

def require_point(p):
    if not isinstance(p, Point):
        raise Exception(f"{p} is not a point")
        return False
    return True
    
def require_line(l):
    if not isinstance(l, Line):
        raise Exception(f"{p} is not a line")
        return False
    return True

def midpoint(p, q):
    require_point(p)
    require_point(q)
    px, py, pz = p.get_normalized().values()
    qx, qy, qz = q.get_normalized().values()
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
