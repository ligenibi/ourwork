from django.contrib import admin

# Register your models here.
import xadmin

import loginupin.models
# Register your models here.
from .models import *

from xadmin import views

class GlobalSetting(object):

# 设置后台顶部标题

    site_title ='我是后台管理'

    # 设置后台底部标题

    site_footer ='hhh'

    menu_style = "accordion"
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(users,GlobalSetting)
xadmin.site.register(Student,GlobalSetting)