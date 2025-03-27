
from typing import List, Dict, Tuple, Union, Optional, Set, Callable
import datetime

def add_numbers(a: int, b: int) -> int:
    return a + b

def filter_even_numbers(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num % 2 == 0]

def create_person(name: str, age: int, hobbies: Optional[List[str]] = None) -> Dict[str, Union[str, int, List[str]]]:
    return {
        "name": name,
        "age": age,
        "hobbies": hobbies if hobbies else [] 
    }

def get_coordinates() -> Tuple[float, float]:
    return (40.7128, -74.0060)  # New York

def process_input(value: Union[str, int]) -> str:
    return str(value).upper()

def find_user(username: str) -> Optional[Dict[str, str]]:
    users = {"alice": {"role": "admin"}, "bob": {"role": "user"}}
    return users.get(username)

def count_unique_words(words: List[str]) -> Set[str]:
    return set(words)

def apply_operation(x: int, y: int, operation: Callable[[int, int], int]) -> int:
    return operation(x, y)

def days_until_new_year() -> int:
    today = datetime.date.today()
    new_year = datetime.date(today.year + 1, 1, 1)
    return (new_year - today).days

UserId = int
UserDict = Dict[str, Union[str, List[str]]]

def get_user(user_id: UserId) -> UserDict:
    """Fetch user data with custom type aliases."""
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