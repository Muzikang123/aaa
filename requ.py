'''
安装requests模块
requests模块是模拟浏览器发送一些网络请求的的工具
清楚一个网址的请求模式。get,post
    get 请求比较不安全，
    post请求专门放到一个安全的区域，然后在传输过去

'''
# import requests
#
# response=requests.post(url="http://www.jasonisoft.cn:8080/HKR/UserServlet?method=findAllStudent")
#
# response.encoding="utf-8"
# users = response.json()
# eval(users)
# for i in users:
#     print(i)
import requests
import pymysql

response = requests.post(url="http://www.jasonisoft.cn:8080/HKR/UserServlet?method=findAllStudent",
                         data={"username":"jason"})
response.encoding = "utf-8"
list1=[]
users = response.json()  #[{age:56},{}]
con=pymysql.connect(host="localhost",user="root",password="",database="requ")
cursoe=con.cursor()
sql14="insert into student (address,age,carte,classname,email,graduation,id,loginname," \
    "phoneNumber,picturePath,registerDate,sex,uid,username) " \
    "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
sql13="insert into student (address,age,classname,email,graduation,id,loginname," \
    "phoneNumber,picturePath,registerDate,sex,uid,username) " \
    "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
list2=[]
newlist14=[]
newlist13=[]
for user in users:
    if len(user.keys())==14:
        list14=list(dict(user).values())
        newlist14.append(list14)
    if len(user.keys())==13:
        list13=list(dict(user).values())
        newlist13.append(list13)
cursoe.executemany(sql14,newlist14)
cursoe.executemany(sql13,newlist13)
con.commit()
cursoe.close()
con.close()
