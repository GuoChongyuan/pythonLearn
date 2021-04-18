class Parent:  # 定义父类
    parentAttr = 100

    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print('调用父类方法')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("父类属性 :", Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print("调用子类的构造函数")

    def parentMethod(self):
        super().parentMethod()
        print("方法override")

    def childMethod(self):
        print("调用子类方法")

if __name__ == '__main__':
    c = Child()          # 实例化子类
    c.childMethod()      # 调用子类的方法
    c.parentMethod()     # 调用父类方法
    c.setAttr(200)       # 再次调用父类的方法 - 设置属性值
    c.getAttr()          # 再次调用父类的方法 - 获取属性值
