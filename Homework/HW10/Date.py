# Write a class named Date where each object remembers information about a month and a day.
# Ignore leap years and don't stre the year in the object
# Incude the following public members

# Date(month, day) - constructor - Constructs a new date representing the given month and day
# d.month - property - property to get/set the month
# d.day - property - property to get/set the day
# d.advance() - method - advances to the next day, wrapping to the next month and or/year if necessary
# d.days_in_month() - method - returns the number of days in the month stored by your date object
# d == other - method - returns True if the two dates have the same state 
# str(d) - method - returns a string representation such as "7/4" for July 4

# Define the entire class including the class heading, the private instance variables, and the declarations and definitions of all the public member functions and constructor

class Date:
    def __init__(self, month, day):
        self._month = month
        self._day = day

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month):
        self._month = month

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day):
        self._day = day

    def advance(self):
        self._day += 1
        if self._day > self.days_in_month():
            self._day = 1
            self._month += 1
            if self._month > 12:
                self._month = 1

    def days_in_month(self):
        if self._month in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif self._month in (4, 6, 9, 11):
            return 30
        else:
            return 28

    def __eq__(self, other):
        return self._month == other._month and self._day == other._day

    def __str__(self):
        return "{}/{}".format(self._month, self._day)

