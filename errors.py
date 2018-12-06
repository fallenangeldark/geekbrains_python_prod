# -*- coding: utf-8 -*-

""" Errors """
import logging
import log.client_log_config

#создаем объект-логгер с именем client.main
logger = logging.getLogger('client.main')
#Исключение когда имя пользователя слишком длинное
class UsernameToLongError(Exception):
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return "Имя пользователя {} должно быть менее 26 символов".format(self.username)

#Исключение, переданный код отсутствует среди стандартных кодов
class ResponseCodeError(Exception):
    def __init__(self, code):
        self.code  = code

    def __str__(self):
        return "Неверный код ответа {}".format(self.code)

#исключение, длина кода - не три символа
class ResponseCodeLenError(ResponseCodeError):
    def __str__(self):
        return "Неверная длина кода {}. Длина кода должна быть 3 символа".format(self.code)

#Исключение, отсутствует обязательный атрибут response
class MandatoryKeyError(Exception):
    def __init__(self, key):
        self.key = key

    def __str__(self):
        return 'Не хватает обязательного атриута {}'.format(self.key)
