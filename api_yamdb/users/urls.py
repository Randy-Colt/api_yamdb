from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.constants import API_VERSION

urlpatterns = [
    path(f'{API_VERSION}/token/',
         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'{API_VERSION}/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
]
