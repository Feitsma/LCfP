"Exercise 11.2.6 of How to Think Like a ComputerScientist: Learning with Python 3Documentation"

from Point import Point
import unittest

class Rectangle:
    """A class to manufacture rectangle objects"""

    def __init__(self, posn, w, h):
        """Initialize rectangle at posn (upper-left corner of rectangle), with width w, and height h"""
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
        location_point_x = location_point.x #x value can be called because user inserts a Point at:location_point
        location_point_y = location_point.y
        lower_bound_x = self.corner.x
        higher_bound_x = self.corner.x + self.width
        higher_bound_y = self.corner.y
        lower_bound_y = self.corner.y - self.height
        if location_point_x in range(lower_bound_x, higher_bound_x)\
                and location_point_y in range(lower_bound_y, higher_bound_y):
            return print("x and y values fall in rectangle!")
        else:
            return print("One of the values is outside of the rectangle!")


box = Rectangle(Point(0,0), 100, 200) #define a rectangle
bomb = Rectangle(Point(100,80), 5, 10)
r = Rectangle(Point(0,0), 10,5) #define a rectangle a, where Point(x,y) is upper-left corner

print("box: ", box) #Printing values of a rectangle
print("bomb: ", bomb)