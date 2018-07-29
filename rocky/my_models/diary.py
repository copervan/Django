from django.db import models
from django.utils import timezone 
import datetime

class Diary(models.Model):
    title = models.CharField("标题", max_length=255)
    content = models.TextField("正文")
    date = models.DateTimeField("日期", default = timezone.now)
    created_at = models.DateTimeField("创建时间", default = datetime.datetime.now() )
    updated_at = models.DateTimeField("更新时间", default = datetime.datetime.now() )    
    