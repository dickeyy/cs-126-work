# Add a method named union to the Rectangle class. Use your Rectangle class solution from the previous exercises as a starting point to solve this problem
# Suppose a class named Rectangle has already been created that has the following members:

# Write code below

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
    
    # Add a method named union to your class. Your method should accept another rectangle as a parameter, and return a new rectangle that represents the area occupied by the tightest bounding box that contains both the current rectangle (self) and the given other rectangle.

    # Write code below
    def union(self, other):
        x = min(self._x, other._x)
        y = min(self._y, other._y)
        w = max(self._x + self._width, other._x + other._width) - x
        h = max(self._y + self._height, other._y + other._height) - y
        return Rectangle(x, y, w, h)
