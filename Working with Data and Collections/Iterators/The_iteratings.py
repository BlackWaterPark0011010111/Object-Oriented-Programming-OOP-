"""Итерационные таблицы, как следует из названия, используются 
для одной основной цели - итерации.
Существует также целый ряд встроенных 
функций, для которых итерации требуются в качестве 
аргументов.
Список строк может быть итерирован для доступа к 
к каждому из его значений, а функция len
может быть использована для получения значения 
количество элементов в переданной итерируемой таблице 
(в данном случае - строке).
То же самое относится к любому типу 
итерируемых."""
iterables_list = [
    "string", "list", "set",
    "кортеж", "словарь"
]
for item in iterables_list:
     print(item, len(item))

"""string 6
list 4
set 3
tuple 5
dictionary 10
"""
"""Словари - это особый случай, 
поскольку каждый элемент является составным 
ключа и значения.
Итератор словаря выдает только 
ключ.
Это имеет тот же эффект, что и использование метода 
keys метода словаря. Этот 
метод выдает ключ каждого элемента в 
словаря.
Словари имеют и другие методы 
для получения значений

profile = {
     "name": "Mary Schmidt",
     "age": 54
 }
for key in iterables:
     print(key)

name
    age


for key in iterables.keys():
     print(key)

name
age
"""
""" 
Значения метода выдает значения каждого элемента.Метод items выдает кортеж кортеж, содержащий ключ и 
значение каждого элементаЭтот кортеж может быть распакован в 
for value in iterables.values():
     print(value)
той же инструкции for, чтобы сделать код более читабельным

Mary Schmidt
54
for item in iterables.items():
     print(item)

('name', 'Mary Schmidt')
('age', 54)
for key, value in iterables.items():
     print(key, "=>", value)

name => Mary Schmidt
age => 54
"""





"""Другой распространенной схемой является использование кортежей 
вместо словарей для хранения пар ключ-значение
пар, которые должны оставаться постоянными. Это 
можно сделать, определив двумерный 
кортеж (кортеж кортежей).
В результате итерации будет получен кортеж, который можно 
распаковать, как это делается в методе items
метод словаря
"""

days = (
    ('Mon', 'Monday'),
    ('Tue', 'Tuesday'),
    ('Wed', 'Wednesday'),
    ('Thu', 'Thursday'),
    ('Fri', 'Friday'),
     ('Sat', 'Saturday'),
     ('Sun', 'Sunday')
 )
for key, value in days:
     print(key, "=>", value)
"""
Mon => Monday
Tue => Tuesday"""
# continues




"""
В Python есть несколько встроенных функций, которые 
требуют или принимают итерации и могут быть очень 
Список, кортеж, 
dict и set - вот некоторые из них.
Еще одной из наиболее часто используемых функций является 
enumerate.
Функция enumerate принимает любую итерируемую переменную 
и для каждого значения выдает кортеж, содержащий 
позицию этого значения и само значение 
само значение.
"""
list = [
     'Monday',
     'Tuesday',
     'Wednesday',
     'Thursday',
     'Friday',
     'Saturday',
     'Sunday'
 ]
for position, value in enumerate(list):
     print(position, "=>", value)
"""
0 => Monday
1 => Tuesday"""
# continues


"""


Функция enumerate позволяет сделать более простой 
и более читабельный код по сравнению с альтернативой 
добавления счетчика вручную"""
list = [
     'Monday',
     'Tuesday',
     'Wednesday',
     'Thursday',
     'Friday',
     'Saturday',
     'Sunday'
 ]
position = 0
for value in list:
     print(position, "=>", value)
     position += 1
"""
0 => Monday
1 => Tuesday"""
# continues


"""


Функция enumerate позволяет сделать более простой 
и более читабельный код по сравнению с альтернативой 
добавления счетчика вручную"""

list = [
     'Monday',
     'Tuesday',
     'Wednesday',
     'Thursday',
     'Friday',
     'Saturday',
     'Sunday'
 ]
position = 0
for value in list:
     print(position, "=>", value)
     position += 1
"""
0 => Monday
1 => Tuesday
"""


"""

Функция enumerate может даже 
можно использовать даже для итераций, которые дают 
итераторы, например, метод items 
словаря.
Эта итерабельность может быть дополнительно 
распаковать с помощью круглых скобок"""
dict = {
     "name": "Mary Schmidt",
     "age": 54
 }
for position, value in enumerate(dict.items()):
     print(position, "=>", value)

"""0 => ('name', 'Mary Schmidt')
1 => ('age', 54)"""
for pos, (key, val) in enumerate(dict.items()):
     print(pos, ".", key, "=>", val)

"""0 . name => Mary Schmidt
1 . age => 54


"""
"""

Функция zip принимает любое 
количество итераций и возвращает 
объект zip.
Этот объект представляет собой итератор, который 
выдает кортеж со значением в 
в каждой позиции каждой переданной 
итератора.
"""
nums = [1, 2, 3]
eng = ("one", "two", "three")
zip1 = zip(nums, eng)
print(zip1)
#<zip object at 0x7ff4f285cd80>
for item in zip(nums, eng):
     print(item)

(1, 'one')
(2, 'two')
(3, 'three')




"""

Итерабельность любого типа (и любого 
количество) может быть передано в функцию 
функции.
Обратите внимание, что можно передавать и множества 
тоже, но поскольку они не имеют порядка 
элементы извлекаются случайным образом.
Каждый раз, когда мы выполняем этот код 
немецкие слова будут появляться в 
разном порядке
"""
nums = "123"
eng = ("one", "two", "three")
deu = {"ein", "zwei", "drei"}
cat = {"un": 1, "dos": 2, "tres": 3}
fra = ["un", "deux", "trois"]
for item in zip(nums, eng, deu, cat, fra):
     print(item)

('1', 'one', 'zwei', 'un', 'un')
('2', 'two', 'drei', 'dos', 'deux')
('3', 'three', 'ein', 'tres', 'trois')





"""


Предметы также могут быть распаковывать, чтобы обеспечить 
более читабельный код внутри цикла."""

nums = "123"
eng = ("one", "two", "three")
deu = {"ein", "zwei", "drei"}
cat = {"un": 1, "dos": 2, "tres": 3}
fra = ["un", "deux", "trois"]
for num, en, de, ca, fr in zip(nums, eng, deu, cat, 
fra):
    (nums, eng, deu, cat, fra)
    print(num + ". " + en, de, ca, fr)
"""
1. one drei un un
2. two zwei dos deux
3. three ein tres trois

nums = [1, 2, 3, 4, 5]
print(sum(nums), max(nums), min(nums))
15 5 1
nums = {1, 2, 3, 4, 5}
print(sum(nums), max(nums), min(nums))
15 5 1
 nums = [1, 2, 3, 4, "5"]
 print(sum(nums), max(nums), min(nums))
Traceback (most recent call last):
File "/home/DCI/test.py", line 30, in <module>
print(sum(nums), max(nums), min(nums))
TypeError: unsupported operand type(s) for +: 
'int' and 'str'
 nums = ["a", "b", "c", "d", "e"]
 print(max(nums), min(nums))
# -----e a

"""
"""

Функция sorted возвращает новый список в 
алфавитном или числовом порядке. 
Она не изменяет существующий итерируемый список.
Сортировка словаря с помощью sorted вернет 
список с ключами в алфавитном порядке, 
поскольку по умолчанию словарь итерируется 
по ключу.
Получить отсортированный список значений можно 
с помощью метода values.
Он принимает аргумент ключевого слова 
reverse как булево значение, которое по умолчанию равно False
"""
nums = [4, 3, 5, 2, 1]
print(sorted(nums))
[1, 2, 3, 4, 5]
print(nums)
[4, 3, 5, 2, 1]
dict1 = {"c": 2, "b": 1, "a": 3}
print(sorted(dict1))
['a', 'b', 'c']
print(sorted(dict1.values()))
[1, 2, 3]
print(sorted(dict1, reverse=True))
['c', 'b', 'a']

"""
Функция sorted также может быть использована 
для сортировки списков словарей 
списка на основе значений одного из 
ключей этих словарей.
Это можно сделать, передав в качестве ключевого аргумента функцию 
функции в качестве ключевого аргумента. Эта 
функция должна возвращать значение, которое 
которое будет использоваться для сортировки.
"""
dict1 = [
     {"name": "John", "age": 31},
     {"name": "Mary", "age": 46},
     {"name": "Lucy", "age": 25}
 ]
 
by_age = lambda user: user["age"]
by_name = lambda user: user["name"]
print(sorted(dict1, key=by_age))
[{'name': 'Lucy', 'age': 25}, {'name': 'John', 
'age': 31}, {'name': 'Mary', 'age': 46}]
print(sorted(dict1, key=by_name))
[{'name': 'John', 'age': 31}, {'name': 'Lucy', 
'age': 25}, {'name': 'Mary', 'age': 46}]

"""

Некоторые функции используют итерируемые таблицы для возврата значения 
булево значение, указывающее, соответствует ли итерабель 
соответствует определенному условию.
Функция any вернет True только в том случае, если 
любое из значений в итерабельной таблице является 
истинным.
Функция all возвращает True только в том случае, если 
все значения в итерируемой таблице являются истинными.
"""
a_list = [1, True, "Mary", {1, 2}]
print(bool(a_list), any(a_list), all(a_list))
#True True True
a_list = [1, True, "Mary", {}]
print(bool(a_list), any(a_list), all(a_list))
#True True False
a_list = [0, False, "", {}]
print(bool(a_list), any(a_list), all(a_list))
#True False False


"""

Некоторые функции, использующие итерируемые таблицы, возвращают 
булево значение, указывающее, соответствует ли итерабель 
соответствует определенному условию.
Функция any возвращает значение True только в том случае, если 
любое из значений в итерабельной таблице является 
истинным.
Функция all возвращает True только в том случае, если 
все значения в итерируемой таблице являются истинными
"""
a_list = [1, True, "Mary", {1, 2}]
print(bool(a_list), any(a_list), all(a_list))
#True True True
a_list = [1, True, "Mary", {}]
print(bool(a_list), any(a_list), all(a_list))
#True True False
a_list = [0, False, "", {}]
print(bool(a_list), any(a_list), all(a_list))
#True False False


"""
Наиболее распространенные функции в 
Наиболее распространенные функции в функциональном программировании требуют как 
итерабельность и функция.
Так обстоит дело с функцией map, которая 
применяет заданную функцию к каждому 
элементу заданной итерируемой таблицы.
Она возвращает объект map, который представляет собой 
итерируемый объект, содержащий вывод данного 
процесс"""

_list = [1, 2, 3, 4, 5]
by_two = lambda num: num * 2
a_list_by_two = map(by_two, a_list)
print(a_list_by_two)
# <map object at 0x7f11957546d0>
print(list(a_list_by_two))
# [2, 4, 6, 8, 10]




"""Функция filter возвращает итерабельную переменную 
с элементами заданного итерабля 
которые соответствуют условию, заданному в 
функции.
Она возвращает объект filter, который представляет собой 
итерируемый объект, содержащий вывод данного 
процесс"""

nums = [1, 2, 3, 4, 5]
is_odd = lambda num: (num % 2) != 0
odds = filter(is_odd, nums)
print(odds)
#<filter object at 0x7fced01036d0>
print(list(odds))
#[1, 3, 5]


"""


CONSTRUCTORS
- list()
- tuple()
- set()
- dict()
PACKING
- enumerate()
- zip()
REDUCE
- sum()
- max()
- min()
ORDER
- sorted()
BOOLEAN
- any()
- all()
FUNCTIONAL
- map()
- filter()


"""


























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































