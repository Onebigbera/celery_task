# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/9/28 上午11:48' 

from django.shortcuts import HttpResponse
from books.tasks import  add
from user_center.tasks import say_hello

def AddHandler(request):
	'''
	/add?x=3&y=5
	:param request:
	:return:
	'''
	x = int(request.GET.get('x', 0))
	y = int(request.GET.get('y', 0))
	#add.delay(x, y)
	say_hello.delay('liubowen')
	return HttpResponse('add delay.')