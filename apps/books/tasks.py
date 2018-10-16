from time import sleep

from celery import shared_task
from django.core.mail import send_mail
from WH1803Django import settings

'''
此文件是属于celery工作worker处理进程文件
'''

@shared_task
def add(x, y):
    sleep(1)
    print("add delay call ")
    r = settings.R
    my_sum = int(x) + int(y)
    r.set("celery_task_add", my_sum)
    return  my_sum


