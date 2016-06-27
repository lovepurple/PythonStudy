#__name__ 可以得到函数的名

import time

def now():
	print(time.strftime('%Y-%m-%d',time.localtime(time.time())))

func = now
func()

print("__name__  :%s"%func.__name__)

print("-----------------Decorator--------------------")

#用于扩展函数功能，还不破坏原函数
def log(func):
	def wrapper(*args,**kw):		#*args 表示可变长度参数
		print("call %s()" %func.__name__)
		return func(*args,**kw)
	return wrapper

#使用@注入(类似Java的Annotation)

@log
def nowDay():
	print(time.strftime('%Y-%m-%d',time.localtime(time.time())))

nowDay()

#python里标准的Decorator写法
print("--------------standard Decorator--------------------")


import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print("call %s():"%func.__name__)
		return func(*args,**kw)
	return wrapper
