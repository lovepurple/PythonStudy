# -*- coding: utf-8 -*-

'''
	Python里关于md5 sha算法。。。都在 hashlib库里
	1. python 里 if判断 xxx is True / False
	2. python 里 可变参数的签名是(*args) 使用len可以获取长度
'''

import os,sys
import hashlib

def get_file_md5_hash(filepath):
	if os.path.isfile(filepath) is False:
		return "file not exist"

	with open(filepath,'rb') as f:
		filebinary = f.read()
		md5object = hashlib.md5()
		md5object.update(filebinary)
		filemd5code = md5object.hexdigest()
		return filemd5code

def get_file_sha1_hash(filepath):
	if os.path.isfile(filepath) is False:
		return "file not exist"

	with open(filepath,'rb') as f:
		filebinary = f.read()
		sha1object = hashlib.sha1()
		sha1object.update(filebinary)
		filesha1code = sha1object.hexdigest()

		return filesha1code

def comparefilebymd5(*filepaths):
	fileNum = len(filepaths)
	
	fileMd5List = []

	for i in range(0,fileNum):
		filePath = filepaths[i]

		if os.path.isfile(filePath) is False:
			return "file " + filePath +"not exist"

		filemd5code = get_file_md5_hash(filePath)
		fileMd5List.append(filemd5code)

	for i in range(0,fileNum):
		currentFileMd5 = fileMd5List[i]

		for j in range(fileNum - 1,fileNum):
			comparedFileMd5 = fileMd5List[j]

			if currentFileMd5 != comparedFileMd5:
				return False;

	return True;

def get_file_binary_length(filePath):
	if os.path.isfile(filePath) is False:
		return "file not exist"

	with open(filePath,'rb') as f:
		return len(f.read())

def get_file_binary_content(filePath):
	if os.path.isfile(filePath) is False:
		return "file not exist"

	with open(filePath,'rb') as f:
		return f.read()
def get_md5code(content):
	md5object = hashlib.md5()
	md5object.update(content)
	return md5object.hexdigest()
