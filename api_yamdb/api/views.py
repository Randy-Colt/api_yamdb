from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets

from .serializers import (
    CommentSerializer,
    GenreSerializer,
    ReviewSerializer,
    TitleSerializer
)
from reviews.models import (
    Genre,
    Review,
    Title
)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all().annotate(
        rating=Avg('reviews__score')
    )
    serializer_class = TitleSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """Вьюсет для получения списка отзывов, либо одельного отзыва."""

    serializer_class = ReviewSerializer
    http_method_names = ['get', 'post', 'delete', 'patch']

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
            # Закомментила пока нет авторизации!
            # author=self.request.user,
            title_id=title
        )


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для получения списка комментариев, либо одельного комментария."""

    serializer_class = CommentSerializer
    http_method_names = ['get', 'post', 'delete', 'patch']

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
            # Закомментила пока нет авторизации!
            # author=self.request.user,
            review_id=review
        )
