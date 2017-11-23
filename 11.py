from urllib import request
import chardet

# https 处理
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# url = 'https://yahoo.co.jp/'
from bs4 import BeautifulSoup

url = 'http://fund.eastmoney.com/fund.html'

response = request.urlopen(url)
rawdata = response.read()

# print(rawdata)
# 程序获取编码
encodingData = chardet.detect(rawdata)
encoding = encodingData['encoding']
print(encoding)

html = rawdata.decode(encoding)

soup = BeautifulSoup(html, "html.parser")
_totalPage = soup.find("div",id="pager").find("span","nv").get_text()
print(_totalPage)
# print(filter(str.isdigit, _totalPage))
totalPage = ''.join(filter(str.isdigit, _totalPage)) # _totalPage字符串遍历处理后在拼接字符串
print(totalPage)

# execjs 执行 js
import execjs
js = execjs.get()
result = js.eval("1+2")
print(result)
