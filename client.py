from socket import *
import sys
from threading import Thread, Timer
from queue import Queue
import time
import threading

LIVE = True
ADDRESS = ('localhost', 10000)
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(ADDRESS)



class ClientThread(Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.q = Queue()

    def get_mes(self):
        global sock
        get_m = sock.recv(1024).decode('ascii')
        self.q.put(get_m)

    def send_mes(self):
        global sock

        new_m = sys.stdin.readline()
        if new_m:
            new_m = sock.send(new_m.encode('ascii'))
            self.q.put(new_m)
            self.q.task_done()
        self.q.task_done()


    def close(self):
        self.q.put(None)
        self.q.join()

    def run(self):
        global sock
        global LIVE
        print('Press <Enter> to get message | some_text + <Enter> to send. You have 30 seconds')
        while True:
            try:
                item = self.q.get(timeout=30)
                    # self.q.task_done()
                    # break
                print(item)
            except Exception as e:
                print('Haven\'t messages')

                sock.close()
                self.q.join()
        self.q.join()


if __name__ == '__main__':
    cli = ClientThread()
    cli.start()
    while True:
        cli.get_mes()
        cli.send_mes()
    cli.close()
