from pet import Pet

class Bird(Pet):
    def __init__(self, name):
        # Call superclass initializer with species set to Bird
        Pet.__init__(self, name, "Bird")

    def make_sound(self):
        # Override make_sound() for a bird
        return "Tweet!"
