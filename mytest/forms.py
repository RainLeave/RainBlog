# 创建一个自定义的表单类
from django import forms


class Mysiteform(forms.Form):
    name = forms.CharField()
    author = forms.CharField()
    date = forms.CharField()