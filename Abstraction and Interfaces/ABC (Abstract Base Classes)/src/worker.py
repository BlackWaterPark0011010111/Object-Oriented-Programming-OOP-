from abc import ABC, abstractmethod


class Worker(ABC):
    def __init__(self, name):
        self.name = name  

    @abstractmethod
    def work(self): #реализуем в подклассах

        pass 
    @abstractmethod
    def take_break(self, minutes):
        pass  

class Programmer(Worker):
    def __init__(self, name, language):
        super().__init__(name)  #вызываем конструктор 
        self.language = language  #дополнительный атрибут - язык программирования

    def __str__(self):
        return f"{self.name} codes with {self.language}"
    def work(self):
        print(f"{self.name} is coding in {self.language}.")
    def take_break(self, minutes):
        print(f"{self.name} is taking a {minutes}-minute coffee break.")


class Janitor(Worker):
    def __init__(self, name, tool):
        super().__init__(name)  #наследуем имя
        self.tool = tool  #дополнительный атрибут инструмент

    def __str__(self):
        return f"{self.name} uses {self.tool}"
    def work(self):
        print(f"{self.name} is fixing pipes with {self.tool}.")
    def take_break(self, minutes):
        print(f"{self.name} is listening to music for {minutes} minutes.")