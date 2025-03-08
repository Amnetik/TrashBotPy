from TrashBot import *
from TrashBot.UI.main_menu import App
from TrashBot.UI.key_manager import KeyListener

trash_rocket_league: dict[str, TrashGenerator] = {
    '1' : TrashGeneratorByList('What a save', 'what_a_save.txt'),
    '2' : TrashGeneratorByList('Nice shot', 'nice_shot.txt'),
    '3' : TrashGeneratorByList('GG', 'gg.txt'),
    '4' : TrashGeneratorByList('GG', 'gg.txt'),
    '5' : TrashGeneratorByList('GG', 'gg.txt'),
    '6' : TrashGeneratorByList('GG', 'gg.txt'),
    '7' : TrashGeneratorByList('Light insult', 'light_insult.txt'),
    '8' : TrashGeneratorByList('Medium insult', 'medium_insult.txt'),
    '9' : TrashGeneratorByList('Hard insult', 'gg.txt')
}

with KeyListener(trash_rocket_league):
    app = App(trash_rocket_league)
    app.mainloop()

