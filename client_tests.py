from jim.config import *
from ex_3_client import create_presence
from errors import UsernameToLongError
import time

import unittest

class TestPresenceFunc(unittest.TestCase):
    """
    Тесты для func create_presence
    """
    def test_create_presence_person(self):
        """ проверка ввода имени"""
        create_presence('Bob')
        mes_standard = {
            ACTION: PRESENCE,
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: 'Bob'
            }
        }
        self.assertEqual(create_presence('Bob'), mes_standard)

    def test_create_presence_action(self):
        """ проверка поля ACTION"""
        create_presence()
        mes_standard = {
            ACTION: 'presence',
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: '',
            }
        }
        self.assertEqual(create_presence(''), mes_standard)

    def test_create_presence_long_name(self):
        """ Проверка порождения исключения на слишком длинное имя"""
        #Если тест прошел, значит было вызвано исключение
        with self.assertRaises(UsernameToLongError):
            create_presence('ThisIsTooLongNameForOurUserTryShorter')

    def test_create_presence_type_name(self):
        """ Проверка порождения исключения на ошибку типа в имени(не строка)"""
        with self.assertRaises(TypeError):
            create_presence(123)


if __name__ == '__main__':
    unittest.main()
