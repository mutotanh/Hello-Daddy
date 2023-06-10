import requests
import xlsxwriter
import time
import pymysql
#多线程相关库
from concurrent.futures import ThreadPoolExecutor
import threading
import time
#向列表中传入一个股票各项数据组成的字典:,将字典的值取出保存到一个列表中
def creatlist(item):
    try:
        temp = []
        temp.append(item['Prod_name'])  # 股票名称
        temp.append("=TEXT(" + item['Market_Symbol'] + ",\"000000\")")  # 股票代码
        temp.append(item['Last_px'])  # 最新价
        temp.append("=TEXT(" + str(item['Px_change_rate'] / 100) + ",\"0.00%\")")  # 跌涨幅
        temp.append(item['Business_amount'])  # 成交量
        temp.append(item['Business_balance'])  # 成交额
        # 基本语句：=TEXT(数值，文本格式)
        temp.append("=TEXT(" + str(item['Amplitude'] / 100) + ",\"0.00%\")")  # 振幅
        temp.append("=TEXT(" + str(item['Turnover_ratio'] / 100) + ",\"0.00%\")")  # 换手率
        temp.append(item['Market_value'])  # 市值
        temp.append(item['Vol_ratio'])  # 量比
        temp.append(item['High_px'])  # 最高
        temp.append(item['Low_px'])  # 最低
        temp.append(item['Open_px'])  # 今开
        temp.append(item['Preclose_px'])  # 昨收
        print("插入excel的列表生成成功")
        return temp
    except Exception as e:
        print(e)
        print("creatlist函数失败")

def shujupandas(res):
    for item in res:
        # 返回值是自己设的一个列表,列表的值是  字典的键对应的 值.
        if item==0:
            res.remove(item)
        if item['Prod_name']==[]:
            res.remove(item)
        if "=TEXT(" + item['Market_Symbol'] + ",\"000000\")"==[]:
            res.remove(item)
        if item['Last_px']==[]:
            res.remove(item)
        if "=TEXT(" + str(item['Px_change_rate'] / 100) + ",\"0.00%\")"==[]:
            res.remove(item)
        if item['Business_amount']==[]:
            res.remove(item)
        if item['Business_balance']==[]:
            res.remove(item)
        if "=TEXT(" + str(item['Amplitude'] / 100) + ",\"0.00%\")"==[]:
            res.remove(item)
        if "=TEXT(" + str(item['Turnover_ratio'] / 100) + ",\"0.00%\")" == []:
            res.remove(item)
        if item['Market_value'] == []:
            res.remove(item)
        if item['Vol_ratio']== []:
            res.remove(item)
        if item['High_px'] == []:
            res.remove(item)
        if item['Low_px'] == []:
            res.remove(item)
        if item['Open_px'] == []:
            res.remove(item)
        if item['Preclose_px'] == []:
            res.remove(item)
    return res

    pass
#插入excel:应当传入一个字典列表，遍历列表，将字典传入creatlist（）函数
def insertexcel(res):
    try:
    # 向excel中插入数据
        timenow = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
        #建立工作簿：    生成文件，文件名是填写的"hushenstockexchange" + timenow + ".xlsx"
        workbook = xlsxwriter.Workbook("沪深京A股" + timenow + ".xlsx")
        # 创建工作表：
        worksheet = workbook.add_worksheet()
        #创建一个列表
        namelist = ['股票名称', '股票代码', '最新价', '跌涨幅', '成交量', '成交额', '振幅', '换手率', '市值', '量比', '最高', '最低', '今开', '昨收']
        # write_row(0, 0, data[, cell_format])  从（row, col）处开始向表中写入行。
        worksheet.write_row(0, 0, namelist)
    # 向excel文件中插入数据，
        i = 1
        # res是一个字典列表
        # item  是一个字典.遍历字典
        for item in res:
            # 返回值是自己设的一个列表,列表的值是  字典的键对应的 值.
            my_list = creatlist(item)
            #向文件的工作表中写入数据
            worksheet.write_row(i, 0, my_list)
            i = i + 1
        workbook.close()
    except Exception as e:
        print(e)
        print("insertexcel将数据插入excel表格失败")

# creatlist2将生成存入数据库的列表
def creatlist2(item):
    try:
        temp = []
        temp.append(item['Prod_name'])  # 股票名称
        temp.append(item['Market_Symbol'])  # 股票代码
        temp.append(item['Last_px'])  # 最新价
        temp.append(item['Px_change_rate'])  # 跌涨幅
        temp.append(item['Business_amount'])  # 成交量
        temp.append(item['Business_balance'])  # 成交额
        # 基本语句：=TEXT(数值，文本格式)
        temp.append(item['Amplitude'])  # 振幅
        temp.append(item['Turnover_ratio'])  # 换手率
        temp.append(item['Market_value'])  # 市值
        temp.append(item['Vol_ratio'])  # 量比
        temp.append(item['High_px'])  # 最高
        temp.append(item['Low_px'])  # 最低
        temp.append(item['Open_px'])  # 今开
        temp.append(item['Preclose_px'])  # 昨收
        print("插入mysql的列表生成成功")
        return temp
    except Exception as e:
        print(e)
        print("creatlist2函数失败")


#插入mysql:应当传入一个字典列表，将字典列表传入多线程，用里面的字典做creatlist2（）函数的参数
def insertmysql(res):
    try:
        # 插入：
        #新建链接
        con = pymysql.connect(
            host="localhost",  # 主机ip
            user="root",  # 数据库用户
            password="root",  # 用户对应的密码
            database="pymsql",  # 对应的数据库
            port=3306,  # 数据库端口，默认3306
            charset='utf8'  # 数据库编码
        )
        #新建游标
        cur = con.cursor()

        # 存入数据库
        # 参数为字典列表，字典列表做多线程参数，将字典传入函数
        with ThreadPoolExecutor(max_workers=2) as pool:
            #my_lists是返回值的列表（二级列表），返回值是creatlist2的返回值（列表）
            #res是字典列表，这是线程池的一种书写形式
            my_lists = pool.map(creatlist2, res)
            print("插入数据库的列表队列  准备中")
            for my_list in my_lists:
                val = tuple(my_list)
                print(val)
                time.sleep(1)
                sql = "INSERT INTO gupiao(mingcheng,daima,zuixinjia,zhangdiefu,chengjiaoliang,chengjiaoer,zhenfu,huanshoulv,shizhi,liangbi,zuigao,zuidi,jinkai,zuoshou) VALUES \
                               (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                print(sql)
                #转为列表包含元组的形式传入执行语句
                cur.executemany(sql, [val])
                print("insertmysql将一条数据插入mysql成功")
                con.commit()
    except Exception as e:
        print(e)
        print("insertmysql将数据插入mysql失败")




if __name__ == "__main__":
    #建表语句
    try:
        con = pymysql.connect(
            host="localhost",  # 主机ip
            user="root",  # 数据库用户
            password="root",  # 用户对应的密码
            database="pymsql",  # 对应的数据库
            port=3306,  # 数据库端口，默认3306
            charset='utf8'  # 数据库编码
        )
        cur = con.cursor()

        sql = 'create table  `gupiao` (`id` int(50) NOT NULL AUTO_INCREMENT ,mingcheng VARCHAR(20), daima VARCHAR(20),zuixinjia float,zhangdiefu float,chengjiaoliang VARCHAR(100)\
                     ,chengjiaoer VARCHAR(100),zhenfu float, huanshoulv float, shizhi VARCHAR(100),  liangbi float, zuigao float,zuidi float,\
                      jinkai float,zuoshou float, PRIMARY KEY (`id`))'
        cur.execute(sql)
        print('ok table')

    except Exception as e:
        print("建表失败")
    try:
        #选取一个网页,获取字典里面Total共多少数量d
        abc = "https://hq.techgp.cn/rjhy-gmg-quote/api/1/stock/quotes/shszstocksort?" \
              "en_hq_type_code=XSHG.ESA%2CXSHE.ESA%2CXSHG.KSH&sort_field_name=px_change_rate&sort_type=1&pageNo=1&pageSize=20"
        sum = requests.get(abc).json()['data']['Total']
        #知道共有多少数据,将数量后缀到网址最后,与网址拼接成一个网址,数量写多少获取多少条数据
        url = "https://hq.techgp.cn/rjhy-gmg-quote/api/1/stock/quotes/shszstocksort?en_hq_type_code=XSHG.ESA%2CXSHE.ESA%2CXSHG.KSH&sort_field_name=px_change_rate&sort_type=1&pageNo=1&pageSize=" + "700"

        # 查看接口返回的json串,并获取字典的data键(键对应一个字典),在获取data对应字典的Stocks键(键对应一个字典列表),
        res = requests.get(url).json()['data']['Stocks']
        print(res)
        # 数据处理
        print(len(res))
        #爬取到的数据进行处理，把含空字典或者字典里面含空值的删除掉
        res=shujupandas(res)
        print(len(res))

        #插入excel
        insertexcel(res)
        # # 插入mysql
        insertmysql(res)
    except Exception as e:
        print(e)

    finally:
        print("Program end!")