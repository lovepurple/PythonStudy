# -*- coding: utf-8 -*-
#使用更方便的方式创建List

from collections import Iterable

A = list(range(1,50))
print(A)

#函数式编程
B = [x * x for x in range(1,10)]
print(B)

print("--------------全排列------------------")
C = [m + n for m in "ABC" for n in "XYZ"]
print(C)

print(isinstance(1224,bool))


L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[x.lower() for x in L1 if isinstance(x,str)]
print(L2)

print("------------yield --------------")

def odd():
	print("step 1")
	yield 1
	print("step 2")
	yield 3
	print("setp 3")
	yield 5

#跟C#里的yield 类似 
o=odd()
next(o)
next(o)
next(o)

print("------------yang -------------")
L = [1]
"""

while True:
	yield L
	L = [L[n-1] + L[n] for n in range(len(L))]
	L.append(1)
	L[0] = 1
"""
print(isinstance(L,Iterable))