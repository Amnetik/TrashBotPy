import keyboard

from Trash import *

trash_rocket_league: dict[str, TrashGeneratorByList] = {
    '1' : TrashGeneratorByList('what_a_save.tl'),
    '2' : TrashGeneratorByList('nice_shot.tl'),
    '3' : TrashGeneratorByList('gg.tl')
}

def on_key_event(event: keyboard.KeyboardEvent):
    if not event.name in trash_rocket_league.keys() or event.event_type == 'up':
        return
    print(f"Key {event.name} {event.event_type} {trash_rocket_league.get(event.name, TrashGenerator)}")
    keyboard.press('enter')
    keyboard.write(trash_rocket_league[event.name].get_trash())
    keyboard.press('enter')

keyboard.hook(on_key_event)  # Hook function to listen to all key events

print('Running..')

keyboard.wait('esc')  # Keep running until 'esc' is pressed