from django.db import models


# Create your models here.

class Area(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)

class Region(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)

class Sector(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)
    number_of_crags = models.IntegerField(null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)

FACE_CHOICES = (
    ('N', 'N'),
    ('NW', 'NW'),
    ('NE', 'NE'),
    ('S', 'S'),
    ('SW', 'SW'),
    ('SE', 'SE'),
)

ROCK_CHOICES = (
    ('granit', 'granit'),
    ('wapień', 'wapień'),
    ('piaskowiec', 'piaskowiec'),
    ('zlepieniec', 'zlepieniec'),
)

class Crag(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255, null=True)
    number_of_routes = models.IntegerField(null=True)
    rock_type = models.CharField(choices=ROCK_CHOICES, max_length=50, null=True)
    face = models.CharField(choices=FACE_CHOICES, max_length=6, null=True)
    gps = models.CharField(max_length=255, null=True)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True)

GRADE_CHOICES = (
    ('I', 'I'),
    ('II', 'II'),
    ('II+', 'II+'),
    ('III', 'III'),
    ('III+', 'III+'),
    ('IV', 'IV'),
    ('IV+', 'IV+'),
    ('V-', 'V-'),
    ('V', 'V'),
    ('V+', 'V+'),
    ('V+/VI-', 'V+/VI-'),
    ('VI-', 'VI-'),
    ('VI', 'VI'),
    ('VI+', 'VI+'),
    ('VI.1', 'VI.1'),
    ('VI.1+', 'VI.1+'),
    ('VI.2', 'VI.2'),
    ('VI.2+', 'VI.2+'),
    ('VI.2+/VI.3', 'VI.2+/VI.3'),
    ('VI.3', 'VI.3'),
    ('VI.3+', 'VI.3+'),
    ('VI.4', 'VI.4'),
    ('VI.4+', 'VI.4+'),
    ('VI.5', 'VI.5'),
    ('VI.5+', 'VI.5+'),
    ('VI.5+/6', 'VI.5+/6'),
    ('VI.6', 'VI.6'),
    ('VI.6+', 'VI.6+'),
    ('VI.7', 'VI.7'),
    ('VI.7+', 'VI.7+'),
    ('VI.8', 'VI.8'),


)

TYPE_CHOICES = (
    ('filar', 'filar'),
    ('komin', 'komin'),
    ('pion', 'pion'),
    ('połóg', 'połóg'),
    ('przewieszenie', 'przewieszenie'),
    ('zacięcie', 'zacięcie'),
)

class Route(models.Model):
    name = models.CharField(max_length=128)
    grade = models.CharField(choices=GRADE_CHOICES, max_length=10, null=True)
    length = models.IntegerField(null=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=50, null=True)
    pitches = models.IntegerField(null=True)
    additional_info = models.CharField(max_length=255, null=True)
    author = models.CharField(max_length=128, null=True)
    crag = models.ForeignKey(Crag, on_delete=models.SET_NULL, null=True)



