"""Blog_Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# 记得引入include
from django.urls import path, include
from django.conf import settings

from articles.views import article_list
from django.conf.urls.static import static


# 存放映射关系的列表
urlpatterns = [
    path('admin/', admin.site.urls),

    # 新增代码，配置app的url
    path('article/', include('articles.urls', namespace='articles')),
    # 用户管理
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('password-reset/', include('password_reset.urls')),

    path('comment/', include('user_operation.urls', namespace='comment')),
    # notice
    path('notice/', include('notice.urls', namespace='notice')),

    path('account/', include('allauth.urls')),

    # home
    path('', article_list, name='home'),

    # mytest
    path('mytest/', include('mytest.urls', namespace="mytest")),
    # path('blog/', include('blog.urls', namespace="blog")),
    # path('read_statistics/', include('read_statistics.urls', namespace="read_statistics"))

]

urlpatterns += [

    path('ckeditor/', include('ckeditor_uploader.urls')),
    # django 2.0以下用
    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

#  添加这行
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)