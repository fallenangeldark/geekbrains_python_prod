import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Тесты для класса Employee"""

    def setUp(self):
        """Создание входных значений"""
        self.my_employee = Employee('Ivan', 'Dorn', 25000)

    def test_give_default_raise(self):
        """Проверка увеличения ЗП по умолчанию"""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.show_worker(), 'Ivan Dorn зарабатывает в год - 30000')

    def test_give_custom_raise(self):
        """"""
        self.my_employee.give_raise(3500)
        self.assertEqual(self.my_employee.show_worker(), 'Ivan Dorn зарабатывает в год - 28500')
unittest.main()
