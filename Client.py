# Client.py
import logging
import socket

module_logger = logging.getLogger("exampleApp.Client")

def add():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 55000))
    sock.send(bytes("Client: " + input("Client "), encoding='UTF-8'))
    data = sock.recv(1024)
    print(data)
    sock.close()


