from abc import ABC, abstractmethod


class Tool(ABC):

    @abstractmethod
    def work(self):
        raise NotImplementedError("Abstract Method not implemented")
    
class Laptop(Tool):
    def work(self):
        print("Laptop is running")