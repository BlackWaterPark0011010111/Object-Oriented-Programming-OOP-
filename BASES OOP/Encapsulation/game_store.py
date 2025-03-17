# Класс игры
class Game:
    def __init__(self, name, price):  
        self.name = name  
        self.price = price 
        self.is_bought = False  #куплена ли игра, по умолчанию False

    def buy(self):  #метод для покупки 
        if not self.is_bought:  #если игра ещё не куплена
            self.is_bought = True  #меняем статус на "куплено"
            print(f"Игра '{self.name}' куплена за {self.price} рублей!")
        else:
            print(f"Игра '{self.name}' уже куплена!")  

    def __str__(self):  #для вывода информации об игре
        return f"Игра: {self.name}, Цена: {self.price} руб., Куплена: {'Да' if self.is_bought else 'Нет'}"


# Класс пользователя
class User:
    def __init__(self, username, balance=0):  #имя пользователя и баланс
        self.username = username  #имя пользователя
        self.balance = balance  #баланс (деньги на счету)
        self.library = []  #библиотека игр (тут будут купленные игры)

    def add_money(self, amount):  #метод для пополнения баланса
        if amount > 0:  #если сумма положительная
            self.balance += amount  #добавляем деньги
            print(f"Баланс пополнен на {amount} руб. Теперь у вас {self.balance} руб.")
        else:
            print("Сумма должна быть больше нуля!")  #если сумма отрицательная или ноль

    def buy_game(self, game):  #метод для покупки игры
        if game.is_bought:  #если игра уже куплена
            print(f"Игра '{game.name}' уже куплена!")
        elif self.balance >= game.price:  #если денег хватает
            self.balance -= game.price  #списываем деньги
            game.buy()  #вызываем метод buy у игры
            self.library.append(game)  #добавляем игру в библиотеку
            print(f"Игра '{game.name}' добавлена в вашу библиотеку!")
        else:
            print(f"Недостаточно денег для покупки игры '{game.name}'!")  #если денег нет

    def show_library(self):  #смотрим библиотеку игр
        if not self.library:  #если библиотека пуста
            print("Ваша библиотека игр пуста :(")
        else:
            print("Ваша библиотека игр:")
            for game in self.library:  #перебираем игры в библиотеке
                print(f"- {game.name}")

    def __str__(self):   #для вывода информации о юзере
        return f"Пользователь: {self.username}, Баланс: {self.balance} руб."


game1 = Game("The Witcher 3", 1500)  #создаём Ведьмак 
game2 = Game("Cyberpunk 2077", 2000)  #создаём  Киберпанк 2077
game3 = Game("Minecraft", 1000)  #создаём  Майнкрафт


user = User("Gamer123", 3000)  #создаём пользователя с именем "Gamer123" и балансом 3000 руб.

#информация о пользователе
print(user)

# Покупаем игры
user.buy_game(game1)  #покупаем Ведьмак 
user.buy_game(game2)  #пытаемся купить Киберпанк, но денег не хватит
user.add_money(1000)  #пополняем баланс на 1000
user.buy_game(game2)  #теперь покупаем Киберпанк 2077
user.buy_game(game3)  #покупаем "Майнкрафт"

#  библиотека игр
user.show_library()

# Пытаемся купить игру ещё раз
user.buy_game(game1)  # игра уже куплена

# итог
print(user)