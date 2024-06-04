# reviews/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import gettext as _
from .models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            response.data['message'] = _("Review created successfully")
            return response
        except Exception as e:
            return Response({'error': _("Error creating review"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            response.data['message'] = _("Review updated successfully")
            return response
        except Exception as e:
            return Response({'error': _("Error updating review"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(request, *args, **kwargs)
            return Response({'message': _("Review deleted successfully")}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': _("Error deleting review"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'], url_path='details')
    def review_details(self, request, pk=None):
        review = self.get_object()
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
