# encoding: utf-8,这个玩意要加到第一行
from django.contrib import admin
from models import GuMember

# Register your models here.
# 这里注册需要管理的数据模型，已经做好了映射关系
admin.site.register(GuMember)
