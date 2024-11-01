import PIL.Image
from customtkinter import CTkLabel, CTkImage
from .main_window import screen
import os
import PIL

class ClientScreen(CTkLabel):
    def __init__(self, child_master: object, **kwargs):
        CTkLabel.__init__(
            self = self,
            master = child_master,
            width = 866,
            height = 490,
            image = self.load_image(),
            text = "",
            **kwargs
        )
        self.place(y = 25, x = 25)
    def load_image(self):
        image_path = os.path.abspath(__file__ + "/../../../images/1.png")
        image = PIL.Image.open(image_path)
        return CTkImage(light_image = image, size = (866, 490))


screen_user = ClientScreen(child_master = screen)