#35的八进制和十六进制
# print(0o43)
# print(0x23)

# score = input("请输入分数:")
# score = int(score)
# if score>=90 and score<=100:
#     print("优秀")
# elif score>=70 and score<90:
#     print("一般")
# elif score>=60 and score<70:
#     print("及格")
# elif score>=0 and score < 60:
#     print("不及格")
# else:
#     print("你输入的不合法")

# 循环打印0~10之间的数字
# i=1    #i定义循环的次数，
# while i<=10:
#      print(i," ",end="")  #
#      i+=1


#猜数字游戏
# import random
# import time

# num=random.randint(1,100)
# num=int(num)
# print(num)
# counter=0
# i=5
# while True:
#     if counter>=3:
#         while i>0:
#             print("系统自动锁定",i,"秒")
#             time.sleep(1)
#             i-=1
#     counter+=1
#     number=input("请输入一个数字：")
#     number=int(number)
#     if number<num:
#         print("猜的数字太小的")
#     elif number>num:
#         print("猜的数字太大了")
#     else:
#         if counter<5:
#             print("恭喜你猜对了！猜的次数为",counter,"次，奖励5元")
#             break
#         else:
#             print("恭喜你猜对了！猜的次数为",counter,"次")
#             break

#九九乘法表
# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         print(i,"*",j,"=",(i*j),"  ",end="")
#         j+=1
#     print()
#     i+=1

#随机生成50~150之间的数字。
# import random
# num=random.randint(50,150)
# num=int(num)
# print(num)

# 判断三角形
# while True:
#     num_1=input("请输入三角形的第一个边:")
#     num_1=int(num_1)
#     num_2=input("请输入三角形的第一个边:")
#     num_2=int(num_2)
#     num_3=input("请输入三角形的第一个边:")
#     num_3=int(num_3)
#     if num_1+num_2>num_3 and num_1+num_3>num_2 and num_3+num_2>num_1:
#         if num_1==num_2==num_3:
#             print("这是一个等边三角形")
#
#         elif num_1==num_2 or num_2==num_3 or num_1==num_3:
#             print("这是一个等腰三角形")
#
#         else:
#             print("这是一个普通三角形")
#         break
#     else:
#         print("请输入有效数据：")


#实现两个数的调换
# A=56
# B=78
# print("A=56 B=78")
# A = A+B
# B  = A-B
# A = A-B
# print("使用求和法得出结果：")
# print("A变换后为",A)
# print("B变换后为",B)

#实现登录密码三次密码输入三次错误锁定功能：
# import time
# password=123456
# counter=0
# while True:
#     num=input("请输入登录密码:")
#     num=int(num)
#     if num!=password:
#         print("密码输入错误，请重新输入:")
#     else:
#         print("密码输入正确，成功登录系统")
#     counter+=1
#     if counter>=3:
#         print("多次输入密码错误，系统锁定一个小时")
#         time.sleep(3600)
#

#打印图形：
# i=1
# x=14
# j=1
# while i<=7:
#     print(" "*x,"*   "*j,end="")
#     print()
#     x-=2
#     i+=1
#     j+=1

#倒序99乘法表
# i=9
# while i>=1:
#     j=1
#     while j<=i:
#         print(i,"*",j,"=",(i*j),"  ",end="")
#         j += 1
#     print()
#     i -= 1
#青蛙爬井

# Day=1
# i=-20
# while True:
#     if i<0:
#         print("第",Day,"天","爬了3米还剩",i+3)
#         i=i+3
#         i=int(i)
#         if i<0:
#             print("下滑2米还剩",i-2)
#             i=i-2
#             i=int(i)
#             Day+=1
#     else:
#         print("成功爬出用时",Day,"天")
#         break
#
# 判断是否合法

# char不合法
# Oax_li合法
# fLul合法
# BYTE不合法
# Cy%ty不合法
# $123不合法
# 3_3 不合法
# T_T合法








