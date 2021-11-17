class ComplexNum:

    def __init__(self, num_1, num_2):
        self.complex_num = complex(num_1, num_2)

    def __add__(self, other):
        result = self.complex_num + other.complex_num
        return result

    def __mul__(self, other):
        result = self.complex_num * other.complex_num
        return result


a = ComplexNum(1, 3)
b = ComplexNum(1, 5)
print(a + b)
print(a * b)
