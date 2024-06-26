import json
import socket
import threading
import time
import keyboard


def handle_client(client_socket, client_address):
    print(f"Подключение от {client_address}")
    try:
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    break
                getting_data = data.decode("utf-8")
                message_dict = json.loads(getting_data)
                print(message_dict)
                keyboard.press_and_release(message_dict["key_to_print"])
                time.sleep(0.05)
                keyboard.write(message_dict["message_text"])
                keyboard.press_and_release("Return")
                client_socket.sendall(data)
            except (ConnectionResetError, ConnectionAbortedError):
                break
    finally:
        client_socket.close()
        print(f"Отключение от {client_address}")


def start_echo_server(host="", port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Сервер запущен на {host}:{port}. Ожидание подключений...")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(
            target=handle_client, args=(client_socket, client_address)
        )
        client_thread.start()


if __name__ == "__main__":
    start_echo_server()
