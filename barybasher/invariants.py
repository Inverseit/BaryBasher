from barybasher.Objects.Point import Point
from barybasher.Objects.Line import Line
from barybasher.Objects.Triangle import Triangle
from barybasher.Objects.Circle import Circle

def require_point(p):
    if not isinstance(p, Point):
        raise Exception(f"{p} is not a point")
        return False
    return True
    
def require_line(l):
    if not isinstance(l, Line):
        raise Exception(f"{l} is not a line")
        return False
    return True
