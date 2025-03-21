from gamemaster import GameMaster
import random
from functools import wraps

print("------------------------Implement a singleton decorator in the singleton_decorator.py---------1-")

def singleton(cls):
    instances = {}
    
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance
print("--------------------------The class must be a singleton.The dice record is a dictionary------2-")

@singleton
class Die:
    def __init__(self):
        self.record = {str(i): (0, 0) for i in range(1, 7)}
        self.total_rolls = 0
    
    def roll(self):
        result = random.randint(1, 6)
        self.total_rolls += 1
        count, _ = self.record[str(result)]
        self.record[str(result)] = (count + 1, (count + 1) / self.total_rolls)
        return result
print("-----------------------complete the classes SumGame and ParityGame-------------------------------3-")

class SumGame:
    def __init__(self):
        self.gains = -10 
        self.die = Die()
    
    def play_game(self):
        total = sum(self.die.roll() for _ in range(4))
        if total in (16, 17):
            self.gains = 0 
        elif total >= 18:
            self.gains = 40  
        return self.gains

class ParityGame:
    def __init__(self):
        self.gains = -10 
        self.die = Die()
    
    def play_game(self):
        rolls = [self.die.roll() for _ in range(3)]
        if all(r % 2 == 0 for r in rolls):
            self.gains = 50  
        return self.gains
print("------------------------------complete the method create_object(game_type)------------------------4-")

class GameFactory:
    @staticmethod
    def create_object(game_type):
        if game_type == "sum":
            return SumGame()
        elif game_type == "parity":
            return ParityGame()
        else:
            raise ValueError("Invalid game type")
print("-------complete the method host_game(game_type)-----------------------------------------------5-")

class GameMaster:
    def __init__(self):
        self.capital = 0 
    
    def host_game(self, game_type):
        game = GameFactory.create_object(game_type)
        self.capital -= game.play_game()
        return game.gains

if __name__ == "__main__":
    master = GameMaster()
    
    print("--- Playing Sum Game ---")
    print("Player's gain:", master.host_game("sum"))
    
    print("--- Playing Parity Game ---")
    print("Player's gain:", master.host_game("parity"))
    
    print("Game Master Capital:", master.capital)
