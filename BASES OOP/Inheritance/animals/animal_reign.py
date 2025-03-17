from animal import Animal
from dog import Dog
from german_shepard import GermanShepard

def main():
    animal = Animal(4, 2)
    dog = Dog()
    german_shepard = GermanShepard()

    print("Animal:")
    animal.summary()
    animal.breathe()
    animal.walk()

    print("\nDog:")
    dog.summary()
    dog.breathe()
    dog.walk()

    print("\nGerman Shepard:")
    german_shepard.summary()
    german_shepard.breathe()
    german_shepard.walk()

if __name__ == "__main__":
    main()
