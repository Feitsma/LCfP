"Exercise 11.3.11 of How to Think Like a ComputerScientist: Learning with Python 3Documentation"

class MyTime:
    """A class that records the time of day"""

    def __init__(self, hrs=0, mins=0, secs=0):
        """Create a MyTime object initialized to hrs, mins, secs"""
        self.hours = hrs
        self.minutes = mins
        self.seconds = secs



tim1 = MyTime(11,59,30)