# 记得引入include
from django.urls import path, include
from . import views

# 正在部署的应用的名称
app_name = 'mytest'


urlpatterns = [
    # path函数将url映射到视图
    path('hello/', views.views, name='hello-list'),
]