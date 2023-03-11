"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""


def my_div():
    try:
        arg_1 = int(input('Ведите делимое: '))
        arg_2 = int(input('Dведите делитель: '))
        return arg_1 / arg_2
    except ZeroDivisionError:
        return 'Дление на 0 недопустимо'
    except ValueError:
        return 'Необходимо ввести число'


res = my_div()
print(res)
