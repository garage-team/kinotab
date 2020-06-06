from django.contrib.auth import password_validation
from django.core import exceptions
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class UserInfoSerializer(serializers.Serializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    email = serializers.CharField(read_only=True)


class TokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        user_serializer = UserInfoSerializer(self.user)
        data['member'] = user_serializer.data
        return data


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    tokens = serializers.SerializerMethodField()

    class Meta(object):
        model = User
        fields = ('email', 'username', 'password',
                  'confirm_password', 'tokens', )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    @staticmethod
    def get_tokens(obj):

        refresh = RefreshToken.for_user(obj)

        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return data

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        errors = dict()
        if password != confirm_password:
            errors['confirm_password'] = ['Passwords do not match']
        try:
            password_validation.validate_password(password=password, user=User)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)
        data.pop('confirm_password')
        return super().validate(data)

    def to_internal_value(self, data):
        for key in list(data.keys()):
            if data[key] is None:
                data.pop(key)
        return super().to_internal_value(data)
