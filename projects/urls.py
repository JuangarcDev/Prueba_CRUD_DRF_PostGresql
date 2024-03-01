from rest_framework import routers
from .api import projectViewSet

router = routers.DefaultRouter()

router.register('api/projectss', projectViewSet, 'projects')

urlpatterns = router.urls