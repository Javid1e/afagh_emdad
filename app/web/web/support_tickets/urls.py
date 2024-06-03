# support_tickets/urls.py
from rest_framework.routers import DefaultRouter
from .views import SupportTicketViewSet

router = DefaultRouter()
router.register(r'support-tickets', SupportTicketViewSet)

urlpatterns = router.urls
