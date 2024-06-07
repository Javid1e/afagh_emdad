# achievements/urls.py
from rest_framework.routers import DefaultRouter
from .views import AchievementViewSet

router = DefaultRouter()
router.register(r'achievements', AchievementViewSet)

urlpatterns = router.urls
