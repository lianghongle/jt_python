# __doc__
# __name__
# __dict__

# 空类
class admin:
    pass

class User:

    def __init__(self,name='empty'):
        self.name = name

    def showname(self):
        return self.name

    def showMoney(self):
        return self.__money

    # 私有 __name
    __money = 0

    # 私有方法
    def __showMoney(self):
        return self.__money

    # 静态方法
    @staticmethod
    def version():
        return 'v1.0'


print(User.version())

user = User()

print(user.showMoney())

# print(user.__money) 私有，无法直接访问
print(user._User__money)
print(user._User__showMoney())
