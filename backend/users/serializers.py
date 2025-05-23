from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "is_mentor", "bio", "phone_number"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            is_mentor=validated_data.get("is_mentor", False),
            bio=validated_data.get("bio", ""),
            phone_number=validated_data.get("phone_number", ""),
        )
        return user
