from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import Point
from rest_framework import serializers

# Create your models here.
#PRIMERO PELICULAS GENERAL
class Project(models.Model):
    titulo = models.CharField(max_length = 300)
    calificacion = models.DecimalField (max_digits=5 ,decimal_places=2)
    pais = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.titulo
    
    from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'titulo', 'calificacion', 'pais']

#AHORA CON LOCALIZACION
class MovieLocation(models.Model):
    titulo = models.CharField(max_length=300)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2)
    pais = models.CharField(max_length=100)
    location = gis_models.PointField(geography=True, null=True, blank=True)

    def __str__(self):
        return self.titulo

class MovieLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLocation
        fields = ['titulo', 'calificacion', 'pais', 'location']