
import socket
import logging

logging.basicConfig(filename='server.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')


def start_server():
    host = input(
        "Введите IP-адрес для сервера (по умолчанию 127.0.0.1): ") or "127.0.0.1"
    port = input("Введите порт для сервера (по умолчанию 65432): ")
    port = int(port) if port else 65432

    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
                server_socket.bind((host, port))
                server_socket.listen()
                logging.info(f"Сервер запущен и слушает на {host}:{port}")
                print(f"Сервер запущен и слушает на {host}:{port}")

                while True:
                    client_socket, client_address = server_socket.accept()
                    with client_socket:
                        logging.info(f"Подключен клиент: {client_address}")
                        while True:
                            data = client_socket.recv(1024)
                            if not data:
                                break
                            message = data.decode()
                            logging.info(
                                f"Получены данные от клиента: {message}")

                            if message.strip().lower() == "exit":
                                logging.info(
                                    "Клиент отправил команду 'exit'. Разрыв соединения.")
                                break

                            client_socket.sendall(data)
                            logging.info(
                                f"Отправлены данные клиенту: {message}")
                        logging.info(f"Клиент отключен: {client_address}")
        except OSError as e:
            logging.error(
                f"Ошибка сокета: {e}. Попытка использовать следующий порт.")
            port += 1
            logging.info(f"Пробуем порт: {port}")
            print(f"Пробуем порт: {port}")
        except KeyboardInterrupt:
            logging.info("Сервер остановлен")
            print("Сервер остановлен")
            break


try:
    start_server()
except Exception as e:
    logging.error(f"Неожиданная ошибка: {e}")
