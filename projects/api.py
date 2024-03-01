from projects.models import Project
from rest_framework import viewsets, permissions
from .serializers import Projectserializer

class projectViewSet (viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes =  [permissions.AllowAny]
    serializer_class = Projectserializer

