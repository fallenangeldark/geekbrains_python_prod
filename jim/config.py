"""Константы для jim протокола, настройки """
#Ключи
#Тип сообщения между клиентом и сервером
ACTION = 'action'
#Значения типов сообщений между клиентом и сервером
A_PRESENCE = 'presence'
A_PROBE = 'probe'
A_MSG = 'msg'
A_QUIT = 'quit'
A_AUTH = 'authenticate'
A_JOIN = 'join'
A_LEAVE = 'leave'
#время запроса
TIME = 'time'
#данные о пользователе - клиенте (вложенный словарь)
USER = 'user'
#Имя пользователя - чата
ACCOUNT_NAME = 'account_name'
#текст ошибки
ERROR = 'error'

#Значения
PRESENCE = 'presence'
RESPONSE = 'response'
#Коды ответов
BASIC_NOTICE = 100
OK = 200
ACCEPTED = 202
WRONG_REQUEST = 400 #неправильный запрос/json объект
SERVER_ERROR = 500

#Кортеж из кодов ответов
RESPONSE_CODES = (BASIC_NOTICE, OK, ACCEPTED, WRONG_REQUEST, SERVER_ERROR)
#Кортеж из типов сообщений между клиентом и сервером
ACTION_MSGS = (A_PRESENCE, A_PROBE, A_MSG, A_QUIT, A_AUTH, A_JOIN, A_LEAVE)
