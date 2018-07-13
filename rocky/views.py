from django.shortcuts import render

# Create your views here.
from my_views import channelViews

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"myusers",channelViews.ChannelViewSet, base_name='user')
urlpatterns = router.urls