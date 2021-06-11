import sympy
from sympy import sympify
a, b, c = sympy.symbols('a,b,c')
x, y, z = sympy.symbols('x,y,z')


class Point():
    def __init__(self, x, y, z):
        self.x = self.getConverted(x)
        self.y = self.getConverted(y)
        self.z = self.getConverted(z)
        self.short = (x, y, z)
        self.normal = self.get_normalized_dict().values()
        self._beautifiedVersion = self.beautified
    @staticmethod
    def getConverted(v):
        if v == 1:
            return sympy.S.One
        if v == 0:
            return sympy.S.Zero
        return sympify(v)
    
    def getAsDict(self):
        return {x: self.x, y: self.y, z: self.z}

    def get_normalized_dict(self):
        sumOfCoords = sympify(self.x + self.y + self.z)
        if sumOfCoords == sympy.S.Zero:
            print("Point at infinity")
        return {x: sympify(self.x/sumOfCoords), y: sympify(self.y/sumOfCoords), z: sympify(self.z/sumOfCoords)}
    
    def beautified(self):
        mx, my, mz = self.x, self.y, self.z
        dens = list(map(lambda i: i.as_numer_denom(), (mx, my, mz)))
        if dens[0][1].equals(dens[1][1]) and dens[0][1].equals(dens[2][1]):
            t = dens[0][0], dens[1][0], dens[2][0]
            mx, my, mz = tuple(map(sympify, t))
        if dens[0][1].equals(-dens[1][1]) and dens[1][1].equals(dens[2][1]):
            t = -dens[0][0], dens[1][0], dens[2][0]
            mx, my, mz = tuple(map(sympify, t))
        return Point(mx, my, mz)

    def __str__(self):
        t = self._beautifiedVersion()
        return f"({t.x}:{t.y}:{t.z})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return
        return self.normal[x].equals(other.normal[x]) and self.normal[y].equals(other.normal[y]) and self.normal[z].equals(other.normal[z])

    def getAsList(self):
        return list(self.short)
