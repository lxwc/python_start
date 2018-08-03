#1/usr/bin/env python3
# -*- coding: utf-8 -*-

def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
print(fact(1))

print(fact(3))

print(fact(100))

L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2

print(L)

