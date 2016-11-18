# encoding: utf-8,这个玩意要加到第一行

from django.core import serializers
from django.http import *

from Feeds.models import GuMember


# 接收请求数据

def api_request(request):
    print request.GET.get('asd1')
    request.encoding = 'utf-8'
    request.is_secure()
    data = serializers.serialize("json", GuMember.objects.all())
    return HttpResponse(data, content_type="application/json")
    # response_data = {}
    # response_data['result'] = 'failed'
    # response_data['message'] = 'You messed up'
    # response_data['data'] = {'code': '123', 'action': 'toast'}
    # return HttpResponse(json.dumps(response_data), content_type="application/json")
