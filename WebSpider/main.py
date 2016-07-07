# -*- coding: utf-8 -*-
"""
	抓糗事百科

	bytes 转换到string 
	bytes.decode(encoding='utf-8')
	str(byte,encoding='xxx')

"""

import urllib.request
import urllib.parse

page = 1
url = "http://www.qiushibaike.com/hot/page/" + str(page)

try:
    httprequest = urllib.request.Request(url)
    httprequest.add_header(
        "User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36")
    httpresponse = urllib.request.urlopen(httprequest)

    response_content = httpresponse.read()


    # 下面两个方法等价
    # print(response_content.decode())
    print(str(response_content, 'utf-8'))

except urllib.error.URLError as e:
    print(e)
