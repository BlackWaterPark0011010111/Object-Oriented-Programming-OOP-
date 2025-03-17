#Дублирование в функциях
def calculate_area_of_square(side: float) -> float:
    return side * side
def calculate_area_of_rectangle(length: float, width: float) -> float:
    return length * width

def calculate_area_of_circle(radius: float) -> float:
    return 3.14 * radius * radius
print("--------------------------------------------------------------------")
class Square:
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side * self.side

class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius * self.radius


print("------------------------Рефакторинг с использованием DRY---------------")


class Shape:
    def area(self) -> float:
        raise NotImplementedError("Подклассы должны реализовать этот метод")

# подклассы которые реализуют  area()метод.
class Square(Shape):
    def __init__(self, side: float):
        self.side = side
    def area(self) -> float:
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width
    def area(self) -> float:
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    def area(self) -> float:
        return 3.14 * self.radius * self.radius


print ("------------------------------------------Использование композиции для DRY-----")
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
    def display_info(self) -> str:
        
        return f"User: {self.name}, Email: {self.email}"

# Вместо того чтобы дублировать код используем композицию.
class Admin:
    def __init__(self, user: User, access_level: str):
        self.user = user
        self.access_level = access_level
    def display_info(self) -> str:
        return f"Admin: {self.user.name}, Access Level: {self.access_level}"

user = User("Alice", "alice@example.com")
admin = Admin(user, "Superuser")
print(user.display_info())
print(admin.display_info()) 

print("---------------------------------------------------------------decorators-------")

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} завершена")
        return result
    return wrapper

@log_function_call
def calculate_sum(a: int, b: int) -> int:
    return a + b
@log_function_call
def calculate_product(a: int, b: int) -> int:
    return a * b

#  логирование не дублируется в каждой функции.
print(calculate_sum(10, 20)) 
print(calculate_product(5, 6)) 

print( " -------------------------------------------------Расчет зарплаты для разных типов сотрудников------")

class Employee:
    def __init__(self, name: str, base_salary: float):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self) -> float:
        raise NotImplementedError("Подклассы должны реализовать этот метод")

class Manager(Employee):
    def calculate_salary(self) -> float:
        return self.base_salary + 1000  # Бонус 

class Developer(Employee):
    def calculate_salary(self) -> float:
        return self.base_salary + 500  # Бонус 

manager = Manager("Alice", 5000)
developer = Developer("Bob", 4000)
print(f"Manager Salary: {manager.calculate_salary()}")  #6000
print(f"Developer Salary: {developer.calculate_salary()}")  # 4500

#по  нарушениям DRY

#  Дублирование для функций
# def calculate_area_of_square(side: float) -> float:
#     return side * side
## def calculate_area_of_rectangle(length: float, width: float) -> float:
#     return length * width
## def calculate_area_of_circle(radius: float) -> float:
#     return 3.14 * radius * radius



# Дублирование в классах
# class Square:
#     def __init__(self, side: float):
#         self.side = side
##     def area(self) -> float:
#         return self.side * self.side
## class Rectangle:
#     def __init__(self, length: float, width: float):
#         self.length = length
#         self.width = width
##     def area(self) -> float:
#         return self.length * self.width
#
# class Circle:
#     def __init__(self, radius: float):
#         self.radius = radius
#
#     def area(self) -> float:
#         return 3.14 * self.radius * self.radius

#  TODO: Задачи для дальнейшего улучшения


# TODO: Добавить поддержку других фигур (треугольник, ромб и т.д.)
# TODO: Реализовать систему бонусов для сотрудников на основе их рейтинга
# TODO: Добавить больше декораторов для логирования и проверки данных
