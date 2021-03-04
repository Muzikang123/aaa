#对象与对象之间的关系
'''
人 类：
        姓名，年龄，性别，身高，地址

地址类：
        属性：国家，省份，街道，门牌号
'''
#地址类中的全部属性作为一个对象传入人这个类中的地址
class Preson:
    username = None
    age = None
    address = None
class Address:
    country = None
    province = None
    street = None
    door = None
#创建地址类的对象
add = Address()
add.country="中国"
add.province="河北省"
add.street="幸福大道"
add.door="001"
#创建人类的对象
p=Preson()
p.username="小明"
p.age=55
p.address=add  #对地址属性传值的时候直接赋值上add对象
#输出
print(p.username,p.age,p.address.country,p.address.province,p.address.street,p.address.door)
