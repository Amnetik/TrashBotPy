import os

class Game:
    
    games: list['Game'] = []
    selected: 'Game' = None
    
    def __init__(self, name: str, picture: str):
        self.name = name
        self.picture = picture
        Game.games.append(self)
        Game.selected = self if Game.selected is None else Game.selected
        
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return self.name
        
ROCKETLEAGUE = Game('Rocket League', os.path.join(os.path.dirname(__file__), 'UI', 'image', 'rocket_league.png'))
CS2 = Game('Counter Strike 2', os.path.join(os.path.dirname(__file__), 'UI', 'image', 'cs2.png'))