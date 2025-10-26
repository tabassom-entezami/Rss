from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import CustomUser


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    class Meta:
        model = CustomUser
        fields = "username", "email", "password"
        extra_kwargs = {'password': {'write_only': True, 'min_length': 1}}


class RetrieveUpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email", "password", "first_name", "last_name", "phone_number", "bio"]


