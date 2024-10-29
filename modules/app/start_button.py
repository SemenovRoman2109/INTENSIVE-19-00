from customtkinter import CTkButton 
from .main_window import screen

class Button(CTkButton):
    def __init__(self, child_master: object, title: str, command: object = None, **kwargs):
        CTkButton.__init__(
            self = self,
            master = child_master,
            width = 347,
            height = 60,
            text = title,
            command = command,
            border_width = 3,
            **kwargs
        )
        self.place(y = 750, x = 916 )

button_start = Button(child_master = screen, title = "START")
