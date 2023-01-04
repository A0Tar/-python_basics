"""
Задание 2.

Выполнить функцию, которая принимает несколько параметров,
описывающих данные пользователя:
 имя, фамилия, год рождения, город проживания, email, телефон.
 Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой.
"""

def user_data(name, surname, year_of_birth, city, email, phone):
    return print(f'Имя: {name} Фамилия: {surname} Год рождения: {year_of_birth}'
                 f'Город проживания: {city} Email: {email} Телефон: {phone}')


user_data(
    name=input('Имя: '),
    surname=input('Фамилия: '),
    year_of_birth=input('Год Рождения: '),
    city=input('Город проживания: '),
    email=input('email: '),
    phone=input('phone: '),
)
