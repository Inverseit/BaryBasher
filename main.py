import sympy
from sympy import sympify

class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.short = (x, y, z)
        self.normal = self.get_normalized()

    def get_normalized(self):
        sumOfCoords = sympify(self.x + self.y + self.z)
        if sumOfCoords == sympy.S.Zero:
            print("Point at infinity")
        return {x: sympify(self.x/sumOfCoords), y: sympify(self.y/sumOfCoords), z: sympify(self.z/sumOfCoords)}

    def __str__(self):
        return f"({self.x}:{self.y}:{self.z})"
    
    def __eq__(self, other):
        if not isinstance(other, Point):
            return
        return self.normal[x].equals(other.normal[x]) and self.normal[y].equals(other.normal[y]) and self.normal[z].equals(other.normal[z])
    
    def getAsList(self):
        return list(self.short)

class Line():
    def __init__(self, p, q):
        self.points = [p, q]
        self.equation = self.get_equation()

    def get_equation(self):
        p, q = self.points
        return sympify(sympy.Matrix([[x, y, z], p.getAsList(), q.getAsList()]).det())
    
    def contains(self, p):
        print(self.equation, p)
        return sympify(self.equation.subs({x:p.x, y:p.y, z:p.z})).equals(sympy.S.Zero)

    def intersection(self, line):
        return sympy.linsolve([self.equation, line.equation, x+y+z-1], (x,y,z))



def getMidpoint(p, q):
    px, py, pz = p.get_normalized().values()
    qx, qy, qz = q.get_normalized().values()
    mx, my, mz = list(map(sympify, ((px+qx)/2,(py+qy)/2,(pz+qz)/2)))
    dens = list(map(lambda i: i.as_numer_denom(), (mx,my,mz)))
    if dens[0][1].equals(dens[1][1]) and dens[0][1].equals(dens[2][1]):
        t = dens[0][0], dens[1][0], dens[2][0]
        mx, my, mz =tuple(map(sympify, t))
    print(mx, my,mz)
    return Point(mx, my, mz)


a, b, c = sympy.symbols('a,b,c')
x,y,z = sympy.symbols('x,y,z')
A = Point(sympy.Integer(1), sympy.Integer(0), sympy.Integer(0))
T = Point(sympy.Integer(0), sympy.Integer(6), sympy.Integer(0))
B = Point(sympy.Integer(0), sympy.Integer(1), sympy.Integer(0))
C = Point(sympy.Integer(0), sympy.Integer(0), sympy.Integer(1))
I = Point(a, b, c)
I_A = Point(-a, b, c)
D = Point(-a, b, c)
H = Point(0, 1 / (a * a + c * c - b * b), 1 / (a * a + b * b - c * c))

# L = getMidpoint(A, H)
# K = Point(a*a, b*b, c*c)
# ML = Line(M, L)
# print(ML.contains(K))
# print(ML.get_equation())
M = getMidpoint(A, B)
N = getMidpoint(A, C)
CB = Line(C, B)
AB = Line(A, B)
print(CB.intersection(Line(N, M)))
# print(CB.contains(M))

# A_ = Point(sympy.Integer(3), sympy.Integer(0), sympy.Integer(0))
# print(T == B)

# print(getMidpoint(A, B))

# print(getMidpoint(A, I))

# def isCollinear(p, q, r):

