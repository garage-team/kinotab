from rest_framework.routers import DefaultRouter

from collection.views import TagViewSet, ItemViewSet, UserEntryViewSet

router = DefaultRouter()
router.register('tag', TagViewSet)
router.register('item', ItemViewSet)
router.register('user-entry', UserEntryViewSet)

urlpatterns = router.urls