from customtkinter import CTkScrollableFrame
from .main_window import screen

class Console(CTkScrollableFrame):
    def __init__(self, childe_master:object, **kwargs ):
        CTkScrollableFrame.__init__(
            self,
            childe_master,
            width= 841,
            height= 258,
            border_width= 3,
            **kwargs
        )
        self.place(x= 25,y= 540)
        
console = Console(childe_master=screen)