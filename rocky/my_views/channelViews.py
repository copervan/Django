from rest_framework import permissions, serializers, viewsets, routers
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action

from ..my_models import channel, channelserialize


class ChannelViewSet(viewsets.ModelViewSet):
    permission_classes  = (permissions.IsAuthenticated,)
    queryset = channel.Channel.objects.all()
    serializer_class = channelserialize.ChannelSerializer
    
    @action(methods=['POST'],detail=True)
    def listchannel(self, request):
        queryset = channel.Channel.objects.all()
        
        #page = self.paginate_queryset(queryset)
        serializer  = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class ChannelDeviceViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = channel.ChannelDevice.objects.all()
    serializer_class = channelserialize.ChannelDeviceSerializer