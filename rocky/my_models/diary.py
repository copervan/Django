from django.db import models
from django.utils import timezone 
import datetime
from django.contrib.auth.models import User

class Diary(models.Model):
    title = models.CharField("标题", max_length=255)
    content = models.TextField("正文")
    date = models.DateTimeField("日期", default = timezone.now)
    owner = models.ForeignKey('auth.User',default = 1,related_name='diary_author',on_delete = models.CASCADE )
    created_at = models.DateTimeField("创建时间", default = timezone.now )
    updated_at = models.DateTimeField("更新时间", default = timezone.now )
    