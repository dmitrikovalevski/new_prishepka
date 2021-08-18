from rest_framework import serializers
from .models import Service, Comment


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'picture',
            'title',
            'descriptions',
            'price',
            'date_created',
            'user',
            'count'
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'body',
            'date_created',
            'user',
            'service'
        ]
