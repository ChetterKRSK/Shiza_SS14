import json
import socket
import threading


class ClientSocket:
    def __init__(self, ip: str = "", port: int = 0) -> None:
        self.ip = ip
        self.port = port
        self.connected = False

    def connect(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.ip, self.port))
        self.connected = True

    def disconnect(self):
        self.client_socket.close()
        self.connected = False

    def send_message(self, message_text: str, key_to_print: str):
        if not self.connected:
            # self.connect()
            return
        message_str = json.dumps({"message_text": message_text, "key_to_print": key_to_print})
        self.client_socket.send(message_str.encode("utf-8"))

    def send_message_in_thread(self, message_text: str, key_to_print: str):
        thread = threading.Thread(target=self.send_message, args=(message_text, key_to_print))
        thread.start()
