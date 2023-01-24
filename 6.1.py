"""
1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

import time

class TrafficLight():

    # Определяем время ожидания сигнала светофора
    red_color_time = 8
    yellow_color_time = 3
    green_color_time = 15

    # Определяем названия цветов сигналов светофора
    red_color_name = 'красный'
    yellow_color_name = 'желтый'
    green_color_name = 'зеленый'

    def __init__(self, color):
        self.__color = color
        print(f'\nСоздан новый объект TrafficLight со стартовым цветом {self.__color}')

    def switch_light(self, color, time_of_work):
        self.time_of_work = time_of_work
        print(f'Включен {color} свет, время ожидания {self.time_of_work} сек')
        time.sleep(self.time_of_work)

    def running(self, color = ''):

        # Если при вызове метода цвет не указан, берем из родительского класса
        # В противном случае стартуем с цвета, объявленного при вызове метода
        if not color:
            loc_color = self.__color
        else:
            loc_color = color

        if loc_color == self.red_color_name:
            self.switch_light('красный', self.red_color_time)
            self.switch_light('желтый', self.yellow_color_time)
            self.switch_light('зеленый', self.green_color_time)
        elif loc_color == self.yellow_color_name:
            self.switch_light('желтый', self.yellow_color_time)
            self.switch_light('зеленый', self.green_color_time)
        else:
            self.switch_light('зеленый', self.green_color_time)

        print('Цикл переключения цветов завершен')

tl1 = TrafficLight('красный')
tl1.running()

tl2 = TrafficLight('желтый')
tl2.running()

tl3 = TrafficLight('зеленый')
tl3.running()

# Инициализируем класс красным цветом, а метод запускаем с желтого
tl1 = TrafficLight('красный')
tl1.running('желтый')

