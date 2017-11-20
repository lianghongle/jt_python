from bs4 import BeautifulSoup
from urllib import request
from datetime import datetime

# 抓取网页
response = request.urlopen("http://fund.eastmoney.com/fund.html")
html = response.read()
html = html.decode('gb2312')  # 这一步是为啥？
with open("./htmls/1.txt", 'wb') as f:
    f.write(html.encode('utf8'))
    f.close()

with open("./htmls/1.txt", 'rb') as f:
    html = f.read().decode('utf8')
    f.close()

soup = BeautifulSoup(html, "html.parser")
fCodes = soup.find("table", id="oTable").tbody.find_all("td", "bzdm")  # 基金编码
result = ()
for fCode in fCodes:
    result += ({"fcode": fCode.get_text()
                   , "fname": fCode.next_sibling.find("a").get_text()
                   , "NAV": fCode.next_sibling.next_sibling.get_text()
                   , "ACCNAV": fCode.next_sibling.next_sibling.next_sibling.get_text(),
                "updatetime": datetime.now().isoformat(sep=' ', timespec="seconds")}
               ,)
print(result)

import pymysql
from pymysql.cursors import Cursor, SSCursor
from common.config import dbconfig

connection = pymysql.connect(**dbconfig)

cursor = Cursor(connection)
cursor.executemany("""
insert into myfund(fcode, fname, NAV, ACCNAV, updatetime)
values(%(fcode)s,%(fname)s,%(NAV)s,%(ACCNAV)s,%(updatetime)s)
ON duplicate KEY UPDATE `updatetime`=%(updatetime)s, NAV=%(NAV)s, ACCNAV=%(ACCNAV)s
""", result)
connection.commit()
connection.close()
