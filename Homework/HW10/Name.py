# Write a class named Name where each object remembers information about a person's full name. You must include the following public members:

# Name(first, middle, last) - constructor - Constructs a new name representing the given first, middle, and last name
# n.first_name - property - get/set the first name as a string
# n.middle_initial - property - get/set the middle initial as a string 
# n.last_name - property - get/set the last name as a string
# n.get_normal_order() - method - returns the name in normal order such as "John Q. Public"
# n.get_reverse_order() - method - returns the name in reverse order such as "Public, John Q." 
# str(n) - method - returns the name in normal order such as "John Q. Public" (same order as get_normal_order)

# Define the entire class including the class heading, the privatre instance variables, and the declarations and definitions of all the public member functions and constructor

# Write code below
class Name:
    def __init__(self, first, middle, last):
        self._first = first
        self._middle = middle
        self._last = last

    @property
    def first_name(self):
        return self._first

    @first_name.setter
    def first_name(self, first):
        self._first = first

    @property
    def middle_initial(self):
        return self._middle

    @middle_initial.setter
    def middle_initial(self, middle):
        self._middle = middle

    @property
    def last_name(self):
        return self._last

    @last_name.setter
    def last_name(self, last):
        self._last = last

    def get_normal_order(self):
        return "{} {}. {}".format(self._first, self._middle, self._last)

    def get_reverse_order(self):
        return "{}, {} {}.".format(self._last, self._first, self._middle)

    def __str__(self):
        return self.get_normal_order()