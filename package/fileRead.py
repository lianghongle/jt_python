class fileReader:

    def __init__(self,_path):
        print("__init__")
        self.path=_path

    def __enter__(self):
        print("__enter__")
        return self

    def printme(self):
        print("printme")
        self.file=open(self.path)
        print(self.file.read())

    # 类似析构函数
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        print(str(exc_type)+str(exc_val)+str(exc_tb))
        if hasattr(self,"file"):
            self.file.close()
        return True # return true 不显示异常

with fileReader("./../files/test.txt") as fr:
        fr.printme()
