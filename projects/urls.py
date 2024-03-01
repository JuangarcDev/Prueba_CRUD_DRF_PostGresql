from rest_framework import routers
from .api import projectViewSet

router = routers.DefaultRouter()

router.register('api/movies', projectViewSet, 'projects')

urlpatterns = router.urls