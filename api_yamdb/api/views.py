from django.db.models import Avg
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets

from reviews.models import Title, Genre
                           
from .serializers import GenreSerializer, TitleSerializer
                          


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


