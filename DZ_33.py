
class Animals:
    def __init__(self, name):
        self.name = name

    def __race(self, race):
        self.race = race

    def _age(self, age):
        self.age = age

    def print(self):
        print("Имя    :",self.name)
        print("раса   :",self.race)
        print("возраст:",self.age)
        try:
            if isinstance(self.type, str):
                print('животное относится к типу:',self.type)
        except:
            print("тип животного не обозначен")
        print()

class sea_animal(Animals):
    def __init__(self, name, max_depth, age):
        self.name = name
        self.age = age
        self.max_depth = max_depth
        self.type = 'морские'
    def print(self):
        print("Имя    :",self.name)
        print("возраст:",self.age)
        print('животное относится к типу:',self.type)
        print()

class bird(Animals):
    def __init__(self, name, max_altitude, age):
        self.name = name
        self.age = age
        self.max_altitude = max_altitude
        self.type = 'птицы'

class arthropod(Animals):
    def __init__(self, name, lifetime, age):
        self.name = name
        self.age = age
        self.lifetime = lifetime
        self.type = 'членистоногие'







# Polkan = Animals("Полкан")
# Polkan.race("собака")
# Polkan.age(5)
#
# Polkan.print()