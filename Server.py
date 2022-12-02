"""
1. Використовуючи код домашнього завдання 1 лекції 11, додайте до
серверу чату систему логування рівня ІМЕРО, МАВМІМС і ЕБКОВ.
ЗАПУСК: СЕРВЕР - ЛОГ (КЛІЄНТ НЕ ЗАПУСКАТИ)
"""
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 55000))
sock.listen(10)
print('Chat is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    flag = 0
    if bytes("hi", encoding='UTF-8') in data:
        conn.send(bytes("Server: HELLLLO", encoding='UTF-8'))
        flag = 1
        print(str(data))
        print("Server: HELLLLO")
    if bytes("problem", encoding='UTF-8') in data:
        conn.send(bytes("Server: I CAN'T HELP YOU", encoding='UTF-8'))
        flag = 1
        print(str(data))
        print("Server: I CAN'T HELP YOU")
    if flag != 1:
        conn.send(bytes("Server: " + input("Server "), encoding='UTF-8'))
        print(str(data))

#conn.close()
print('Chat is closed')

