# otp/urls.py
from rest_framework.routers import DefaultRouter
from .views import OTPViewSet

router = DefaultRouter()
router.register(r'otp', OTPViewSet)

urlpatterns = router.urls
