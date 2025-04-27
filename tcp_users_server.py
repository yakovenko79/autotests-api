import socket

messages = []


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 1234)
    server_socket.bind(server_address)
    server_socket.listen(10)
    print('Сервер запущен и ждет подключений...')

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        data = client_socket.recv(1024).decode()
        messages.append(data)

        print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")
        client_socket.send('\n'.join(messages).encode())

        client_socket.close()


if __name__ == "__main__":
    server()
