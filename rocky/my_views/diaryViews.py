from rest_framework import permissions, serializers, routers
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from ..my_models import diary, diaryserialize

import logging
logger = logging.getLogger(__name__)

class DiaryViewSet(viewsets.ModelViewSet):
    permission_classes  = (permissions.IsAuthenticated,)
    #queryset = diary.Diary.objects.all().order_by('-id')
    serializer_class = diaryserialize.DiarySerializers
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)     
        
    def get_queryset(self) :
        user = self.request.user
        logger.info("Current User: " + str(user) )
        return diary.Diary.objects.all().filter(owner=user).order_by('-id')     