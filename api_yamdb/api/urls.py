from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TitleViewSet, GenreViewSet

from .constants import API_VERSION
from .views import ReviewViewSet, CommentViewSet

router_v1 = DefaultRouter()

router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register('genres', GenreViewSet, basename='genres')


router_v1 = routers.DefaultRouter()
router_v1.register(r'titles/(?P<title_id>\d+)/reviews',
                   ReviewViewSet, basename='reviews')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path(f'{API_VERSION}/', include(router_v1.urls)),
]
