import pymysql

pymysql.install_as_MySQLdb()
default_app_config='register.apps.RegisterConfig'

# 在Django项目的__init__.py文件中写如下代码，告诉Django使用pymysql模块连接MySQL数据库: