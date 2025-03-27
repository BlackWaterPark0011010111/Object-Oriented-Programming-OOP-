
from typing import List, Dict, TypeVar, Generic, Optional, TypedDict#здесб мы импортируем  стандартные аннотации типов из модуля typing.
#Generic —  для создания обобщённых (дженерик) классов.
#TypedDict — аннотируем словари с фиксированным набором ключей и типов значений.
# TypedDict — это контракт для словаря. указываем, какие ключи обязательны,фиксируем типы их значений.

#statistics — библиотека для математических операций (например, mean()).
import statistics as stats
#TypeVar('T') он связывает типы в сolumn и dataframe
T = TypeVar('T')# T это абстрактный тип-заполнитель

class Column(TypedDict): #TypedDict- он определяет структуру колонки с именем и данными:
#зжесь проверяет, что в Column передаются только поля name и data.
# то есть это словарь с предопределёнными ключами и типами значений. в name: str — мы указываем чтобы ключ name  был строкой.

    name: str
    data: List[T]#ключ data должен быть списком элементов типа T (определили через typevar)

class DataFrame(Generic[T]):
    """здесь указываем, что класс DataFrame  работает с любым типом через T.
и если написать  dataframe[int] — это значит, все колонки содержат только int.

columns: Dict[str, List[T]] -значит ключи словаря —названия колонок (str).а значения — списки данных типа T (например, list[int])."""
    def __init__(self, columns: Dict[str, List[T]]):#T — это заполнитель для типа данных
        self.columns = columns
    def get_column(self, name: str) -> List[T]:#Возвращаем список данных колонки или пустой список, если колонки нет.list[T] гарантирует, 
        #и аннотация list[t], говорит. что возвращаемое значение будет списком типа T
        return self.columns.get(name, [])

    def mean(self, column: str) -> Optional[float]:#float возвращает либо float либо none
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