# 子路由
from django.conf.urls import url, include
from app.views import login,regiser,shouye,page_test,page_test1,bar,Pie,Radar,scatter,echartstubiao
urlpatterns = [
    url('login/',login),
    url('regiser/', regiser),
    url('shouye/', shouye),
    url('page_test/', page_test),
    url('page_test1/', page_test),


    url('bar/', bar),
    url('Pie/', Pie),
    url('Radar/', Radar),
    url('scatter/', scatter),
    #echarts实现的图表
    url('echartstubiao/', echartstubiao),

]
# Django的迁移命令和反向生成命令：
#     生成迁移命令
#     python manage.py makemigrations
#
#     执行迁移命令
#     python manage.py migrate
#

#     反向生成命令
#     python manage.py inspectdb > app/models.py
# Django的迁移命令和反向生成命令：
#     生成迁移命令
#     python manage.py makemigrations
#
#     执行迁移命令
#     python manage.py migrate
#

#     反向生成命令
#     python manage.py inspectdb > app/models.py