import os

f=None
try:
    f = open(os.path.dirname(__file__) + "/files/test.txt")  #因为这个文件不存在
    print(f.read())
except:
    print("找不到这个文件")
finally:
    if f is not None:
        f.close()
