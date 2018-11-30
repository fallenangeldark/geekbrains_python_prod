# -*- coding: utf-8 -*-

"""
Функции клиента:
- сформировать presence - сообщение
- отправить сообщение серверу;
- получить ответ сервера;
- разобрать сообщение сервера;
- параметры командной строки скрипта client.py <addr> [<port>]:
addr - ip-адрес сервера;
port - tcp-порт на сервере, по умолчанию 7777
"""

import sys
import time
from socket import socket, AF_INET, SOCK_STREAM
from errors import UsernameToLongError, ResponseCodeLenError, MandatoryKeyError, ResponseCodeError
from jim.config import *
from jim.utils import send_message, get_message

#функция формирования сообщения
def create_presence(account_name='Guest'):
    """
    Сформировать presence - сообщения
    param account_name: Имя пользователя
    return: Словарь сообщения
    """
    #Если имя не строка
    if not isinstance(account_name, str):
        #Генерируем ошибку передан неверный тип
        raise TypeError
    #Если длина имени пользователя больше 25 символов
    if len(account_name) > 25:
        #генерируем нашу ошибку имя пользователя слишком длинное
        raise UsernameToLongError(account_name)
    #если все хорошо то формируем словарь сообщения
    message = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    #возвращаем сообщение в виде словаря
    return message



def translate_message(response):
    """
    Разбор сообщения
    param response: Словарь ответа от сервера
    return корректный словарь ответа
    """
    #Передали не словарь
    if not isinstance(response, dict):
        raise TypeError
    #Нету ключа response
    if RESPONSE not in response:
        #Ошибка нужен обязательный ключ
        raise MandatoryKeyError(RESPONSE)
    #если все хорошо то получаем код ответа
    code = response[RESPONSE]
    #длина кода не 3 символа
    if len(str(code)) != 3:
        #Ошибка неверной длины кода ошибки
        raise ResponseCodeLenError(code)
    #неправильные коды символов
    if code not in RESPONSE_CODES:
        #ошибка неверный код ответа
        raise ResponseCodeError(code)
    #возвращаем ответ
    return response

#Запуск клиента
if __name__ == "__main__":
    #Создать TCP-сокет клиента
    client = socket(AF_INET, SOCK_STREAM) #Создатаь сокет TCP
    #Пытаемся получить параметры скрипта
    #Получаем аргументы скрипта
    # ip-adress
    #если ip-адрес указан в параметрах -p <addr>
    try:
        addr = sys.argv[1]
    #если ip-адрес не указан в параметрах
    except IndexError:
        addr = 'localhost'
    #Если порт указан в параметрах
    try:
        port = int(sys.argv[2])
    except IndexError:
        port = 7777
    except ValueError:
        print('Порт должен быть целым числом')
        sys.exit(0)
    try:
        account_name = str(sys.argv[3])
    except IndexError:
        account_name = 'Guest'
    except ValueError:
        print('Введите корректное имя')
        sys.exit(0)
    # Данные получили -> Соединяемся с сервером
    client.connect((addr, port))
    #Сформировать сообщение серверу
    presence = create_presence(account_name)
    #Отправить сообщение серверу
    send_message(client, presence)
    #Получить ответ от сервера
    response = get_message(client)
    #Разобрать ответ сервера
    response = translate_message(response)
    print(response)
