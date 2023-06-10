# Register your models here.
#超级管理员  root  密码：admin123
from django.contrib import admin
from app.models import Gupiao
# admin美化
admin.site.site_header = '股票数据展示系统'
admin.site.index_title = '首页'

class UserAdmin(admin.ModelAdmin):
    list_display = ['mingcheng','daima','zuixinjia','zhangdiefu','chengjiaoliang','chengjiaoer','zhenfu','huanshoulv','shizhi','liangbi'
                    ,'zuigao','zuidi','jinkai','zuoshou']
    list_per_page =15
    search_fields = ('mingcheng','daima')  # 设置搜索框
admin.site.register(Gupiao,UserAdmin)