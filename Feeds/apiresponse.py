# encoding: utf-8,这个玩意要加到第一行
import json

from django.http import *
from django.views.decorators.csrf import csrf_exempt

from Feeds.models import DeviceInfo, UserInfo


# 登陆时，存储指纹数据
@csrf_exempt
def login_request(request):
    data = request.COOKIES
    guresponse = GuResponse(0, 'toast', 'no cookie', '')
    if data != None and len(data) > 0:
        try:
            uid = data['uid']
            finger_value = data['finger']
            userInfo = UserInfo(jmuid=uid, jmdevice=finger_value)
            userInfo.save()
            guresponse.message = 'userInfo save success'
        except:
            print ' happen exception'
            uid = ''
            finger_value = ''
            guresponse.message = 'userInfo save exception'

    real_data = getJsonStr(guresponse)
    response = HttpResponse(real_data, content_type="application/json")
    return response


# 普通接口请求时，验证指纹
@csrf_exempt
def gu_request(request):
    data = request.COOKIES
    print 'request begin ======================'
    guresponse = GuResponse(0, 'toast', 'no cookie', '')
    gustring = GuString()
    if data != None and len(data) > 0:
        try:
            uid = data['uid']
            finger_value = data['finger']
            finger_dy_value = data['finger_dy']
            device_info_value = data['device_info']
        except:
            print ' happen exception'
            uid = ''
            finger_value = ''
            finger_dy_value = ''
            device_info_value = ''
        if uid == None or uid == '':
            # 未登录，存设备信息
            if finger_value != '':
                device = DeviceInfo(jmudid=finger_value, jmdevice=device_info_value)
                device.save()
                print ' save device success'
                guresponse.message = 'device save success'
        else:
            # 登陆状态，判断md5value
            storedValue = queryDataFromDatabase(uid)
            print storedValue
            if storedValue == finger_value:
                guresponse.code = 0
                guresponse.action = "alert"
                guresponse.message = gustring.validString
                print 'return legal'
            else:
                guresponse.code = 0
                guresponse.action = "alert"
                guresponse.message = gustring.invalidString
                print 'return ilegal'

    real_data = getJsonStr(guresponse)
    # 字典数据转换成json数据，indent=2表示换行，indent=1表示单行显示
    response = HttpResponse(real_data, content_type="application/json")
    return response


def getJsonStr(data):
    try:
        real_data = json.dumps(data.__dict__, indent=1)
    except TypeError:
        real_data = '{"code"="-1","action"="toast","message"="oh yeah","data"="{}"}'
    return real_data


def queryDataFromDatabase(uidvalue):
    try:
        queryMember = UserInfo.objects.get(jmuid=uidvalue)
    except:
        queryMember = None
    if queryMember == None:
        # 数据库没有用户uid，不可能，但是模拟的时候需要处理这种情况，return为none后create这条数据
        return ''
    else:
        return queryMember.jmdevice


def addData(data):
    print data.id + "save data 111=================="
    data.save()
    print data.id + "save data 222=================="
    # DeviceInfo.objects.create()
    return ''


class GuString:
    validString = '用户合法'
    invalidString = '用户非法'
    needVerify = '用户验证策略'


class GuRequest:
    uid = ''
    md5value = ''
    deviceinfo = ''


class GuResponse:
    code = 0
    action = 'alert'
    message = 'u are a invaild user'
    data = ''

    def __init__(self, var1, var2, var3, var4):
        self.code = var1
        self.action = var2
        self.message = var3
        self.data = var4
