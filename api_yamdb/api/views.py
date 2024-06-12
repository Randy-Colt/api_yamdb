from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import filters

from reviews.models import (
    Category,
    Genre,
    Review,
    Title
)
from .filters import TitleFilter
from .mixins import ListCreateDeleteMixin
from .permissions import IsAdminOrReadOnly, IsAuthorModeratorAdminOrReadOnly
from .serializers import (
    CategorySerializer,
    CommentSerializer,
    GenreSerializer,
    ReviewSerializer,
    TitleSerializer,
    TitlePostSerializer
)


class CategoryViewSet(ListCreateDeleteMixin):
    """Вьюсет для получения списка категорий, их создания и удаления."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('name',)


class TitleViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с произведениями."""

    queryset = Title.objects.all().annotate(
        rating=Avg('reviews__score')
    )
    serializer_class = TitleSerializer
    http_method_names = ['get', 'post', 'delete', 'patch']
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filterset_class = TitleFilter
    search_fields = ('name',)

    def get_serializer_class(self):
        if self.action in ['create', 'partial_update']:
            return TitlePostSerializer
        return TitleSerializer


class GenreViewSet(ListCreateDeleteMixin):
    """Вьюсет для получения списка жанров, их создания и удаления."""

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ('name',)


class ReviewViewSet(viewsets.ModelViewSet):
    """Вьюсет для получения списка отзывов, либо одельного отзыва."""

    serializer_class = ReviewSerializer
    http_method_names = ['get', 'post', 'delete', 'patch']
    permission_classes = (IsAuthorModeratorAdminOrReadOnly,)

    def get_title(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        return title

    def get_queryset(self):
        title = self.get_title()
        queryset = title.reviews.all()
        return queryset

    def perform_create(self, serializer):
        title = self.get_title()
        serializer.save(
            author=self.request.user,
            title=title
        )


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для получения списка комментариев, либо одельного комментария."""

    serializer_class = CommentSerializer
    http_method_names = ['get', 'post', 'delete', 'patch']
    permission_classes = (IsAuthorModeratorAdminOrReadOnly,)

    def get_review(self):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        return review

    def get_queryset(self):
        review = self.get_review()
        queryset = review.comments.all()
        return queryset

    def perform_create(self, serializer):
        review = self.get_review()
        serializer.save(
            author=self.request.user,
            review=review
        )
