Xp = 0
Xn = 0

flip = True

while True:

    if flip:
        X = Xp
        Xp += 1
        flip = False
    else:
        X = Xn
        Xn -= 1
        flip = True

    if (X**3 - 300*X) == 2961:
        print(X)
        break
