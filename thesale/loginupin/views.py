from django.conf.urls import url

from django.shortcuts import HttpResponse, render, redirect
from loginupin import models
from datetime import datetime
# Create your views here.
def loginin(request):
    if request.method == "GET":
        return render(request, 'loginin.html')
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        result = models.users.objects.filter(user_email=email,user_password=password)
        if result:
            return redirect('/loginupin/signup/')
        else:
            return render(request, 'loginin.html')
def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    if request.method == "POST":
        name = request.POST.get("name", None)
        email = request.POST.get("email", None)
        phone = request.POST.get("phone", None)
        password = request.POST.get("password", None)
        if name != None and email != None and password != None and phone != None:
            models.users.objects.create(user_name=name, user_email=email, user_phone=phone, user_password=password)
            return redirect('/')
        else:
            return render(request, "signup.html")

def test(request):
     now = datetime.now()
     print(now)
     return render(request, 'test.html', {
        'userinfo':{'k1': 'v1','k2': 'v2'}
         ,'name':'xxx',
          'now': now
    })

def blank(request):
    return render(request , "blank.html")

def xxx(request):
    return render(request, "try.html")

def self(request):
    return render(request, "self.html")


def uploadImg(request):
    """
    图片上传
    :param request:
    :return:
    """
    if request.method == 'POST':
        print(request.FILES.get('img').name)
        new_img = models.IMG(
            img=request.FILES.get('img'),
            name=request.FILES.get('img').name
        )
        new_img.save()
    return redirect('/loginupin/show/')


def showImg(request):
    """
    图片显示
    :param request:
    :return:
    """
    imgs = models.IMG.objects.all()
    content = {
        'imgs': imgs,
    }
    for i in imgs:
        print(i.img.url)
    return render(request, 'show.html', content)





