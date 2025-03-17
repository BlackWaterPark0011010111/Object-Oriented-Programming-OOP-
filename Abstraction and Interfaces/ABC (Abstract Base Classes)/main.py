from abc import ABC, abstractmethod
print("---------------------------------------------------------1-------")
class Instrument(ABC):
    @abstractmethod
    def play(self):
        pass  #implemented in subclasses


class Guitar(Instrument):
    def play(self):
        return "Strumming the guitar"


class Piano(Instrument):
    def play(self):
        return "Playing the piano keys"


guitar = Guitar()
piano = Piano()
print("Guitar:", guitar.play())
print("Piano:", piano.play())

print("---------------------------------------------------------2-------")
class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def display_info(self):
        pass 
class Book(Product):
    def display_info(self):
        return f"Book: {self.name}, Price: ${self.price:.2f}"

class Electronics(Product):
    def display_info(self):
        return f"Electronics: {self.name}, Price: ${self.price:.2f}"


book = Book("Python Programming", 29.99)
laptop = Electronics("Laptop", 999.99)
print(book.display_info())
print(laptop.display_info())
print("---------------------------------------------------------3-------")
class Question(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def display_question(self):
        pass  
class MultipleChoiceQuestion(Question):
    def __init__(self, text, options):
        super().__init__(text)
        self.options = options

    def display_question(self):
        options_str = "\n".join(self.options)
        return f"{self.text}\n{options_str}"


class TrueFalseQuestion(Question):
    def display_question(self):
        return f"{self.text} (True/False)"


class Quiz:
    def __init__(self):
        self.questions = []
    def add_question(self, question):
        self.questions.append(question)
    def display_quiz(self):
        print("Quiz Questions:")
        for i, question in enumerate(self.questions, 1):
            print(f"Q{i}: {question.display_question()}")

quiz = Quiz()
q1 = MultipleChoiceQuestion("What is the capital of France?", ["A. Paris", "B. London", "C. Berlin"])
q2 = TrueFalseQuestion("Python is a compiled language.",)

quiz.add_question(q1)
quiz.add_question(q2)
quiz.display_quiz()
print("---------------------------------------------------------4------")

class Course(ABC):
    def __init__(self, title, instructor):
        self.title = title
        self.instructor = instructor

    @abstractmethod
    def display_course_info(self):
        pass 

class ProgrammingCourse(Course):
    def display_course_info(self):
        return f"Programming Course: {self.title} by {self.instructor}"


class MathCourse(Course):
    def display_course_info(self):
        return f"Math Course: {self.title} by {self.instructor}"


class LearningPlatform:
    def __init__(self):
        self.courses = []
    def add_course(self, course):
        self.courses.append(course)
    def display_all_courses(self):
        for course in self.courses:
            print(course.display_course_info())


platform = LearningPlatform()
python_course = ProgrammingCourse("Python Basics", "John Doe")
math_course = MathCourse("Algebra 101", "Jane Smith")
platform.add_course(python_course)
platform.add_course(math_course)
print("Available Courses:")
platform.display_all_courses()


print("---------------------------------------------------------5------")
class MenuItem(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def display(self):
        pass 
class Food(MenuItem):
    def display(self):
        return f"Food: {self.name}, Price: ${self.price:.2f}"


class Drink(MenuItem):
    def display(self):
        return f"Drink: {self.name}, Price: ${self.price:.2f}"



class Menu:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def display_menu(self):
        print("Menu:")
        for item in self.items:
            print(item.display())


menu = Menu()
pizza = Food("Pizza", 12.99)
cola = Drink("Cola", 1.99)

menu.add_item(pizza)
menu.add_item(cola)
menu.display_menu()
