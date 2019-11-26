"Exercise 11.1.12"

import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

class Point:
    """Point class represents and manipulates x,y coords."""

    def __init__(self, x=0, y=0):
        """Create a new point at x,y"""
        self.x = x
        self.y = y

    def distance_class(self):
        """Calculates distance from each other"""
        x_dist = q.x - p.x
        y_dist = q.y - p.y
        return math.sqrt((x_dist)**2 + (y_dist)**2)

p = Point(3,4)
q = Point(5,4)


print(p.x, p.y, q.x, q.y)
to_Print = distance_class(p,q)
