# coding=utf-8

from urllib import request

def testGetHtml():

    response = request.urlopen("http://fund.eastmoney.com/fund.html")
    html = response.read()

    # html = html.decode('gb2312')  #这一步是为啥？
    html = html.decode('gbk')  #这一步是为啥？
    html = html.strip()

    print(html)

    with open("./htmls/1.txt",'wb') as f:
        f.write(html.encode('utf8'))
        f.close()

# testGetHtml()

a = 10
print(a)
print(bin(a))               # 二进制 0b1010
print(format(a, 'b'))       # 去掉0b
print(int('1010', 2))       # 1010当作二进制，转化成10进制

print(chr(65))
print(ord('a'))

