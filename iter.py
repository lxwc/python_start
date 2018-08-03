#!/usr/bin/env pythin3
# -*- coding: utf-8 -*-

d={'a':1,'b':2,'c':3}

for key in d:
    print(key)

for value in d.values():
    print(value)

for k,v in d.items():
    print(k,'=',v)

#from collections import Iterable
#isinstance('abc',Iterable)
#isinstance(123,Iterable)
#isinstance([1,2,3],Iterable)

for i,value in enumerate(['A','B','C']):
    print(i,'=',value)

for x,y in [(1,1),(2,4),(3,9)]:
    print(x,':',y)