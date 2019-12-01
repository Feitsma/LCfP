"Exercise 11.2.6"

from Point import Point
import unittest

class Rectangle:
    """A class to manufacture rectangle objects"""

    def __init__(self, posn, w, h):
        """Initialize rectangle at posn, with width w, and height h"""
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        """Let a rectangle be printed as a string"""
        return "({0},{1},{2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        """Grow or shrink this object by deltas"""
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """Move this object by the deltas"""
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        """Returns area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns circumference of a rectangle"""
        return 2*(self.width + self.height)

    def flip(self):
        """Flips the height and width values of a rectangle"""
        width = self.width
        height = self.height
        self.width = height
        self.height = width
        return print('The values were: ', Point(width, height), 'and are now: ', Point(self.width, self.height))

    def contains(self, location_point):
        """Give Point and determines whether it falls within the rectangle"""
        point = Point(x,y)



box = Rectangle(Point(0,0), 100, 200)
bomb = Rectangle(Point(100,80), 5, 10)
r = Rectangle(Point(0,0), 10,5)
print("box: ", box)
print("bomb: ", bomb)