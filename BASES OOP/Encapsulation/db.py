#class Database:
#    def __init__(self):
#        self.__tables = []  # Приватный список таблиц
#
#    # Геттер для получения списка таблиц (без возможности изменения)
#    def get_tables(self):
#        return self.__tables.copy()  # Возвращаем копию, чтобы исходный массив нельзя было изменить извне
#
#    # Метод для добавления таблицы (единственный способ изменения списка)
#    def add_table(self, table):
#        self.__tables.append(table)
#
#    # Метод для удаления таблицы (если потребуется)
#    def remove_table(self, table):
#        if table in self.__tables:
#            self.__tables.remove(table)
#db = Database()
##db.__tables = []  # Ошибка! Нельзя изменить приватное поле
#db.add_table("users")  # Добавляем таблицу "users" только через метод add_table

class DatabaseManager:
    def __init__(self):
        # Приватный список таблиц, инициализируется пустым массивом
        self.__tables = []
    
    # Геттер для получения списка таблиц (без возможности изменения)
    @property
    def tables(self):
        # Возвращаем копию списка, чтобы оригинал нельзя было изменить извне
        return self.__tables.copy()
    
    # Метод для добавления новой таблицы
    def add_table(self, table_name):
        if isinstance(table_name, str) and table_name not in self.__tables:
            self.__tables.append(table_name)
    
    # Метод для удаления таблицы
    def remove_table(self, table_name):
        if table_name in self.__tables:
            self.__tables.remove(table_name)


# Пример использования
db = DatabaseManager()

# Попытка прямого доступа к таблицам (не сработает)
try:
    db.__tables = ["users"]  # Не получится изменить
except AttributeError as e:
    print(f"Ошибка: {e}")

# Добавляем таблицы через специальный метод
db.add_table("users")
db.add_table("products")

# Получаем список таблиц (только для чтения)
current_tables = db.tables
print(f"Текущие таблицы: {current_tables}")  # ['users', 'products']

# Попытка изменить список таблиц через геттер (не сработает)
current_tables.append("orders")  # Добавление не повлияет на внутренний список
print(f"Таблицы после попытки изменения: {db.tables}")  # ['users', 'products']

# Удаление таблицы через специальный метод
db.remove_table("products")
print(f"Таблицы после удаления: {db.tables}")  # ['users']