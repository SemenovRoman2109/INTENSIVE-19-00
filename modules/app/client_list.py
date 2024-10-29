from customtkinter import CTkScrollableFrame
from .main_window import screen

class ConnectedUsers(CTkScrollableFrame):
    def __init__(self, child_master: object, **kwargs):
        CTkScrollableFrame.__init__(
            self,
            master = child_master,
            width = 322,
            height = 680,
            border_width = 3,
            **kwargs
        )
        self.place(x = 916, y = 25)

list_user = ConnectedUsers(screen)