"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open('my_test_2.txt') as my_job:
    line_cnt = 0
    world_cnt = 0
    for line in my_job:
        line_cnt += 1
        world_cnt += len(line.split())
        print(f'Строка №: "{line_cnt}", Кол-во слов с троке: "{len(line.split())}", текстк в строке : "{line}"')
print(f'Количество строк: {line_cnt}')
print(f'Количество слов во всех строках: {world_cnt}')
