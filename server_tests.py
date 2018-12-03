from jim.config import *
from ex_3_server import presence_response

import time

import unittest

class TestPresenceFunc(unittest.TestCase):
    """
    Тесты для func presence_response
    """

    presence_message = {
        ACTION: '',
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: 'Guest'
        }
    }
    def test_action_in_presence_mess(self):
        """ проверка RESPONSE:400 для отсутствия поля ACTION в presense_message"""
        self.assertEqual(presence_response(self.presence_message), {RESPONSE: 400, ERROR: 'Неверный запрос'})

    presence_message = {
        ACTION: 'notAction',
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: 'Guest'
        }
    }
    def test_action_error_in_presence_mess(self):
        """ проверка переменной action на другое значение для вывода RESPONSE: 400"""
        self.assertEqual(presence_response(self.presence_message), {RESPONSE: 400, ERROR: 'Неверный запрос'})

    presence_message = {
        ACTION: 'action',
        TIME: 10101010,
        USER: {
            ACCOUNT_NAME: 'Guest'
        }
    }
    def test_time_in_presence_mess(self):
        """ проверка переменной TIME на тип float для вывода RESPONSE: 400"""
        self.assertEqual(presence_response(self.presence_message), {RESPONSE: 400, ERROR: 'Неверный запрос'})


if __name__ == '__main__':
    unittest.main()
