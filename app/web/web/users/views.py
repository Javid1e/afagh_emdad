from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from django.utils.translation import gettext as _


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data['message'] = _("User created successfully")
        return response
