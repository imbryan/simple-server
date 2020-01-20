# Link to repo
# https://github.com/imbryan/simple-server

import socket

def main():
    host = '127.0.0.1'
    port = 5000

    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)  # TCP

    sock.bind((host, port))
    sock.listen()

    conn, addr = sock.accept()

    sock.recv(1024)

    sock.close()

if __name__ == '__main__':
    main()