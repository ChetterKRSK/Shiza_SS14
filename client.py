from ast import arg
import json
import socket
import threading
import time


class ClientSocket:
    def __init__(self, ip: str = "", port: int = 0) -> None:
        self.ip = ip
        self.port = port
        self.connected = False
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((self.ip, self.port))
        self.connected = True

    def disconnect(self):
        self.client_socket.close()
        self.connected = False

    def send_message(self, message_text: str, key_to_print: str):
        if not self.connected:
            self.connect()
        message_str = json.dumps(
            {"message_text": message_text, "key_to_print": key_to_print}
        )
        self.client_socket.send(message_str.encode("utf-8"))

    def send_message_in_thread(self, message_text: str, key_to_print: str):
        thread = threading.Thread(
            target=self.send_message, args=(message_text, key_to_print)
        )
        thread.start()


# Что-то, что замораживает поток, например запуск визуала
# def freeze():
#     while True:
#         print(123)
#         time.sleep(10)

# Пример запуска
# client = ClientSocket()
# client.ip = "localhost"
# client.port = 12345
# client.send_message_in_thread("text", "key") Это по нажатию кнопки нужно сделать.
# freeze()
