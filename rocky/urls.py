from django.urls import path

from .my_views import channelViews, diaryViews ,noticeViews,bookviews
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"channel",channelViews.ChannelViewSet, base_name='channel')
router.register(r"device",channelViews.ChannelDeviceViewSet, base_name='device')
router.register(r"diary",diaryViews.DiaryViewSet, base_name="diary")
router.register(r"notice",noticeViews.NoticeViewSet, base_name="notice")
router.register(r"booklist",bookviews.BookListViewSet,base_name="booklist")
router.register(r"bookcontent",bookviews.BookContentViewSet,base_name="bookcontent")
router.register(r"bookchapter",bookviews.BookChapterViewSet,base_name="bookchapter")
router.register(r"chaptercomment",bookviews.ChapterCommentViewSet,base_name="chaptercomment")
urlpatterns = router.urls

print(urlpatterns)
