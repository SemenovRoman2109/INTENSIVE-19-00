import customtkinter as ctk
app_width, app_height = 1280, 832

screen = ctk.CTk()
screen.title('Project')

x = screen.winfo_screenwidth() // 2 - app_width // 2
y = screen.winfo_screenheight() // 2 - app_height // 2

screen.geometry(f"{app_width}x{app_height}+{x}+{y}")