from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Project
from .serializers import Projectserializer

# Create your views here.
@api_view(['GET'])
def search_movies(request):
    query = request.query_params.get('query', '')

    # Filtra las películas que coincidan con el título, calificación o país
    movies = Project.objects.filter(
        titulo__icontains=query
    ).filter(
        calificacion__icontains=query
    ).filter(
        pais__icontains=query
    )

    # Serializa los resultados
    serializer = Projectserializer(movies, many=True)

    return Response(serializer.data)