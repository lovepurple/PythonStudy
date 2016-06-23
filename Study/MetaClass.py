# -*- coding: utf-8 -*-

"""
	1. Python 里，类也是对象
	2. type()动态创建类，type(name,bases,dict)   (类名，继承，字典)
	3. metaclass就是用来创建类的，type()
	4. __class__属性
	5. __metaclass__属性，
	6. type就是一个类（int str）
	7. __new__ 在 __init__之前被调用
	8. __init__ 用来将传入的参数初始化给对象(相当于构造函数)
	
"""

#动态创建类

def choose_class(classname):
	if classname == "dynamicClass":
		class DynamicClass(object):
			pass

		return DynamicClass
	else:
		class DymaincClass2(object):
			pass

		return DymaincClass2


dynamicclass = choose_class("dynamicClass")
print(dynamicclass)
#output:<class '__main__.choose_class.<locals>.DynamicClass'> 
#这里返回的类，而不是类的实例

#创建类的实例
dynamicClassInstance = dynamicclass()
print(dynamicClassInstance)
# output:<__main__.choose_class.<locals>.DynamicClass object at 0x01D16B90> 

print('------------------------------------------------')
print('\n')

#type() ，有点类似C#的

print(type(1))
print(type("nimabi"))
print(type(choose_class))
print(type(dynamicclass))
print(type(dynamicClassInstance))
print("\n")

print("-----------dynamic create class by type(name,bases,dict)----------")

class MyShinyClass(object):
	pass

classByType = type("MyShinyClass",(),{})

#两个效果相同，
print(classByType)	#是类，不是类的实例
print(MyShinyClass)

classByTypeInstance = classByType()
print(classByTypeInstance)

#接受参数
class Foo(object):
	pass

#相当于给属性的初始值 用第三个参数指定的
classByType = type("Foo",(),{'bar':True,'xxx':10})
instance = classByType()
print(instance.bar)
print(instance.xxx)

#继承
class FooChild(Foo):
	pass

def echo_bar(self):
	print(self.bar)

#第二个参数的写法(xxx,) 是一个Tuple
#第三个参数扩展了子类里的方法
childClass = type("FooChild",(Foo,),{'echo_bar':echo_bar})
print(hasattr(Foo,'echo_bar'))
print(hasattr(childClass,'echo_bar'))



print("\n --------------------__metaclass__ ------------------------")

"""
	1.当类里有__metaclass__时，Python用这种方法创建类，如果没有就使用type创建
"""

def upper_attr(future_class_name,future_class_parent,future_class_attr):
	attrs = ((name,value) for name,value in future_class_attr.items() if not name.startswith('__'))

	#Python 里的函数式模式
	uppercase_attr = dict((name.upper(),value) for name,value in attrs)
	print("")

	return type(future_class_name,future_class_parent,uppercase_attr)

#作用到这个模块中的所有类
__metaclass__ = upper_attr


class Foo2(object):
	#在这里定义__metaclass__ 只会作用到这个类
	__metaclass__ = upper_attr
	bar = 'bip'

print(hasattr(Foo,'echo_bar'))


