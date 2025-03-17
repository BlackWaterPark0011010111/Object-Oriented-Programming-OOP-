from enum import Enum

class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    NON_BINARY = "Non-binary"
    OTHER = "Other"

class Author:
    def __init__(self, name: str, email: str, gender: Gender):
        self._name = name
        self._email = email
        self._gender = gender
    
    def get_name(self):
        return self._name
    
    def get_email(self):
        return self._email
    
    def set_email(self, email: str):
        self._email = email
    
    def get_gender(self):
        return self._gender
    
    def __str__(self):
        return f"Author[name={self._name},email={self._email},gender={self._gender.value}]"

class Book:
    def __init__(self, name: str, author: Author, price: float, qty: int = 1):
        self._name = name
        self._author = author
        self._price = price
        self._qty = qty
    
    def get_name(self):
        return self._name
    
    def get_author(self):
        return self._author
    
    def get_price(self):
        return self._price
    
    def set_price(self, price: float):
        self._price = price
    
    def get_qty(self):
        return self._qty
    
    def set_qty(self, qty: int):
        self._qty = qty
    
    def get_author_name(self):
        return self._author.get_name()
    
    def get_author_email(self):
        return self._author.get_email()
    
    def __str__(self):
        return f"Book[name={self._name},{str(self._author)},price={self._price},qty={self._qty}]"

#  тесты
if __name__ == "__main__":
    author1 = Author("J.K. Rowling", "jk.rowling@email.com", Gender.FEMALE)
    author2 = Author("George R.R. Martin", "grrm@email.com", Gender.MALE)
    
    print(author1)
    print(author2)
    
    author1.set_email("new.email@domain.com")
    print(author1)
    
    book1 = Book("Harry Potter", author1, 29.99, 100)
    book2 = Book("A Game of Thrones", author2, 39.99, 50)
    
    print(book1)
    print(book2)
    
    book1.set_price(24.99)
    book1.set_qty(120)
    
    print(book1)
    
    print("Author's name is: " + book1.get_author_name())
    print("Author's email is: " + book1.get_author_email())