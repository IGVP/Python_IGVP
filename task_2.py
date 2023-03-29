"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


# задаем класс на определение деления на нуль
class ZeroDivError(Exception):
    def __init__(self, txt):
        self.txt = txt


# заправшимаем данные
inp_num_a = int(input('Введите делимое: '))
inp_num_b = int(input('Введите делитель, делитель не может быт равным "0": '))

try:
    if inp_num_b == 0:
        raise ZeroDivError('Деление на ноль недопустимо!')  # поднимаем Exception
# отлавливаем и выводим уведомление об ошибке
except ZeroDivError as err:
    print(err)
# при положительном исходе выводим результат деления
else:
    print(f"Результат деления: {inp_num_a / inp_num_b:.2f}")
