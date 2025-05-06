import keyboard
import queue
from ..Trash.TrashGenerator import *

class KeyListener():
    fifo_queue: queue.Queue = queue.Queue()
    
    def __init__(self, trash_dict: dict[str, TrashGenerator]):
        self.trash_dict: dict[str, TrashGenerator] = trash_dict
        
    def __enter__(self):
        keyboard.hook(self.on_key_event)
        
    def __exit__(self, *args, **kwargs):
        keyboard.unhook(self.on_key_event)
    
    def on_key_event(self, event: keyboard.KeyboardEvent):
        if not event.name in self.trash_dict.keys() or event.event_type == 'up':
            return
        KeyListener.fifo_queue.put(self.trash_dict[event.name].get_trash())

                