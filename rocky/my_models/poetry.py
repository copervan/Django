from django.db import models
from rest_framework import serializers 
from django.utils import timezone 
from django.contrib.auth.models import User

class Poetry(models.Model):
    title = models.CharField("备忘内容",max_length=255)
    author = models.CharField("备忘内容",max_length=255)
    content = models.TextField("章节内容",max_length=50000)
    created_at = models.DateTimeField("创建时间", default = timezone.now )
    updated_at = models.DateTimeField("更新时间", default = timezone.now )
    
class PoetryComment(models.Model):
    poetry_id = models.ForeignKey('Poetry',related_name='Poetry_comments',on_delete = models.CASCADE)
    #user_id = models.ForeignKey('User',related_name='comment_user',on_delete = models.CASCADE )
    comments = models.CharField("注释内容",max_length=255)
    created_at = models.DateTimeField("创建时间", default = timezone.now )
    updated_at = models.DateTimeField("更新时间", default = timezone.now )
    owner = models.ForeignKey('auth.User',default = 1,related_name='poetry_commener',on_delete = models.CASCADE )

class PoetrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Poetry
        fields = ('id', 'title', 'author','content', 'created_at' ,'updated_at')
        
class PoetryCommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = PoetryComment
        fields = ('id', 'poetry_id', 'comments', 'created_at' ,'updated_at')