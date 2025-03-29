
import socket

def start_client():
    host = input("Введите IP-адрес сервера (по умолчанию 127.0.0.1): ") or "127.0.0.1"
    port = input("Введите порт сервера (по умолчанию 65432): ")
    port = int(port) if port else 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Соединение с сервером {host}:{port} установлено")

        try:
            while True:
                message = input("Введите сообщение для отправки (или 'exit' для выхода): ")
                client_socket.sendall(message.encode())
                print(f"Отправлены данные серверу: {message}")

                if message.lower() == 'exit':
                    print("Команда 'exit' отправлена. Разрыв соединения.")
                    break

                data = client_socket.recv(1024)
                print(f"Получены данные от сервера: {data.decode()}")
        finally:
            print("Разрыв соединения с сервером")

try:
    start_client()
except ConnectionRefusedError:
    print("Не удалось подключиться к серверу. Убедитесь, что сервер запущен.")

