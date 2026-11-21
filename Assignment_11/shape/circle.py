import math
from shape import Shape

class Circle(Shape):
    def __init__(self, name, radius):
        # Call superclass initializer and set circle radius
        Shape.__init__(self, name)
        self.__radius = radius

    def set_radius(self, radius):
        # Update the circle's radius
        self.__radius = radius

    def get_radius(self):
        # Return the circle's radius
        return self.__radius

    def get_area(self):
        # Override get_area() to calculate circle area
        return math.pi * (self.__radius ** 2)
