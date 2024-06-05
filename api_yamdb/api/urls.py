from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TitlesViewSet

router_v1 = DefaultRouter()

router_v1.register('titles', TitlesViewSet, basename='titles')
router_v1.register('genres', GenreViewSet, basename='genres')



urlpatterns = [
    
]
