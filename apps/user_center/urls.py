# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/9/27 下午3:56' 

from django.conf.urls import url, include
from user_center.register_handler import RegisterHandler

'''
用户注册url： /user/register
'''
urlpatterns = [
    url(r'^register/$', RegisterHandler, name="user_register"),
]
