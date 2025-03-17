# Простой декоратор для логирования
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"func  {func.__name__} with arguments {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(2, 3)) 

#для замера времени выполнения
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"func {func.__name__} made4 {end - start:.4f} sec.")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)

slow_function()  

# with arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()  # Вывод: Hello! Hello! Hello!

#  Декоратор для кэширования результатов
def cache(func):
    cached_results = {}
    def wrapper(*args):
        if args in cached_results:
            return cached_results[args]
        result = func(*args)
        cached_results[args] = result
        return result
    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Вывод: 55 (результат кэшируется)

#  Декоратор для проверки прав доступа
def check_access(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if role == "admin":
                return func(*args, **kwargs)
            else:
                raise PermissionError("Доступ запрещён")
        return wrapper
    return decorator

@check_access("admin")
def sensitive_operation():
    return "Важные данные"

print(sensitive_operation())  

#Декоратор с использованием @wraps для сохранения 
from functools import wraps

def preserve_metadata(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@preserve_metadata
def example():
    """Это пример функции."""
    pass

print(example.__name__)  # example
print(example.__doc__)   #  Это пример функции.