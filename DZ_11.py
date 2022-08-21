
import datetime
today = datetime.date.today()

date = input('введите дату рождения в формате dd.mm.yyyy: ')
date_list = date.split(".")
Err_flag = False

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
        some_date = datetime.date(date_list[2], date_list[1], date_list[0])
        days_diff = (today - some_date)
        age = days_diff.days // 365
        print('Количество полных лет:',age)
    except:
        if not (Err_flag):
            print("некорректная дата")
        Err_flag = True


