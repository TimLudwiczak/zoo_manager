import pytest

# Import the classes from the module where they are defined
from your_module import Animal, Mammal, Primate, Bird, Reptile

def test_animal():
    animal = Animal(name="Generic Animal", species="Unknown")
    assert animal.name == "Generic Animal"
    assert animal.species == "Unknown"

def test_mammal():
    mammal = Mammal(name="Generic Mammal", species="Mammalia")
    assert mammal.name == "Generic Mammal"
    assert mammal.species == "Mammalia"
    assert hasattr(mammal, 'give_birth')
    assert callable(getattr(mammal, 'give_birth', None))

def test_primate():
    primate = Primate(name="Generic Primate", species="Primate")
    assert primate.name == "Generic Primate"
    assert primate.species == "Primate"
    assert hasattr(primate, 'give_birth')
    assert callable(getattr(primate, 'give_birth', None))
    assert hasattr(primate, 'speak')
    assert callable(getattr(primate, 'speak', None))

def test_bird():
    bird = Bird(name="Generic Bird", wingspan=1.5)
    assert bird.name == "Generic Bird"
    assert bird.species == "Bird"
    assert bird.wingspan == 1.5

def test_reptile():
    reptile = Reptile(name="Generic Reptile", back_in_sun=True)
    assert reptile.name == "Generic Reptile"
    assert reptile.species == "Reptile"
    assert reptile.back_in_sun is True

if __name__ == "__main__":
    pytest.main()
