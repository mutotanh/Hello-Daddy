# Register your models here.
#超级管理员  root  密码：admin123
from django.contrib import admin
from app.models import Food
# admin美化
admin.site.site_header = '美食数据展示系统'
admin.site.index_title = '首页'

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','city','shopname','mainregionname','maincategoryname','tastescore','environmentscore','servicescore','avgprice','shopurl']

    list_per_page =15
    search_fields = ('shopname','mainregionname')  # 设置搜索框
admin.site.register(Food,UserAdmin)