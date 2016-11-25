# encoding: utf-8,这个玩意要加到第一行
import json

from django.core import serializers
from django.http import *
from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def gu_request(request):
    data = request.COOKIES
    uid = data['uid']
    md5Value = data['md5value']
    # for (k, v) in data.items():
    #     print '%s:%s' % (k, v)
    # DeviceInfo.objects.create(udid=md5Value)
    # GuMember.objects.create(guuid=uid, guname='add')
    real_data = json.dumps(data, indent=1)
    # 字典数据转换成json数据，indent=2表示换行，indent=1表示单行显示
    response = HttpResponse(real_data, content_type="application/json")
    return response
