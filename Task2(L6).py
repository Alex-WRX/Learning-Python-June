class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_full_profit(self, weigth=25, thickness=5):
        return f'{self._length} m * {self._width} m * {weigth} кг * {thickness} см =' \
            f' {(self._length * self._width * weigth * thickness) / 1000 } т'

road_1 = Road(5000, 20)
print(road_1.get_full_profit())
