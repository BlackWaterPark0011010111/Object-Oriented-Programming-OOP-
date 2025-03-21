import random
from singleton_decorator import singleton

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
