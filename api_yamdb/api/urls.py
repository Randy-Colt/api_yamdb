from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (TitleViewSet, GenreViewSet,
                    UserViewSet, CategoryViewSet,
                    ReviewViewSet, CommentViewSet)

router_v1 = DefaultRouter()

router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('users', UserViewSet, basename='users')
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('reviews', ReviewViewSet, basename='reviews')
router_v1.register('comments', CommentViewSet, basename='comments')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
