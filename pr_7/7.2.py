"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды.
 Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def get_square_c(self):
        return self.size / 6.5 + 0.5

    def get_square_s(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Общая площадь ткани:  {self.size / 6.5 + 0.5 + self.height * 2 + 0.3:.2f}')


class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_c = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани для пальто: {self.square_c}'


class Suit(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_s = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани для костюма: {self.square_s}'

coat = Coat(2, 4)
suit = Suit(1, 2)
print(coat)
print(suit)
print(suit.get_sq_full)
