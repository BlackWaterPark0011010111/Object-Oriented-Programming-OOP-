class Animal:
    def __init__(self, number_of_legs, number_of_eyes):
        self.number_of_legs = number_of_legs
        self.number_of_eyes = number_of_eyes

    def breathe(self):
        print("Animal is breathing.")

    def walk(self):
        print("Animal is walking.")

    def summary(self):
        print(f"This animal has {self.number_of_legs} legs and {self.number_of_eyes} eyes.")
