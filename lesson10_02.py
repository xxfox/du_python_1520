from abc import abstractmethod


class Clothes:

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fabric_amount(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def fabric_amount(self):
        fabric = (self.size / 6.5 + 0.5)
        return f'Для пошива пальто {self.size} размера потребуется {round(fabric, 2)} метров ткани'


class Suit(Clothes):

    def __init__(self, height):
        self.height = height

    @property
    def fabric_amount(self):
        fabric = (2 * self.height + 0.3)
        return f'Для пошива костюма на рост {self.height} потребуется {fabric} метров ткани'


a = Coat(42)
b = Suit(165)
print(a.fabric_amount)
print(b.fabric_amount)
