from rest_framework import permissions, serializers, routers
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from ..my_models import mybook

import logging
logger = logging.getLogger(__name__)

class BookListViewSet(viewsets.ModelViewSet):
    permission_classes  = (permissions.IsAuthenticated,)
    queryset = mybook.Book.objects.all().order_by('-id')
    serializer_class = mybook.BookListSerializer
    
class BookContentViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)    
    queryset = mybook.Book.objects.all().order_by('-id')
    serializer_class = mybook.BookDetailSerializer
    
class BookChapterViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    
    queryset = mybook.BookContent.objects.all().order_by('-id')
    serializer_class = mybook.BookContentSerializer
    
class ChapterCommentViewSet(viewsets.ModelViewSet) :
    permission_classes = (permissions.IsAuthenticated,)   
    queryset = mybook.ContentComment.objects.all().order_by('-id')
    serializer_class = mybook.BookCommentSerializer    
    