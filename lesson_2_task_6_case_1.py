"""
6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.

Пример:

{
“названия”: [“компьютер”, “принтер”, “сканер”],
“цены”: [20000, 6000, 2000],
“количества”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

products = []
count = 1
title, price, amount = None, None, None
while True:

    if title is None:
        tmp = input('Введите название товара: ')
        if not tmp.isalpha():
            print('Наименование товара не может быть пустым и не должно быть пустым. Введите корректно.')
            continue
        title = tmp

    if price is None:
        tmp = input('Введите стоимость товара: ')
        if not tmp.isdigit():
            print('Цена должна быть числом. Введите корректно.')
            continue
        price = int(tmp)

    if amount is None:
        tmp = input('Введите количество: ')
        if not tmp.isdigit():
            print('Количество должно быть числом. Введите корректно.')
            continue
        amount = int(tmp)

    tmp = input('Введите единицы измерения без точки: ')
    if not tmp.isalpha():
        print('Единица изменерения не может быть пустой, не может быть числом. Попробуйте еще раз.')
        continue
    unit = tmp

    products.append((
        count,
        {
            'Название': title,
            'Цена': price,
            'Кол-во': amount,
            'Ед.изм': f'{unit}.'
        }
    ))

    title, price, amount = None, None, None
    count += 1

    print(products)

    q = input('Формирование списка завершено? (`Введите "y" для выхода, для продолжения нжмите Enter ) ')
    if q.lower() == 'y':
        break

print('Сформированный перечень:')

for el in products:
    print(el)