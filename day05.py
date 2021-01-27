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
#存钱的逻辑
def bank_saveMoney(account,saveMoney):
    values = users.values()
    for i in values:
        if account in i.values():
            i["money"]=i["money"]+saveMoney
            return True
        else:
            return False
#查询功能的逻辑
def bank_queryMoney( username, password,money,country,province,street,door):
    values = users.values()
    if username in users:
        for i in values:
            if password in i.values():
                users[username]={
                    "money":money,
                    "password":password,
                    "country":country,
                    "province":province,
                    "street":street,
                     "door":door,
                    "bank_name": bank_name
                }
                return 1
    else:
        return 2


def queryMoney():
    username=input("请输入用户名")
    password=input("请输入你的密码:")
    money=users[username]["money"]
    country=users[username]["country"]
    province = users[username]["province"]
    street = users[username]["street"]
    door = users[username]["door"]
    query=bank_queryMoney(username,password,money,country,province,street,door)
    if query==1:
        print("当前账号为：",username)
        print("当前密码为",users[username]["password"])
        print("当前余额为：",users[username]["money"])
        print("国家为：", users[username]["country"])
        print("城市为：", users[username]["province"])
        print("街道：", users[username]["street"])
        print("门牌号：", users[username]["door"])
        print("开户行名为:", users[username]["bank_name"])
    elif query==2:
        print("该用户不存在")

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

def saveMoney():
    account = input("请输入账号:")
    saveMoney = input("请输入金额:")
    while True:
        if saveMoney.isdigit():
             saveMoney=int(saveMoney)
             break
        else:
            print("余额输入错误，请重新输入！")
    save=bank_saveMoney(account,saveMoney)
    if save==True:
        print("存钱成功")
        print(users)
    else:
        print("此用户不存在")


#转账核心方法
def transfer(to_username, out_username, out_username_pass, out_money):
    if out_username in users and to_username in users:  #判断库里是否转出账户和装入账户
        if out_username_pass==users[out_username]["password"]:  #判断装出账户密码是否正确
            if out_money<=users[out_username]["money"]:    #判断转出账户金额是否够
                   return 0
            else:
                  return 3
        else:
            return 2
    else:
        return 1

#转账方法
def transferAccounts():
    out_username=input("请输入转出账户：")
    to_username=input("请输入转入账户：")
    out_username_pass = input("请输入转出账户的密码：")
    out_money = int(input("请输入转账金额："))

    status4=transfer(to_username,out_username,out_username_pass,out_money)
    if status4==1:
        print("转出账户或转入账户不存在！")
    elif status4==2:
        print("转出账户的密码不正确！！!")
    elif status4==3:
        print("金额不足！！！")
    elif status4==0:
        users[out_username]["money"]=users[out_username]["money"]-out_money
        users[to_username]["money"]=users[to_username]["money"]+out_money
        print("转账成功！","\n",out_username,"余额为：",users[out_username]["money"],"\n",to_username,"余额为：",users[to_username]["money"])

def bank_withdraw(username,password,money):

    for value in users.values():
        if username not in value.values():
            return 1
        elif password not in value.values():
            return 2
        elif money > value["money"]:
            return 3
        else:
            value["money"] = value["money"] - money
            users[username]={
                "username":username,
                "password":password,
                "money":value["money"]
            }
            return 0

def withdraw():
    username = input("请输入姓名：")
    password = input("请输入取款密码：")
    money = int(input("请输入您要取的金额："))
    returnvalue= bank_withdraw(username,password,money)
    if returnvalue == 1:
        print("用户不存在")
    elif returnvalue == 2:
        print("密码不正确")
    elif returnvalue == 3:
        print("账户余额不足")
    elif returnvalue == 0:
        print("以取出：",money,"元","余额还剩：",users[username]["money"])
        print(users)
while True:
    print(welcome) # 打印欢迎信息
    chose = input("请输入您的业务编号：")
    if chose == "1":
        addUser()
    elif chose == "2":
        saveMoney()
    elif chose == "3":
        withdraw()
    elif chose == "4":
        transferAccounts()
    elif chose == "5":
        queryMoney()
    elif chose  == "6":
        print("退出成功！欢迎下次光临！")
        break
    else:
        print("输入非法！请重新输入！")


