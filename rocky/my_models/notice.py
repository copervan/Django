from django.db import models
from django.utils import timezone 

class Notice(models.Model):
    notice_item = models.CharField("备忘内容",max_length=255)
    datetime = models.DateTimeField("开始时间")
    schedule = models.DecimalField("计划时长")
    status = models.SmallIntegerField("notice状态：0_未完成，1_已完成" ,max_length=255)
    created_at = models.DateTimeField("创建时间", default = timezone.now )
    updated_at = models.DateTimeField("更新时间", default = timezone.now )