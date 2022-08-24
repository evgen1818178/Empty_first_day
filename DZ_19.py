# задача 1
#вводные

import random
list_size = 30
count_min_values = 5

range_min = -25
range_max = 25

rand_list = []
min_values = []
position = 0

for i in range(list_size):
    rand_list.append(random.randint(-99,99))
rand_list_copy = rand_list.copy()
rand_list_copy_2 = rand_list.copy()

for i in range(len(rand_list_copy_2)):
    while (rand_list_copy_2[i] > range_min) and (rand_list_copy_2[i] < range_max) and (rand_list_copy_2[i] != 0):
        rand_list_copy_2.pop(i)
        rand_list_copy_2.append(0)

while count_min_values > 0:
    for i in range(list_size):
        if i == 0:
            min_val = rand_list[i]
        else:
            if min_val > rand_list[i]:
                min_val = rand_list[i]
                position = i

    min_values.append(min_val)
    rand_list.pop(position)
    list_size -= 1
    count_min_values -= 1

print('исходный массив:',rand_list_copy)
print('минимальные значения из массива (задача 1):',min_values)
print('исключены элементы в диапазоне от',range_min,'до',range_max,'(задача 2):',rand_list_copy_2)






