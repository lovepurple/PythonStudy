# -*- coding: utf-8 -*-

"""
	1. Python里实现SocketServer
	2. multiprocessing 类里是Python多线程的库
		(1) 分配线程 process = multiprocessing.Process(handler,args)
		(2) multiprocessing.active_children() 里面有当前所有线程的集合
	3. 可以用C# 直接连接
"""

import socket
import multiprocessing

def msg_handle(connection,address):
	try:
		while True:
			data = connection.recv(1024)
			if len(data) > 0:
				print("received data :%r"%data)
	except:
		print("Exception ....")
	finally:
		connection.close()


class Server(object):
	def __init__(self,hostname,port):
		self.hostname = hostname
		self.port = port

	def start_server(self):
		self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.socket.bind((self.hostname,self.port))
		self.socket.listen(1)

		while True:
			#Python可以返回两个参数，Tuple格式
			conn,address = self.socket.accept()
			print("Got Connection.....")
			process = multiprocessing.Process(target=msg_handle,args=(conn,address))
			process.daemon = True
			process.start()

if __name__ == '__main__':
	server = Server("127.0.0.1",9000)
	server.start_server()

	for process in multiprocessing.active_children():
		process.terminate()
		process.join()