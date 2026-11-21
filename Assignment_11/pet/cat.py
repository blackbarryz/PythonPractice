from pet import Pet

class Cat(Pet):
    def __init__(self, name):
        # Call superclass initializer with species set to Cat
        Pet.__init__(self, name, "Cat")

    def make_sound(self):
        # Override make_sound() for a cat
        return "Meow!"
