# -*- coding: utf-8 -*-
"""
	1. decorator就是wrap,参数是原函数，把原函数包一层
	2. decorator 就是Java里的面向切面编程思想
	3. decorator 参数问题，decorator可传递参数，被包装的还有参数
	4. decorator 会有性能问题（貌似Python本身就不注重性能，爽就行）
	5. decorator 使用多了Debug会更困难
"""

def my_decorator(function_to_decorator):

	#wrap 函数

	def wrapper_around_the_origin_function():
		print("Before the function ")

		function_to_decorator()

		print("After the function")

	#返回包装函数
	return wrapper_around_the_origin_function


def test_origin_function():
	print("origin function")


function_after_decorator = my_decorator(test_origin_function)

#函数并没调用
print(function_after_decorator)

#调用wrap
function_after_decorator()

print("\n--------------------")
#Python 一切都是对象，把decorator 指向原函数，就看不出来原函数被wrap

test_origin_function = my_decorator(test_origin_function)
test_origin_function()


print("\n --------------use @ in python-------------------------")

#使用@....类之后，就相当于先执行了my_decorator，然后再执行原函数
#原理跟上方的示例一样

# another_origin_function = my_decorator(another_origin_function)  跟下面的写法一致
@my_decorator
def another_origin_function():
	print("another function")

another_origin_function()


print("\n  -------------------- multy decorator-----------")


def function_decoratorA(function_to_decorator):

	def wrap():
		print("decorator A ")

		function_to_decorator()

	return wrap


def function_decoratorB(function_to_decorator):

	def wrap():
		print("decorator B")

		function_to_decorator()


	return wrap

@function_decoratorA
@function_decoratorB
def origin_function():
	print("origin fun......")


origin_function()

#output:
#		decorator A
#		decorator B
#	 	origin fun .....

# 流程:
#		origin_function = function_decoratorA(origin_function)
#		origin_function = function_decoratorB(origin_function)
#		origin_function()

print("-----------------decorator with args ------------------\n")

#传递参数（签名需要跟被包装的一致）


def decorator_passing_arguments(function_to_decorator):

	def wrapper_acception_arguments(arg1,arg2):
		print("wrapper acception arg %s ,%s"%(arg1,arg2))

		function_to_decorator(arg1,arg2)

	return wrapper_acception_arguments


@decorator_passing_arguments
def print_full_name(firstname,lastname):
	print("my name is %s %s"%(lastname,firstname))

print_full_name("guangze","song")

print("\n")

#这个例子里就是闭包操作，可以访问decorator_arg1 ...

def decorator_with_arguments(decorator_arg1,decorator_arg2):
	print("decorator accept arguments:%s,%s"%(decorator_arg1,decorator_arg2))

	def my_decorator(function_to_decorator):
		print("I am the decorator. Somehow you passed me arguments:%s, %s" %(decorator_arg1,decorator_arg2))  


		#函数里又套入函数
		def wrapped(function_arg1,function_arg2):
			print("I am the wrapper around the decorated function ,decorator args %s,%s, function args %s,%s"%(decorator_arg1,decorator_arg2,function_arg1,function_arg2))

			#注意参数 别乱了
			return function_to_decorator(function_arg1,function_arg2)

		#返回的是wrapped函数,闭包，返回的的是wrapped,在外部已经访问不到decorator_arg1,decorator_arg2,但是调用wrapped的时候，虽然可以访问到最外层传入的参数
		return wrapped

	return my_decorator


@decorator_with_arguments("Leonard","Sheldon")
def decorated_function_with_arguments(function_arg1,function_arg2):
	print("I am the decorated function and only nkonws about my arguments:{0} {1}".format(function_arg1, function_arg2))

decorated_function_with_arguments("A","B")


#functools里提供wrap
print("\n-------------------- functiontools---------------")

import functools

def bar(func):

	#将func wrap
	@functools.wraps(func)
	def wrapper():
		print("bar")
		return func()
	return wrapper

@bar
def foo():
	print("foo")

foo()

"""
	执行顺序：
		foo = bar(foo)

"""