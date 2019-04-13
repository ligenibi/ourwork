"""thesale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.shortcuts import HttpResponse
from django.shortcuts import render
from loginupin import views as loginupin_views
import xadmin

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', loginupin_views.loginin),
    path('signup/', loginupin_views.signup),
    path('test/', loginupin_views.test),
    path('blank/', loginupin_views.blank),
]