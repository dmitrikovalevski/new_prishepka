# Модели
from django.conf.urls import url
from django.shortcuts import render
from django.http import HttpResponse
import json

# REST FRAMEWORK
from rest_framework.views import APIView
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from .serializers import (
    CommentSerializer,
    ServiceSerializer
)

import User.models
from .models import Service, Comment

# Формы
from .forms import CommentForm

# Перенаправление
from django.urls import reverse
from django.shortcuts import redirect

# CBV для работы с представлениями
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)


# Класс вида главной страницы
class ServiceListView(ListView):
    model = Service
    template_name = 'service/all_services.html'

    # Метод класса, который выведет все услуги
    # сортированные по дате публикации от ранней к поздней.
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.order_by('-date_created')
        return context


# Класс вывода поиска
class SearchView(ListView):
    model = Service
    template_name = 'service/search_list.html'

    # Метод класса, который выведет услуги по запросу пользователя
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        # Принимаем запрос из строки поиска
        user_request = self.request.GET.get('user_search')

        # Формируем контекст по запросу.
        context['list_result'] = Service.objects.filter(title__icontains=user_request)
        return context


# Класс вывода информации по услуге
class ServiceDetailView(DetailView, CreateView):
    model = Service
    context_object_name = 'service'
    template_name = 'service/service_id.html'
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            body = request.POST.get('the_comment')
            data = {}

            comment = Comment(
                body=body,
                user=request.user,
                service=Service.objects.get(pk=self.kwargs['pk']),
            )
            comment.save()

            data['user_pk'] = str(comment.user.pk)
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # В переменную получаем владельца услуги
        service_user = Service.objects.get(pk=self.kwargs['pk']).user

        # Если услугу просмотривает не владелец услуги, тогда прибавим 1 к счётчику
        if not self.request.user == service_user:
            service = Service.objects.get(pk=self.kwargs['pk'])
            service.count += 1
            service.save()

        # Получим контекст счётчика просмотров
        context['count'] = Service.objects.get(pk=self.kwargs['pk']).count

        # Только зарегистрированный пользователь может оставить комментарий
        context['perm_for_comment'] = self.request.user.is_authenticated

        # Получим переменную для доступа к редактированию и удалению услуги.
        # Доступ к этим действиям получит только владелец услуги.
        context['owner'] = self.request.user == service_user

        # Переменная данной услуги
        current_service = Service.objects.get(pk=self.kwargs['pk'])

        # Если есть комментарий
        context['have_comment'] = current_service.comment_set.order_by('-date_created')

        return context

    # Сохранение формы комментария
    def form_valid(self, form):
        comment = form.save()

        # Проверка на регистрацию пользователя
        if self.request.user.is_authenticated and self.request.is_ajax():
            # Привязка комментария к пользователю
            comment.user = self.request.user

            # Привязка комментария к услуге
            comment.service = Service.objects.get(pk=self.kwargs['pk'])

            # Сохранение формы
            comment.save()
        return self.get_success_url()

    # После отправки комментария вернёт на страницу с откомментироавнной услугой
    def get_success_url(self):
        return redirect('detail', self.kwargs['pk'])


# Класс создания услуги
class ServiceCreateView(CreateView):
    model = Service
    fields = ['picture', 'title', 'descriptions', 'price']
    template_name = 'service/add_service.html'

    # Вернёт на главную страницу после создания услуги
    def get_success_url(self):
        return reverse('home')

    # Проверка на валидность
    def form_valid(self, form):
        service = form.save(commit=False)

        # Только зарегистрированный пользователь может оставить комментарий
        if self.request.user.is_authenticated:
            # Привязка пользователя к услуге
            service.user = self.request.user
            service.save()
        return redirect(self.get_success_url())


# Класс редактирования услуги
class ServiceUpdateView(UpdateView):
    model = Service
    fields = ['picture', 'title', 'descriptions', 'price']
    template_name = 'service/update_service.html'

    # После подтверждения редактирования вернёт на ранее отредактированную услугу
    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})


# Класс удаления услуги
class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'service/delete_service.html'

    # При удалении услуги удаляется так же картинка из папки "MEDIA"
    def delete(self, request, *args, **kwargs):
        service_for_delete = Service.objects.get(pk=self.kwargs['pk'])
        service_for_delete.picture.delete()
        service_for_delete.delete()
        return redirect(self.get_success_url())

    # После подтверждения удаления вернёт на главную страницу
    def get_success_url(self):
        return reverse('home')


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
