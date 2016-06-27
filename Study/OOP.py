#Python 里的面向对象

class Student(object):

	def __init__(self,name,score):
		self.name = name
		self.score = score

	def print_score(self):
		print("%s:%s"%(self.name,self.score))

	def setScore(self,score):
		self.score = score

studentA = Student("Lovepurple",100)
studentA.setScore(1000)

studentA.print_score()

print(studentA.score)

print("--------------private and public ------------")

class  StudentWithPrivateMember(object):
	"""docstring for  StudentWithPrivateMember"""
	def __init__(self, name,score,grade):
		self.__name = name 		#__XXX开头的成员 是private的
		self.__score = score
		self.__grade = grade

	def print_score(self):
		print("%s:%s grade :%s"%(self.__name,self.__score,self.__grade))


privateStudent = StudentWithPrivateMember("LovePurple",100,"1601220117")
privateStudent.print_score()

#成员访问，由于是__XXX的 外部无法直接访问，可以定义getxxx setxxx读写
#print(privateStudent.__grade)

#Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
print(privateStudent._StudentWithPrivateMember__name)

#使用dir() 能获取对象所有的方法，属性

print("--------------------dir() -----------------------------------------------")
Tuple={"asdf",234,True}
print(dir(Tuple))

print("--------------instance attr and static attr --------------------------")

class  StudentWithStaticAttribute(object):
	staticName = "Dashabi"		#相当 于静态类，使用类名.属性名 访问

	"""docstring for  StudentWithStaticAttribute"""
	def __init__(self, name,score):
		super( StudentWithStaticAttribute, self).__init__()
		self.__name = name
		self.__score = score
	def print_score(self):
		print("%s:%s  staticAttribute :%s"%(self.__name,self.__score,StudentWithStaticAttribute.staticName))


studentC = StudentWithStaticAttribute("LovePurple",200)
studentC.print_score()


print(hasattr(studentC,'__name'))
print(dir(studentC))

print("----------------------------slot------------------------------------------------")

class StudentWithSlot(object):
	#定义slot,允许外部访问，格式是Tuple，也就是slots里的是类的实例
	#如果不是slot里 直接写 就跟上方的例子一样，类似于静态属性
	__slots__=('name','age')			#__slots__的属性只对实例起作用

s = StudentWithSlot()
s.name = "Love purple"		#绑定slots里枚举的属性
s.age = 26

#__slots__里没枚举，无效
#s.score = 100			


print("%s : %s "%(s.name,s.age))

s2 = StudentWithSlot()
s2.age = 20
s2.name = "Nimabi"		#如果不赋初始值 ，也会报错
print("%s : %s "%(s2.name,s2.age))
		

print("\n\n\n\n--------------------------------------@property-----------------------")

class StudentWithPropery(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

#使用@property 是读属性，相当于get
#使用@xxx.setter是写属性，相当于set

s3 = StudentWithPropery()

#通过@score.setter赋值
s3.score = 40
#直接get访问
print(s3.score)


print("\n\n\n\n--------------------------------------@property practice-----------------------")

class Screen(object):

	#设置成员变量的时候，一定要self.__XXX 一定要加self
	@property
	def screen_width(self):
		return self.__width

	@property
	def screen_height(self):
	    return self.__height

	@screen_width.setter
	def screen_width(self,value):
		self.__width = value;

	@screen_height.setter
	def screen_height(self,value):
		self.__height = value

	@property
	def resolution(self):
	    return str(self.__width) +"*" + str(self.__height)	

screen = Screen()
screen.screen_width = 1920
screen.screen_height = 1080
print(screen.resolution)		


print("\n\n\n ----------------------override __iter__ -------------------------------")
#定义__iter__方法 使对象可以被迭代
#需要同时重写__next__

#__getitem__ 可能把对象当成list

class Fib(object):

	def __init__(self):
		self.__a,self.__b = 0,1

	#迭代
	def __iter__(self):
		return self

	def __next__(self):
		temp = self.__a + self.__b
		self.__a = self.__b
		self.__b = temp

		if self.__a > 10000:
			raise StopIteration()
		return self.__b

	def __getitem__(self,n):
		if isinstance(n,int):
			self.__c = 1
			self.__d = 1
			for i in range(n):
				temp = self.__c + self.__d
				self.__c = self.__d
				self.__d = temp
			return self.__d

		#切片操作
		if isinstance(n,slice):
			_start = n.start
			_stop = n.stop

			if _start is None:
				_start = 0

			a,b=1,1
			L = []
			for x in range(_stop):
				if x >= _start:
					L.append(a)
				a,b = b,a+b
			return L

#raise 关键字
#python里空的关键字是None
#直接可以使用for 迭代Fib

for n in Fib():
	print(n)

f = Fib()

#直接使用[] 获取索引的值 
print(f[5])

print(f[5:10])







