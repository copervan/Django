from rest_framework import permissions, serializers, routers
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from ..my_models import channel, channelserialize

import logging
logger = logging.getLogger(__name__)

class ChannelViewSet(mixins.CreateModelMixin,
                           mixins.ListModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    permission_classes  = (permissions.IsAuthenticated,)
    queryset = channel.Channel.objects.all()
    serializer_class = channelserialize.ChannelSerializer
    
class ChannelDeviceViewSet(mixins.CreateModelMixin,
                           mixins.ListModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    
    queryset = channel.ChannelDevice.objects.all()
    serializer_class = channelserialize.ChannelDeviceSerializer

device_view = ChannelDeviceViewSet.as_view(
    {'get':'list','post':'create','delete':'destroy','put':'partial_update'})

logger.info(device_view)