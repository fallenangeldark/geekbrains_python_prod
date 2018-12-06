from functools import wraps

class Log:
    """ Класс декоратор для логирования функций"""
    def __init__(self, logger):
        self.logger = logger
        # pass

    @staticmethod
    def _create_message(res = None, *args):
        """
        Формирует сообщения для записи в лог.
        param result - результат работы функции
        args - любые параметры
        """
        message = ''
        #так как мы не передаем в функцию словари то этот, код излишен
        #ведь верно?)
        # if kwargs:
        #     message += 'kwargs: {}'.format(kwargs)
        if args:
            message += 'args: {}'.format(args)
        if res:
            message += ' {}'.format(res)
        return message

    def __call__(self, F):
        """
        Определеляем __call__ для возможности вызова экземпляра как декоратора
        param F - функция которую будем декорировать.
        """
        @wraps(F)
        def decorated(*args):
            res = F(*args)
            message = Log._create_message(res, *args)
            self.logger.info('{} - {} | {}'.format(message, F.__name__, F.__module__))
            return res
        return decorated
