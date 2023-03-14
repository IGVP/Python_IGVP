"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(text):
    # Задаем функицю получения строки
    # Проверка на вхождение в алфавит, ошибка ввода - выход
    if not text.isalpha():
        print('Слова должны содержать только строчные латинские буквы,'
              'запустите программу повторно и корректно  осуществите ввод!')
        quit()
    # Проверка на вхождение в нижний регистр (строчные буквы), ошибка ввода - выход
    elif not text.islower():
        print('Слова должны содержать только строчные латинские буквы, '
              'запустите программу повторно и корректно  осуществите ввод!')
        quit()
    # Проверка на вхождение в кодировку ascii (исключение кирилицы), ошибка ввода - выход
    elif not text.isascii():
        print('Слова должны содержать только строчные латинские буквы, '
              'запустите программу повторно и корректно  осуществите ввод!')
        quit()
    else:
        res = text.title()

    # Возвращаем результат
    return res


# Обозначаем первый блок
print('Перевод к формату: первая заглавная / остальные - строчные буквы:')
# Вызываем функцию
print(int_func(text=input('Введитe слово: ')))
# Отделяем блоки
print("")
# Блок 2
print('Введите строку слов через пробел строчными буквами')
# Формируем список для дальнейшей работы
my_list = input('Введите слова через проблел: ').split()
# запускаем цикл по замене слов с использвоанием функции int_func(text)
i = 0
for el in my_list:
    my_list.insert(i, int_func(el))
    my_list.pop(i + 1)
    i += 1
# Выводим на печать список (трансформируем для читаемости)
print(*my_list)
