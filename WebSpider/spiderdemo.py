# -*- coding: utf-8 -*-
"""
	urllib 库里包括常用的url对象接口
	1. python3 里urllib urllib 都归并到urllib.里
"""

"""
from Lib.urllib import request
from Lib.urllib import response
from Lib.urllib import parse


# 直接抓网页内容
response = request.urlopen("http://www.mafengwo.cn")


#send post requset
values = {"username":"sgz115@gmail.com","password":"xxxxx"}
data = parse.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
postRequest = request.Request(url,data)
postResponse = request.urlopen(postRequest)

print(postResponse.read())
"""

# send get requset

from urllib import parse
from urllib import request
from urllib import response

sendvalues = {}
sendvalues["username"] = "sgz115@gmail.com"
sendvalues["password"] = "xxx"

data = parse.urlencode(sendvalues)
url = "http://www.mafengwo.cn/?"+data 

"""
http_get_request = request.Request(url)
http_get_response = request.urlopen(http_get_request)
print(http_get_response.read())
"""
print(url)
print(request.urlopen(url))

""" post
data = parse.urlencode(sendvalues).encode(encoding="utf-8")
url = "http://www.csdn.net"
httprequest = request.Request(url,data)
httpresponse = request.urlopen(url,data)
print(httpresponse.read())
"""

