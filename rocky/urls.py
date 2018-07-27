from django.urls import path

from .my_views import channelViews
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"channel",channelViews.ChannelViewSet, base_name='channel')
router.register(r"device",channelViews.ChannelDeviceViewSet, base_name='device')
urlpatterns = router.urls

print(urlpatterns)
