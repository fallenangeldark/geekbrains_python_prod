from jim.config import *
from jim.utils import *

import time
import unittest
import json

class TestPresenceFunc(unittest.TestCase):
    """
    Тесты для utils.py
    """

    def test_dict_to_bytes(self):
        """ проверяем на корректность словарь при переводе в байты"""
        presence_message = {
            ACTION: 'action',
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: 'Guest'
            }
        }
        jsdict = json.dumps(presence_message)
        jsbytes = jsdict.encode('utf-8')
        self.assertEqual(dict_to_bytes(presence_message), jsbytes)

    def test_bytes_to_dict(self):
        """ проверяем на корректность декодирование"""
        presence_message = {
            ACTION: 'action',
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: 'Guest'
            }
        }
        jsdict = json.dumps(presence_message)
        jsbytes = jsdict.encode('utf-8')
        jsbytes1 = jsbytes.decode('utf-8')
        jsnewdict = json.loads(jsbytes1)
        self.assertEqual(bytes_to_dict(jsbytes), jsnewdict)




if __name__ == '__main__':
    unittest.main()
