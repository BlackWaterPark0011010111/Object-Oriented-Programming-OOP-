"""
Они придают дополнительную функциональность существующим 
функции, не изменяя их.
Декораторы

make_pretty() - это декоратор, который печатает некоторый текст 
перед выполнением переданной ему функции.
Закрытие, использующее функцию в качестве аргумента и 
выполняет (или не выполняет) вложенную функцию.
Декораторы - это способ добавить определенную функциональность в 
нашим функциям. Сами по себе они также являются функциями.
Мы можем временно применить декоратор в новой 
имя переменной, просто вызвав его и передав 
функцию, которую мы хотим украсить."""

def make_pretty(func):
    def inner():
        print("im pretty")
    func()
    return inner

def ordinary():
    print("Hello World!")

ordinary()
#Hello World!
pretty = make_pretty(ordinary)
pretty()
#im pretty
#Hello World!




"""

Наши функции могут быть постоянно украшены, если 
предваряя их определения словами 
@имя_декоратора.
Сокращение
Это эквивалентно выполнению приветствия = 
make_uppercase(greeting) сразу после 
определения приветствия
"""
def make_uppercase(func):

    def inner():
        return func().upper()
    return inner


@make_uppercase

def greeting():

    return "Hello World!"


print( greeting() )
#HELLO WORLD!


"""

Декораторы будут применяться, начиная с ближайшего к определению, в данном случае @make_split.Множественные
декораторыСначала мы разбиваем предложение на список слов и 
затем подсчитаем полученный список. В нашем предложении 2слова.Инвертирование декораторов приведет к подсчету 
символов в строке, преобразовать их в текст и разделит этот текст на список, вернув ['12'].
"""
def make_count(func):
    def inner():
        return str(len(func()))
    return inner 
def make_split(func):
    def inner():
        return func().split()
    return inner


@make_count

@make_split

def ordinary():

    return "Hello World!"


print( ordinary() )
2


"""

Если декорируемая функция имеет параметры мы должны включить их во внутреннюю функцию декоратора
и включить их в вызов func.Использование аргументов функцииМы можем оперировать или не оперировать этими аргументами"""

def make_capitalized(func):
    def inner(*args):
        capitalized = [w.capitalize() 
                       for w in args]
        return func(*capitalized)
    return inner
@make_capitalized
def greeting(first, last):
    return f"Hello, {first} {last}!"
print( greeting("jAMES", "bROWN") )
# Hello, James Brown!

"""



Использование аргументов декоратораНам необходимо обернуть еще одну функцию 
для хранения аргументов декоратора декоратора.Использование аргументов декоратораИ вернуть внутренний декоратор.
Теперь мы можем указать, какие из аргументов ключевого слова функции мы следует писать заглавными буквами"""


def make_capitalized(*deco_args):
    def decorator(func):
        def inner(**kwargs):
            data = []
            for k, w in kwargs.items():
                if k in deco_args:
                    data.append(w.capitalize())
                else:
                    data.append(w)
            return func(*data)
        return inner
    return decorator

@make_capitalized("first")
def greeting(first, last):
    return f"Hello, {first} {last}!"

print( greeting(first="jAMES", last="bROWN") )
# Hello, James bROWN!
































































































































































































































































































































































































































































































































































































































































































