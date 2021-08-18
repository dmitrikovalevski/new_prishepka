from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import UserInfo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'name',
            'permissions'
        ]


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = [
            'image',
            'phone',
            'user'
        ]
