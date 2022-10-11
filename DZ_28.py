
import math


def circle():
    r = float(input('Введите радиус круга: '))
    S = math.pi * r**2
    print('Площадь круга:',S,'\n')

def triangle():
    a = float(input('Введите сторону а: '))
    b = float(input('Введите сторону b: '))
    c = float(input('Введите сторону c: '))

    p = (a+b+c) / 2

    S = (p*(p-a)*(p-b)*(p-c))**0.5

    print('Площадь треугольника:',S,'\n')

def rectangle():
    a = float(input('Введите сторону а: '))
    b = float(input('Введите сторону b: '))

    S = a * b

    print('Площадь прямоугольника:',S,'\n')


while(True):

    print('введите запрос:')
    print('для площади круга          введите "с"')
    print('для площади треугольника   введите "t"')
    print('для площади прямоугольника введите "r"')
    print('для выхода введите пустую строку')

    match input():
        case 'c': circle()
        case 't': triangle()
        case 'r': rectangle()
        case '': break