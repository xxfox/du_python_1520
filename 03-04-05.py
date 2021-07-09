import csv
from itertools import zip_longest

file_1 = input('Введите имя файла с именами: ') #users.csv
file_2 = input('Введите имя файла с хобби: ') #hobby.csv
file_3 = input('Введите имя файла для записи: ')

with open(file_1, 'r', encoding='utf-8') as u, open(file_2, 'r', encoding='utf-8') as h, open(file_3, 'a', encoding='utf-8') as f:
    user_reader = csv.reader(u, delimiter=',')
    hobby_reader = csv.reader(h, delimiter=',')
    for row_1, row_2 in zip_longest(user_reader, hobby_reader):
        if row_1 is None:
            exit(1)
        elif row_2 is None:
            b = 'None'
        else:
            b = ', '.join(list(row_2))
        a = ' '.join(list(row_1))
        f.write(f'{a}: {b} \n')

