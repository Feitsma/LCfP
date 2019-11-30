"Exercise 11.1.12"

import math

class Point:
    """Point class represents and manipulates x,y coords."""

    def __init__(self, x=0, y=0):
        """Create a new point at x,y"""
        self.x = x
        self.y = y

p = Point(3,4)
q = Point(5,4)


print(p.x, p.y, q.x, q.y)
