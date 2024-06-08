from rest_framework import serializers

from reviews.models import (
    Category,
    Comment,
    Genre,
    Review,
    Title,
)


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Category."""

    class Meta:
        model = Category
        fields = ('name', 'slug')


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
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'rating', 'description',
                  'genre', 'category')


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Genre."""

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Отзывов."""
    # Закомментила пока нет авторизации!
    # author = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='username'
    # )

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Комментариев."""
    # Закомментила пока нет авторизации!
    # author = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='username'
    # )

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Comment
