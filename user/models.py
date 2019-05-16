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

class CragRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crag = models.ForeignKey(Crag, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)

class SectorRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)

class RegionRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)

class AreaRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)







