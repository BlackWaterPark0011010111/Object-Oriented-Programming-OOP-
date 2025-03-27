
from typing import List, Dict, Tuple, Union, Optional, Set, Callable
import datetime
"""add two integers and return the result."""
print("----------------------------------------------1-----")
def add_numbers(a: int, b: int) -> int:
    return a + b
print("----------------------------------------------2-----")
"""Filter even numbers from a list."""

def filter_even_numbers(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num % 2 == 0]
print("----------------------------------------------3-----")
"""create a person dictionary with type hints."""
def create_person(name: str, age: int, hobbies: Optional[List[str]] = None) -> Dict[str, Union[str, int, List[str]]]:
    return {
        "name": name,
        "age": age,
        "hobbies": hobbies if hobbies else [] 
    }
print("--------------------------------------------4-------")
"""return (latitude, longitude) as a tuple."""

def get_coordinates() -> Tuple[float, float]:
    return (40.7128, -74.0060)  # New York
print("---------------------------------------------5------")
"""process input that can be either string or integer."""
def process_input(value: Union[str, int]) -> str:
    return str(value).upper()
print("----------------------------------------------6-----")
"""simulate a user search (may return None)."""
def find_user(username: str) -> Optional[Dict[str, str]]:
    users = {"alice": {"role": "admin"}, "bob": {"role": "user"}}
    return users.get(username)
print("----------------------------------------------7-----")
"""Return a set of unique words."""
def count_unique_words(words: List[str]) -> Set[str]:
    return set(words)
print("----------------------------------------------8-----")
"""apply a function to two integers."""

def apply_operation(x: int, y: int, operation: Callable[[int, int], int]) -> int:
    return operation(x, y)
print("---------------------------------------------9------")
"""calculate days remaining until New Year."""

def days_until_new_year() -> int:
    today = datetime.date.today()
    new_year = datetime.date(today.year + 1, 1, 1)
    return (new_year - today).days

UserId = int
UserDict = Dict[str, Union[str, List[str]]]
print("----------------------------------------------10-----")

"""fetch user data with custom type aliases."""
def get_user(user_id: UserId) -> UserDict:
    return {"id": user_id, "name": "Alice", "tags": ["python", "coding"]}


if __name__ == "__main__":

    print("1. add_numbers:", add_numbers(3, 5))
    print("2. filter_even_numbers:", filter_even_numbers([1, 2, 3, 4]))
    print("3. create_person:", create_person("Bob", 30, ["hiking"]))
    print("4. get_coordinates:", get_coordinates())
    print("5. process_input:", process_input(42))
    print("6. find_user:", find_user("alice"))
    print("7. count_unique_words:", count_unique_words(["hello", "world", "hello"]))
    print("8. apply_operation (multiply):", apply_operation(3, 4, lambda x, y: x * y))
    print("9. days_until_new_year:", days_until_new_year())
    print("10. get_user:", get_user(123))