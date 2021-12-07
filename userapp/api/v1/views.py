from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from userapp.models import User
from .serializers import RegistrationSerializer


class RegistrationView(APIView):
    def post(self, request, *args, **kwargs):

        serializer = RegistrationSerializer(data=request.data)

        for user in User.objects.all():
            if not user:
                break
            else:
                try:
                    Token.objects.get(user_id=user.id)
                except Token.DoesNotExist:
                    Token.objects.create(user=user)

        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)

            return Response(
                {
                    "user": {
                        "id": serializer.data["id"],
                        "username": serializer.data["username"],
                        "email": serializer.data["email"],
                        "is_active": serializer.data["is_active"],
                        "is_staff": serializer.data["is_staff"],
                        "role": serializer.data["role"],
                    },
                    "status": {
                        "message": "User created",
                        "code": f"{status.HTTP_200_OK} OK",
                    },
                    "token": token.key,
                }
            )
        return Response(
             {
                "error": serializer.errors,
                "status": f"{status.HTTP_203_NON_AUTHORITATIVE_INFORMATION}\
                    NON AUTHORITATIVE INFORMATION",
                }
        )


class LoginAPIView(APIView):

    def post(self, request):
        user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
        if user is None:
            return Response({
                "ok": False,
                "data": "Login yoki parol hato"
            })
        token, is_create = Token.objects.get_or_create(user=user)

        return Response({
            "succes": True,
            "status": status.HTTP_200_OK,
            "message": "ok",
            "token": token.key,
            "user": {
                "id": user.id,
                "username": token.user.username,
                'role': user.role,
                'email': user.email,
                'is_staff': user.is_staff,
                "is_active": user.is_active,
            },
        })

    def delete(self, request):
        if request.user.is_authenticated:
            request.auth.delete()

            return Response({
                    "ok": True
                })

