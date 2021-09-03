from django.views.generic import TemplateView
from django.http import HttpResponse
import json

from .models import Service, Comment

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
)

from .serializers import (
    CommentSerializer,
    ServiceSerializer
)


class SwaggerDocumentationTemplateView(TemplateView):
    template_name = 'documentation.html'
    extra_context = {
        'schema_url': 'openapi'
    }


class ServiceList(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if request.is_ajax() or request.data:
            picture = request.data.get('picture')
            title = request.data.get('title')
            descriptions = request.data.get('descriptions')
            price = request.data.get('price')

            service = Service(
                picture=picture,
                title=title,
                descriptions=descriptions,
                price=price
            )
            service.user = request.user
            service.save()

            return HttpResponse(json.dumps({'message': 'Ваша услуга сохранена!'}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'message': 'error'}), content_type='application/json')


class ServiceListByID(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class CommentList(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentListByID(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
