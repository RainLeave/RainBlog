from django.urls import path

from blog.views import PostDetailView

urlpatterns = [
    path('(?P<pk>[0-9]+)/$', PostDetailView.as_view(), name='article-detail'),
]
