from collections import Iterable,Iterator

#不包括:后面的索引

#List结构
L = ['Michael','Sarah','Tracy','Bob','Jack']


#从第0个取到第三个(不包括索引3)
E = L[0:3]
print(E)

#从第1个取到第三个
S=L[1:3]
print(S)

#从倒数第三个取到倒致第一个
A=L[-3:-1]
print(A)

#隔一个取一个
B=L[::2]
print(B)

#复制
C=L[:]
print(C)

print("-----------------------Tuple Operation---------------------------------")
#Tuple结构跟上面一样
Tuple=(1,2,3,4,5,'a',"love","purple")
print(Tuple)

A = Tuple[-4:-1]
print(A)

B = Tuple[2::]
print(B)

C = Tuple[::3]
print(C)

Tuple[0]

print("-----------------Tuple List Iterater operation------------------------------------------")
for ch in iter(B):
	print(ch)

for x in Tuple:
	print(x)

print("------------------------------------------------------------------")

for x,y in [(1,2),('a',1),("love purple",'true')]:
	print(x,y)


for key,value in {"a":1,"b":"purple"}.items():
	print(value)

#Tuple 是”一维“的 这里使用enumerate()将Tuple转化为迭代器
#i输出的信息有索引
for i in enumerate(Tuple):
	print(i)