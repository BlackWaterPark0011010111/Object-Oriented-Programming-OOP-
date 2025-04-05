# Класс игры
class Game:
    def __init__(self, name, price):  
        self.name = name  
        self.price = price 
        self.is_bought = False  #куплена ли игра, по умолчанию False  whether the game is purchased, default is False

    def buy(self):  #метод для покупки   method for purchasing
        if not self.is_bought:  #если игра ещё не куплена  if the game is not purchased yet
            self.is_bought = True  #меняем статус на "куплено"  change the status to "purchased"
            print(f"Game '{self.name}' was purchased for {self.price} rubles!")
        else:
            print(f"Game '{self.name}' has already been purchased!") 

    def __str__(self):  #для вывода информации об игре to display information about the game
        return f"Game: {self.name}, Price: {self.price} rub., Purchased: {'Yes' if self.is_bought else 'No'}"

# Класс пользователя  user class
class User:
    def __init__(self, username, balance=0):  #имя пользователя и баланс username and balance
        self.username = username  #имя пользователя user name
        self.balance = balance  #баланс (деньги на счету) balance (money on u`re accaunt`)
        self.library = []  #библиотека игр (тут будут купленные игры) games library (purchased games will be here)

    def add_money(self, amount):  #метод для пополнения баланса  method for replenishing the balance
        if amount > 0:  #если сумма положительная if the sum is positive
            self.balance += amount  #добавляем деньги  add money
            print(f"Balance replenished by {amount} rubles. Now you have {self.balance} rubles.")
        else:
            print("The sum must be greater than zero!") #if the sum is negative or zero

    def buy_game(self, game):  #метод для покупки игры  method for purchasing a game
        if game.is_bought:  #если игра уже куплена   if the game is already purchased
            print(f"Game '{game.name}' has already been purchased!")        
        elif self.balance >= game.price:  #если денег хватает  if you have enough money
            self.balance -= game.price  #списываем деньги write off money
            game.buy()  #вызываем метод buy у игры  call the game's buy method
            self.library.append(game)  #добавляем игру в библиотеку add game to library
            print(f"Game '{game.name}' added to your library!")
        else:
            print(f"Not enough money to buy game '{game.name}'!") #if no money
    def show_library(self):  #смотрим библиотеку игр CHECKING THE GAME LIBRARY
        if not self.library:  #если библиотека пуста iflibrary is empty
            print("Your games library is empty :(") #u`re lib is empty`
        else:
            print("U`re game library:")
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