#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = ['Michaer','Sarah','Tracy','Bob','Jack']

r = []
n = 3
for i in range(n):
    r.append(L[n-1-i])
print(r)

print(L[:3])
print(L[-2:-1])

print((list(range(100))))

T = list(range(100))
print(T[:10])

print(T[:10:2])
print(T[::5])