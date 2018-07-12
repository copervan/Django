from rest_framework import permissions, serializers, viewsets, routers
from rest_framework.response import Response

from ..my_models import channel


class ChennelViewSet(viewsets.ViewSet):
    parser_classes = (permissions.IsAuthenticated,)
    
    def list(self, request)