from django.core.files.images import ImageFile

# Модели
from django.conf.urls import url
from django.shortcuts import render
from django.http import HttpResponse
import json

import User.models
from .models import Service, Comment

# Формы
from .forms import CommentForm, ServiceForm

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

        # Если отработал ajax и пришел pk, тогда удалить комментарий
        if request.is_ajax() and request.POST.get('comment_pk'):
            comment_pk = request.POST.get('comment_pk')
            comment = Comment.objects.get(pk=comment_pk)
            comment.delete()

        # Если отработал ajax и пришло не пустое тело комментария тогда сохранить его и отслать на страницу
        if request.is_ajax() and request.POST.get('the_comment') is not None:
            body = request.POST.get('the_comment')
            data = {}

            # Сохраним новый комменатрий
            comment = Comment(
                body=body,
                user=request.user,
                service=Service.objects.get(pk=self.kwargs['pk']),
            )
            comment.save()

            # Формируем ответ в виде json
            data['comment_pk'] = str(comment.pk)
            data['user_pk'] = str(comment.user.pk)
            data['service_pk'] = str(self.kwargs['pk'])
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
