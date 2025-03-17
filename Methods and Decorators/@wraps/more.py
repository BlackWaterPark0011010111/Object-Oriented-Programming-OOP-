
def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice")) 
def retry(max_attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
            raise Exception("All attempts failed")
        return wrapper
    return decorator

@retry(max_attempts=3)
def risky_operation():
    import random
    if random.random() < 0.5:
        raise ValueError("Something went wrong!")
    return "Success!"

print(risky_operation()) 

def validate_args(func):
    def wrapper(*args, **kwargs):
        if all(isinstance(arg, int) for arg in args):
            return func(*args, **kwargs)
        else:
            raise TypeError("All arguments must be integers")
    return wrapper

@validate_args
def add_numbers(a, b):
    return a + b

print(add_numbers(2, 3)) 
# print(add_numbers(2, "3"))  

#to count function calls
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"{func.__name__} has been called {wrapper.calls} times.")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_calls
def say_hello():
    print("Hello!")

say_hello()  # say_hello has been called once -> Hello!
say_hello()  # say_hello has been called twice -> Hello!

#to add a prefix to the function output
def add_prefix(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{prefix} {result}"
        return wrapper
    return decorator

@add_prefix("INFO:")
def log_message(message):
    return message
 # Out INFO: This is a log message.


def enforce_return_type(return_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, return_type):
                raise TypeError(f"Return value must be of type {return_type}")
            return result
        return wrapper
    return decorator

@enforce_return_type(str)
def get_message():
    return "This is a string."

print(get_message())  # Out: This is a string.
# @enforce_return_type(int)
# def get_message():
#     return "This is a string."  # Raises TypeError: Return value must be of type <class 'int'>