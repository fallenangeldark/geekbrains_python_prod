from socket import *
import sys

ADDRESS = ('localhost', 10000)

def echo_client():
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(ADDRESS)
        m = sock.recv(1024).decode('ascii')
        print(m)
        msg = input('Listen (l) / Send (s)/ exit (q): ')
        if msg == 'l':
            while True:
                data = sock.recv(1024).decode('ascii')
                print(data)
        elif msg == 's':
            while True:
                new_mes = input('Ваше сообщение: ')
                sock.send(new_mes.encode('ascii'))
        elif msg == 'q':
            while True:
                break

        # while True:
        #     # data = sock.recv(1024).decode('ascii')
        #     msg = input('Ваше сообщение: ')
        #     if msg == 'exit':
        #         break
        #     elif msg == 'l':
        #         while True:
        #             data = sock.recv(1024).decode('ascii')
        #             print(data)
        #             new_mes = input('Listen (any key)/ Send (s)')
        #             if new_mes == 's':
        #                 break
        #             else:
        #                 pass
        #     sock.send(msg.encode('ascii'))
        #     data = sock.recv(1024).decode('ascii')
        #     print('Ответ: ', data)

if __name__ == '__main__':
    echo_client()
