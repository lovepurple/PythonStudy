# -*- coding: utf-8 -*-
#Python 里的单例写法，基于decorator

#cls 的意思是，使用的是Class.Method() 约定的写法

def singleton(cls):
	instances = {}
	def wrapper():
		if cls not in instances:
			instances[cls] = cls()
		return instances[cls]
	return wrapper


#@singleton
class myclass:
	def __init__(self):
		self.num = 0

myclass = singleton(myclass)

c1 = myclass()
print(c1.num)
c1.num +=1

c2 = myclass()
print(c2.num)

print(c1 == c2)
