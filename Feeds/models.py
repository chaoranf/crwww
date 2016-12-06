# encoding: utf-8,这个玩意要加到第一行
# Create your models here.
from django.db import models


class GuMember(models.Model):
    guuid = models.CharField(max_length=64, default='')
    guname = models.CharField(max_length=20)
    gupass = models.CharField(max_length=20)
    device = models.CharField(max_length=64, default='')

    # 这个函数相当于java的toString
    def __str__(self):
        return 'guname=' + self.guname + ' gupass' + self.gupass

    def __unicode__(self):
        return self.guuid


class DeviceInfo(models.Model):
    jmudid = models.CharField(max_length=64, )
    jmdevice = models.CharField(max_length=64, default='')

    def __unicode__(self):
        return self.jmudid


# 登陆成功之后记录device数据
class UserInfo(models.Model):
    jmuid = models.CharField(max_length=64, default='', )
    jmdevice = models.CharField(max_length=64, default='')

    def __unicode__(self):
        return self.jmuid
