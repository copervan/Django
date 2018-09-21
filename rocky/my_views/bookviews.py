from rest_framework import permissions, serializers, routers
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from ..my_models import mybook

import logging
logger = logging.getLogger(__name__)

# Book列表管理
class BookListViewSet(viewsets.ModelViewSet):
    permission_classes  = (permissions.IsAuthenticated,)
    queryset = mybook.Book.objects.all().order_by('-id')
    serializer_class = mybook.BookListSerializer

#Book Book列表 及书籍章节列表   
class BookContentViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)    
    queryset = mybook.Book.objects.all().order_by('-id')
    serializer_class = mybook.BookDetailSerializer

# 章节详情管理    
class BookChapterViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,) 
    queryset = mybook.BookContent.objects.all().order_by('-id')
    serializer_class = mybook.BookContentSerializer
    
    @action(methods=['GET'],detail=True)
    def chapter_detail(self, request, pk=None):
        queryset = mybook.BookContent.objects.all().filter(id=pk)
        self.serializer_class = mybook.ChaptorCommentSerializer
        serializer = self.get_serializer(queryset, many=True)
        logger.debug("章节序列化结果"+str(serializer.data) )
        return Response(serializer.data)

# 评论管理    
class ChapterCommentViewSet(viewsets.ModelViewSet) :
    permission_classes = (permissions.IsAuthenticated,)   
    queryset = mybook.ContentComment.objects.all().order_by('-id')
    serializer_class = mybook.BookCommentSerializer    
    
    @action(methods=['GET'],detail=False)
    def chapter_comments(self, request):
        id = request.query_params["chapter_id"]
        self.queryset = mybook.ContentComment.objects.all().filter(chapter_id=id).order_by('-id')
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
  