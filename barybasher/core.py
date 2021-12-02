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
