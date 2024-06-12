class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
class Mammal(Animal):
    def __init__(self,name, species, give_birth):
        super().__init__(name, species = 'Mammal')
        self.give_birth = give_birth
class Bird(Animal):
    def __init__(self, name, species,  wingspan):
        super().__init__(name, species = 'Bird')
        self.wingspan = wingspan
class Reptile(Animal):
    def __init__(self, name, back_in_sun):
        super().__init__(self, name, species = 'Reptile')
        self.back_in_sun = back_in_sun