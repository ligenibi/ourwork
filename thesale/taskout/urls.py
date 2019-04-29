from django.urls import path
from taskout import views as taskout_views


app_name = 'taskout' # 一定要写这一行，否则html中会报错 'account' is not a registered namespace

urlpatterns = [

    #path('articles/<int:num>/', theteam_views.articles, name='articles'),

]#+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  这句话是用来指定和映射静态文件的路径
