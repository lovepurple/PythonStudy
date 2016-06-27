from functools import reduce
from collections import Iterator

#map/reduce

#map(function,iterator) 将iterator里的每一个元素进行function的操作，返回L1操作后的结果集
#reduce(function,iterator) 将iterator里的元素进行function操作，然后把操作的结果和iterator的下一个元素再进行function的操作，
#	最后操作后的结果返回。

def normailze(name):
	return str.capitalize(name)

L1 = ["adam","LISa","BasseT"]
L2 = list(map(normailze,L1))
print(L2)

print("----------------practice 2------------------")

def mutiply(a,b):
	return  a*b;

def prod(L):
	 return reduce(mutiply,L)

def prodWithLambda(L):
	return reduce(lambda x,y:x*y,L)		#使用Lambda 关键字，匿名函数的写法，不需要定义外部函数，类似C# 里的 ()=>{}写法

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
print("lambda operation " + "3* 5 * 7 * 9 = ",prodWithLambda([3,5,7,9]))

print("-------------practice 3---------------")


"""
def str2float(s):
	L = map(lambda x:int(x),s)
"""
"""
strNum = "123.456"
L = strNum.split('.')
L0 = L[0]
L1 = L[1]

def toInt(T):
	tLen = len(T)
	return reduce(lambda x,y,position: x*(tLen - position) + y,1,2,3)

print(toInt(L0))
"""

"""
print("--------------------------------filter---------------------------")		 


RangeList = list(range(1,100))

def not_divisible(n):
	return lambda x:x%n >0

def primes():
	yield 2
	it = RangeList()
	while True:
		n = next(it)
		yield n
		it = filter(not_divisible(n),it)

for n in primes():
	if n < 1000:
		print(n)
	else:
		break
"""

print("--------------------lambda 嵌套 ---------------")

def action(n):
	return  lambda y:n +y;

a = action(10)
print(a(1))

print("---------------yield & filter  operation --------")


def is_palindrome(n):
	numStr = str(n)
	numLenght = len(numStr)
	middleIndex = numLenght / 2 

	if middleIndex < 1:
		return False;
	else:
		for i  in range(middleIndex):
			if numStr[i] != numStr[numLenght-i-1]:
				return False
			elif i == middleIndex -1:
				return True
			else:
				return False

output = filter(is_palindrome,range(1,11000))
print(list(output))

print("---------------sorted -------------------------")
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return len(t[0])

#对于sorted排序的值，传入的t相当于('Bob',75)  而t[0] 就是Bob t[1]=75
print(sorted(L,key=by_name,reverse=True))

