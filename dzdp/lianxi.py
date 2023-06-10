import pymysql
import numpy
list=numpy.zeros(10,10)
for i in range(len(list)):
    # # sql建表语句
    # 打开数据库连接
    conn = pymysql.connect(
        host='localhost',  # mysql服务器地址
        port=3306,  # 端口号
        user='root',  # 用户名
        passwd='root',  # 密码
        db='pymsql',  # 数据库名称
        charset='utf8'  # 连接编码，根据需要填写,python3中的pymysql连接mysql时charset参数填utf8,而非HTML中的charset的参数utf-8
    )
    cur = conn.cursor()  # 创建并返回游标
    sql2 = """INSERT INTO Food(city,
             shopName, mainRegionName, mainCategoryName, tasteScore, environmentScore,serviceScore,avgPrice,shopUrl)
             VALUES ("%s", "%s", "%s","%s","%s","%s","%s","%s","%s")"""
    try:
        # 执行sql语句
        cur.execute(sql2,list[i])
        print(list[i])
        # 执行sql语句
        print("插入成功")
        conn.commit()
    except:
        # 发生错误时回滚
        print(list[i])

        print("插入失败")
        conn.rollback()

    # 关闭数据库连接

conn.close()
#
# # # #插入表中
# # churumysql(list)