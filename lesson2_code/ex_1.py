# 1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
#
#     Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
import csv
import re


def get_data():
    files_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    str_list = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    all_lists = [os_prod_list, os_name_list, os_code_list, os_type_list]
    for el in files_list:
        with open(el) as f_1:
            for str in f_1:
                for regex in str_list:
                    match = re.search(regex, str)
                    if match:
                        if regex == 'Изготовитель системы':
                            s = str.split()
                            s = s[2:]
                            s = ' '.join(s)
                            os_prod_list.append(s)
                        elif regex == 'Название ОС':
                            s = str.split()
                            s = s[2:]
                            s = ' '.join(s)
                            os_name_list.append(s)
                        elif regex == 'Код продукта':
                            s = str.split()
                            s = s[2:]
                            s = ' '.join(s)
                            os_code_list.append(s)
                        elif regex == 'Тип системы':
                            s = str.split()
                            s = s[2:]
                            s = ' '.join(s)
                            os_type_list.append(s)
                        else:
                            continue
                    else:
                        continue
    main_data = []
    main_data.append(str_list)
    in_main_data = list(zip(os_prod_list, os_name_list, os_code_list, os_type_list))
    for el in in_main_data:
        main_data.append(list(el))

    return(main_data)
    #     Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
    #
    #     Проверить работу программы через вызов функции write_to_csv().
# print(get_data())

def write_to_csv(link):
    with open(link, 'w') as f_n:
        f_n_writer = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC, delimiter='|')
        for row in get_data():
            f_n_writer.writerow(row)

    with open(link) as f_n:
        print(f_n.read())

write_to_csv('new_csv.csv')
