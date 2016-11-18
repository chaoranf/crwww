# encoding: utf-8,这个玩意要加到第一行
from django.test import TestCase

from django.http import HttpResponse
from models import GuMember


def testdb(request):
    request.encoding = 'utf-8'
    test1 = GuMember()
    if 'insertname' in request.GET:
        test1.guname = request.GET['insertname'].encode('utf-8')
        test1.gupass = request.GET['insertpass'].encode('utf-8')
    test1.save()
    msg = "<p>数据添加成功！" + test1.guname + "</p>";
    return HttpResponse(msg)
