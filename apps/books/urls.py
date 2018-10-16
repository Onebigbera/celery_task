# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/9/27 下午3:56' 

from django.conf.urls import url, include
from books.index_handler import IndexHandler
from books.add_handler import AddHandler


urlpatterns = [
    url(r'^index/$', IndexHandler),
    url(r'^add/$', AddHandler),
]
