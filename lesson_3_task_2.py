"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def my_list(**kwargs):
    return list(kwargs.values())


print(my_list(name=input('Enter name: '),
              s_name=input('Enter second name: '),
              b_date=input('Enter birth day: '),
              l_town=input('Enter live town: '),
              email=input('Enter email: '),
              tel=input('Enter tel number: ')))

