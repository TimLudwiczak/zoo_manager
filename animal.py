class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        class Mammal(Animal):
            def give_birth(self):
                pass
            class Primate(Mammal):
                def climb_tree(self):
                    pass
                def speak(self):
                    pass
            class Marsupial(Mammal):
                def carry_baby(self):
                    pass
        class Bird(Animal):
            def __init__(self, name, wingspan):
                super().__init__(name, species = 'Bird')
                self.wingspan = wingspan
        class Reptile(Animal):
            def __init__(self, name, back_in_sun):
                super().__init__(name, species = 'Reptile')
                self.back_in_sun = back_in_sun