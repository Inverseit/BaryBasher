from .Point import Point
from .Line import Line
import barybasher.core as core
sympy = core.sympy
sympify = core.sympify



class Circle():
    def __init__(self, points = None, equation = None):
        if points == None and equation == None:
            raise Exception("you must submit at least some parametres")
        if points != None and equation != None:
            raise Exception("overparametrized equation")
        self.coefs = (None, None, None)
        self.uvw = core.uvw
        self.xyz = core.xyz
        self.abc = core.abc
        self.general = self.generalEquation()
        self.points = points
        self.equation = equation
        if self.points != None:
            self.equation = self.__makeEquation()
    
    def generalEquation(self):
        u, v, w = self.uvw
        x, y, z = self.xyz
        a, b ,c = self.abc
        equation = -1 * a * a * y * z - b*b*z*x - c*c*x*y + (u*x + v*y + w*z) * (x + y + z)
        return equation

    def generalCircleSubstitution(self, p):
        x, y, z = self.xyz
        return self.general.subs({x: p.x, y: p.y, z: p.z})
    
    def __makeEquation(self):
        x, y, z = self.xyz
        u,v,w = self.uvw
        f, s, t = map(self.generalCircleSubstitution, self.points)
        # return sympy.linsolve([l1.get_equation(), l2.get_equation(), x - 1], (x, y, z))
        solution = list(sympy.linsolve([f, s, t], self.uvw))[0]
        self.coefs = solution
        u_solved, v_solved, w_solved = solution
        circleEquation = sympify(self.general.subs({u: u_solved, v: v_solved, w: w_solved}))
        return circleEquation 
    
    def power(self, p):
        return self.equation.subs(p.getAsDict())

    def contains(self, p):
        return self.power(p).equals(core.sympy.S.Zero)

    def radicalAxisWith(self, c):
        if not isinstance(c, Circle):
            raise Exception("Input must be a circle")
        x, y, z = self.xyz
        u1, v1, w1 = self.coefs
        u2, v2, w2 = c.coefs
        u3, v3, w3 = u1 - u2, v1-v2, w1-w2
        return Line(equation=core.sympy.Eq(u3*x+v3*y+w3*z,0), description=f"Radical axis of {self} and {c}")

    
