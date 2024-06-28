import json
import socket
import threading
import time
from typing import Dict
import keyboard

import my_keyboard


class Server:
    def __init__(self) -> None:
        self.keyboard_fetch_toggle = False
        self.key_list = []

    def handle_client(self, client_socket, client_address):
        print(f"Подключение от {client_address}")
        try:
            while True:
                try:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    getting_data = data.decode("utf-8")
                    data_dict = json.loads(getting_data)
                    # print(data_dict)
                    if data_dict["type"] == "message":
                        self.message(data_dict)
                    elif data_dict["type"] == "keyboard_block":
                        self.keyboard_block(data_dict)
                        client_socket.send("1".encode("utf-8"))
                    elif data_dict["type"] == "keyboard_fetch":
                        self.keyboard_fetcher(data_dict)
                    # client_socket.sendall(data)
                except (ConnectionResetError, ConnectionAbortedError):
                    break
        finally:
            client_socket.close()
            print(f"Отключение от {client_address}")

    def message(self, message_dict: Dict):
        my_keyboard.block()
        keyboard.press_and_release(message_dict["key_to_print"])
        time.sleep(0.05)
        keyboard.write(message_dict["message_text"])
        keyboard.press_and_release("Return")
        my_keyboard.unblock()

    def keyboard_block(self, keyboard_block_dict: Dict):
        keyboard_block_toggle = keyboard_block_dict["status"]
        if keyboard_block_toggle:
            self.keyboard_block_toggle = False
            my_keyboard.block()
        else:
            self.keyboard_block_toggle = True
            my_keyboard.unblock()

    def keyboard_fetcher(self, keyboard_dict: Dict):
        print(str(keyboard_dict) + " - " + str(self.key_list))
        client_keys_list = keyboard_dict["keys"].split(";")
        if not client_keys_list[0] and self.key_list:
            for server_key in self.key_list:
                keyboard.release(server_key)
            self.key_list.clear()
        elif not client_keys_list[0] and not self.key_list:
            pass
        elif client_keys_list != self.key_list:
            for server_key in self.key_list:
                if server_key not in client_keys_list:
                    self.key_list.pop(self.key_list.index(server_key))
                    keyboard.release(server_key)
            for client_key in client_keys_list:
                if client_key not in self.key_list:
                    self.key_list.append(client_key)
                    keyboard.press(client_key)

    def start_echo_server(self, host="", port=12345):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(5)

        print(f"Сервер запущен на {host}:{port}. Ожидание подключений...")

        while True:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(
                target=self.handle_client, args=(client_socket, client_address)
            )
            client_thread.start()


if __name__ == "__main__":
    server = Server()
    server.start_echo_server()
