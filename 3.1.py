"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
def calc(a, b):
    try:
        return a/b
    except ZeroDivisionError as a:
        print(f'Ошибка: делить на ноль нельзя')




print(calc(int(input('Введите делимое: ')), int(input('Введите делитель: '))))
