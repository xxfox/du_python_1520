class Road:
    WEIGHT = 25
    THICKNESS = 5

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
        result = _length * _width * self.WEIGHT * self.THICKNESS
        return print(f'Для дороги длиной {_length}м и шириной {_width}м вам понадобится {result} тонн асфальта')


my_road = Road(5, 15)
