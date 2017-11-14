# 引用

# 第一种
# import functions
# print(functions.name)
# functions.showFuns("test")

# 第二种
# from functions import * 引用所有
# from functions import showFuns
# showFuns("from x import y")

# 包
from package.functions import *
showFuns("package")

# sys 系统
import sys
print(sys.version)
print(sys.path)

# 以字典形式返回当前局部符号表
# print(locals())

# 以字典形式返回当前全局符号表
# print(globals())

