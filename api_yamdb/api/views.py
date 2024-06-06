from django.db.models import Avg
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets

from reviews.models import (Title, Genre,
                            User, Category,
                            Review, Comment)   # УБРАТЬ 4 ПОСЛЕДНИЙ
from .serializers import (GenreSerializer, TitleSerializer,
                          UserSerializer, CategorySerializer,
                          ReviewSerializer, CommentSerializer)   # УБРАТЬ 4 ПОСЛЕДНИЕ


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class UserViewSet(viewsets.ModelViewSet):   # НЕ МОЯ ЗАДАЧА
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):    # НЕ МОЯ ЗАДАЧА
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ReviewViewSet(viewsets.ModelViewSet):   # НЕ МОЯ ЗАДАЧА
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CommentViewSet(viewsets.ModelViewSet):     # НЕ МОЯ ЗАДАЧА
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer