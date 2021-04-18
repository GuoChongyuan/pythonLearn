class Employee:
    empCount = 0

    # __init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
    # self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
    def __init__(self,name,salary):
        self.name = name;
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print
        "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print
        "Name : ", self.name, ", Salary: ", self.salary

    def prt(self):
        print(self)
        print(self.__class__)

    def prt1(test):
        print(test)
        print(test.__class__)

if __name__ == '__main__':
    e = Employee(1,2)
    e.prt()

