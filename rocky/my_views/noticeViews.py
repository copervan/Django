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
    queryset = notice.Notice.objects.all().order_by('-datetime')
    serializer_class = notice.NoticeSerializers
    
    @action(detail=False)
    def today_notice(self, request):
        today = now().date() + timedelta(days=0)
        tomorrow = now().date() + timedelta(days=1)
        logger.info(today,tomorrow)
        my_notice = notice.Notice.objects.all().filter(datetime__lt=today).exclude(status=1) 

        serializer = self.get_serializer(my_notice, many=True)
        return Response(serializer.data)    
