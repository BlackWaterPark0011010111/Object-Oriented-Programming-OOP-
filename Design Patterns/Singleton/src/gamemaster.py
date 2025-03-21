from game_factory import GameFactory

class GameMaster:
    def __init__(self):
        self.capital = 0  # Банк казино
    
    def host_game(self, game_type):
        game = GameFactory.create_object(game_type)
        if game:
            gains = game.play_game()
            self.capital -= gains  # Казино теряет, если игрок выигрывает
            return gains
        return 0
