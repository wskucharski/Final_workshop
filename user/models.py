from django.db import models
from django.contrib.auth.models import User
from topo.models import Route, Crag, Sector, Region, Area


# Create your models here.

RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
)

class RouteRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)








