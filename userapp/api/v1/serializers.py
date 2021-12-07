from rest_framework import serializers

from userapp.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "is_active",
            "is_staff",
            'role'
        ]
        extra_kwargs = {"id": {"read_only": True}, "password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        role = validated_data['role']

        user = User.objects.create(
            username=username,
            email=email,
            role=role,
        )
        user.set_password(validated_data['password'])
        user.save()
        return user