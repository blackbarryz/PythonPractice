from shape import Shape

class Rectangle(Shape):
    def __init__(self, name, width, height):
        # Call superclass initializer and set rectangle dimensions
        Shape.__init__(self, name)
        self.__width = width
        self.__height = height

    def set_width(self, width):
        # Update the rectangle's width
        self.__width = width

    def set_height(self, height):
        # Update the rectangle's height
        self.__height = height

    def get_width(self):
        # Return the rectangle's width
        return self.__width

    def get_height(self):
        # Return the rectangle's height
        return self.__height

    def get_area(self):
        # Override get_area() to calculate rectangle area
        return self.__width * self.__height
