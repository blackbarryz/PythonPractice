from pet import Pet

class Dog(Pet):
    def __init__(self, name):
        # Call superclass initializer with species set to Dog
        Pet.__init__(self, name, "Dog")

    def make_sound(self):
        # Override make_sound() for a dog
        return "Woof!"
