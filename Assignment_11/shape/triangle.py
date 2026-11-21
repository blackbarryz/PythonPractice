from shape import Shape

class Triangle(Shape):
    def __init__(self, name, base, height):
        # Call superclass initializer and set triangle base and height
        Shape.__init__(self, name)
        self.__base = base
        self.__height = height

    def set_base(self, base):
        # Update the triangle's base
        self.__base = base

    def set_height(self, height):
        # Update the triangle's height
        self.__height = height

    def get_base(self):
        # Return the triangle's base
        return self.__base

    def get_height(self):
        # Return the triangle's height
        return self.__height

    def get_area(self):
        # Override get_area() to calculate triangle area
        return 0.5 * self.__base * self.__height
