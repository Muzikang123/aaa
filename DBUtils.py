import pymysql
host="localhost"
database="bank"
user="root"
password=""
def update(sql,param):
    con=pymysql.connect(host=host,user=user,password=password,database=database)
    cursor=con.cursor()
    cursor.execute(sql,param)
    con.commit()
    cursor.close()
    con.close()

def find(sql,param,mode="all",size=1):
    con=pymysql.connect(host=host,user=user,password=password,database=database)
    curs=con.cursor()
    curs.execute(sql,param)
    con.commit()
    if mode == "all":
        return curs.fetchall()
    elif mode == "one":
        return curs.fetchone()
    elif mode == "many":
        return curs.fetchmany(size)
    curs.close()
    con.close()

sql="select * from users"
param=[]
lis=""
data = find(sql,param,mode="all",size=6)
list=data
f = open("user.txt","a+",encoding="utf-8")
for i in range(0,6):
    # lis=""
    # for j in range(0,3):
    #     lis=str(lis)+str(list[i][j])+","
    lis="".join(str(list[i])).replace("(","").replace("'","").replace(")","")
    f.write(lis+"\n")
f.close()

# sql="select * from user"
# param=[]
# data=find(sql,param,mode="many",size=1)
# print(data)

# f = open("user.txt","r+",encoding="utf-8")
# lis = f.readlines()
# sum=0
# for i in lis:
#     use_lis = i.replace("\n", "").split(",")
#     num=int(use_lis[2])
#     sum=sum+num
#     sql ="insert into users values(%s,%s,%s)"
#     param=use_lis
#     update(sql,param)
# print("资产综合为:",sum)
# f.close()

# sql ="insert into users values(%s,%s,%s)"
# param=["穆子康",24,230023]
# update(sql,param)
# sql="update user set 存款余额=存款余额+1000 where 姓名=%s"
# param=["muzikang"]
# update(sql,param)
