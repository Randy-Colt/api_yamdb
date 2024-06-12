from django.contrib.auth import get_user_model
from rest_framework import (
    filters,
    generics,
    permissions,
    status,
    views,
    viewsets
)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import SignUpSerializer, UserSerializer, UserMeSerializer
from api.permissions import IsAdmin
from .utils import send_confirmation_email, generate_confirmation_code

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """Вьюсет для получения администратором доступа к данным пользователей."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    http_method_names = ['get', 'post', 'delete', 'patch']
    permission_classes = (IsAdmin,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('username',)


class UserMeView(generics.RetrieveUpdateAPIView):
    """
    Представление для просмотра и обновления информации о текущем пользователе.

    Разрешенные методы: GET, PATCH.
    """

    serializer_class = UserMeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ['get', 'patch']

    def get_object(self):
        return self.request.user


class SignUpView(views.APIView):
    """
    Представление для регистрации нового пользователя.

    Разрешенный метод: POST.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        username = request.data.get('username')
        email = request.data.get('email')
        confirmation_code = request.data.get('confirmation_code')

        try:
            user = User.objects.get(username=username, email=email)
            if user.confirmation_code == confirmation_code:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            else:
                # Обновляем код подтверждения для существующего пользователя
                user.confirmation_code = generate_confirmation_code()
                user.save()
                send_confirmation_email(user.email, user.confirmation_code)
                return Response({
                                'message': (
                                    'Новый код подтверждения '
                                    'отправлен на вашу почту.')
                                }, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            serializer = SignUpSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                send_confirmation_email(user.email, user.confirmation_code)
                return Response({
                    'username': user.username,
                    'email': user.email
                }, status=status.HTTP_200_OK)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])

def obtain_token(request):
    username = request.data.get('username')
    confirmation_code = request.data.get('confirmation_code')

    try:
        user = User.objects.get(
            username=username, confirmation_code=confirmation_code)
    except User.DoesNotExist:
        return Response({'error': (
            'Неверное имя пользователя или код подтверждения')},
            status=status.HTTP_404_NOT_FOUND)

    refresh = RefreshToken.for_user(user)

    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }, status=status.HTTP_200_OK)
