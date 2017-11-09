def printxing(desc='desc'):
    print('**********'+desc+'**********')

# 形参*xxx, 不定参数
# 形参**xxx, 不定参数(key=value)
def showme(name, *args, **kvs):
    printxing('参数')
    print(name)
    print(args)
    print(kvs)

    printxing('循环1')
    # 循环
    for arg in args:
        print(arg)
    printxing('循环2')
    for kv in kvs:
        print(kvs[kv])

    printxing('类型')
    # 类型
    print(type(name))
    print(type(args))
    print(type(kvs))


showme('name',1,'2',[3,'4'],age=18,gender='f')

printxing('list')
items = []
# range(min,max(不包含),step)
for x in range(0,10,1):
    items.append(x)
print(items)
items = list(range(10))
print(items)
# 乘以2
items = [a*2 for a in range(10,0,-1)]
print(items)
# 平方
items = [a**2 for a in range(10,0,-1)]
print(items)
# 带条件
items = [a**2 for a in range(10,0,-1) if a>7]
print(items)

printxing('class')
class Me:
    age = 19
    def __init__(self,name='empty'):
        self.name = name
    def showname(self):
        return self.name
    # 静态方法
    @staticmethod
    def version():
        return 'v1.0'
me = Me('lhl')
print(me)
print(me.age)
print(me.name)
print(me.showname())
print( Me.version())
