import pytest
from animal import Animal, Mammal, Primate, Marsupial, Bird, Reptile

def test_animal_creation():
    animal = Animal("Generic Animal", "Unknown")
    assert animal.name == "Generic Animal"
    assert animal.species == "Unknown"

def test_mammal_creation():
    mammal = Mammal("Generic Mammal", "Mammal")
    assert mammal.name == "Generic Mammal"
    assert mammal.species == "Mammal"
    assert mammal.give_birth() == "Giving birth to live young"

def test_primate_creation():
    primate = Primate("Chimpanzee", "Primate")
    assert primate.name == "Chimpanzee"
    assert primate.species == "Primate"
    assert primate.climb_tree() == "Climbing a tree"
    assert primate.speak() == "Speaking"

def test_marsupial_creation():
    marsupial = Marsupial("Kangaroo", "Marsupial")
    assert marsupial.name == "Kangaroo"
    assert marsupial.species == "Marsupial"
    assert marsupial.carry_baby() == "Carrying baby in pouch"

def test_bird_creation():
    bird = Bird("Eagle", 2.0)
    assert bird.name == "Eagle"
    assert bird.species == "Bird"
    assert bird.wingspan == 2.0
    assert bird.fly() == "Flying"

def test_reptile_creation():
    reptile = Reptile("Lizard", True)
    assert reptile.name == "Lizard"
    assert reptile.species == "Reptile"
    assert reptile.back_in_sun is True
    assert reptile.bask() == "Basking in the sun"

if __name__ == "__main__":
    pytest.main()



