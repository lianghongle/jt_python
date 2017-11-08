# 不需要设置类型，程序自动判断
# r 原样输出
# 字符串取字符（类数组方式）
name = r'\'梁宏乐'
print(name)
print(name[4])
print(name[1:2]) # 前包含，后不包含
print(len(name))

# 原样输出  '''内容'''
test = '''
I
    am
        what?
'''
print(test)

# 字符串*数字
str3 = '123' * 3
print(str3)

# 长字符串
strLong = ('111111111111111\n' \
          '111111111111')
print(strLong)

# 自定义函数
# 支持默认值
# 参数支持无序，按 key 对应
def showName(name = 'empty', age = 19):
    print(name+':'+str(age))

showName(age = 22, name='show')