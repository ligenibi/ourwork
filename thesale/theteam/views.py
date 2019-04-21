from django.shortcuts import render
from django.shortcuts import HttpResponse, render, redirect
from theteam import models
# Create your views here.

def listtemaer(request):
    listteam = models.team.objects.all()
    return render(request, 'list.html',{
        'listteam': listteam
    })


def publish(request):
    if request.method == "GET":
        return render(request, "publish.html")
    if request.method == "POST":
        first = request.POST.get("first", None)
        telephone = request.POST.get("telephone", None)
        email = request.POST.get("email", None)
        competition = request.POST.get("competition", None)
        teamer = request.POST.get("teamer", None)
        description = request.POST.get("description", None)
        print(first, telephone, email, competition, teamer, description )
        models.team.objects.create(first=first, telephone=telephone, email=email, competition=competition, teamer=teamer, description=description)
        return render(request, 'publish.html', {
             'error': "不能有要求的字段为空!"
            })


