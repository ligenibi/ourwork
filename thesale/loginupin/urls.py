from django.urls import path
from loginupin import views as loginupin_views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
app_name = 'loginupin' # 一定要写这一行，否则html中会报错 'account' is not a registered namespace

urlpatterns = [
     # 列表页的url规则
    # path('1/', theteam_views.post_detail, name=''),# 详情页的url规则
    path('', loginupin_views.loginin, name='loginin'),
    path('signup/', loginupin_views.signup, name='signup'),
    path('test/', loginupin_views.test, name='test'),
    path('blank/', loginupin_views.blank, name='blank'),
    path('try/', loginupin_views.xxx, name='xxx'),
    path('self/', loginupin_views.self, name='self'),
    path('upload/', loginupin_views.uploadImg, name='upload'),
    path('show/', loginupin_views.showImg, name='show'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  这句话是用来指定和映射静态文件的路径
