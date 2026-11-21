class Shape:
    def __init__(self, name):
        # Initialize the shape's name attribute
        self.__name = name

    def set_name(self, name):
        # Update the shape's name
        self.__name = name

    def get_name(self):
        # Return the shape's name
        return self.__name

    def get_area(self):
        # Default area method to be overridden by subclasses
        return 0.0
