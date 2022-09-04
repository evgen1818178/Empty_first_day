import random

#Задача 1
pack_1 = {'Wowmaking','iTechArt Group','IT-Academy','TESLASUIT','Nominal Techno','ScienceSoft','BelPrime Solutions','iT-eLab'}
pack_2 = {'TESLASUIT','LogicNow','INSPIRATIV','IBT Company','Isec-System','Itexus','Wowmaking','iTechArt Group','IT-Academy'}
print(pack_1 & pack_2)


#Задача 2
n = 9
size = 10

massive = []
for i in range(n):
    set_1 = set()
    while (len(set_1) < size):
        set_1.add(random.randint(0,20))
    massive.append(set_1)
    print('Множество','№'+str(i+1)+':',set_1)

demo_string = ''
temp = massive[2].copy()
for i in range(3,len(massive)+1,3):
    temp = temp & massive[i-1]
    for j in (massive[0] & massive[i-1]):
        temp.discard(j)
    demo_string += str(i) + ', '

print()
print('элементы входящие в множества №',demo_string,'исключая множество 1')
print(temp)