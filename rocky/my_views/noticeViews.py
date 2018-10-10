from rest_framework import permissions, serializers, routers
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
#import  django_filters  
from django.utils.timezone import now , timedelta

from ..my_models import notice

import logging
logger = logging.getLogger(__name__)


class NoticeViewSet(viewsets.ModelViewSet):
    permission_classes  = (permissions.IsAuthenticated,)
    #queryset = notice.Notice.objects.all().order_by('-datetime')
    serializer_class = notice.NoticeSerializers
    
    @action(methods=["GET"],detail=False)
    def today_notice(self, request):
        user = self.request.user
        today = now().date() + timedelta(days=0)
        tomorrow = now().date() + timedelta(days=1)
        logger.info(today,tomorrow)
        # 
        my_notice = notice.Notice.objects.all().filter(datetime__lt=tomorrow,owner=user).exclude(status__in=[1,3]) 

        serializer = self.get_serializer(my_notice, many=True)
        return Response(serializer.data)    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user) 
        
    def get_queryset(self) :
        user = self.request.user
        logger.info("Current User: " + str(user) )
        return notice.Notice.objects.all().filter(owner=user).order_by('-id') 