import socket
from threading import Thread
import io
import PIL.Image
import os
from .app.client_screen import screen_user

IMAGE_PATH = os.path.abspath(__file__ + "/../../images/1.png")

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
        while True:
            # data_image - Зберігає загальну суму поточних даних вiд клiента 
            # response_data - Зберігає 1 кБ даних та перезаписуємо його
            data_image = b''
            # Приймає данi клієнту
            response_data = client_socket.recv(1024)
            # Поки довжина отриманого байт рядка бiльше нiж 0 
            while len(response_data) > 0:
                # Об'єднуемо пакети даних у data_image ( отримуємо повне значення байт рядка зображення )
                data_image = data_image + response_data
                if b'\x00IEND\xaeB`\x82' in response_data:
                    break
                response_data = client_socket.recv(1024)
                
            # Якщо довжина байт коду зображення більше 0 ( його вдалось отримати )
            if len(data_image) > 0:
                try:
                    # Перетворюємо отриманні дані в об'єкт BytesIO ( байти )
                    image_bytes = io.BytesIO(data_image)
                    # Створюємо картинку з отриманних байтів та зберігаємо змінну image в оперативній пам'яті
                    image = PIL.Image.open(image_bytes) 
                    # Зберігаємо картинку за вказаним шляхом
                    image.save(IMAGE_PATH)
                    screen_user.configure(image =  screen_user.load_image())
                except:
                    print("Error")

server_thred = Thread(target = start_server) 
server_thred.start()
print("Работаю одновременно с запуском сервера")
