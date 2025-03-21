from die import Die

class SumGame:
    def __init__(self):
        self.gains = -10 
        
        self.die = Die()
    
    def play_game(self):
        rolls = [self.die.roll() for _ in range(4)]
        total = sum(rolls)
        print(f"Rolls: {rolls}, Sum: {total}")

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
        print(f"Rolls: {rolls}")

        if all(r % 2 == 0 for r in rolls):
            self.gains = 50
        return self.gains
