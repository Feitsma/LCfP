"Exercise 11.3.11 of How to Think Like a ComputerScientist: Learning with Python 3Documentation"

from Point import Point

class MyTime:
    """A class that records the time of day"""

    def __init__(self, hrs=0, mins=0, secs=0):
        """Create a MyTime object initialized to hrs, mins, secs.
            The values of mins and secs may be outside the range
            0-59, but the resulting MyTime object will be normalized"""
        #Calculate total seconds to represent
        totalsecs = hrs*3600 + mins*60 + secs
        self.hours = totalsecs //3600
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __str__(self):
        """Print time as string"""
        return "({0}:{1}:{2})".format(self.hours, self.minutes, self.seconds)

    def increment(self, seconds):
        self.seconds += seconds

        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes +=1

        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1

    def to_seconds(self):
        """Returns the number of seconds represented by this instance"""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def after(self, time2):
        """Return True if I am strictly greater than time2"""
        return self.to_seconds() > time2.to_seconds()

    def __add__(self, other):
        """add times using only seconds by to_seconds method.
        Due to how __init__ method is written, if seconds are
        higher than 59, it automatically converts it to standard
        time units"""
        return MyTime(0,0,self.to_seconds() + other.to_seconds())

    def __sub__(self, other):
        """substract two time units from eachother using only the seconds
        seconds will be converted to standard time units again since that
        is defined in __init__"""
        return MyTime(0,0,self.to_seconds() - other.to_seconds())

    def between(self, t1, t2):
        """Determines whether invoking object falls between t1 and t2 and
        returns True or False"""
        return self.to_seconds() in range(t1.to_seconds(), t2.to_seconds())

    def __gt__(self, other):
        """Does the same as .after() method but uses __gt__
        (greater than), such that simply t1 > t2 can be used
        in code"""
        return self.to_seconds() > other.to_seconds()

    def increment_seconds(self, seconds):
        """increment function rewritten in seconds, to make is easier"""
        return MyTime(0,0,self.to_seconds()+seconds)


tim1 = MyTime(1,59,30)
tim2 = MyTime(2,30,30)
t3 = tim1 + tim2 #test addition, working with __add__ method
t33 = tim1 - tim2 #__sub__ method
print(t3)
print(t33)
print(tim1)
print(tim1.to_seconds())
print(MyTime(23,1,1).to_seconds())
print(tim1.after(MyTime(23,10,10)))
t1 = MyTime(10,0,0)
t2 = MyTime(11,0,0)
t3 = MyTime(11,30,0)
print(t3.between(t1,t2)) #test between method
print(t1.after(t2))
print(t1 > t2) #test if __gt__  works
print(t1.increment_seconds(10))
