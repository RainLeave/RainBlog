from mytest.models import *
from mytest.forms import *
from django.http import HttpResponse
from django.shortcuts import render_to_response

"""
>>> from django import forms
>>> class OptionalPersonForm(forms.Form):
...     first_name = forms.CharField()
...     last_name = forms.CharField()
...     nick_name = forms.CharField(required=False)
>>> data = {'first_name': 'John', 'last_name': 'Lennon'}
>>> f = OptionalPersonForm(data)
>>> f.is_valid()
True
>>> f.cleaned_data
{'nick_name': '', 'first_name': 'John', 'last_name': 'Lennon'}
"""
# 创建视图函数，来处理我们写好的表单
def views(request): # 视图函数第一个参数必须是request
    if request.method == 'POST':
        # 当请求时POSTd时，将request.POST中的数据填入表单中
        form = Mysiteform(request.POST)
        # 如果form有效，验证中的数据
        if form.is_valid():
            data = form.cleaned_data
            # 取title这样一个字段数据做验证
            title = data["title"]
        # 返回
        return HttpResponse

    # 当请求时GET时，返回并渲染这个模板
    form = Mysiteform()
    return render_to_response('mytest/form.html', {'form': form})


# 之前我们通过使用render和context来处理一些东西
# 现在不使用render,使用render_to_response(可以直接将参数放入)

# from django.shortcuts import render_to_response
#
#
# def views(request):
#     return render_to_response('2.html', {'name': 'Hello'})
#


# # 写下第一个视图函数
# from django .http import HttpResponse, Http404
#
# """
# Django可识别的视图需要瞒住以下两个条件:
# 第一个参数的类型:HttpReuqest
# 返回HttpResponse实例
#
# """
#
#
# def hello(request):
#     return HttpResponse("Hello World!")
#
#
# # 第一个参数:request
# # d第二个参数:num 即路径后面匹配的数字
# def hello1(request, num):
#     # 对路径中的数字做一个处理
#     try:
#         num = int(num)
#     except ValueError:
#         # 将错误抛出去
#         # 引入函数Http404
#         raise Http404
