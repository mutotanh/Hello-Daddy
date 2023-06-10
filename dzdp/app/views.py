from django.shortcuts import render,HttpResponse,redirect
# from cryptography.hazmat.backends import default_backend
from app import models

def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    username = request.POST.get("user")
    password = request.POST.get("password")
    #
    data_list = models.User.objects.all()#将返回一个列表，列表中的每一个是一个对象
    print(data_list)
    for obj in data_list:
        if username == obj.users and password == obj.password:
            return render(request, "shouye.html")
            # return HttpResponse("登录失败")
    #如果失败，返回页面，进行重新登录
    return render(request, 'login.html', {"error_msg": "用户名或密码错误"})

def regiser(request):
    if request.method == "POST":
        username = request.POST.get("user")
        password = request.POST.get("password")
        models.User.objects.create(users=username,password=password)
        #注册成功，返回给一个登录页面
        return render(request, "login.html", {"error_msg": "用户名或密码错误"})

def shouye(request):
    return render(request, "shouye.html")


quanju=[]
quanju2=[]
#展示页面
from django.core.paginator import Paginator
def page_test(request):
    #global设置全局变量，在各个函数里面都能用，只要在使用函数里面也填上这两句
    global quanju
    global quanju2
    quanju=[]
    quanju2=[]
    # 测试分页功能
    if request.method == "GET":
        data_list = models.Food.objects.all().order_by("city")#将返回一个列表，列表中的每一个是一个对象
        paginator = Paginator(data_list, 15)    #
        num_p = request.GET.get('page', 1)  # 以page为键得到默认的页面1  #在用户进行get请求时，在提交的url里，寻找名为page的GET参数，而且如果参数没有提交，返回一个空的字符串
        page = paginator.page(int(num_p))
        return render(request, 'page_test.html', {"paginator":paginator,"page":page})

    if request.method == 'POST':
        category = request.POST.get('category')#下拉框
        quanju.append(category)
        search = request.POST.get('search')#获取搜索提交的内容
        quanju2.append(search)
        if category == 'id':
            data_list = models.Food.objects.filter(id=search)
        if category == 'city':
            data_list = models.Food.objects.filter(city=search)
        if category == 'shopname':
            data_list = models.Food.objects.filter(shopname=search)
        if category == 'mainregionname':
            data_list = models.Food.objects.filter(mainregionname=search)#__icontains 包含 忽略大小写 ilike ‘%aaa%’
        if category == 'maincategoryname':
            data_list = models.Food.objects.filter(maincategoryname=search)
        if category == 'tastescore':
            data_list = models.Food.objects.filter(tastescore=search)
        if category == 'environmentscore':
            data_list = models.Food.objects.filter(environmentscore=search)
        if category == 'servicescore':
            data_list = models.Food.objects.filter(servicescore=search)
        if category == 'avgprice':
            data_list = models.Food.objects.filter(avgprice=search)
        if category == 'shopurl':
            data_list = models.Food.objects.filter(shopurl=search)
        paginator = Paginator(data_list, 15)
        num_p = request.POST.get('page', 1)  # 以page为键得到默认的页面1,post请求未传入page，默认无参返回第一页
        page = paginator.page(int(num_p))
        return render(request, 'page_test1.html', {"paginator":paginator,"page":page})  # locals()用法：


def page_test1(request):
    global quanju
    global quanju2
    if request.method == "GET":
        if quanju== []:
            return HttpResponse("访问http://127.0.0.1:8000/page_test1/查询后自动跳转本网页")
        else:
            if quanju[0] == 'id':
                data_list = models.Food.objects.filter(id=quanju2[0])
            if quanju[0] == 'city':
                data_list = models.Food.objects.filter(city=quanju2[0])
            if quanju[0] == 'shopname':
                data_list = models.Food.objects.filter(shopname=quanju2[0])
            if quanju[0] == 'mainregionname':
                data_list = models.Food.objects.filter(mainregionname=quanju2[0])  # __icontains 包含 忽略大小写 ilike ‘%aaa%’
            if quanju[0] == 'maincategoryname':
                data_list = models.Food.objects.filter(maincategoryname=quanju2[0])
            if quanju[0] == 'tastescore':
                data_list = models.Food.objects.filter(tastescore=quanju2[0])
            if quanju[0] == 'environmentscore':
                data_list = models.Food.objects.filter(environmentscore=quanju2[0])
            if quanju[0] == 'servicescore':
                data_list = models.Food.objects.filter(servicescore=quanju2[0])
            if quanju[0] == 'avgprice':
                data_list = models.Food.objects.filter(avgprice=quanju2[0])
            if quanju[0] == 'shopurl':
                data_list = models.Food.objects.filter(shopurl=quanju2[0])
            paginator = Paginator(data_list, 15)  #
            num_p = request.GET.get('page',
                                    1)  # 以page为键得到默认的页面1  #在用户进行get请求时，在提交的url里，寻找名为page的GET参数，而且如果参数没有提交，返回一个空的字符串
            page = paginator.page(int(num_p))
            return render(request, 'page_test1.html',{"paginator": paginator, "page": page})  # locals()用法：locals()可以直接将函数中所有的变量全部传给模板。
            # 当然这可能会传递一些多余的参数，有点浪费内存的嫌疑。
            # 用法：
            # return render(request, 'blog_add.html', locals())
            # return render_to_response('blog_add.html', locals())
    if request.method == 'POST':
        category = request.POST.get('category')  # 下拉框
        quanju.append(category)
        search = request.POST.get('search')  # 获取搜索提交的内容
        quanju2.append(search)
        if category == 'id':
            data_list = models.Food.objects.filter(id=search)
        if category == 'city':
            data_list = models.Food.objects.filter(city=search)
        if category == 'shopname':
            data_list = models.Food.objects.filter(shopname=search)
        if category == 'mainregionname':
            data_list = models.Food.objects.filter(mainregionname=search)  # __icontains 包含 忽略大小写 ilike ‘%aaa%’
        if category == 'maincategoryname':
            data_list = models.Food.objects.filter(maincategoryname=search)
        if category == 'tastescore':
            data_list = models.Food.objects.filter(tastescore=search)
        if category == 'environmentscore':
            data_list = models.Food.objects.filter(environmentscore=search)
        if category == 'servicescore':
            data_list = models.Food.objects.filter(servicescore=search)
        if category == 'avgprice':
            data_list = models.Food.objects.filter(avgprice=search)
        if category == 'shopurl':
            data_list = models.Food.objects.filter(shopurl=search)
        paginator = Paginator(data_list, 15)
        num_p = request.POST.get('page', 1)  # 以page为键得到默认的页面1,post请求未传入page，默认无参返回第一页
        page = paginator.page(int(num_p))
        return render(request, 'page_test1.html', {"paginator": paginator, "page": page})  # locals()用法：

def bar(request):
    return render(request, "bar.html")

def Pie(request):
    return render(request, "Pie.html")

def Radar(request):
    return render(request, "Radar.html")

def scatter(request):
    return render(request, "scatter.html")

def echartstubiao(request):
    data_list = models.Food.objects.all()  # 将返回一个列表，列表中的每一个是一个对象
    data_list=data_list[:50]
    return render(request, "echartstubiao.html",{"data_list":data_list})

