from shape import Shape

class Square(Shape):
    def __init__(self, name, side):
        # Call superclass initializer and set square side length
        Shape.__init__(self, name)
        self.__side = side

    def set_side(self, side):
        # Update the square's side length
        self.__side = side

    def get_side(self):
        # Return the square's side length
        return self.__side

    def get_area(self):
        # Override get_area() to calculate square area
        return self.__side * self.__side
