# 字符串不变性

def test(list):
    # id() 内存地址
    print(id(list))
    list.append(3)

list = []
test(list)
print(list)
print(id(list))

