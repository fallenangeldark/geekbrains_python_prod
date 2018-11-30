class Employee():
    """Работник с заработной платой"""
    def __init__(self, name, lastname, annual_salary = 25000):
        self.name = name
        self.lastname = lastname
        self.annual_salary = annual_salary

    def give_raise(self, raise_salary = 5000):
        """Увеличение заработной платы"""
        self.annual_salary += raise_salary

    def show_worker(self):
        """Показ данных о работнике"""
        show_worker_info = str(self.name.title()) + ' ' + str(self.lastname.title()) + ' зарабатывает в год - ' + str(self.annual_salary)
        return show_worker_info
