import socket

client_socket = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
#підключаємо клієнта до серверу
client_socket.connect(("127.0.0.1", 8080))
# Вiдправляє закодованi данi на сервер
client_socket.send("HI server".encode())