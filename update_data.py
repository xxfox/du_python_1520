def update_data(position, new_sum):
    #position = int(input('Введите номер изменяемой строки: '))
    #new_sum = input('Введите новую сумму выручки: ')
    position = int(position)
    lins = open('bakery.csv', 'r').readlines()
    lins[position - 1] = f'{new_sum} \n'
    out = open('bakery.csv', 'w')
    out.writelines(lins)
    out.close()


if __name__ == '__main__':
    import sys
    update_data(*sys.argv[1:])