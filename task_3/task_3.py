"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open('my_test_3.txt', 'r', encoding='UTF-8') as file_en:
    text_en = file_en.read()

text_ru = text_en

for x, y in dictionary.items():
    text_ru = text_ru.replace(x, y)

with open('my_test_3_ru.txt', 'w', encoding='UTF-8') as file_ru:
    file_ru.write(text_ru)
