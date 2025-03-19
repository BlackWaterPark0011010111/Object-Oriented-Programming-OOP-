from worker import Programmer, Janitor

def test_programmer():
    programmer = Programmer("Alice", "Python")
    print(programmer)  #выводит alice codes with Python
    programmer.work()  # alice is coding in Python
    programmer.take_break(10)  # alice is taking a 10-minute coffee break

def test_janitor():
    janitor = Janitor("Bob", "Wrench")
    print(janitor)  # bob uses Wrench
    janitor.work()  # bob is fixing pipes with Wrench
    janitor.take_break(5)  # bob is listening to music for 5 minutes

if __name__ == "__main__":
    print("Testing Programmer class:")
    test_programmer()
    
    print("\nTesting Janitor class:")
    test_janitor()
