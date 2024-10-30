import socket

# створили socket для передачи даних вказавши версію IP TCP тип з'єднання
server_socket = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) 
# зв'язуємо socket з IP та портом
server_socket.bind(("127.0.0.1", 8080))
#Переводить socket в режим очікування
server_socket.listen()

print("connecting ... ")
# Очікує та приймає підключення клієнту
client_socket, adress = server_socket.accept()

print("connected", adress)
# Приймає данi клієнту та декодує їх
data = client_socket.recv(1024).decode()
print(data)