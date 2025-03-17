"""Декоратор — это функция, которая принимает другую функцию и возвращает её модифицированную версию. Декораторы нужны, чтобы добавлять какое-то дополнительное поведение к функциям, не меняя их код. Например, можно добавить логирование, замер времени выполнения или проверку прав доступа.
Проблема с декораторами,когда я создаю декоратор, он заменяет оригинальную функцию своей внутренней функцией-обёрткой (wrapper). 
Из-за этого теряются метаданные оригинальной функции, такие как её имя (__name__) и документация (__doc__). Это может быть проблемой, особенно при отладке.
Решение: @wraps из functools. Чтобы сохранить метаданные оригинальной функции, нужно использовать декоратор @wraps из модуля functools. Он копирует имя, документацию и другие атрибуты оригинальной функции в функцию-обёртку. Это помогает избежать проблем с отладкой и делает код более читаемым.

Декоратор без @wraps: создаю функцию my_decorator, которая добавляет вывод до и после вызова функции.Применил её к функции say_hello.После вызова say_hello её имя и документация потерялись. Вместо имени функции выводится wrapper, а документация становится None.
Декоратор с @wraps: создаю функцию my_decorator_with_wraps, которая использует @wraps(func).Применяю её к функции say_goodbye.
После вызова say_goodbye её имя и документация сохранились.по выводу без @wraps say_hello.__name__ выводит wrapper, а say_hello.__doc__ выводит None.С @wraps:
say_goodbye.__name__ выводит say_goodbye, а say_goodbye.__doc__ выводит документацию.
"""
from functools import wraps

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"b4 calling a func {func.__name__}")
        result = func(*args, **kwargs)
        print(f"after calling a func {func.__name__}")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    """just says hello"""
    print(f"hello, {name}!")

say_hello("Jack")

print(say_hello.__name__)
print(say_hello.__doc__)

def my_decorator_with_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"b4 calling a func {func.__name__}")
        result = func(*args, **kwargs)
        print(f"after calling a func {func.__name__}")
        return result
    return wrapper

@my_decorator_with_wraps
def say_goodbye(name):
    """just says hello"""
    print(f"Bye, {name}!")

say_goodbye("me")

print(say_goodbye.__name__)
print(say_goodbye.__doc__)