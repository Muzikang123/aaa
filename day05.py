import random

# 银行的名称
bank_name = "北京市工商银行昌平支行"

# 银行的库
users = {}
'''
{"张三":
    {account:"12345",
    "国家":"中国"}
}

'''
# 欢迎界面
welcome = '''
*********************************
*    欢迎来到中国工商银行管理系统 *
*********************************
*    1.开户                      *
*    2.存钱                      *
*    3.取钱                      *
*    4.转账                      *
*    5.查询                      *
*    6.bye！                     *
*********************************
'''
# 专门来获取8位随机账号
def getRandom():
    li = [1,2,3,4,5,6,7,8,9,0]
    # 循环8次
    string = ""
    for i in range(8): # 循环8次获取随机字符
        ch = li[random.randint(0,9)]
        string = string + str(ch)
    return string

# 银行的核心开户方法
def bank_addUser(account,username,password,money,country,province,street,door):
    # 先判断银行库是否已满 ： 100个最大
    if len(users) >= 100:
        return 3
    # 判断是否已经存在
    elif username in users: # 这种方式只判断是否在字典的键里存在
        return 2
    # 可以正常开户：将个人数据存到用户库里
    else:
        users[username] = {
            "account":account,
            "password":password,
            "money":money,
            "country":country,
            "province":province,
            "street":street,
            "door":door,
            "bank_name":bank_name
        }

        return 1

#查询功能的逻辑
def bank_queryMoney(username,password):
    import pymysql
    con = pymysql.connect(host="localhost",user="root",password="",database="bank")
    cursor = con.cursor()
    sql = "select * from user where 姓名 = %s"
    param=[username]
    num=cursor.execute(sql,param)
    data = cursor.fetchall()
    if num==0:
        print("没有此用户")
    elif password != data[0][2]:
        print("密码输入错误")
    else:
        print("查询信息的账号为：",data[0][0],",姓名",data[0][1],",密码：",data[0][2],",余额：",data[0][3],
              ",国家",data[0][4],",省份",data[0][5],",街道",data[0][6],",门牌号",data[0][7])
        cursor.fetchall()
        con.commit()
        cursor.close()
        con.close()
def queryMoney():
    username=input("请输入用户名")
    password=input("请输入你的密码:")
    bank_queryMoney(username,password)


# 普通的开户方法
def addUser():
    # 完成具体的开户输入
    # 姓名(str)、密码(int:6位数字)、地址、存款余额(int)、国家(str)、省份(str)、街道(str)、门牌号(str)
    username = input("请输入姓名：")
    password = input("请输入初始取款密码：")
    money = int(input("请输入您的初始金额：")) # 金额是整数形式
    print("接下来输入地址信息：")
    country =  input("请输入您所在国家：")
    province = input("亲输入您所在省份：")
    street = input("请输入您所在的街道：")
    door = input("请输入您地址的门牌号：")
    account =  getRandom() # 获取随机账号
    # 将数据传给银行
    status = bank_addUser(account,username,password,money,country,province,street,door)
    status1 = addSql(account,username,password,money,country,province,street,door)
    if status == 3:
        print("对不起，银行用户已满！请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，您的个人信息已存在！请勿重复开户！")
    elif status == 1:
        print("恭喜，开户成功！以下是您的个人开户信息：")
        print("-------------------------------------")
        print("您的账号为:",users[username]["account"])
        print("您的密码为:", users[username]["password"])
        print("您的余额为:", users[username]["money"])
        print("您的用户名为:", username)
        print("您所在国家为:", users[username]["country"])
        print("您所在省份为:", users[username]["province"])
        print("您所在街道为:", users[username]["street"])
        print("您所在门牌号为:", users[username]["door"])
        print("开户行名为:", users[username]["bank_name"])
    elif status1==1:
        print("保存成功")
def addSql(account,username,password,money,country,province,street,door) :
    import pymysql
    con=pymysql.connect(host="localhost",user="root",password="",database="bank")#通过pymysql获取连接
    cursor=con.cursor()
    sql="insert into user values(%s,%s,%s,%s,%s,%s,%s,%s)"
    param = [account,username,password,money,country,province,street,door]
    print(param)
    num= cursor.execute(sql,param)
    print("影响了",num,"行数据")
    con.commit()
    cursor.close()
    con.close()

#存钱的逻辑
def saveMoney():
    username= input("请输入账户:")
    saveMoney = input("请输入金额:")
    while True:
        if saveMoney.isdigit():
             saveMoney=int(saveMoney)
             break
        else:
            print("余额输入错误，请重新输入！")
    saveMoneysql(username,saveMoney)

def saveMoneysql(username,saveMoney):
    import pymysql
    con = pymysql.connect(host="localhost",user="root",password="",database="bank")
    cursor = con.cursor()
    sql = "select * from user where 姓名 = %s"
    param=[username]
    num=cursor.execute(sql,param)
    if num==0:
        print("没有此用户")
    else:
        data = cursor.fetchall()
        newsaveMoney=saveMoney+int(data[0][3])
        print("存钱成功，本次存入金额：",saveMoney,"账户余额：",newsaveMoney)
        sql1="update user set 存款余额=%s where 姓名=%s"
        param1=[newsaveMoney,username]
        cursor.execute(sql1,param1)
        cursor.fetchall()
        con.commit()
        cursor.close()
        con.close()

#转账核心方法
def transfer(to_username, out_username, out_username_pass, out_money):
    import pymysql
    con = pymysql.connect(host="localhost",user="root",password="",database="bank")
    cursor = con.cursor()
    sql = "select * from user where 姓名 = %s"
    param=[out_username]
    num=cursor.execute(sql,param)
    data = cursor.fetchall()
    sql0 = "select * from user where 姓名 = %s"
    param=[to_username]
    num0=cursor.execute(sql0,param)
    data1=cursor.fetchall()
    if num0==0:
        print("没有此用户")
    elif num==0:
        print("没有此用户")
    elif out_username_pass != data[0][2]:
        print("密码输入错误")
    elif out_money>data[0][3]:
        print("账户余额不足!!")
    else:
        newMoney=data[0][3]-out_money
        newMoney2=data1[0][3]+out_money
        print("转钱成功，本次转出：",out_money,"账户余额：",newMoney)
        sql2="update user set 存款余额=%s where 姓名=%s"
        param2=[newMoney,out_username]
        cursor.execute(sql2,param2)
        sql3="update user set 存款余额=%s where 姓名=%s"
        param3=[newMoney2,to_username]
        cursor.execute(sql3,param3)
        cursor.fetchall()
        con.commit()
        cursor.close()
        con.close()

#转账方法
def transferAccounts():
    out_username=input("转入账户：")
    to_username=input("转出账户：")
    out_username_pass = input("转出账户的密码：")
    out_money = int(input("转账金额："))
    transfer(out_username,to_username,out_username_pass,out_money)

#取钱功能
def withdraw():
    username = input("请输入姓名：")
    password = input("请输入取款密码：")
    money = int(input("请输入您要取的金额："))
    drawMoneysql(username,password,money)

def drawMoneysql(username,password,money):
    import pymysql
    con = pymysql.connect(host="localhost",user="root",password="",database="bank")
    cursor = con.cursor()
    sql = "select * from user where 姓名 = %s"
    param=[username]
    num=cursor.execute(sql,param)
    data = cursor.fetchall()
    if num==0:
        print("没有此用户")
    elif password != data[0][2]:
        print("密码输入错误")
    elif money>data[0][3]:
        print("账户余额不足!!")
    else:
        newMoney=int(data[0][3])-money
        print("取钱成功，本次取出金额：",money,"账户余额：",newMoney)
        sql2="update user set 存款余额=%s where 姓名=%s"
        param2=[newMoney,username]
        cursor.execute(sql2,param2)
        cursor.fetchall()
        con.commit()
        cursor.close()
        con.close()

def writeFile():
    f=open("bank.txt","w+",encoding="utf-8")
    for key in users.keys():
        string=""
        string=string+key
        string = string+ "," + users[key]["account"]
        string = string + "," + users[key]["password"]
        string = string + "," + str(users[key]["money"])
        string = string + "," + users[key]["country"]
        string = string + "," + users[key]["province"]
        string = string+ ","  + users[key]["street"]
        string = string + "," + users[key]["door"]
        string = string + "," + users[key]["bank_name"]
        f.write(string + "\n")
    f.close()
while True:
    print(welcome) # 打印欢迎信息
    chose = input("请输入您的业务编号：")
    if chose == "1":
        addUser()
    elif chose == "2":
        saveMoney()
        writeFile()
    elif chose == "3":
        withdraw()
        writeFile()
    elif chose == "4":
        transferAccounts()
        writeFile()
    elif chose == "5":
        queryMoney()
    elif chose  == "6":
        print("退出成功！欢迎下次光临！")
        break
    else:
        print("输入非法！请重新输入！")

