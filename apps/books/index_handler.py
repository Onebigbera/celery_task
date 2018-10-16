# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/9/27 下午4:14' 

from django.shortcuts import render, HttpResponseRedirect
from books import models

def IndexHandler(request):
	#logger.debug("IndexHandler:enter.")
	url = request.path
	t = int(request.GET.get('t', 0))
	page = int(request.GET.get('page', 1))
	tags = models.Tag.objects.filter(t_flag=0)  # 获取未删除的标签
	if t == 0:
		total = models.Art.objects.filter(a_flag=0).count()
	else:
		total = models.Art.objects.filter(a_flag=0, a_tag_id=t).count()
	#logger.info(f"IndexHandler, t:{t}, page:{page}, total:{total}")
	context = dict(
		pagenum=1,
		total=0,
		prev=1,
		next=1,
		pagerange=range(1, 2),
		data=[],
		url=url,
		tags=tags,
		page=page,
		t=t,
	)
	shownum = 10
	if total > 0:
		import math
		pagenum = int(math.ceil(total / shownum))
		# logger.warn(f"IndexHandler, pagenum: {pagenum}")
		if page < 1:
			url = url + "?page=1&t=%d" % t
			return HttpResponseRedirect(url)
		if page > pagenum:
			url = url + "?page=%d&t=%d" % (pagenum, t)
			return HttpResponseRedirect(url)
		offset = (page - 1) * shownum
		if t == 0:
			data = models.Art.objects.filter(a_flag=0)[offset:offset + shownum]
		else:
			data = models.Art.objects.filter(a_tag_id=t, a_flag=0)[offset:offset + shownum]
		key = "page:%d:t:%d" % (page, t)
		#logger.warn(key)
		#utils.store_rds_str(key, data)

		btnum = 5
		if btnum > pagenum:
			firtpage = 1
			lastpage = btnum
		else:
			if page == 1:
				firtpage = 1
				lastpage = btnum
			else:
				firtpage = page - 2
				lastpage = page + btnum - 2
				if firtpage < 1:
					firtpage = 1
				if lastpage > pagenum:
					lastpage = pagenum
		prev = page - 1
		next = page + 1
		if prev < 1:
			prev = 1
		if next > pagenum:
			next = pagenum

		context = dict(
			pagenum=pagenum,
			total=total,
			prev=prev,
			next=next,
			pagerange=range(firtpage, lastpage + 1),
			data=data,
			url=url,
			tags=tags,
			page=page,
			t=t,
		)
	return render(request, "index_handler.html", context=context)





