import json
import socket
import threading
import time
from my_keyboard import keyboard_fetcher
from socket_client import HeaderSocket


class ClientSocket:
    HEADER_SIZE = 4  # размер заголовка в байтах

    def __init__(self, ip: str = "", port: int = 0) -> None:
        self.ip = ip
        self.port = port
        self.connected = False
        self.client_socket = None
        self.kbf = keyboard_fetcher()
        self.shutdown_event = threading.Event()

    def connect(self):
        self.client_socket = HeaderSocket()
        self.client_socket.connect(self.ip, self.port)
        self.connected = True

    def disconnect(self):
        self.client_socket.close()
        self.connected = False

    def send_message(self, message_text: str, key_to_print: str):
        if not self.connected:
            return
        data_str = json.dumps(
            {"type": "message", "message_text": message_text, "key_to_print": key_to_print}
        )
        self.client_socket.send(data_str)

    def send_message_in_thread(self, message_text: str, key_to_print: str):
        thread = threading.Thread(target=self.send_message, args=(message_text, key_to_print))
        thread.start()

    def server_keyboard_block_toggle(self, status: bool):
        data_str = json.dumps({"type": "keyboard_block", "status": status})
        self.client_socket.send(data_str)
        self.client_socket.recv()  # Что-бы он с ума не сошел.

    def server_keyboard(self):
        while not self.shutdown_event.is_set():
            data_str = json.dumps({"type": "keyboard_fetch", "keys": ";".join(self.kbf.key_list)})
            self.client_socket.send(data_str)
            time.sleep(0.1)

    def keyboard_fetch_on(self):
        if not self.connect:
            return
        self.server_keyboard_block_toggle(True)  # Эта зараза фризит все
        self.kbf.handler_all()
        self.shutdown_event.clear()
        self.thread_keyboard = threading.Thread(target=self.server_keyboard)
        self.thread_keyboard.start()

    def keyboard_fetch_off(self):
        self.server_keyboard_block_toggle(False)
        self.kbf.stop_handler_all()
        self.shutdown_event.set()
