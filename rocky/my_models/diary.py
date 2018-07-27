from django.db import models
from django.utils import timezone 

class Diary(models.Model):
    title = models.CharField("标题", max_length=255)
    content = models.TextField("正文")
    date = models.TimeField("日期", default = timezone.now)
    created_at = models.DateTimeField("创建时间", default = timezone.now )
    updated_at = models.DateTimeField("更新时间", default = timezone.now )    
    