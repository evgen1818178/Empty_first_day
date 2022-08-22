# задача 1
try:
    in_list = list(input('введите натуральное число: '))
    in_list = list(map(int, in_list))

    num_sum  = 0
    num_mult = 0
    for i in range(len(in_list)):
        num_sum += in_list[i]
        if i==0:
            num_mult = in_list[i]
        else:
            num_mult *= in_list[i]
    print('сумма цифр       :', num_sum)
    print('произведение цифр:', num_mult)

except:
    print('некорректный ввод')

# задача 2
try:

    start_val = int(input('введите начальное число: '))
    end_val   = int(input('введите конечное  число: '))
    step_val  = int(input('введите шаг            : '))

    out_string = ''

    while end_val >= start_val:
        out_string += str(start_val)
        out_string += ' '
        start_val += step_val

    print(out_string)

except:
    print('некорректный ввод')


