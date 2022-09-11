
# Задача 1
with open("class.txt",encoding='utf-8') as file:
    marks_sum = marks_count = 0
    for line in file.readlines():
        line = line.rstrip("\n")
        marks_count += 1
        line_list = line.split()
        mark = int(line_list[-1])
        marks_sum += mark
        if mark < 3:
            print("Ученик, чья оценка меньше 3-х:", line[:-1])
print("Средний бал по группе:", marks_sum / marks_count)

print()

# Задача 2
print('Открыт файл write_file.txt для записи вводимых строк')
print('для выхода введите пустую строку')
with open("write_file.txt",'a',encoding='utf-8') as file:
    line = 'a'
    while line != '':
        line = input()
        file.writelines(line + '\n')