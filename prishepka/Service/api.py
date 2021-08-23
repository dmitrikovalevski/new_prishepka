from django.views.generic import TemplateView

from .models import Service, Comment

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
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


class ServiceListByID(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class CommentList(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentListByID(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


