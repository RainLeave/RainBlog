

# 导入数据模型ArticlePost
from .models import Blog, BlogType

# 引入 Q 对象
from django.db.models import Q
# 引入redirect重定向模块
from django.shortcuts import render, redirect
# 引入分页模块
from django.core.paginator import Paginator
#
#
# def blog_list(request):
#
    # # 从 url 中提取查询参数
    # search = request.GET.get('search')
    # order = request.GET.get('order')
    # column = request.GET.get('column')
    # tag = request.GET.get('tag')
    #
    # # 初始化查询集
    # article_list = ArticlePost.objects.all()
    #
    # # 搜索查询集
    # if search:
    #     article_list = article_list.filter(
    #         Q(title__icontains=search) |
    #         Q(body__icontains=search)
    #     )
    # else:
    #     search = ''
    #
    # # 栏目查询集
    # if column is not None and column.isdigit():
    #     article_list = article_list.filter(column=column)
    #
    # # 标签查询集
    # if tag and tag != 'None':
    #
    #     article_list = article_list.filter(tags__name__in=[tag])
    #
    # # 查询集排序
    # if order == 'total_views':
    #     article_list = article_list.order_by('-total_views')
    #
    # paginator = Paginator(article_list, 1)
    # page = request.GET.get('page')
    # articles = paginator.get_page(page)
    #
    # # 需要传递给模板（templates）的对象
    # context = {
    #     'articles': articles,
    #     'order': order,
    #     'search': search,
    #     'column': column,
    #     'tag': tag,
    #     'order': order,
    #
    # }
    #
    # return render(request, 'article/list.html', context)



# test for DetailView
# 追梦人物的博客
from django.views.generic import ListView, DetailView
from articles.models import ArticlePost
from user_operation.forms import CommentForm
import markdown

from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


class PostDetailView(DetailView):
    """
    需求：
    查看某一篇文章的详情
    从数据库获取模型的一条记录
    然后渲染模板
    Django 提供了DetailView视图
    """
    # 属性的含义同ListView
    mode = ArticlePost
    template_ame = 'articles/detail.html'
    queryset = ArticlePost.objects.filter(created__lt=timezone.now())
    content_object_name = 'post'

    def get(self, request, *args, **kwargs):
        # 覆写 get 方法: 因为每当文章被访问一次，就需要将文章阅读量+1
        # get 方法：返回一个HttpRespose对象
        # 需要先调用父类的get方法：因为只有当get 方法被调用后，才有self.object属性
        # 值为ArticlePost模型实例（即被访问的文章post）
        response = super(PostDetailView, self).get(request, *args, **kwargs)


        # 将文章阅读量 +1
        # 注意self.object的值 就是被访问的文章 post
        self.object.increase_views()

        # 视图必须返回一个 HttpResponse 对象
        return response

    def get_object(self, queryset=None):
        # 覆写 get_object 方法： 因为需要对文章post的值进行渲染
        post = super(PostDetailView, self).get_object(queryset=None)
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                            'markdown.extensions.extra',
                                            'markdown.extensions.codehilite',
                                            'markdown.extensions.toc',
            ]
        )
        return post

    # def get_object(self):
    #     return get_object_or_404(User, pk=self.request.user.id)

    def get_context_data(self, **kwargs):
        # 覆写 get_context_data: 因为除了将post文章传递给模板外(DetailView已经帮我们完成)
        # 还需要将评论表单、post下的评论列表传递给模板
        context = super(PostDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        return context