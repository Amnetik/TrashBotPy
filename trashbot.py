from TrashBot import *
#from TrashBot.UI.GraphicalInterface import App
from TrashBot.UI.KeyListener import KeyListener
import keyboard

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
    while True:
        message = KeyListener.fifo_queue.get()
        keyboard.press('enter')
        keyboard.write(message)
        keyboard.press('enter')


