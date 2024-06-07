# payments/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet

router = DefaultRouter()
router.register(r'payments', PaymentViewSet)

urlpatterns = router.urls + [
    path('payments/verify/', PaymentViewSet.as_view({'get': 'verify_payment'}), name='verify_payment'),
]
