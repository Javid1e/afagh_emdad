# media/urls.py
from rest_framework.routers import DefaultRouter
from .views import MediaViewSet

router = DefaultRouter()
router.register(r'media', MediaViewSet)

urlpatterns = router.urls
