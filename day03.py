


#实现输入10个数字，并打印10个数的求和结果，
# s=0
# for i in range(1,11):
#      num=input("请输入数字：")
#      num=int(num)
#      s=s+num
# print("十个数字之和是：",s)

#从键盘一次输入10个数字，最后打印最大的数，10个数字的和，和平均数。
# li=[]
# s=0
# num=0
# for i in range(10):
#     num=input("请输入数字:")
#     num=int(num)
#     li.append(num)
# print(li)
# for i in li:
#     s=s+i
# for i in li:
#     if i>num:
#         num=i
#
# print("数字总和为：",s)
# print("数字中最大值为：",num)
# print("数字的平均数为",s/10)
# num=0
# agenum=0
# names = [
#     ["曹操",56,"男","106","IBM", 500,"50"],
#     ["大乔",19,"女","230","微软", 501 ,"60"],
#     ["小乔", 19, "女", "210", "Oracle", 600, "60"],
#     ["许褚", 45, "男", "230", "Tencent",700 , "10"]
# ]
# for i in range(0,4):
#     list1=names[i]
#     num1=list1[5]
#     num=num+num1
# print("平均薪资是：",num/4)
#
# num=0
# for i in range(0,4):
#     list1=names[i]
#     num1=list1[1]
#     num=num+num1
# print("平均年龄是：",num/4)
#
# num=["刘备",45,"男",220,"alibaba",500,30]
# names.append(num)
# for i in range(0,5):
#     print(names[i])
#
# counter=0
# counter1=0
# for i in range(0,5):
#     list1=names[i]
#     if list1[2]=="男":
#         counter+=1
#     else:
#         counter1+=1
# print("男的有",counter,"个","女的有",counter1,"个")
#
# list=[50,60,60,10,30]
# print("50部门的人数为：",list.count(50))
# print("60部门的人数为：",list.count(60))
# print("10部门的人数为：",list.count(10))
# print("30部门的人数为：",list.count(30))

# 数据翻转
# s=0
# list=[1,2,3,4,5,6,7,8,9]
# for i in range(0,5):
#         s=list[i]
#         list[i]=list[8-i]
#         list[8-i]=s
#         print(list)

#计算每个数字出现的次数”


# list=[1,4,7,5,8,2,1,3,4,5,9,7,6,10]
# for i in list:
#     print(list[i],"的出现次数",list.count(list[i]))
#


# # 实现20以内的数的阶乘：（1!+2!+....+20!）
# x = 1
# sum=0
# for i in range(1,21):
#     x = x * i
#     sum=x+sum
# print(sum)

#求其中是5的倍数的和
# a=[1,5,21,30,15,9,30,24]
# sum=0
# for i in range(0,7):
#     if a[i]%5==0:
#         sum=sum+a[i]
#     else:
#         i=i+1
# print("5的倍数和为：",sum)

#求每个人的总成绩
# counter=0
# num=[
# ["罗恩",23,35,44],
# ["哈利",60,77,68,88,90],
# ["赫敏",97,99,89,91,95,90],
# ["马尔福",100,85,90]
#     ]
# list=[]
# for i in range(0,4):
#     s=0
#     list=num[i]
#     li=list[1:]
#     for j in li:
#         s=s+j
#     print(num[i][0], "的总成绩是：",s)
#












