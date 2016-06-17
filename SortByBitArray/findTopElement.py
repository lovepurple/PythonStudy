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

	x[1] = x[1] | 30 使用位或
	 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0

	 (1) 把所有的数遍历，根据指定的index position 放入bitmap里
	 (2) bitmap的顺序就是实际数据的排序(类似桶排序),index的顺序是一组里的具体顺序
	 (3) 取出最后的个数，去原数组里查找对应的元素就是最后的排序结果

'''

import random

class findTopElements(object):
	__elementsArray=[]

	__bitmap = []

	"""docstring for findTopElements"""
	def __init__(self, elementsNum):
		super(findTopElements, self).__init__()
		self.elementsNum = elementsNum


	#生成随机数组
	def getShuffledArray(self):

		#在范围内生成不重复的随机数
		self.__elementsArray = random.sample(range(0,self.elementsNum * 10),self.elementsNum)
		return self.__elementsArray

	def _getBitmapPosition(self,num):
		return num //32		#Python 里 //才是取整！

	def _getIndexInBitmap(self,num):
		return num % 32

	def _getNumByPositionAndIndex(self,position,index):
		indexInElementArray = position * 32 + index

	def _buildBitmap(self,elements):
		#分配bitmap空间
		__bitmap =[ 0 for x in range(len(elements) + 1)]
		print(self.__bitmap)
"""
		for element in elements:
			bitmapPosition = self._getBitmapPosition(element)
			indexInBitmap = self._getIndexInBitmap(element)


			#使用 | 标识为有元素
			self.__bitmap[bitmapPosition] |= indexInBitmap
		return self.__bitmap
"""

	def getTopElements(self,topNum,bitmap= None):
		if bitmap is None:
			bitmap = self._buildBitmap(self.__elementsArray)

		print(bitmap)

"""		result = []
		for n in range(0,len(bitmap)):
			print(n)
"""





if "__name__ == __main__":
	f = findTopElements(1)
	shuffledElements = f.getShuffledArray()
	f.getTopElements(1)