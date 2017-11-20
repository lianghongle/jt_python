from bs4 import BeautifulSoup

with open("./htmls/1.txt", 'rb') as f:
    html = f.read().decode('utf8')
    f.close()

soup = BeautifulSoup(html, "html.parser")
fCodes = soup.find("table", id="oTable").tbody.find_all("td", "bzdm")  # 基金编码
result = ()
for fCode in fCodes:
    result += ({
                   "code": fCode.get_text()
                   , "name": fCode.next_sibling.find("a").get_text()
                   , "NAV": fCode.next_sibling.next_sibling.get_text()
                   , "ACCNAV": fCode.next_sibling.next_sibling.next_sibling.get_text()
               },)
print(result)
