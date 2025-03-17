#The main topic
print("==================================================================1===")
# по компонентам (Processor, RAM, HardDrive) —  должны быть отдельные классы, которые можно использовать независимо.
#мы присоединяем другие классы и один объект состоит из других объектов. Вместо наследования от класса,  создаем его экземпляр внутри другого класса.
class Processor:
    def __init__(self, brand, cores):
        self.brand = brand
        self.cores = cores
    def info(self):
        return f"PROCESSOR : {self.brand}, {self.cores} CORES"



class RAM:
    def __init__(self, size):
        self.size = size
    def info(self):
        return f"RAM: {self.size}GB"



class HardDrive:
    def __init__(self, capacity):
        self.capacity = capacity

    def info(self):
        return f"STORAGE: {self.capacity}GB"

# не наследуем класс Computer от этих классов,потому что он должен содержать их внутри себя (композиция)
# мы можнм модифицировать этот класс, меняя компоненты.
class Computer:
    def __init__(self, processor, ram, hard_drive):
        self.processor = processor  # содержание процессора   композиция
        self.ram = ram  #оперативная память                   композиция
        self.hard_drive = hard_drive  #харды                  композиция

    def show_specs(self):
        print(self.processor.info())
        print(self.ram.info())
        print(self.hard_drive.info())


#Cоздаем компоненты
cpu = Processor("INTEL i5", 4)# Создание компонентов
ram = RAM(8)
storage = HardDrive(256)


my_pc = Computer(cpu, ram, storage)# Cобираем все вместе 

#характеристика
my_pc.show_specs()


print("==================================================================2===")
class Engine:    
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "ENGINE STARTED!"

class Car:
    def __init__(self, model, engine_power):
        self.model = model
        self.engine = Engine(engine_power)  # композиция

    def drive(self):
        return f"{self.model} IS DRIVING WITH {self.engine.horsepower} HP!"

my_car = Car("Tesla", 400)
print(my_car.engine.start())  
print(my_car.drive())
print("==================================================================3===")
class Screen:
    def display(self):
        return "SHOWING ON SCREEN"

class Keyboard:
    def type(self):
        return "TYPING......"

class Laptop:
    def __init__(self):
        self.screen = Screen()  # композиция
        self.keyboard = Keyboard()#композиция

    def use(self):
        return f"{self.screen.display()} | {self.keyboard.type()}"

# И вывод характеристики
my_laptop = Laptop()
print(my_laptop.use()) 