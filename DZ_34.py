from DZ_33 import Animals, sea_animal, bird, arthropod

Polkan = Animals("Полкан")
Polkan.race("собака")
Polkan.age(5)

Polkan.print()


kit = sea_animal("blue whale", 550, 10)
kit.print()

eagle = bird("desert eagle", 9000, 4)
eagle.print()

shark = sea_animal()
shark.print()

#
# spider = arthropod("tarantul", 0.3, 0.1)
# spider.print()