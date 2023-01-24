"""
Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    def __init__(self, title= 'Somewhat'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        self.title = 'pen'
        print(f'Creating grafic by {self.title}')


class Pencil(Stationery):

    def draw(self):
        self.title = 'pencil'
        print(f'Creating sketch by {self.title}')


class Handle(Stationery):

    def draw(self):
        self.title = 'handle'
        print(f'Creating illustration by {self.title}')


pen = Pen()
pencil = Pencil()
handle = Handle()
pen.draw()
pencil.draw()
handle.draw()

