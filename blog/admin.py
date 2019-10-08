from django.contrib import admin
from .models import Blog, BlogType


# 2.0以上使用装饰器
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=('id', 'blog_type', 'content', 'author', 'created_time', 'created_time')
admin.site.unregister(Blog)
admin.site.register(Blog, BlogAdmin)


# 2.0以上使用装饰器
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display=('id', 'type_name')
admin.site.unregister(BlogType)
admin.site.register(BlogType, BlogTypeAdmin)