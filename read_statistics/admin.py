from django.contrib import admin
from .models import ReadNum, ReadDetail


# 2.0以上使用装饰器
@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display=('id', 'tag', 'read_num', 'object_id', 'content_object')


admin.site.unregister(ReadNum)
admin.site.register(ReadNum, ReadNumAdmin)


# 2.0以上使用装饰器
@admin.register(ReadDetail)
class ReadDetailAdmin(admin.ModelAdmin):
    list_display=('id', 'date', 'read_num', 'content_type', 'object_id', 'content_object')


admin.site.unregister(ReadDetail)
admin.site.register(ReadDetail, ReadDetailAdmin)
