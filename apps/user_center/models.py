from django.db import models

# Create your models here.
from django.utils import timezone
from WH1803Django.settings import USER_CHOICES

'''
会员信息
'''
class  ArtsUser(models.Model):
	username = models.CharField(max_length=50, verbose_name="用户名")
	password = models.CharField(max_length=100, verbose_name="密码")
	email = models.EmailField(verbose_name="邮箱")
	createtime = models.DateTimeField(default=timezone.now, db_index=True, verbose_name="添加时间")
	flag = models.IntegerField(default=0, verbose_name="会员控制字段", choices=USER_CHOICES)
	operator = models.ForeignKey("auth.User", default=1, verbose_name="api操作者")

	def __str__(self):
		return self.username

	class Meta:
		db_table = "arts_user"
		verbose_name = "会员信息"
		verbose_name_plural = verbose_name
		ordering = ["-createtime"]

