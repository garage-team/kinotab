from rest_framework.routers import DefaultRouter

from movie.views import MetaFieldViewSet, MetaDataViewSet, ItemTypeViewSet

router = DefaultRouter()
router.register('meta-field', MetaFieldViewSet)
router.register('meta-data', MetaDataViewSet)
router.register('item-type', ItemTypeViewSet)

urlpatterns = router.urls