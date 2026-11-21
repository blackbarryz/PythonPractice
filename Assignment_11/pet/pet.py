class Pet:
    def __init__(self, name, species):
        # Initialize common pet attributes
        self.__name = name
        self.__species = species

    def set_name(self, name):
        # Update the pet's name
        self.__name = name

    def get_name(self):
        # Return the pet's name
        return self.__name

    def get_species(self):
        # Return the pet's species
        return self.__species

    def make_sound(self):
        # Default sound method to be overridden by subclasses
        return "Some sound"

    def __str__(self):
        # Return formatted string showing pet name, species, and sound
        return f"{self.__name} the {self.__species} says {self.make_sound()}"
