
# Import the classes from the module where they are defined
class animal_test:
    def test_animal(self):
        animal = Animal("Generic Animal", "Unknown")
        self.assertEqual(animal.name, "Generic Animal")
        self.assertEqual(animal.species, "Unknown")

    def test_mammal(self):
        mammal = Mammal("Generic Mammal", "Mammal")
        self.assertEqual(mammal.name, "Generic Mammal")
        self.assertEqual(mammal.species, "Mammal")

    def test_primate(self):
        primate = Primate("Chimpanzee", "Primate")
        self.assertEqual(primate.name, "Chimpanzee")
        self.assertEqual(primate.species, "Primate")
        self.assertTrue(hasattr(primate, 'climb_tree'))
        self.assertTrue(hasattr(primate, 'speak'))

    def test_marsupial(self):
        marsupial = Marsupial("Kangaroo", "Marsupial")
        self.assertEqual(marsupial.name, "Kangaroo")
        self.assertEqual(marsupial.species, "Marsupial")
        self.assertTrue(hasattr(marsupial, 'carry_baby'))

    def test_bird(self):
        bird = Bird("Eagle", 2.0)
        self.assertEqual(bird.name, "Eagle")
        self.assertEqual(bird.species, "Bird")
        self.assertEqual(bird.wingspan, 2.0)

    def test_reptile(self):
        reptile = Reptile("Lizard", True)
        self.assertEqual(reptile.name, "Lizard")
        self.assertEqual(reptile.species, "Reptile")
        self.assertTrue(reptile.back_in_sun)

if __name__ == "__main__":
    animal_test.main()

