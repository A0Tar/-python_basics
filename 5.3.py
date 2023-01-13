"""
Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.

"""

import sys

min_salary = 20000
filename = "salary.txt"

if __name__ == "__main__":
    try:
        with open(filename, encoding='utf-8') as f:
            employees = f.readlines()
    except IOError as e:
        print(e)
        sys.exit(1)

    sum_salary = 0

    for employee in employees:
        name, salary = employee.split()

        try:
            salary = float(salary)
        except ValueError:
            continue

        sum_salary += salary
        if salary < min_salary:
            print(f'Оклад меньше 20.000:',name)

    print('Cредний оклад: ', round(sum_salary / len(employees), 2))


