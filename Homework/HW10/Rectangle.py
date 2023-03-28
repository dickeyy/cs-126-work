# Write a class named Rectangle where each object represents a rectangular two-dimensional region. Your class should have the following public members:

# Rectangle(x, y, w, h) - constructor - Initializes a new rectangle whose top-left corner is specified by the given (x, y) coordinates and with the given width and height, w by h. Raises a ValueError on a negative width or height.
# ba.x, ba.y, ba.width, ba.height - property - the rectangle location and dimensions (read-only)
# str(r) - method - returns a string representation of the rectangle such as "Rectangle[x=1,y=2,width=3,height=4]"

# Define the entire class including the class heading, the private data attributes, and the declarations and definitions of all the methods and constructor.

class Rectangle:
    def __init__(self, x, y, w, h):
        if w < 0 or h < 0:
            raise ValueError("Width and height must be non-negative")
        self._x = x
        self._y = y
        self._w = w
        self._h = h

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def width(self):
        return self._w

    @property
    def height(self):
        return self._h

    def __str__(self):
        return "Rectangle[x={}, y={}, width={}, height={}]".format(self._x, self._y, self._w, self._h)

