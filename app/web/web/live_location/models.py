# live_location/models.py
from django.contrib.gis.db import models as geomodels
from django.db import models
from users.models import User
from reqs.models import Request
from .validations import validate_latitude, validate_longitude, validate_location


class LiveLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='live_locations')
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='live_locations')
    location = geomodels.PointField(validators=[validate_location])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Live Location of {self.user.username}"
