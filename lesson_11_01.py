import re


class Data:

    def __init__(self, date='dd-mm-yyyy'):
        self.date = date

    @classmethod
    def date_split(cls, date):
        date_list = date.split('-')
        date_int = [int(item) for item in date_list]
        return print(date_int)

    @staticmethod
    def valid_int(date):
        re_date = re.compile(r'(0[1-9]|[12][0-9]|3[01])[-](0[1-9]|1[012])[-](19|20)\d\d')
        if re_date.match(date) is None:
            return print(f'Дата {date} не прошла валидацию')
        else:
            return print(f'Дата {date} прошла валидацию')


Data.valid_int('01-10-2031')

