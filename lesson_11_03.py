class Numbers(Exception):
    @staticmethod
    def num_list():
        user_list = []
        while True:
            user_data = input('Введите число, либо команду stop для завершения работы программы: ')
            try:
                if user_data.isdigit():
                    user_list.append(user_data)
                elif user_data == 'stop':
                    print(f'Вы остановили программу, результат работы: {user_list}')
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Вы ввели не число. Попробуйте снова!')




Numbers.num_list()