"""PlacePass URL Configuration

"""
from rest_framework.routers import DefaultRouter

from .views import UserViewSet

router = DefaultRouter()
router.register('profile', UserViewSet)

urlpatterns = router.urls
