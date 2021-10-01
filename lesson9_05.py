class Stationery:
    title = input('Which color of your stationery? ')

    def draw(self):
        return print(f'{self.title} stationery')


class Pen(Stationery):
    def draw(self):
        return print(f'{self.title} pen')


class Pencil(Stationery):
    def draw(self):
        return print(f'{self.title} pencil')


class Handle(Stationery):
    def draw(self):
        return print(f'{self.title} handle')



