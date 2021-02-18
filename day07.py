'''
    1.安装pymysql
    2.导入pymysql
    3.通过pymysql连接mysql数据库 --> 获取一个数据库连接
    4.通过连接创建一个游标（控制台：执行sql语句）
    5.执行sql语句
    6.得到执行结果
    7.关闭资源
'''
'''
    insert,delete,update : 更新数据库。返回结果都是1或者23445
    select: 查询数据库，并返回查询结果
        区别：查询后，需要将返回的数据进行二次处理。
        获取数据：
            fetchall() 获取所有
            fetchone()  获取一条
            fetchmany() 获取多条
    优化：
        采用sql语句和数据进行分离的方式进行增，删，改，查来对数据库进行操作。
        好处：一条sql语句可以多次使用。填充的数据也可以动态替换，一本万利，岂不美哉！！！！！
    任务：将增、删、改、查四大操作，写出来使用模板和数据分离的方式来做。提交到云仓库，地址发到群里。
    工商银行的数据库统一采用mysql来存储。增、删、改、查都使用今天的知识来做。
    V1.2.5
    V2.1.0

'''
#对数据库进行添加数据
# import pymysql
# con=pymysql.connect(host="localhost",user="root",password="123456",database="company")#通过pymysql获取连接
# cursoe=con.cursor()
# sql="insert into t_dept values('1185','炊事班','北京')"
# num=cursoe.execute(sql)
# print("影响了",num,"行数据")
# con.commit()
# cursoe.close()
# con.close()

#对数据库的数据进行删除
# import pymysql
# con=pymysql.connect(host="localhost",user="root",passwd="123456",database="company")
# cursor=con.cursor()
# sql="delete from t_dept where dname = '炊事班'"
# num=cursor.execute(sql)
# print(num)
# con.commit()#提交数据,把缓存的数据真正的提交给数据库
# cursor.close()
# con.close()

#对数据库的数据进行修改
# import pymysql
# con=pymysql.connect(host="localhost",user="root",passwd="123456",database="company")
# cursor=con.cursor()
# sql="update t_dept set dname='炊事班' where deptno=183"
# num=cursor.execute(sql)
# print(num)
# con.commit()#提交数据,把缓存的数据真正的提交给数据库
# cursor.close()
# con.close()
#对数据库进行查询
#
# import pymysql
# con = pymysql.connect(host="localhost",user="root",passwd="123456",database="company")#通过pymysql 获取连接
# cursor = con.cursor()#使用cursor()方法获取数据库的操作游标
# sql="select * from t_employees where ename=%s"#准备一条SQL语句
# a=input("请输入姓名")
# param=[a]
# print(sql)
# num= cursor.execute(sql,param)#执行sql语句
# data= cursor.fetchall()#获取游标的所有数据
# print("影响了",num,"行数据")
# print(data)
# con.commit()#提交数据,把缓存的数据真正的提交给数据库
# cursor.close()#关闭连接,
# con.close()

import pymysql
con = pymysql.connect(host="localhost",user="root",passwd="",database="company")#通过pymysql 获取连接
cursor = con.cursor()#使用cursor()方法获取数据库的操作游标
sql="select * from t_employees where ename and empno in (%s,%s)"#准备一条SQL语句
a=input("请输入姓名")
b=input("请输入号码")
param=[a,b]
num= cursor.execute(sql,param)#执行sql语句
data= cursor.fetchall()#获取游标的所有数据
print("影响了",num,"行数据")
print(data)
con.commit()#提交数据,把缓存的数据真正的提交给数据库
cursor.close()#关闭连接,
con.close()