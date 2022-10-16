

def fun(x,c):
    a = x % 10
    c += a
    if a == x:
        return x,c
    else:
        return fun(x//10,c)

print(fun(int(input()),0)[1])
