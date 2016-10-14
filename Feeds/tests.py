# encoding: utf-8,这个玩意要加到第一行
from django.test import TestCase

from django.http import HttpResponse
from models import GuMember


def testdb(request):
    test1 = GuMember(guname='w3cschool.cc', gupass='asdf')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")
