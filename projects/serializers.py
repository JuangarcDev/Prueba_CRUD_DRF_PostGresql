from rest_framework import serializers
from .models import Project

class Projectserializer (serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'titulo',  'calificacion', 'pais')