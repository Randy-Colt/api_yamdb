from django.urls import include, path
from rest_framework.routers import DefaultRouter
# Импорты как у Андрея!
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .constants import API_VERSION
from .views import (
    CommentViewSet,
    GenreViewSet,
    ReviewViewSet,
    TitleViewSet,
    UserViewSet  # Удали перед пушем!
)

router_v1 = DefaultRouter()

# Костыль для просмотра юзеров! Удали перед пушем!
router_v1.register('users', UserViewSet, basename='userss')

router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path(f'{API_VERSION}/', include(router_v1.urls)),

    # Костыли для просмотра юзеров! Удали перед пушем!
    path(f'{API_VERSION}/token/',
         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'{API_VERSION}/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
]
