from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (
    filters,
    permissions,
    status,
    views,
    viewsets
)
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from api.permissions import IsAdmin
from users.serializers import (
    AccessTokenSerializer,
    SignUpSerializer,
    UserSerializer,
    # UserMeSerializer
)
from users.utils import send_confirmation_email

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """Вьюсет для получения администратором доступа к данным пользователей."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    http_method_names = ['get', 'post', 'delete', 'patch']
    permission_classes = (permissions.IsAuthenticated, IsAdmin,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('username',)

    @action(detail=False, methods=['get', 'patch'],
            permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        if request.method == 'GET':
            serializer = UserSerializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = UserSerializer(request.user, data=request.data,
                                    partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(role=request.user.role)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
            if default_token_generator.check_token(user, confirmation_code):
                access = AccessToken.for_user(user)
                return Response({
                    'access': str(access),
                }, status=status.HTTP_200_OK)
            # Обновляем код подтверждения для существующего пользователя
            confirmation_code = default_token_generator.make_token(user)
            user.save()
            send_confirmation_email(user.email, confirmation_code)
            return Response({
                            'message': (
                                'Новый код подтверждения '
                                'отправлен на вашу почту.')
                            }, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            serializer = SignUpSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            send_confirmation_email(user.email, confirmation_code)
            return Response({
                'username': user.username,
                'email': user.email
            }, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def obtain_token(request):
    serializer = AccessTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data['username']
    confirmation_code = serializer.validated_data['confirmation_code']

    user = get_object_or_404(User, username=username)

    if not default_token_generator.check_token(user, confirmation_code):
        return Response(
            {'error': 'Неверный код подтверждения'},
            status=status.HTTP_400_BAD_REQUEST
        )

    access = AccessToken.for_user(user)

    return Response({
        'access': str(access),
    }, status=status.HTTP_200_OK)
