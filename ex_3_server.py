"""
Функции сервера:
 - принимает сообщение клиента
 - формирует ответ клиенту
 - отправляет ответ клиенту
 - имеет параметры командной строкиЖ
 - -p <port> - TCP-порт для работы(по дефолту 7777)
 - -a <addr> - IP-адрес для прослушивания ( по умолчанию все доступные адреса)
"""
import sys
# import json
from socket import socket, AF_INET, SOCK_STREAM
from jim.utils import get_message, send_message
from jim.config import *
import logging
import log.server_log_config

logger = logging.getLogger('server.main')

#Func формирования ответа
def presence_response(presence_message):
    """
    Формирование ответа клиенту
    :param presence_message: Словарь presence запроса
    :return: Словарь ответа
    """
    #Делаем проверки
    if ACTION in presence_message and presence_message[ACTION] == PRESENCE and TIME in presence_message and isinstance(presence_message[TIME], float):
        #Если все хорошо
        logger.info('Успешная обработка сообщения от {}.'.format(addr))
        return {RESPONSE: 200}
    else:
        #Шлем код ошибки
        logger.error('Неверный запрос.')
        return {RESPONSE: 400, ERROR: 'Неверный запрос'}

#Запускаем сервер
if __name__ == '__main__':
    #Создается TCP-сокет сервера
    server = socket(AF_INET, SOCK_STREAM)
    #Получаем аргументы скрипта
    # ip - адрес
    #если ip указан в параметрах
    try:
        addr = sys.argv[1]
    #если ip не указан в параметрах
    except IndexError:
        addr = ''
        logger.info('Просшушиваем все адреса.')
    # порт
    #если порт указан в параметрах
    try:
        port = int(sys.argv[2])
    #если порт не указан в параметрах
    except IndexError:
        port = 7777
        logger.info('Порт установлен по умолчанию на {}.'.format(port))
    #Если порт не целое число
    except ValueError:
        logger.debug('Порт должен быть целым числом.')
        sys.exit(0)

    server.bind((addr, port)) #присваивает порт 7777
    server.listen(5)
    while 1:
        #Принять запрос на соединение
        client, addr = server.accept()
        #принимает сообщение клиента
        presence = get_message(client)
        print(presence)
        # print(client)
        #формирует ответ
        response = presence_response(presence)
        #отправляет ответ клиенту
        send_message(client, response)
        client.close()
