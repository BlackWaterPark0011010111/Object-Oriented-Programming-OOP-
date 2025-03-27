from typing import List, Dict, TypeVar, Generic, Optional, TypedDict
import statistics as stats

T = TypeVar('T')

class Column(TypedDict):
    name: str
    data: List[T]

class DataFrame(Generic[T]):
    def __init__(self, columns: Dict[str, List[T]]):
        self.columns = columns
    def get_column(self, name: str) -> List[T]:
        return self.columns.get(name, [])

    def mean(self, column: str) -> Optional[float]:
        data = self.get_column(column)
        if not data or not all(isinstance(x, (int, float)) for x in data):
            return None
        return stats.mean(data)  #ignoretype

if __name__ == "__main__":
    
    df = DataFrame({
        "age": [25, 30, 35],
        "salary": [50000, 60000, 70000]
    })
    print("Mean age:", df.mean("age"))  # 30.0
    print("Mean salary:", df.mean("salary"))  # 60000.0