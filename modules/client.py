import socket

with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as client_socket:
    #підключаємо клієнта до серверу
    client_socket.connect(("", 8081))
    # Вiдправляє закодованi данi на сервер
    client_socket.send("Hello server".encode())