from customtkinter import CTkFrame
from .main_window import screen

class ClientScreen(CTkFrame):
    def __init__(self, child_master: object, **kwargs):
        CTkFrame.__init__(
            self = self,
            master = child_master,
            width = 866,
            height = 490,
            border_width = 3,
            **kwargs
        )
        self.place(y = 25, x = 25)

screen_user = ClientScreen(child_master = screen)