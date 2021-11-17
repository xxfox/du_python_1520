class OwnError(Exception):
    @staticmethod
    def zero_error(*args):
        num_1, num_2 = args
        try:
            result = num_1 / num_2
            if num_2 < 0:
                raise OwnError(f'{num_2} не может быть делителем')
        except ZeroDivisionError:
            print('На ноль делить нельзя')
        except OwnError as err:
            print(err)
        else:
            print(result)
        finally:
            print('Работа программы завершена')


OwnError.zero_error(20, 5)
OwnError.zero_error(20, 0)
OwnError.zero_error(20, -3)
