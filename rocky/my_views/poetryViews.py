from rest_framework import permissions, serializers, routers
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from ..my_models import poetry

import logging
logger = logging.getLogger(__name__)

class PoetryViewSet(viewsets.ModelViewSet):
    permission_classes  = (permissions.IsAuthenticated,)
    queryset = poetry.Poetry.objects.all().order_by('-id')
    serializer_class = poetry.PoetrySerializers
    
class PoetryCommnetViewSet(viewsets.ModelViewSet):
    permission_classes  = (permissions.IsAuthenticated,)
    queryset = poetry.PoetryComment.objects.all().order_by('-id')
    serializer_class = poetry.PoetryCommentSerializers
    
    @action(methods=['GET'],detail=False)
    def poetry_comments(self, request):
        id = request.query_params["poetry_id"]
        self.queryset = poetry.PoetryComment.objects.all().filter(poetry_id=id).order_by('-id')
        #serializer = self.get_serializer(self.queryset, many=True)
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            logger.info(page)
            serializer = self.get_serializer(page, many=True)
            logger.debug("章节序列化结果"+str(serializer.data) )
            return self.get_paginated_response(serializer.data)
        else :
            serializer = self.get_serializer(queryset, many=True)
            logger.debug("章节序列化结果"+str(serializer.data) )
            return Response(serializer.data)   