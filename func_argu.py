#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add_end(L=[]):
    L.append('END')
    return L

print(add_end())
print(add_end())

def add_end_M(L=None):
    print('22',L)
    if L is None:
        L = []
    print('1',L)
    L.append('END')
    return L

print('2',add_end_M())
print('3',add_end_M())

def calc(numbers):
    sum=0
    for n in numbers:
        sum = sum + n
    return sum

print(calc([1,2,3]))
print(calc((13,5,7)))

def cals(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum
print(cals(1,2,3,4))
nums = [1,2,3]
print(cals(nums[0],nums[1],nums[2]))
print(cals(*nums))

def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
person('Michael',30)
person('Micheal',30,city='BeiJing')
person('Micheal',30,city='BeiJing',job='Engineer')
extra = {'city':'BeiJing','job':'Engineer'}
person('Micheal',30,**extra)

def person_D(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)
person_D('Jack',24,city='BeiJing',job='ChaoYang',zipCode=123123)
