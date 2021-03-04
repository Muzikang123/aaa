
# import pymongo
# import requests
# response = requests.post(url="http://www.jasonisoft.cn:8080/HKR/UserServlet?method=findAllStudent",
#                          data={"username":"jason"})
# response.encoding = "utf-8"
# list1=[]
# users = response.json()
# #连接数据库
# client = pymongo.MongoClient("mongodb://localhost:27017")
# # 展示数据库
# lists = client.list_database_names()
# print(lists)
# #选择数据库，然后插入数据
# db = client["admin"]
# user=users
# status = db["student"].insert_many(user)
# print(status)


# for i in db["student"].find({"username":"贾生"},{"username":"王朔"}):
#     print(i)
#     print(type(i))
#修改表信息内容
# db["student"].update_many({"username":"贾生"},{"$set":{"username":"jason"}})
#多条件查询，查询student表中叫 jason和王朔的所有信息。
# for i in db["student"].find({"$or":[{"username":"jason"},{"username":"王朔"}]}):
#     print(i)
#删除数据
# db["student"].delete_one({"username":"不再爱了"})






