# payments/urls.py
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet, verify_payment
from django.urls import path

router = DefaultRouter()
router.register(r'payments', PaymentViewSet)

urlpatterns = router.urls + [
    path('payments/verify/', verify_payment, name='verify_payment'),
]
