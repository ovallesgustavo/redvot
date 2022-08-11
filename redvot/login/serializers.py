from django.contrib.auth import authenticate, get_user_model
from django.http import Http404
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from redvot.login.maps import map_user

User = get_user_model()


class LoginSerializers(serializers.Serializer):

    email = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):

        user = User.objects.filter(email=data["email"])

        if not user:
            raise AuthenticationFailed('El Email o la clave no son válidos')

        user_login = user[0].username
        current_user = authenticate(
            username=user_login,
            password=data['password']
        )

        if not current_user:
            raise AuthenticationFailed('El Email de usuario o la clave no son válidos')

        return {"user": current_user, "data": data}

    def create(self, data):
        user = data["user"]
        refresh = RefreshToken.for_user(user)
        tokens = {
            'access': str(refresh.access_token),
            "refresh": str(refresh),
            }
        return tokens

    def get_all(self):

        if not self.context['request'].user.is_authenticated:
            raise serializers.ValidationError({"Usuario": "El usuario no esta logeado"})

        users = User.objects.filter(is_active=True)
        __data = []
        for i in users:
            __data.append(map_user(i))
        return __data

    def get_one(self, pk):

        if not self.context['request'].user.is_authenticated:
            raise serializers.ValidationError({"Usuario": "El usuario no esta logeado"})

        if not pk.isnumeric():
            raise Http404

        user = User.objects.filter(id=pk, is_active=True).first()
        if user:
            return map_user(user)

        return {}


class LogoutSerializers(serializers.Serializer):

    refresh = serializers.CharField()

    def validate(self, data):
        self.token = data['refresh']
        return data

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            raise serializers.ValidationError({"Token": "Error en el token"})

        return {"Message": "Successful Logout"}
