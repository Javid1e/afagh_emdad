# payments/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import gettext as _
from .models import Payment
from .serializers import PaymentSerializer
from zarinpal import Zarinpal
from django.conf import settings


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            response.data['message'] = _("Payment created successfully")
            return response
        except Exception as e:
            return Response({'error': _("Error creating payment"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            response.data['message'] = _("Payment updated successfully")
            return response
        except Exception as e:
            return Response({'error': _("Error updating payment"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(request, *args, **kwargs)
            return Response({'message': _("Payment deleted successfully")}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': _("Error deleting payment"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], url_path='start')
    def start_payment(self, request, pk=None):
        payment = self.get_object()
        zarinpal = Zarinpal(settings.ZARINPAL_MERCHANT_ID)
        result = zarinpal.payment_request(
            amount=payment.amount,
            description=f'Payment for request ID: {payment.request.id}',
            email=payment.request.client.email,
            mobile=payment.request.client.phone_number,
            callback_url=settings.ZARINPAL_CALLBACK_URL
        )

        if result['Status'] == 100:
            payment.transaction_details = result['Authority']
            payment.save()
            return Response({'url': zarinpal.get_gateway_url(result['Authority'])}, status=status.HTTP_200_OK)
        else:
            return Response({'error': _("Payment request failed")}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], url_path='verify')
    def verify_payment(self, request):
        authority = request.GET.get('Authority')
        status = request.GET.get('Status')

        try:
            payment = Payment.objects.get(transaction_details=authority)
        except Payment.DoesNotExist:
            return Response({'error': _("Payment not found")}, status=status.HTTP_404_NOT_FOUND)

        if status == 'OK':
            zarinpal = Zarinpal(settings.ZARINPAL_MERCHANT_ID)
            result = zarinpal.payment_verification(
                amount=payment.amount,
                authority=authority
            )

            if result['Status'] == 100:
                payment.status = 'completed'
                payment.save()
                return Response({'message': _("Payment successful")}, status=status.HTTP_200_OK)
            else:
                return Response({'error': _("Payment verification failed")}, status=status.HTTP_400_BAD_REQUEST)
        else:
            payment.status = 'failed'
            payment.save()
            return Response({'error': _("Payment failed")}, status=status.HTTP_400_BAD_REQUEST)
