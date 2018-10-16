from time import sleep

from celery import shared_task
from WH1803Django import settings

'''
此文件是属于celery工作worker处理进程文件
'''

@shared_task
def say_hello(str):
    sleep(1)
    print("say hello.")
    r = settings.R
    r.set("celery_hello", 'hello, ' + str)
    return  str


