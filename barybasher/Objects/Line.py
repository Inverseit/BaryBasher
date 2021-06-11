# import sympy
# from sympy import sympify
# a, b, c = sympy.symbols('a,b,c')
# x, y, z = sympy.symbols('x,y,z'
import barybasher.core as core
sympy = core.sympy 
sympify = core.sympify

from .Point import Point

class Line():
    def __init__(self, points = None, equation = None, description = None):
        if None == points and None == equation:
            raise Exception("no parametres are sent")
        if None != points and equation != None:
            raise Exception("overparametrized")
        self.points = points
        if points:
            # check valid points and that they are two of them
            self.equation = self.__make_equation()
        else:
            # check valid equation
            self.equation = equation
        self.description = description
        

    def __make_equation(self):
        x, y, z = core.x, core.y, core.z
        p, q = self.points
        if not isinstance(p, Point):
            raise Exception(f"{p} is not a point")
        if not isinstance(q, Point):
            raise Exception(f"{q} is not a point")
        return sympy.Eq(sympify(sympy.Matrix([[x, y, z], p.getAsList(), q.getAsList()]).det()),0)
    
    def get_equation(self):
        return self.equation

    def contains(self, p):
        x, y, z = core.x, core.y, core.z
        # requires point
        return self.equation.subs({x: p.x, y: p.y, z: p.z}).equals(sympy.S.Zero)

    def intersectWith(self, line):
        x, y, z = core.x, core.y, core.z
        s = sympy.linsolve([self.equation, line.get_equation(), x+y+z-1], (x, y, z))
        if not s:
            return Point(0,0,0)
        s = list(s)
        px, py, pz = s[0]
        variables = set()
        variables = variables.union(px.free_symbols, py.free_symbols, pz.free_symbols)
        if variables.intersection(set((x,y,z))):
            raise Exception("Line you are comparing are the same line")
        return Point(px, py, pz)
    
    def __str__(self):
        res = ""
        if self.description:
            res = self.description
        if self.points:
            return res + f" -> Line through {self.points[0]} and {self.points[1]}"
        if self.equation != None:
            # print(list(self.equation))
            return res + f" -> Line defined with equation {self.equation}"
    
    def __eq__(self, o):
        if not isinstance(o, Line):
            raise Exception("o is not a line")
        x, y, z = core.x, core.y, core.z
        s = sympy.linsolve(
            [self.equation, o.get_equation(), x+y+z-1], (x, y, z))
        if not s:
            return False
        s = list(s)
        px, py, pz = s[0]
        variables = set()
        variables = variables.union(
            px.free_symbols, py.free_symbols, pz.free_symbols)
        if variables.intersection(set((x, y, z))):
            return True
        return False
