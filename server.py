# -------- Эхо-сервер, обрабатывающий "одновременно" несколько клиентов -------
#              Обработка клиентов осуществляется функцией select

import select
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from queue import Queue


def read_requests(r_clients, all_clients):
    ''' Чтение запросов из списка клиентов
    '''
    sending_clients = all_clients[:]
    responses = {}      # Словарь ответов сервера вида {сокет: запрос}

    for sock in r_clients:
        try:
            data = sock.recv(1024).decode('ascii')
            responses[sock] = data
            # sending_clients.remove(sock)
            print(responses)

        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            # all_clients.remove(sock)
    return responses


def write_responses(requests, w_clients, all_clients):
    ''' Эхо-ответ сервера клиентам, от которых были запросы
    '''
    alm_all_clients = all_clients[:]
    for sock in w_clients:
        if sock in requests:
            try:
                alm_all_clients.remove(sock)
                resp = requests[sock].encode('ascii')
                for sock in alm_all_clients:
                    test_len = sock.send(resp.upper())
            except:                 # Сокет недоступен, клиент отключился
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock)

def mainloop():
    ''' Основной цикл обработки запросов клиентов
    '''
    address = ('', 10000)
    clients = []

    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    s.settimeout(1)   # Таймаут для операций с сокетом

    while True:
        try:
            conn, addr = s.accept()  # Проверка подключений
        except OSError as e:
            pass                     # timeout вышел
        else:
            print("Получен запрос на соединение от %s" % str(addr))
            clients.append(conn)
            welc = 'Welcome'
            conn.send(welc.encode('ascii'))
        finally:
            # Проверить наличие событий ввода-вывода
            wait = 10
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass            # Ничего не делать, если какой-то клиент отключился

            responses = read_requests(r, clients)
            write_responses(responses, w, clients)
             # Выполним отправку ответов клиентам

print('Эхо-сервер запущен!')
mainloop()
