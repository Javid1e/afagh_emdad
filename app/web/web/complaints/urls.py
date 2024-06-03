# complaints/urls.py
from rest_framework.routers import DefaultRouter
from .views import ComplaintViewSet

router = DefaultRouter()
router.register(r'complaints', ComplaintViewSet)

urlpatterns = router.urls
