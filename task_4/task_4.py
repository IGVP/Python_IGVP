"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

with open('my_test_4.txt', 'r', encoding='UTF-8') as my_f:
    # читаем файл, формируем список из элементов [фамилия ЗП] в виде строк
    my_list = my_f.read().split('\n')
print('Таблица сотрудников с окладами ниже 20.000:')
# объявляем переменные
i = 0 # № п.п.
poor_list = [] # Список сотурдников с ЗП менеее 20 т.
sum_total = 0 # фонд ЗП (для определения средней ЗП по сотрудникам)
# запускаем цикл по списку
for el in my_list:
    el = el.split() # формируем список по каждой строке исходного списка
    if float(el[1]) < 20000: # если второй едемент нового списка <20.000
        i += 1
        print(i, ' ', *el) # выодим на печать строку с фамилией и ЗП
        poor_list.append(el[0]) # формируем список сотрудников с ЗП < 20.000
    sum_total += float(el[1]) # ситаем фонд ЗП
# выводим результат на печать
print('Сотрудники с окладом менее 20.000:', *poor_list, '\n' f'Cредний оклад {round(((sum_total) / len(my_list)), 2)}')
