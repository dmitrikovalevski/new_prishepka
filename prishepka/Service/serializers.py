from rest_framework import serializers
from .models import Service, Comment


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'pk',
            'picture',
            'title',
            'descriptions',
            'price',
            'date_created',
            'user',
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'pk',
            'body',
            'date_created',
            'user',
            'service'
        ]
