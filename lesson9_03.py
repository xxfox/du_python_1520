class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'salary': _income, 'bonus': int(_income * 0.2)}


class Position(Worker):
    def get_full_name(self):
        return print(f'Full name: {self.surname} {self.name}')


    def get_total_income(self):
        total_income = self._income['salary'] + self._income['bonus']
        return print(f'Total income for {self.position} is {total_income}')


a = Position('Oksana', 'Falkova', 'Manager', 100)
a.get_total_income()
a.get_full_name()
print(a.name, a.surname, a.position, a._income)