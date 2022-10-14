
class Person:
    def __init__(self, name, age):
        self.age = int(age)
        self.name = name

    def hello(self):
        print("Привет",self.name,"ваш возраст",self.age)

person1 = Person("некий чел 1",1)
person2 = Person("некий чел 2",2)
person3 = Person("некий чел 3",3)
person4 = Person("некий чел 4",4)
person5 = Person("некий чел 5",5)


person1.hello()
person2.hello()
person3.hello()
person4.hello()
person5.hello()