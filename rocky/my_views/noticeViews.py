from rest_framework import permissions, serializers, routers
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from ..my_models import notice

import logging
logger = logging.getLogger(__name__)

class NoticeViewSet(viewsets.ModelViewSet):
    permission_classes  = (permissions.IsAuthenticated,)
    queryset = notice.Notice.objects.all().order_by('-id')
    serializer_class = notice.NoticeSerializers