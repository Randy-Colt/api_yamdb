from rest_framework import serializers
from reviews.models import (Title, Genre,
                            User, Category,
                            Review, Comment)   # УБРАТЬ ПОСЛЕДНИЕ 4 МОДЕЛИ


class TitleSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Title."""
    genre = serializers.SlugRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        slug_field='slug'
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )
    # rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'description',
                  'genre', 'category')
    

class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Genre."""

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class UserSerializer(serializers.ModelSerializer):    # НЕ МОЯ ЗАДАЧА
    """Сериализатор для модели User."""
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'role')


class CategorySerializer(serializers.ModelSerializer):   # НЕ МОЯ ЗАДАЧА
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class ReviewSerializer(serializers.ModelSerializer):     # НЕ МОЯ ЗАДАЧА
    """Сериализатор для модели Review."""
    class Meta:
        model = Review
        fields = ('id', 'title_id', 'text', 'author', 'score', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):     # НЕ МОЯ ЗАДАЧА
    """Сериализатор для модели Comment."""
    class Meta:
        model = Comment
        fields = ('id', 'review_id', 'text', 'author', 'pub_date')
