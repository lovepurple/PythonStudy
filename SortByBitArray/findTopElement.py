# -*- coding: utf-8 -*-

''' 在大量数组里取出前100个数的算法，
    1. 可以使用HeapSort,空间上有优势
    2. 可以使用多线程，把大数组分成小的，然后对每个小的数组使用排序（分冶）
    	把结果每个取出100个，在主线程把所有的结果汇总，再进行一次排序，取出前100个数就是结果
        速度可以很快，但相对空间开销较大
    3. 使用位图（类似桶排序）
'''

'''
	使用int[] 储存所有排序好的数的索引 
	一个int是32bit

	int[0] = 62

	index = 62 / 32 = 1   
	bit_index = 62 % 32 = 30

	!!!!!
		设置指定的位
		获取指定的位
		指定的位是否存在数

	x[1] = x[1] | 30 使用位或
	 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0

	 (1) 把所有的数遍历，根据指定的index position 放入bitmap里
	 (2) bitmap的顺序就是实际数据的排序(类似桶排序),index的顺序是一组里的具体顺序
	 (3) 取出最后的个数，去原数组里查找对应的元素就是最后的排序结果

	 2016-6-20 17:31:502 终于对了，你妈了个逼的

'''

import random

class findTopElements(object):
	_elementsArray=[]

	__bitmap = []

	"""docstring for findTopElements"""
	def __init__(self, elementsNum):
		super(findTopElements, self).__init__()
		self.elementsNum = elementsNum


	#生成随机数组
	def getShuffledArray(self):
		#在范围内生成不重复的随机数
		self._elementsArray = random.sample(range(0,self.elementsNum * 10),self.elementsNum)
		return self._elementsArray

	def _getBitmapPosition(self,num):
		return num //32		#Python 里 //才是取整！

	def _getIndexInBitmap(self,num):
		return num % 32

	def _getNumByPositionAndIndex(self,position,index):
		indexInElementArray = position * 32 + index
		
		return indexInElementArray

	def _buildBitmap(self,elements):
		#分配bitmap空间
		self.__bitmap =[ 0 for x in range(len(elements) + 1)]
		
		for element in elements:
			bitmapPosition = self._getBitmapPosition(element)
			indexInBitmap = self._getIndexInBitmap(element)

			self.__bitmap[bitmapPosition] = self.set_bit(self.__bitmap[bitmapPosition],indexInBitmap)
			
		return self.__bitmap



	#按位设置的算法
	def set_bit(self,num,index,flag=True):
		if index > 31 or index < 0:
			raise ValueError("index error:index:%d"%index)

		#确定Offset
		bitIndex = 1 if index ==0  else 2<< (index -1)

		#设置的核心方法
		return (num | bitIndex) if flag else (num & ~bitIndex)

	#获取指定的位上的值
	def get_bit(self,num,index):
		if index > 32 or index < 0:
			raise ValueError("index error:index %d"%index)

		return 1 if (num & 1<<index) else 0

		

	def getTopElements(self,topNum,bitmap= None):
		if bitmap is None:
			bitmap = self._buildBitmap(self._elementsArray)

		result = []

		#反向遍历bitmap
		for bitmapIndex in reversed(range(0,len(bitmap))):

			bitnum = bitmap[bitmapIndex]

			if bitnum == 0:
				continue

			for byteindex in reversed(range(0,32)):
				if self.get_bit(bitnum,byteindex) == 1 :
					originNum = self._getNumByPositionAndIndex(bitmapIndex,byteindex)
					
					result.append(originNum)
					
					#result.append(originNum)
					if result is not None and len(result) >= topNum:
						return result
					

		return result




if "__name__ == __main__":
	f = findTopElements(100000)

	shuffledElements = f.getShuffledArray()

	print("origin element list :%s"%shuffledElements)

	result =f.getTopElements(10)
	print("element after bitmap sort%s"%result)

