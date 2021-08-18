from rest_framework import serializers
from .models import Service, Comment


class ServiceSerializer(serializers.Serializer):  # HyperlinkedModelSerializer):
    picture = serializers.ImageField()
    title = serializers.CharField(max_length=200)
    descriptions = serializers.CharField()
    price = serializers.CharField()
    date_created = serializers.DateTimeField()
    count = serializers.CharField()
    user_id = serializers.IntegerField()

    def create(self, validated_data):
        return Service.objects.create(**validated_data)


#    class Meta:
#        model = Service
#        fields = [
#            'picture',
#            'title',
#            'descriptions',
#            'price',
#            'date_created',
#            'user',
#            'count'
#        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'body',
            'date_created',
            'user',
            'service'
        ]
