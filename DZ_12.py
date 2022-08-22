
import datetime

Err_flag = False

for i in range(2):

    if Err_flag:
        break

    print('Для персоны', i+1)
    date = input('введите дату рождения в формате dd.mm.yyyy: ')
    date_list = date.split(".")

    try:
        date_list = map(int, date_list)
        date_list = list(date_list)
        if len(date_list) != 3:
            print('ввод в неправильном формате')
            Err_flag = True
    except:
        if not(Err_flag):
            print('ввод в неправильном формате')
        Err_flag = True

    if not(Err_flag):
        try:
            if i==0:
                date_1 = datetime.date(date_list[2], date_list[1], date_list[0])
            else:
                date_2 = datetime.date(date_list[2], date_list[1], date_list[0])
                days_diff = (date_1 - date_2)
                if days_diff.days < 0:
                    print('Персона 1 старше')
                else:
                    print('Персона 2 старше')
        except:
            if not (Err_flag):
                print("некорректная дата")
            Err_flag = True



