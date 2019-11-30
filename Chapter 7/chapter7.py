"Exercise 11.1.12"

import math
import datetime
import time

class Point:
    """Point class represents and manipulates x,y coords."""

    def __init__(self, x=0, y=0):
        """Create a new point at x,y"""
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """Return the halfway point between myself and target"""
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    def reflect_x(self):
        """Reflects a point around x-axis"""
        x = self.x
        y = self.y * -1
        return Point(x, y)

    def slope_from_origin(self):
        origin = Point(0, 0)
        dx = self.x - origin.x
        dy = self.y - origin.y
        return (dy / dx)

    def get_line_to(self, target):
        """determine a and b in y=ax+b"""
        # a is slope of line
        # b is distance in x value
        dx = target.x - self.x
        dy = target.y - self.y
        return Point(dy / dx, dy)


# print(Point(4,11).get_line_to(Point(6,15)))

class SMS_store:
    """This class handles storage of SMS messages in tuples of (has_been_viewed, from_number, time_arrived, text_of_sms)"""

    def __init__(self):
        self.inbox = []

    def add_new_arrival(self, from_number, text_of_sms):
        ti = time.gmtime()
        local_time = time.asctime(ti)
        self.inbox.append((False, from_number, local_time, text_of_sms))

    def message_count(self):
        return len(self.inbox)

    def get_unread_indexes(self):
        i = 0
        result = []
        for i in self.inbox:
            if self.inbox[i][0] == False:
                result.append(i)
            else:
                continue
        return result


my_inbox = SMS_store()
my_inbox.add_new_arrival('06', 'hey')
my_inbox.add_new_arrival('06test', 'Hey, works this?')
unread_messages = my_inbox.get_unread_indexes
