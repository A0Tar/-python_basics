"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.
"""


n = int(input("Введите число n: "))
res = n + n * 11 + n * 111
print(f"n + nn + nnn = {res}")
