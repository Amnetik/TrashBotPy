
import customtkinter
from ..Trash.TrashGenerator import *

class ScrollableItems(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.label_list = []

    def add_item(self, key: str, value: str, image=None):
        title = f"{key:>3} - {value}" 
        label = customtkinter.CTkLabel(self, text=title, image=image, compound="left", padx=0)
        label.grid(row=len(self.label_list), column=0, pady=(0, 00), columnspan=1, sticky='w')
        self.label_list.append(label)

    def remove_item(self, item):
        for label in zip(self.label_list):
            if item == label.cget("text"):
                label.destroy()
                self.label_list.remove(label)
                return

class App(customtkinter.CTk):
    def __init__(self, trash_dict: dict[str, TrashGenerator]):
        super().__init__()

        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        self.title("Trashtalk Bot")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        self.trash_dict = trash_dict

        # create scrollable label and button frame
        self.scrollable_label_button_frame = ScrollableItems(master=self, width=300, corner_radius=0)
        self.scrollable_label_button_frame.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
        for trash_key in trash_dict.keys():
            self.scrollable_label_button_frame.add_item(trash_key, trash_dict[trash_key]._name)

if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    app = App()
    app.mainloop()