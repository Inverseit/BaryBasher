from .Point import Point
from .Line import Line
import barybasher.core as core

class Triangle():
    def __init__(self, a, b, c):
        self.A = Point(1,0,0)
        self.B = Point(0,1,0)
        self.C = Point(0,0,1)
        self.a, self.b, self.c = a, b, c
        self.___conway_inited = False

    def getVertices(self):
        return (self.A, self.B, self.C)

    def getPoint(self, s):
        if s == "I" or s.lower() == "incenter":
            return Point(self.a, self.b, self.c)

        if s == "G" or s.lower() == "median":
            return Point(1,1,1)
        
        if s == "K" or s.lower() == "symmedian":
            return Point(self.a * self.a, self.b * self.b, self.c*self.c)
        
        if s == "H" or s.lower() == "orthocenter":
            self.init_conway()
            return Point(1/self.S_A, 1/self.S_B, 1/self.S_C)

        if s == "O" or s.lower() == "circumcenter":
            self.init_conway()
            return Point(self.a * self.a * self.S_A, self.b * self.b * self.S_B, self.c * self.c * self.S_B)
        
        if s == "I_A" or s == "IA" or s.lower() == "a-excenter":
            return Point(-self.a, self.b, self.c)

        if s == "I_B" or s == "IB" or s.lower() == "b-excenter":
            return Point(self.a, -self.b, self.c)

        if s == "I_C" or s == "IC" or s.lower() == "c-excenter":
            return Point(self.a, self.b, -self.c)

        # if s == "D" or s.lower() == "incenter"

        raise Exception("other points will be later")

    def getLine(self, s):
        if s.lower() == "ab" or  s.lower() == "ba":
            return Line(points=(self.A, self.B))
        if s.lower() == "ac" or s.lower() == "ca":
            return Line(points=(self.A, self.C))
        if s.lower() == "bc" or s.lower() == "cb":
            return Line(points=(self.B, self.C))
        raise Exception("other lines will be later")
    
    def getTangent(self, s):
        if s.lower() == "a":
            return Line(equation=core.sympy.Eq(core.b * core.b * core.z + core.c * core.c * core.y, 0))
        if s.lower() == "b":
            return Line(equation=core.sympy.Eq(core.a * core.a * core.z + core.c * core.c * core.x, 0))
        if s.lower() == "c":
            return Line(equation=core.sympy.Eq(core.a * core.a * core.y + core.b * core.b * core.x, 0))
        raise Exception("general tangents will be later")


    def isogonal(self, p):
        if not isinstance(p, Point):
            raise Exception(f"{p} is not a point")
        return Point(self.a * self.a / p.x, self.b * self.b / p.y, self.c * self.c / p.z)
    
    
    def isatomic(self, p):
        if not isinstance(p, Point):
            raise Exception(f"{p} is not a point")
        return Point(1/p.x, 1/p.y, 1/p.z)

    def init_conway(self):
        if self.___conway_inited:
            return
        self.___conway_inited = True
        self.S_A = conway("A", self.a, self.b, self.c)
        self.S_B = conway("B", self.a, self.b, self.c)
        self.S_C = conway("C", self.a, self.b, self.c)

    @staticmethod
    def conway(vertex, a, b, c):
        if vertex == "A":
            return (b * b + c * c - a * a) / 2
        if vertex == "C":
            return (b * b + a * a - c * c) / 2
        if vertex == "B":
            return (a * a + c * c - b * b) / 2

