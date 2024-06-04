# notifications/urls.py
from rest_framework.routers import DefaultRouter
from .views import GCMDeviceViewSet, APNSDeviceViewSet, WebPushDeviceViewSet

router = DefaultRouter()
router.register(r'gcm-devices', GCMDeviceViewSet)
router.register(r'apns-devices', APNSDeviceViewSet)
router.register(r'web-push-devices', WebPushDeviceViewSet)

urlpatterns = router.urls
