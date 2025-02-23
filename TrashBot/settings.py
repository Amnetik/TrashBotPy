from enum import Enum

class Game(Enum):
    RocketLeague = 0
    CS2 = 1
    Default = 99

class Settings:
    current_game = Game.RocketLeague