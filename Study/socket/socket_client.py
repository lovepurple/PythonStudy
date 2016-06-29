# -*- coding: utf-8 -*-

import socket


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 9000))
    data = "some data"
    b = data.encode('utf-8')
    sock.send(b)
    result = sock.recv(1024)
    print(result)
    sock.close()