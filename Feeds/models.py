# encoding: utf-8,这个玩意要加到第一行
# Create your models here.
from django.db import models


class GuMember(models.Model):
    guuid = models.CharField(max_length=20, primary_key=True)
    guname = models.CharField(max_length=20)
    gupass = models.CharField(max_length=20)

    def __init__(self, uid_, name_, pass_):
        self.guuid = uid_
        self.guname = name_
        self.gupass = pass_

    # 这个函数相当于java的toString
    def __str__(self):
        return 'guname=' + self.guname + ' gupass' + self.gupass


class GuCookie(models.Model):
    name = models.CharField(max_length=20)
    value = models.CharField(max_length=128)
    domain = models.CharField(max_length=50)

    def __str__(self):
        return self.name + '=' + self.value


class DeviceInfo(models.Model):
    udid = models.CharField(max_length=64, primary_key=True)
    device = models.CharField(max_length=64, primary_key=True)
