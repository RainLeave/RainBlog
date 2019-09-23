# -*- coding:utf-8 -*-


class MyMiddleWare(object):
    def __init__(self):
        print('Middleware')

    def process_view(self, request, func, args, kwargs):
        print(func)