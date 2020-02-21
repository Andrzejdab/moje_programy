import math


class Circle:
    """Class to create Circle objects"""

    def __init__(self, radius=1):
        """Circle initializer"""
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        self._radius = radius

    @property
    def area(self):
        """Calculate and return the area of the Circle"""
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        """Calculate and return the diameter of the Circle"""
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        """Set the diameter"""
        self.radius = diameter / 2

    def __str__(self):
        return 'Circle({})'.format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)





