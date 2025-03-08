import keyboard
from ..Trash.TrashGenerator import *

class KeyListener():
    def __init__(self, trash_dict):
        self.trash_dict = trash_dict
        
    def __enter__(self):
        keyboard.hook(self.on_key_event)
        
    def __exit__(self, *args, **kwargs):
        keyboard.unhook(self.on_key_event)
    
    def on_key_event(self, event: keyboard.KeyboardEvent):
        if not event.name in self.trash_dict.keys() or event.event_type == 'up':
            return
        print(f"Key {event.name} {event.event_type} {self.trash_dict.get(event.name, TrashGenerator)}")
        keyboard.press('enter')
        keyboard.write(self.trash_dict[event.name].get_trash())
        keyboard.press('enter')