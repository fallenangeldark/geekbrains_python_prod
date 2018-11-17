
#1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и также проверить тип и содержимое переменных.

str_1 = 'разработка' #\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430
print(type(str_1), str_1)
str_2 = 'сокет'
#\u0441\u043e\u043a\u0435\u0442
print(type(str_2), str_2)
str_3 = 'декоратор'
#\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440
print(type(str_3), str_3)


str_1_b = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
print(type(str_1_b), str_1_b)
str_2_b = '\u0441\u043e\u043a\u0435\u0442'
print(type(str_2_b), str_2_b)
str_3_b = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
print(type(str_3_b), str_3_b)



#2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

#Здесь ведь не нужно преобразовывать в последовательность юникод в онлайн конвертере? На всякий случай один пример напишу внизу )
# function - \u0066\u0075\u006e\u0063\u0074\u0069\u006f\u006e
b_1 = b'class'
print(type(b_1), b_1, len(b_1))
b_2 = b'function'
print(type(b_2), b_2, len(b_2))
b_3 = b'method'
print(type(b_3), b_3, len(b_3))

#Хотя судя по выводу это не то чего вы от нас хотели) Но, оставлю для истории.
b_1_u = b'\u0066\u0075\u006e\u0063\u0074\u0069\u006f\u006e'
print(type(b_1_u), b_1_u, len(b_1_u))



# 3.  Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

#В байтовом типе невозможно отобразить символы не присутствующие в ASCII кодировке, проверяем.
s_1 = b'attribute'
# s_2 = b'класс' #SyntaxError: bytes can only contain ASCII literal characters.
#s_3 = b'функция' #SyntaxError: bytes can only contain ASCII literal characters.
s_4 = b'type'

print(s_1)
#print(s_2)
#print(s_3)
print(s_4)
#Что и требовалось доказать)



#4.Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).

st_1 = 'разработка'
st_2 = 'администрирование'
st_3 = 'protocol'
st_4 = 'standard'

#Преобразуем в байтовое представление
st_1_b = st_1.encode('utf-8')
st_2_b = st_2.encode('utf-8')
st_3_b = str.encode(st_3, encoding='utf-8')
st_4_b = str.encode(st_4, encoding='utf-8')
print(st_1_b, st_2_b, st_3_b) # Как видим Кириллица имеет вид кодировки, а латиница в строке вывода имеет такой же вид с пометкой "b" - байтовый вид

st_1_s = st_1_b.decode('utf-8')
st_2_s = st_2_b.decode('utf-8')
st_3_s = bytes.decode(st_3_b, 'utf-8')
st_4_s = bytes.decode(st_4_b, 'utf-8')

# print(st_1_s, st_2_s, st_3_s)# Вывод показывает что преобразование кириллицы и латиницы прошло успешно



#5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.

import subprocess


args = ['ping', 'yandex.ru']

subproc_ping_ya = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc_ping_ya.stdout:
    print(line.decode('cp866'))

#Пошарив в документации был обнаружен вот такой вот выход P.S. С версии 3.6
args = ['ping', 'youtube.com']

subproc_ping_youtube = subprocess.Popen(args, stdout=subprocess.PIPE, encoding='cp866')
for line in subproc_ping_youtube.stdout:
    print(line)

# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.

with open('test_file.txt', 'w') as t_f:
    t_f.write('сетевое программирование\nсокет\nдекоратор')


encodings = ['windows-1252','utf-8','cp866', 'windows-1251', 'latin']
for e in encodings:
    try:
        fh = open('test_file.txt', 'r', encoding=e)
        for line in fh:
            print(line)
        print(e)
        fh.seek(0)
    except UnicodeDecodeError:
        print('got unicode error with %s , trying different encoding\n\n\n' % e)
    else:
        print('opening the file with encoding:  %s \n\n\n' % e)

#Судя по выводу на экран мы понимаем что хоть ошибку получили только на utf-8, но адекватный вид имеет только windows-1251 - значит это наша кодировка

#При такой записи мы получим ошибку преобразования,
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in position 0: invalid continuation byte
#  поймаем же ее
try:
    with open('test_file.txt', 'r', encoding='utf-8') as u_file:
        for line in u_file:
            print(line)
except UnicodeDecodeError:
    print("UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in position 0: invalid continuation byte  ")
#Так как мы знаем что по дефолту windows сохраняет файлы в cp1251 сделаем следующее: 
#Откроем файл на чтение в вышеуказанной кодировке
with open('test_file.txt', 'r', encoding='cp1251') as u2_file:
    str = ''
    for line in u2_file:
        str+=line
    print(str)
    print(str.encode('utf-8'))
    str = str.encode('utf-8') #закодируем в кодировку utf-8
    print(str.decode('utf-8')) #раскодируем в читаемый вид из кодировки utf-8


# Конечно мы могли просто записать данные в файл в кодировке utf-8, и не иметь проблем)
# with open('test_file.txt', 'w', encoding='utf-8') as t_f:
#     t_f.write('сетевое программирование\nсокет\nдекоратор')
#
# with open('test_file.txt', 'r', encoding='utf-8') as u_file:
#     for line in u_file:
#         print(line)
