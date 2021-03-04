class Person:
    __username = None
    __age = None
    __high = None
    __sex = None

    #构造方法：帮助完成一个对象的初始化
    def __init__(self, username, age, sex, high):
        self.__username = username
        self.__age = age
        self.__sex = sex
        self.__high = high

    def setUsername(self, username):
        self.__username = username

    def getUsername(self):
        return self.__username

    def setAge(self,age):
         self.__age = age

    def getAge(self):
        return self.__age

    def setHigh(self,high):
        self.__high = high

    def getHigh(self):
        return self.__high

    def setSex(self,sex):
        self.__sex = sex

    def getSex(self):
        return self.__sex

    #在创建对象的同时，将参数传入进去，就避免大量调用setXXX方法类赋值
    #这样传值的前提是前面有__init__构造方法
p = Person("李四", 56, "男", 155)
print(p.getUsername(), p.getAge(), p.getSex(), p.getHigh())




