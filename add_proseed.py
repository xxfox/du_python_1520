def add_data(num):
     with open('bakery.csv', 'a', encoding='utf-8') as add:
        add.write(f'{num} \n')
        print(f'Сумма {num} добавлена')

if __name__ == '__main__':
    import sys
    add_data(sys.argv[1])