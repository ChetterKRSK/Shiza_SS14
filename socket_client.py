import socket


class HeaderSocket:
    HEADER_SIZE = 4  # размер заголовка в байтах

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def bind_and_listen(self, host, port):
        self.sock.bind((host, port))
        self.sock.listen(5)

    def accept(self):
        client_socket, addr = self.sock.accept()
        return HeaderSocket(client_socket), addr

    def send(self, message):
        message_bytes = message.encode("utf-8")
        message_length = len(message_bytes)
        header = message_length.to_bytes(self.HEADER_SIZE, byteorder="big")
        self.sock.sendall(header + message_bytes)

    def recv(self):
        header = self.sock.recv(self.HEADER_SIZE)
        if not header:
            return None
        message_length = int.from_bytes(header, byteorder="big")
        message = self.sock.recv(message_length).decode("utf-8")
        return message

    def close(self):
        self.sock.close()
