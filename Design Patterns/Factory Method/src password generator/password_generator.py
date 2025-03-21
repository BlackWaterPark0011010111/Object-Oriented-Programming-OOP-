import random

#базовый класс для всех генераторов паролей
class PasswordGenerator:
    def generate(self, length):
        raise NotImplementedError("этот метод должен быть переопределён в дочерних классах")

#генератор паролей, использующий только буквы
class AlphaGenerator(PasswordGenerator):
    def generate(self, length):
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return "".join(random.choice(letters) for _ in range(length))

#генератор паролей, использующий буквы и цифры
class AlphaNumericGenerator(PasswordGenerator):
    def generate(self, length):
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        return "".join(random.choice(chars) for _ in range(length))
