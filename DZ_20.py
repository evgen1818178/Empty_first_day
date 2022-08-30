import random

matrix_x = 5
matrix_y = 8

lower_side = min(matrix_x,matrix_y)
matrix = []

#создание матрицы
for i in range(matrix_y):
    matrix_part = []
    for j in range(matrix_x):
        matrix_part.append(random.randint(-99,99))
    matrix.append(matrix_part)

#наименьший элемент диагонали
lower_element = matrix[0][0]
for i in range(lower_side):
    lower_element = min(lower_element,matrix[i][i])

#чило отриц элементов под диагональю
counter = 0
for i in range(matrix_x):
    for j in range(i):
        if matrix[i][j] < 0:
            counter += 1
if matrix_y > matrix_x:
    for i in range(matrix_x,matrix_y):
        for j in range(matrix_x):
            if matrix[i][j] < 0:
                counter += 1

print('Исходная матрица:')
for i in matrix:
    print(*[f"{x:>4}" for x in i])

print('Наименьший элемент в диагонали:',lower_element)
print(counter)