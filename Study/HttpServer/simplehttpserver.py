# -*- coding: utf-8 -*-

from http.server import HTTPServer,BaseHTTPRequestHandler
import shutil

class MySimpleHttpServer(BaseHTTPRequestHandler):

	def do_GET(self):
		encoding = "UTF-8"
		responseContent = "Hello World"
		self.send_header("Content-type", "text/html; charset=%s"% encoding) 
		self.send_header("Content-Length",len(responseContent))
		self.end_headers()
		self.wfile.write(bytes(responseContent,encoding="utf8"))

		httpd = HTTPServer(('',9080),MySimpleHttpServer)
		httpd.serve_forever()
