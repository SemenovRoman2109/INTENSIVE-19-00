import socket
from threading import Thread

def start_server(): 
    # створили socket для передачи даних вказавши версію IP TCP тип з'єднання
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as server_socket:
        # зв'язуємо socket з IP та портом
        server_socket.bind(("0.0.0.0", 8081))
        #Переводить socket в режим очікування
        server_socket.listen()

        print("connecting ... ")
        # Очікує та приймає підключення клієнту
        client_socket, adress = server_socket.accept()

        print("connected", adress)
        # Приймає данi клієнту та декодує їх
        data = client_socket.recv(1024).decode()
        print(data)
        # client_socket.send(input("Enter message ").encode())

server_thred = Thread(target = start_server) 
server_thred.start()
print("Работаю одновременно с запуском сервера")
# server_thred.join()