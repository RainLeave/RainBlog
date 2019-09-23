
from django import template
register = template.Library()

@register.filter(name='transfer')
def transfer(value, arg):
    """将输出强制转换为字符串 arg """
    return arg

@register.filter()
def lower(value):
    """将字符串转换为小写字符"""
    return value.lower()