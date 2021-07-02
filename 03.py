from itertools import zip_longest

children = ['Иван', 'Кристина', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Дарья', 'Анна', 'Эрик', 'Эмма']
class_num = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

a = ((el_1, el_2) for el_1, el_2 in zip_longest(children, class_num))

print(type(a))
