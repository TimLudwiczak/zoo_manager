class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
class Mammal(Animal):
    def __init__(self,name,give_birth):
        super().__init__(name, species = 'Mammal')
        self.give_birth = give_birth