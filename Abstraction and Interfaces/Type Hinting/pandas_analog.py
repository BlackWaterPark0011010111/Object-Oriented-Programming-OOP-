from typing import List, Dict, TypeVar, Generic, Optional, TypedDict
# Here we import standard type annotations from the typing module
# Generic - for creating generic classes
# TypedDict - for annotating dictionaries with fixed keys and value types
# TypedDict is a contract for dictionaries. It specifies required keys and their value types.

# statistics - library for mathematical operations (e.g. mean())
import statistics as stats
# TypeVar('T') binds types in Column and DataFrame
T = TypeVar('T')  # T is a generic type placeholder

class Column(TypedDict):  # TypedDict defines a column structure with name and data
    # Here it ensures Column only contains name and data fields
    # It's a dictionary with predefined keys and value types
    # name: str means the 'name' key must be a string
    name: str
    data: List[T]  # data key must be a list of type T (defined via TypeVar)

class DataFrame(Generic[T]):
    """Here we specify that DataFrame works with any type via T.
    If we write DataFrame[int], it means all columns contain only ints.
    
    columns: Dict[str, List[T]] means dictionary keys are column names (str),
    and values are data lists of type T (e.g. list[int])."""
    def __init__(self, columns: Dict[str, List[T]]):  # T is a data type placeholder
        self.columns = columns
    
    def get_column(self, name: str) -> List[T]:
        """Returns column data list or empty list if column doesn't exist.
        List[T] guarantees the return value will be a list of type T"""
        return self.columns.get(name, [])

    def mean(self, column: str) -> Optional[float]:  #кeturns either float or None
        data = self.get_column(column)
        if not data or not all(isinstance(x, (int, float)) for x in data):
            return None
        return stats.mean(data)  # ignoretype

if __name__ == "__main__":
    df = DataFrame({
        "age": [25, 30, 35],
        "salary": [50000, 60000, 70000]
    })
    print("Mean age:", df.mean("age"))  # 30.0
    print("Mean salary:", df.mean("salary"))  # 60000.0