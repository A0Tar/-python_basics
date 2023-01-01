"""
Задание 6.

Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.


Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.


"""

my_list = []
while True:
    my_list.append((input("Номер товара: "),
                   {"Название": input("Название: "),
                    "Цена": input("Цена: "),
                    "Количество": input("Количество: "),
                    "ед.": input("Единицы учёта: ")}))
    q = input("Закончить ввод позиций? Да, Нет: ")
    if q == "Да":
        break

my_list = [(1, {"название": "колбаса", "цена": 700, "количество": 20, "eд": "кг"}),
          (2, {"название": "хлеб", "цена": 60, "количество": 120, "eд": "шт."}),
          (3, {"название": "молоко", "цена": 70, "количество": 200, "eд": "л"})]

names_list = []
prices_list = []
counts_list = []
units_list = []
res_dict = {}
for i in range(len(my_list)):
    names_list.append(my_list[i][1]['название'])
    prices_list.append(my_list[i][1]['цена'])
    counts_list.append(my_list[i][1]['количество'])
    units_list.append(my_list[i][1]['eд'])

res_dict.update({'названия': names_list, 'цены': prices_list, 'количества': counts_list, 'единицы': units_list})
print(res_dict)
