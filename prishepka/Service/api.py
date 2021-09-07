from django.views.generic import TemplateView
from django.http import HttpResponse
import json

from .models import Service, Comment

from rest_framework.permissions import AllowAny
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
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
    permission_classes = [AllowAny]

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

    # Обновление услуги
    def put(self, request, *args, **kwargs):
        if request.is_ajax():
            pk = request.POST.get('pk')
            title = request.POST.get('title')
            descriptions = request.POST.get('descriptions')
            price = request.POST.get('price')
            picture = request.FILES.get('picture')
            data = {}
            service = Service.objects.get(pk=pk)

            if picture is not None:
                service.picture = picture
            service.title = title
            service.descriptions = descriptions
            service.price = price

            service.save()

            data['title'] = service.title
            data['descriptions'] = service.descriptions
            data['price'] = service.price
            if picture is not None:
                data['picture'] = service.picture.url

            return HttpResponse(json.dumps(data), content_type='application/json')

        else:
            return HttpResponse(json.dumps({'message': 'error'}), content_type='application/json')

    # Удаление услуги
    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            pk = request.POST.get('pk')

            service = Service.objects.get(pk=pk)
            service.delete()
            return HttpResponse(json.dumps({'message': f'Услуга {service.title} удалена'}),
                                content_type='application/json')
        else:
            return HttpResponse(json.dumps({'message': 'ERROR'}),
                                content_type='application/json')


class CommentList(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def post(self, request, *args, **kwargs):

        # Если отработал ajax и пришло не пустое тело комментария тогда сохранить его и отслать на страницу
        if request.is_ajax() and (request.POST.get('comment') != '' or request.POST.get('comment') is not None):
            body = request.POST.get('comment')
            service_pk = request.POST.get('service_pk')
            data = {}

            # Сохраним новый комменатрий
            comment = Comment(
                body=body,
                user=request.user,
                service=Service.objects.get(pk=service_pk),
            )
            comment.save()

            # Формируем ответ в виде json
            data['comment_pk'] = str(comment.pk)
            data['user_pk'] = str(comment.user.pk)
            data['service_pk'] = str(service_pk)
            data['body'] = comment.body
            data['date_created'] = str(comment.date_created.strftime('%d.%m.%Y %H:%M:%S'))
            data['user'] = str(comment.user)
            if comment.user.userinfo.image:
                data['image'] = comment.user.userinfo.image.url
            else:
                data['image'] = ''

            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'error': 'error'}), content_type='application/json')


class CommentListByID(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            comment_pk = request.POST.get('comment_pk')
            comment = Comment.objects.get(pk=comment_pk)
            comment.delete()

            return HttpResponse(json.dumps({'message': 'Комментарий удалён'}),
                                content_type='application/json')
        else:
            return HttpResponse(json.dumps({'message': 'ERROR'}),
                                content_type='application/json')
