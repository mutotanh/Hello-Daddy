
#     for i in range(len(list)):
#         # # sql建表语句
#         # 打开数据库连接
#         conn = pymysql.connect(
#             host='localhost',  # mysql服务器地址
#             port=3306,  # 端口号
#             user='root',  # 用户名
#             passwd='root',  # 密码
#             db='pymsql',  # 数据库名称
#             charset='utf8'  # 连接编码，根据需要填写,python3中的pymysql连接mysql时charset参数填utf8,而非HTML中的charset的参数utf-8
#         )
#         cur = conn.cursor()  # 创建并返回游标
#         sql2 = """INSERT INTO Food(city,
#                  shopName, mainRegionName, mainCategoryName, tasteScore, environmentScore,serviceScore,avgPrice,shopUrl)
#                  VALUES ("%s", "%s", "%s","%s","%s","%s","%s","%s","%s")"""
#         try:
#             # 执行sql语句
#             cur.execute(sql2,list[i])
#             print(list[i])
#             # 执行sql语句
#             print("插入成功")
#             conn.commit()
#         except:
#             # 发生错误时回滚
#             print(list[i])
#
#             print("插入失败")
#             conn.rollback()
#
#         # 关闭数据库连接
#
#     conn.close()
#
# # #插入表中
# churumysql(list)
#
import requests
import xlsxwriter
import time
import pymysql
#多线程相关库
from concurrent.futures import ThreadPoolExecutor
import threading

#各地美食餐厅xml接口，需拼接,大概1200数据
list_city = [["上海", "fce2e3a36450422b7fad3f2b90370efd71862f838d1255ea693b953b1d49c7c0"],
             ["北京", "d5036cf54fcb57e9dceb9fefe3917fff71862f838d1255ea693b953b1d49c7c0"],
             ["广州", "e749e3e04032ee6b165fbea6fe2dafab71862f838d1255ea693b953b1d49c7c0"],
             ["深圳", "e049aa251858f43d095fc4c61d62a9ec71862f838d1255ea693b953b1d49c7c0"],
             ["天津", "2e5d0080237ff3c8f5b5d3f315c7c4a508e25c702ab1b810071e8e2c39502be1"],
             ["杭州", "91621282e559e9fc9c5b3e816cb1619c71862f838d1255ea693b953b1d49c7c0"],
             ["南京", "d6339a01dbd98141f8e684e1ad8af5c871862f838d1255ea693b953b1d49c7c0"],
             ["苏州", "536e0e568df850d1e6ba74b0cf72e19771862f838d1255ea693b953b1d49c7c0"],
             ["成都", "c950bc35ad04316c76e89bf2dc86bfe071862f838d1255ea693b953b1d49c7c0"],
             ["武汉", "d96a24c312ed7b96fcc0cedd6c08f68c08e25c702ab1b810071e8e2c39502be1"],
             ["重庆", "6229984ceb373efb8fd1beec7eb4dcfd71862f838d1255ea693b953b1d49c7c0"],
             ["西安", "ad66274c7f5f8d27ffd7f6b39ec447b608e25c702ab1b810071e8e2c39502be1"]]

# 抓取数据，列表嵌套列表形式，三重列表[【{上海1}，{上海2}】，【{北京1}，{北京2}】，【】]
def foodSpider(list_city):
    bigdata=[]
    for i in range(len(list_city)):
        city = list_city[i][0]
        url = list_city[i][1]
        base_url = "http://www.dianping.com/mylist/ajax/shoprank?rankId=" + url
        diningroom = requests.get(base_url).json()['shopBeans']
        # 一个城市一个列表
        bigdata.append(diningroom)
    return bigdata

# 接受抓取的数据
bigdata=foodSpider(list_city)

# 传入函数解析，存入全局变量list
list=[]
def findFood(bigdata,list_city):
    for i in range(len(bigdata)):
        for j in range(len(bigdata[i])):
            list1=[]
            #城市名:取城市名
            city=list_city[i][0]
            # 店名
            shopName = bigdata[i][j]["shopName"]
            # 位置
            mainRegionName = bigdata[i][j]["mainRegionName"]
            # 分类名称
            mainCategoryName = bigdata[i][j]["mainCategoryName"]
            # 口味评分
            tasteScore = bigdata[i][j]["refinedScore1"]
            # 环境评分
            environmentScore = bigdata[i][j]["refinedScore2"]
            # 服务评分
            serviceScore = bigdata[i][j]["refinedScore3"]
            # 均价
            avgPrice = bigdata[i][j]["avgPrice"]
            # 商铺网址
            shopUrl = "http://www.dianping.com/shop/" + bigdata[i][j]["shopId"]
            list1.append(city)
            list1.append(shopName)
            list1.append(mainRegionName)
            list1.append(mainCategoryName)
            list1.append(tasteScore)
            list1.append(environmentScore)
            list1.append(serviceScore)
            list1.append(avgPrice)
            list1.append(shopUrl)
            list.append(list1)
            # print(list1)
findFood(bigdata,list_city)
# print(list)

# 存储list
# 插入csv文件
def chunrucsv(list):
    # 将获取的源码  以追加的方式  保存进lianjie.txt文件,每个文件用**分割开
    with open('lianjie.csv', 'a', encoding='utf-8') as f:
        for i in range(len(list)):
            f.write(str(list[i]).strip('[').strip(']'))
            f.write("\n")
# chunrucsv(list)


# #插入表中
def churumysql(list):
    # 打开数据库连接
    conn = pymysql.connect(
        host='localhost',  # mysql服务器地址
        port=3306,  # 端口号
        user='root',  # 用户名
        passwd='root',  # 密码
        db='bysj',  # 数据库名称
        charset='utf8'  # 连接编码，根据需要填写,python3中的pymysql连接mysql时charset参数填utf8,而非HTML中的charset的参数utf-8
    )
    cur = conn.cursor()  # 创建并返回游标
    cur.execute("DROP TABLE IF EXISTS Food")
    # # sql建表语句
    sql1= """
       CREATE TABLE `Food` (
        `id`  int NOT NULL AUTO_INCREMENT ,
        `city`  varchar(1000) NOT NULL ,
        `shopName`  varchar(1000) NOT NULL ,
        `mainRegionName`  varchar(1000) NOT NULL ,
        `mainCategoryName`  varchar(1000) NOT NULL ,
        `tasteScore`  varchar(1000) NOT NULL ,
        `environmentScore`  varchar(1000) NOT NULL ,
        `serviceScore`  varchar(1000) NOT NULL ,
        `avgPrice`  varchar(1000) NOT NULL ,
        `shopUrl`  varchar(1000) NOT NULL ,
        PRIMARY KEY (`id`)
        );
       """
    sql2 = """INSERT INTO Food(city,
                       shopName, mainRegionName, mainCategoryName, tasteScore, environmentScore,serviceScore,avgPrice,shopUrl)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    try:

        # 执行sql语句
        cur.execute(sql1)
        print("建表成功")
        for i in range(len(list)):
            cur.execute(sql2,list[i])
        # 执行sql语句
        conn.commit()
    except:
        # 发生错误时回滚
        print("建表失败")
        conn.rollback()



# #插入表中
churumysql(list)





