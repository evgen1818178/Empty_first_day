# задача 1 с треугольником
# треугольник будет существовать если ниодна из сторон не больше суммы оставшихся

a = 0.1
b = 0.2
c = 0.2

if (a > b+c) or (b > a+c) or (c > a+b) :
    print('not exist')
else:
    print('exist')



# задача 2
year = 28

t1 = year % 10
t2 = year % 100

if (t1 == 1 and t2 != 11):
    let = 'год'
elif (t1 >= 2 and t1 <= 4 and (t2 < 10 or t2 >= 20)):
    let = 'года'
else:
    let = 'лет'

print('мне', str(year), let)



