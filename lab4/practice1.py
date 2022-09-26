import socket


def echo():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 5551))
    s.listen(10)
    s.settimeout(0.5)
    while True:
        try:
            conn, address = s.accept()
            while True:
                data = conn.recv(2048)
                if data and data != b'exit':
                    conn.send(data)
                    print(data)
                else:
                    conn.close()
                    break
        except socket.timeout:
            continue


if __name__ == "__main__":
    try:
        echo()
    except KeyboardInterrupt:
        pass
