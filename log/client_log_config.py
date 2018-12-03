import logging

#создаем объект-логгер с именем client.main
logger = logging.getLogger('client.main')

#создаем объект форматирования "<дата-время> <уровень_важности> <имя_модуля> <сообщение>
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s")

#создаем файловый обработчик логирования
fh = logging.FileHandler('client.main.log', encoding = 'utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

#Добавляем в логгер наш обработчик событий
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    # Создаем потоковый обработчик логирования (по умолчанию sys.stderr):
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logger.addHandler(console)
    logger.info('Тестовый запуск логирования client')
