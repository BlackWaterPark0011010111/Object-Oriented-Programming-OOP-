# File: src/worker.py

# First, I need to import the ABC module to make Worker an abstract class.
from abc import ABC, abstractmethod

# Defining the abstract class Worker
class Worker(ABC):  # Inheriting from ABC to make it abstract
    def __init__(self, name):
        self.name = name

    @abstractmethod  # Marking work() as abstract
    def work(self):
        pass  # No implementation here, just a placeholder

    @abstractmethod  # Marking take_break() as abstract
    def take_break(self, minutes):
        pass  # No implementation here, just a placeholder

# Now, implementing the Programmer class
class Programmer(Worker):
    def __init__(self, name, language):
        super().__init__(name)  # Calling the parent class constructor
        self.language = language  # Adding the language attribute

    def __str__(self):
        return f"{self.name} codes with {self.language}"  # String representation

    def work(self):
        print(f"{self.name} is coding in {self.language}")  # Custom print statement

    def take_break(self, minutes):
        print(f"{self.name} takes a {minutes}-minute break to drink coffee")  # Custom print statement

# Implementing the Janitor class
class Janitor(Worker):
    def __init__(self, name, tool):
        super().__init__(name)  # Calling the parent class constructor
        self.tool = tool  # Adding the tool attribute

    def __str__(self):
        return f"{self.name} uses {self.tool}"  # String representation

    def work(self):
        print(f"{self.name} is fixing pipes with {self.tool}")  # Custom print statement

    def take_break(self, minutes):
        print(f"{self.name} listens to music for {minutes} minutes")  # Custom print statement

# Testing:
# programmer = Programmer("Alice", "Python")
# print(programmer)  # Should print "Alice codes with Python"
# programmer.work()  # Should print "Alice is coding in Python"
# programmer.take_break(10)  # Should print "Alice takes a 10-minute break to drink coffee"

# janitor = Janitor("Bob", "wrench")
# print(janitor)  # Should print "Bob uses wrench"
# janitor.work()  # Should print "Bob is fixing pipes with wrench"
# janitor.take_break(15)  # Should print "Bob listens to music for 15 minutes"

# I think this should work. Let me run the check_2.py script to test it.