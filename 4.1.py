"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""


from sys import argv

script_name, output_in_hours, rate_per_hour, premium = argv

print("Имя скрипта: ", script_name)
print("Выработка в часах: ", output_in_hours)
print("Ставка в час: ", rate_per_hour)
print("Премия: ", premium)
print("Зарплата сотрудника: ", (float(output_in_hours) * float(rate_per_hour)) + float(premium))