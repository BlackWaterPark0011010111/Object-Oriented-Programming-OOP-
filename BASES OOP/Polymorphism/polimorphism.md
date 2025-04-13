Параметрический (истинный) и ad-hoc - мнимый

Чтото многообразное, в чем много форм, можно воспринимать как некий принцип  который позволяет одному и тосцу же фрагменту кода работать с разными типами данных.
если у нас есть один класс но в нем методы но разные типы. например если первый работает с числовым сложение а второй со строковым, то для определения какой именно метод нам нужен, то и записывать данные для вывода нам нужно именно с тем методом с которым мы хотим работать. это перегрузка методов , и это считаеться мнимый
```class Calculator:
    def add(self, a, b):
        if isinstance(a, str) and isinstance(b, str):
            return a + b  # string concatenation
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b  # numeric addition
        else:
            raise TypeError("Cannot add objects of different or unsupported types!")

calc = Calculator()
print(calc.add(2, 3))          ---> 5 
print(calc.add("hi", " there"))   ---> "hi there" (strings)
# print(calc.add("hi", 2))       ---> TypeError: Cannot add objects of different or unsupported types!
```


