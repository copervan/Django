from django.db import models
from rest_framework import serializers 
from django.utils import timezone 
from django.contrib.auth.models import User

class Notice(models.Model):
    notice_item = models.CharField("备忘内容",max_length=255)
    datetime = models.DateTimeField("开始时间")
    end_time = models.DateTimeField("End_time",default = timezone.now )
    schedule = models.DecimalField("计划时长",max_digits = 5, decimal_places = 2)
    status = models.SmallIntegerField("notice状态：0_未完成，1_已完成" ,max_length=255)
    owner = models.ForeignKey('auth.User',default = 1,related_name='notic_author',on_delete = models.CASCADE )
    created_at = models.DateTimeField("创建时间", default = timezone.now )
    updated_at = models.DateTimeField("更新时间", default = timezone.now )
    

class NoticeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ('id', 'notice_item', 'datetime', 'end_time', 'schedule', 'status' ,'created_at' ,'updated_at')