"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
"""
from itertools import count, cycle

# первый блок, формаирование списка
a = int(input('Введите начальное число последовательности: '))
b = int(input('Введите последенее число последовательности: '))
my_list = []

for a in count(a):
    if a > b:
        break
    else:
        print(a)
        my_list.append(a)
print(f'Итоговая последовательность: {my_list}')
print(f'Количество символов: {len(my_list)}')
# второй блок, функция cycle

i = 0
for el in cycle(my_list):
    if i > len(my_list) * 2:
        break
    else:
        print(i)
        i += 1
