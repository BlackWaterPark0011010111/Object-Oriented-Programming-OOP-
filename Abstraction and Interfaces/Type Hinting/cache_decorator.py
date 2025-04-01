from typing import Callable, ParamSpec, TypeVar, Dict, Any
from functools import wraps

T = TypeVar('T')
P = ParamSpec('P')

def cache(func: Callable[P, T]) -> Callable[P, T]:
    _cache: Dict[str, T] = {}

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        key = f"{args}_{kwargs}"
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return wrapper

@cache
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Пример
if __name__ == "__main__":
    print("Fibonacci(10):", fibonacci(10))  # 55 (кэшируется)