# 装饰器

def showMan(name):
    def showMe(other_func):
        prefix='我的名字是'
        def showName(*args, **kwargs):
            print(prefix+name)
            other_func(*args, **kwargs)
        return showName
    return showMe

@showMan("www")
def showAge(age):
    print(str(age)+"岁")


# showAge = showMe(showAge)
# showAge(11)   # showMe就是showAge 的装饰器, 通过"包裹"则执行了真正的业务

showAge(12)