# encoding: utf-8,这个玩意要加到第一行
from django.db import models

# Create your models here.
from django.db import models


class GuMember(models.Model):
    guname = models.CharField(max_length=20)
    gupass = models.CharField(max_length=20)

#这个函数相当于java的toString
    def __str__(self):
        return 'guname=' + self.guname + ' gupass' + self.gupass
