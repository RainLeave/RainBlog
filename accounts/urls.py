from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # 用户登录
    path('login/', views.user_login, name='login'),
    # 用户退出
    path('logout/', views.user_logout, name='logout'),
    # 用户注册
    path('register/', views.user_register, name='register'),
    # 用户删除
    path('delete/<int:id>/', views.user_delete, name='delete'),
    # 用户信息
    path('edit/<int:id>/', views.profile_edit, name='edit'),

    # 关于
    path('about/', views.about, name='about'),
    # 微语
    path('whisper/', views.whisper, name='whisper'),

    # 相册集
    path('album/', views.album, name='album'),

    # 留言薄
    path('leacots/', views.leacots, name='leacots'),

]