import socket
import pyautogui
import io
import time
INTERVAL = 0.1

with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as client_socket:
    #підключаємо клієнта до серверу
    client_socket.connect(("WAN_IP_SERVER", 8081))
    while True:
        # Робимо скрiншот екрану клiенту 
        screenshot = pyautogui.screenshot()
        # Отримуємо порожнiй об'єкт для запису байт даних
        image_bytes = io.BytesIO()
        # Зберігаємо скріншот у змінну image_bytes у вигляді байт коду в форматi PNG
        screenshot.save(fp = image_bytes, format="PNG")
        # Отримуємо значення байти коду та зберiгаємо в data_bytes
        data_bytes = image_bytes.getvalue()
        # Вiдправляє закодованi данi на сервер
        client_socket.sendall(data_bytes)
        time.sleep(INTERVAL)