from rest_framework.routers import DefaultRouter

from collection.views import TagViewSet, ContentItemViewSet, UserEntryViewSet, \
    MetaFieldViewSet, MetaDataViewSet, ContentTypeViewSet

router = DefaultRouter()
router.register('tag', TagViewSet)
router.register('item', ContentItemViewSet)
router.register('user-entry', UserEntryViewSet)
router.register('meta-field', MetaFieldViewSet)
router.register('meta-data', MetaDataViewSet)
router.register('item-type', ContentTypeViewSet)

urlpatterns = router.urls
