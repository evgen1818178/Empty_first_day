


def CAPS(func):
    def wrapper():
        print("Привет", input('введите имя\n').upper())
    return wrapper





@CAPS
def privet():
    print("Привет", input('введите имя\n'))



privet()