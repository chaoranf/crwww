# encoding: utf-8,这个玩意要加到第一行

from django.http import HttpResponse
from django.shortcuts import render_to_response

# 表单
def search_form(request):
	return render_to_response('sheet.html')

# 接收请求数据
def search(request):
	request.encoding='utf-8'
	if 'q' in request.GET:
		message = '你搜索的内容为: ' + request.GET['q'].encode('utf-8')
	else:
		message = '你提交了空表单'
	return HttpResponse(message)