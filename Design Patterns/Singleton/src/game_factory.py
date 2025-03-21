from game import SumGame, ParityGame

class GameFactory:
    @staticmethod
    def create_object(game_type):
        if game_type == "sum":
            return SumGame()
        elif game_type == "parity":
            return ParityGame()
        else:
            print("Invalid game type")
            return None
