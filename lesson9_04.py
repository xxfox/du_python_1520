class Car:
    speed = int(input('Введите скорость автомобиля: '))
    color = input('Введите цвет автомобиля: ')
    name = input('Введите имя автомобиля: ')
    is_police = False

    def go(self):
        print(f'Автомобиль {self.name} поехал')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        print(f'Автомобиль поворачивает {direction}')

    def show_speed(self, curr_speed):
        if curr_speed > self.speed:
            print(f'Максимальная скорость {self.name} составляет: {self.speed} км/час, быстрее никак')
        else:
            print(f'Текущая скорость автомобиля: {curr_speed}км/час')

class PoliceCar(Car):
    is_police = True

    def police(self):
        print('Уступите дорогу полицейским!')


class TownCar(Car):
    MAX_SPEED = 80

    def show_s_peed(self, curr_speed):
        if curr_speed > self.MAX_SPEED:
            print(f'Снизьте скорость! Максимально разрешенная скорость: {self.MAX_SPEED}км/час!')
        else:
            print(f'Текущая скорость автомобиля: {curr_speed}км/час')


class SportCar(Car):
    def sport(self):
        print(f'{self.name} прошел процедуру чип-тюнинга и может участвовать в гонках!')


class WorkCar(Car):
    MAX_SPEED = 40

    def show_speed(self, curr_speed):
        if curr_speed > self.MAX_SPEED:
            print(f'Снизьте скорость! Максимально разрешенная скорость: {self.MAX_SPEED}км/час!')
        else:
            print(f'Текущая скорость автомобиля: {curr_speed}км/час')


a = PoliceCar()
a.go()
a.stop()
a.turn('направо')
a.show_speed(120)
a.police()


