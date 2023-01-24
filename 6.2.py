"""
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна;
проверить работу метода.
"""

class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width, weight, thickness):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.thickness = thickness

    def mass(self):
        leng = self._length
        wid = self._width
        w = self.weight
        thick = self.thickness
        total = leng * wid * w * thick / 1000
        return print(f"Масса асфальта\n {leng} м * {wid} м * {w} кг * {thick} см = ", total, "т")


r = Road(30, 2000, 30, 5)
r.mass()

