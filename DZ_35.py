from abc import abstractmethod

class Animals:
    def __init__(self):
        pass

    def print(self):
        pass

class sea_animal(Animals):
    def __init__(self, name = 'unknown', max_depth = 'unknown', age = 'unknown', race = 'unknown'):
        self.race = race
        self.name = name
        self.age = age
        self.max_depth = max_depth
        self.type = 'морские'

    def print(self):
        print()
        print("Имя    :",self.name)
        print("возраст:",self.age)
        print('животное относится к типу:',self.type)
        print('глубина плавания:',str(self.max_depth)+'м')

class bird(Animals):
    def __init__(self, name = 'unknown', max_altitude = 'unknown', age = 'unknown'):
        self.name = name
        self.age = age
        self.max_altitude = max_altitude
        self.type = 'птицы'

    def print(self):
        print()
        print("Имя    :",self.name)
        print("возраст:",self.age)
        print('животное относится к типу:',self.type)
        print('высота полёта:',str(self.max_altitude)+'м')

class arthropod(Animals):
    def __init__(self, name = 'unknown', lifetime = 'unknown', age = 'unknown'):
        self.name = name
        self.age = age
        self.lifetime = lifetime
        self.type = 'членистоногие'

    def print(self):
        print()
        print("Имя    :",self.name)
        print("раса   :",self.race)
        print("возраст:",self.age)
        try:
            if isinstance(self.type, str):
                print('животное относится к типу:',self.type)
        except:
            print("тип животного не обозначен")
