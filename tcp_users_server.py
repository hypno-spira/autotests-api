import socket


def server():
    # Создаем TCP-сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязываем его к адресу и порту
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Начинаем слушать входящие подключения (максимум 10 в очереди)
    server_socket.listen(10)
    print("Сервер запущен и ждет подключений...")
    all_messages = []

    while True:
        # Принимаем соединение от клиента
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        # Получаем данные от клиента
        data = client_socket.recv(1024).decode()
        print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")

        # Сохраняем полученные сообщения
        all_messages.append(data)

        # Отправляем в ответ клиенту все полученные сообщения
        client_socket.send('\n'.join(all_messages).encode())

        # Закрываем соединение с клиентом
        client_socket.close()


if __name__ == '__main__':
    server()
