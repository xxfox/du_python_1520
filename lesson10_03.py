class Organic_Cell:

    def __init__(self, cell_amount, row):
        self.cell_amount = cell_amount
        self.row = row

    def __add__(self, other):
        return f'Сумма двух клеток равна: {self.cell_amount + other.cell_amount}'

    def __sub__(self, other):
        if self.cell_amount - other.cell_amount > 0:
            return f'Разность клеток равна: {self.cell_amount - other.cell_amount}'
        else:
            return f'Вычисление не выполнено, так как разность меньше нуля'

    def __mul__(self, other):
        return f'Результат умножения двух клеток: {self.cell_amount * other.cell_amount}'

    def __floordiv__(self, other):
        return f'Результат деления двух клеток: {self.cell_amount // other.cell_amount}'

    def make_order(self):
        length_amount = self.cell_amount
        for i in range(length_amount):
            if length_amount > self.row:
                print('*' * self.row, end='/n')
                length_amount -= self.row
            else:
                return '*' * length_amount


a = Organic_Cell(5, 2)
b = Organic_Cell(40, 4)
print(a.make_order())
print(b.make_order())
