from django.db import models

# Create your models here.
from django.utils import timezone
from WH1803Django.settings import DB_FIELD_VALID_CHOICES


'''
小说标签类
'''
class Tag(models.Model):
	t_name = models.CharField(max_length=20, verbose_name="文章标签")
	t_info = models.CharField(max_length=50, verbose_name="标签描述")
	t_createtime = models.DateTimeField(default=timezone.now, db_index=True, verbose_name="创建时间")
	t_flag = models.IntegerField(default=0, verbose_name="控制字段", choices=DB_FIELD_VALID_CHOICES)
	operator = models.ForeignKey("auth.User", default=1, verbose_name="api操作者")

	def __str__(self):
		return self.t_name

	class  Meta:
		verbose_name = "标签"
		verbose_name_plural = verbose_name
		db_table = "tag"
		ordering = ["-t_createtime"]    #按照创建时间降序




'''
小说内容
Tag -- Art
1 ---- N
'''
class Art(models.Model):
	a_title = models.CharField(max_length=100, verbose_name="文章标题")
	a_info = models.CharField(max_length=200, verbose_name="文章描述")
	a_content= models.TextField(verbose_name="文章内容")
	# a_content = UEditorField(verbose_name="文章内容", width=1000, height=600,
	# 						 imagePath="media/arts_ups/ueditor/",
	# 						 filePath="media/arts_ups/ueditor/",
	# 						 blank=True, toolbars="full", default='')
	a_img = models.ImageField(null=True, blank=True, upload_to="media/arts_ups/%Y/%m",
							  verbose_name="封面", max_length=150)
	a_createtime = models.DateTimeField(default=timezone.now, db_index=True,
								   verbose_name="添加时间")

	a_tag = models.ForeignKey(Tag, verbose_name="关联文章标签")
	a_price = models.IntegerField(default=0, verbose_name="单价")
	a_flag = models.IntegerField(default=0, verbose_name="控制字段", choices=DB_FIELD_VALID_CHOICES)
	operator = models.ForeignKey("auth.User", default=1, verbose_name="api操作者")


	def __str__(self):
		return self.a_title


	class Meta:
		verbose_name = "小说"
		verbose_name_plural = verbose_name
		db_table = "art"
		ordering = ["-a_createtime"]  # 按照创建时间降序


'''
小说的章节信息
'''
class Chapter(models.Model):
	art = models.ForeignKey(Art, verbose_name="小说")
	title = models.CharField(max_length=100, verbose_name="章节标题")
	content = models.TextField(verbose_name="小说章节内容")
	create_time = models.DateTimeField(default=timezone.now, db_index=True,
								   verbose_name="添加时间")

	class Meta:
		db_table = "art_chapter"
		verbose_name = "小说章节"
		verbose_name_plural = verbose_name
