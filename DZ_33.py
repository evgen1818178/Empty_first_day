
class Animals:
    def __init__(self, name = 'unknown'):
        self.name = name

    def race(self, race = 'unknown'):
        self.race = race

    def age(self, age = 'unknown'):
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
    def __init__(self, name = 'unknown', max_depth = 'unknown', age = 'unknown'):
        self.name = name
        self.age = age
        self.max_depth = max_depth
        self.type = 'морские'
    def print(self):
        print("Имя    :",self.name)
        print("возраст:",self.age)
        print('животное относится к типу:',self.type)
        print('глубина плавания:',str(self.max_depth)+'м')
        print()

class bird(Animals):
    def __init__(self, name = 'unknown', max_altitude = 'unknown', age = 'unknown'):
        self.name = name
        self.age = age
        self.max_altitude = max_altitude
        self.type = 'птицы'

    def print(self):
        print("Имя    :",self.name)
        print("возраст:",self.age)
        print('животное относится к типу:',self.type)
        print('высота полёта:',str(self.max_altitude)+'м')
        print()

class arthropod(Animals):
    def __init__(self, name = 'unknown', lifetime = 'unknown', age = 'unknown'):
        self.name = name
        self.age = age
        self.lifetime = lifetime
        self.type = 'членистоногие'







# Polkan = Animals("Полкан")
# Polkan.race("собака")
# Polkan.age(5)
#
# Polkan.print()