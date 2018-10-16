# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/9/27 下午3:57' 

from django.shortcuts import render

from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from user_center import forms
from user_center import models
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def RegisterHandler(request):
	reg_form = forms.ArtsUserRegForm()

	context = dict(form=reg_form)

	return render(request, "register_handler.html", context=context)

