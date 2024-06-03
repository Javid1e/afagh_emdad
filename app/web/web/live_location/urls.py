# live_location/urls.py
from rest_framework.routers import DefaultRouter
from .views import LiveLocationViewSet

router = DefaultRouter()
router.register(r'live-location', LiveLocationViewSet)

urlpatterns = router.urls
