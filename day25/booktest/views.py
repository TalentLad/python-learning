import io

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from booktest.models import BookInfo, HeroInfo, Areas, PicTest,GoodsInfo
from datetime import date
from PIL import Image, ImageDraw, ImageFont


# Create your views here.

def index(request):
    context = '<h1>hello python</h1>'
    return render(request, 'booktest/index.html', {'context': context})


def index2(request):
    return HttpResponse('Hello python2')


def my_render(request, temp_name, contex=None):
    # 加载模板文件
    if contex is None:
        contex = {}
    temp = loader.get_template(temp_name)
    # 定义模板上下文
    res_html = temp.render(contex)
    # 返回给浏览器
    return HttpResponse(res_html)


def show_books(request):
    books = BookInfo.objects.all()
    return render(request, 'booktest/show_books.html', {'books': books})


def show_heros(request, bid):
    book = BookInfo.objects.get(id=bid)
    heros = book.heroinfo_set.all()

    return render(request, 'booktest/show_heros.html', {'book': book, 'heros': heros})


def create(request):
    b = BookInfo()
    b.btitle = '神雕侠侣'
    b.bpub_date = date(2001, 7, 28)
    b.save()
    return HttpResponseRedirect('/books')


def delete(request, bid):
    b = BookInfo.objects.get(id=bid)
    b.delete()
    return HttpResponseRedirect('/books')


def areas(request):
    area = Areas.objects.get(atitle='西安市')
    aparent = area.aparent
    area_list = area.areas_set.all()
    return render(request, 'booktest/areas.html', {'area': area, 'aparent': aparent, 'area_list': area_list})


def login(request):
    if request.session.has_key('islogin'):
        return redirect('/index2')
    elif 'username' in request.COOKIES:
        username = request.COOKIES['username']
    else:
        username = ''
    return render(request, 'booktest/login.html', {'username': username})


def login_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    print(username)
    print(password)
    print(remember)
    # return HttpResponse('ok')
    if username == 'xiaohu' and password == '123':
        response = redirect('/index2')
        if remember == 'on':
            response.set_cookie('username', username, max_age=14 * 24 * 3600)
        request.session['islogin'] = True
        return response
    else:
        return redirect('/login')


def test_ajax(request):
    return render(request, 'booktest/test_ajax.html')


def ajax_handle(request):
    return JsonResponse({'res': 1})


def login_ajax(request):
    return render(request, 'booktest/login_ajax.html')


def login_ajax_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username)
    print(password)
    if username == '小胡' and password == '123':
        return JsonResponse({'res': 1})
    else:
        return JsonResponse({'res': 0})


def set_session(request):
    request.session['username'] = 'admin'
    request.session['age'] = 18
    return HttpResponse('设置session ok')


def get_session(request):
    username = request.session['username']
    age = request.session['age']
    return HttpResponse(username + str(age))


def test_filter(request):
    books = BookInfo.objects.all()
    return render(request, 'booktest/test_filters.html', {'books': books})


def test_inherit_base(request):
    return render(request, 'booktest/base.html')


def test_ingerit_children(request):
    return render(request, 'booktest/children.html')


def verify_code(request):
    # 引入随机函数模块
    import random
    # 定义变量,用于画面的背景色,宽,高,RGB
    bg_color = (random.randrange(20, 100), random.randrange(20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image('RGB', (width, height), bg_color)
    #创建画笔对象
    draw = ImageDraw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0,100):
        xy = (random.randrange(0,width),random.randrange(0,height))
        fill = (random.randrange(0,255),255,random.randrange(0,255))
        draw.point(xy,fill=fill)
    #定义验证码的备选值
    str1 = 'ABC123EFGHIJK456LMNPQRS789TUVWXYZ0'
    #随机选取四个值作为验证码
    rand_str = ''
    for i in range(4):
        rand_str += str1[random.randrange(0,len(str1))]
    #构造字体对象
    font = ImageFont.truetype('STSONG.TTF',23)
    #构造字体颜色
    fontcolor = (255,random.randrange(0,255),random.randrange(0,255))
    #绘制四个字
    draw.text((5,2),rand_str[0],font=font,fill = fontcolor)
    draw.text((25,2),rand_str[1],font=font,fill = fontcolor)
    draw.text((50,2),rand_str[2],font=font,fill = fontcolor)
    draw.text((75,2),rand_str[3],font=font,fill = fontcolor)
    #释放画笔
    del draw
    #存入session用于进一步做验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    buf = io.BytesIO()
    #将图片保存在内存中,文件类型为png
    im.save(buf,'png')
    #将内存中的图片数据返还给客户端
    return HttpResponse(buf.getvalue(),'image/png')

def show_args(request,a,b):
    return HttpResponse(str(a) + ':' + str(b))

def show_kwargs(request,c,d):
    return HttpResponse(str(c) + ':' + str(d))

def url_reverse(request):
    return render(request,'booktest/url_reverse.html')

def show_upload(request):
    return render(request,'booktest/upload_pic.html')

from day25 import settings

def upload_handle(request):
    # 1获取上传文件的处理对象
    pic = request.FILES['pic']
    # 2创建一个文件
    save_path = '%s/booktest/%s' % (settings.MEDIA_ROOT,pic.name)
    with open(save_path,'wb') as f:
        # 3 获取文件上传的内容并写到创建的文件中
        for content in pic.chunks():
            f.write(content)

    # 4 在数据库中保存上传记录
    PicTest.objects.create(goods_pic='booktest/%s' % pic.name)
    return HttpResponse('ok')

def pic_show(request):
    pic = PicTest.objects.get(id = 2)
    context = {'pic':pic}
    return render(request,'booktest/pic_show.html',context)

def show_page(request,pindex=1):
    areas = Areas.objects.filter(aparent__isnull=True)
    paginator = Paginator(areas,10)
    pindex = int(pindex)
    page = paginator.page(pindex)
    return render(request,'booktest/show_areas.html',{'page':page})

def editor(request):
    return render(request,'booktest/editor.html')

def save_editor(request):
    goodInfo = GoodsInfo()
    goodInfo.gcontent = request.POST.get('gcontent')
    goodInfo.save()
    return HttpResponse('ok')

def show(request):
    goods = GoodsInfo.objects.get(id = 3)
    return render(request,'booktest/show.html',{'goods':goods})
