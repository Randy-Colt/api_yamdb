from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from api.constants import API_VERSION

urlpatterns = [
    path(f'{API_VERSION}/auth/token/',
         TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
