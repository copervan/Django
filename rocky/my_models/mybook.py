from django.db import models
from rest_framework import serializers 
from django.utils import timezone 
from django.contrib.auth.models import User
import json

class Book(models.Model):
    name = models.CharField("书籍名称",max_length=255)
    author = models.CharField("作者",max_length=255)
    introduction =  models.TextField("内容简介",max_length=1500,default = "")
    book_style = models.CharField("书籍标签",max_length=255)
    created_at = models.DateTimeField("创建时间", default = timezone.now )
    updated_at = models.DateTimeField("更新时间", default = timezone.now )
    
class BookContent(models.Model):
    book_id = models.ForeignKey('Book',related_name='book_content' , on_delete = models.CASCADE)
    chapter = models.CharField("章节名称",max_length=255)
    content = models.TextField("章节内容",max_length=50000)
    created_at = models.DateTimeField("创建时间", default = timezone.now )
    updated_at = models.DateTimeField("更新时间", default = timezone.now )
    
    def __unicode__(self):
        #print(json.dumps({"id":self.id,'chapter': self.chapter}) )
        return json.dumps({"id":self.id,'chapter': self.chapter})   
    
class ContentComment(models.Model):
    chapter_id = models.ForeignKey('BookContent',related_name='chapter_comments',on_delete = models.CASCADE)
    #user_id = models.ForeignKey('User',related_name='comment_user',on_delete = models.CASCADE )
    comments = models.CharField("注释内容",max_length=255)
    created_at = models.DateTimeField("创建时间", default = timezone.now )
    updated_at = models.DateTimeField("更新时间", default     = timezone.now )
    
    def __unicode__(self):
        return json.dumps({'id':self.id,"comments":comments,
                "created_at":created_at,'updated_at':updated_at} )    

# #######################################################################################
#CommentDetails 章节注释     
class BookCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentComment
        fields = ('id', 'chapter_id', 'comments', 'created_at' ,'updated_at')
#chapterComment 章节内容和相关注释
class ChaptorCommentSerializer(serializers.ModelSerializer):
    chapter_comments = BookCommentSerializer(many=True)
    class Meta:
        model = BookContent
        fields = ('id', 'chapter', 'content', 'chapter_comments' ,'created_at' ,'updated_at')

#ChapterDetails 章节 及章节内容
class BookContentSerializer(serializers.ModelSerializer):
    #chapter_comments = serializers.StringRelatedField(many=True)
    class Meta:
        model = BookContent
        fields = ('id', 'book_id','chapter', 'content' ,'created_at' ,'updated_at')

#ChapterList 章节列表 配合BookListSerializer 使用
class ChapterListSerializer(serializers.ModelSerializer):
    #chapter_comments = serializers.StringRelatedField(many=True)
    class Meta:
        model = BookContent
        fields = ('id','chapter')
        
# BookList 获取书籍名称及所有章节
class BookListSerializer(serializers.ModelSerializer):
    #book_content = serializers.StringRelatedField(many=True)
    class Meta:
        model = Book
        fields = ('id', 'name', 'author','introduction', 'book_style')
 
#BookContentList  获取全部书籍
class BookDetailSerializer(serializers.ModelSerializer):
    book_content = ChapterListSerializer(many=True)
    class Meta:
        model = Book
        fields = ('id', 'name', 'author','introduction','book_style', 'book_content','created_at' ,'updated_at')

