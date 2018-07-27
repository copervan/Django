from rest_framework import serializers 
from .diary import Diary

class DiarySerializers(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ('id', 'title', 'content', 'date', 'created_at' ,'updated_at' )