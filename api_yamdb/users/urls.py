from django.urls import include, path
from rest_framework.routers import DefaultRouter

from reviews.constants import API_VERSION
from users.views import obtain_token, SignUpView, UserViewSet

router_u_v1 = DefaultRouter()

router_u_v1.register('users', UserViewSet, basename='users')

urlpatterns = [
    path(f'{API_VERSION}/auth/token/', obtain_token, name='obtain_token'),
    path(f'{API_VERSION}/auth/signup/', SignUpView.as_view(), name='signup'),
    path(f'{API_VERSION}/', include(router_u_v1.urls)),
]
