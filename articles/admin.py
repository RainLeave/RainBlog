from django.contrib import admin

from articles.models import ArticlePost, ArticleColumn


# 2.0以上使用装饰器
@admin.register(ArticlePost)
class ArticlePostAdmin(admin.ModelAdmin):
    list_display=('id', 'author', 'title', 'body', 'created', 'updated')

admin.site.unregister(ArticlePost)
admin.site.register(ArticlePost, ArticlePostAdmin)


# 2.0以上使用装饰器
@admin.register(ArticleColumn)
class ArticleColumnAdmin(admin.ModelAdmin):
    list_display=('id',  'title', 'created')

admin.site.unregister(ArticleColumn)
admin.site.register(ArticleColumn, ArticleColumnAdmin)

# ArticlePost的模型管理器 # 1.7版本之前的
# class ArticlePostAdmin(admin.ModelAdmin):
#   list.display('id', 'author', 'title', 'body', 'created', 'updated')

# admin.site.register(ArticlePost, ArticlePostAdmin)

# 1.7以上使用装饰器
# @admin.register(admin.ModelAdmin)
# class ArticlePostAdmin(admin.ModelAdmin):
#  list_display('id', 'author', 'title', 'body', 'created', 'updated')



# 注册文章栏目
# admin.site.register(ArticleColumn)