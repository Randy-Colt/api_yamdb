from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, permissions, viewsets

from api.filters import TitleFilter
from api.permissions import IsAdminOrReadOnly, IsAuthorModeratorAdminOrReadOnly
from api.serializers import (
    CategorySerializer,
    CommentSerializer,
    GenreSerializer,
    TitlePostSerializer,
    TitleSerializer,
    ReviewSerializer
)
from reviews.models import (
    Category,
    Genre,
    Title,
    Review
)


class ListCreateDeleteViewSet(mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              mixins.DestroyModelMixin,
                              viewsets.GenericViewSet):
    lookup_field = 'slug'
    search_fields = ('name',)
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)


class CategoryViewSet(ListCreateDeleteViewSet):
    """Вьюсет для получения списка категорий, их создания и удаления."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TitleViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с произведениями."""

    queryset = Title.objects.all().annotate(
        rating=Avg('reviews__score')
    ).order_by('name')
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


class GenreViewSet(ListCreateDeleteViewSet):
    """Вьюсет для получения списка жанров, их создания и удаления."""

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """Вьюсет для получения списка отзывов, либо одельного отзыва."""

    serializer_class = ReviewSerializer
    http_method_names = ['get', 'post', 'delete', 'patch']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorModeratorAdminOrReadOnly,)

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
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorModeratorAdminOrReadOnly,)

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
