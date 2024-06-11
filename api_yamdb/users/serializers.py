from django.contrib.auth import get_user_model
from rest_framework import serializers
from .utils import generate_confirmation_code

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')


class UserMeSerializer(UserSerializer):

    role = serializers.CharField(read_only=True)


class SignUpSerializer(serializers.ModelSerializer):
    confirmation_code = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'confirmation_code')

    def validate_username(self, value):
        if value.lower() == 'me':
            raise serializers.ValidationError("Имя пользователя 'me' недопустимо.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        confirmation_code = generate_confirmation_code()
        user.confirmation_code = confirmation_code
        user.save()
        return user