# Перенаправление
from django.urls import reverse

# Модель пользователя
from django.contrib.auth.models import User

# CBV для смены пароля пользователя
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetCompleteView,
)

# CBV для входа и выхода из системы пользователя
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)

# CBV для работы с представлениями
from django.views.generic import (
    CreateView,
    DetailView,
)

# Формы
from .forms import (
    CreateUserForm,
    UserAccountUpdateForm,
    UpdateUserForm,
)

# Перенаправление и отображение
from django.shortcuts import (
    redirect,
    render,
)


# Класс регистрации пользователя на сайте
class UserFormView(CreateView):
    form_class = CreateUserForm
    template_name = 'users/add.html'

    # После регистрации пользователь попадёт на страницу входа
    def get_success_url(self):
        return reverse('login')


# Вход в систему
class UserLogIn(LoginView):
    pass


# Выход из системы
class UserLogOut(LogoutView):
    pass


# Класс просмотра кабинета пользователя
class UserAccountView(DetailView):
    model = User
    template_name = 'users/account_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Переменная, которая позволяет видеть пользователю только свои услуги
        # в своём кабинете.
        context['owner'] = self.request.user.pk == self.kwargs['pk']

        # Услуги пользователя, которые сортируются по дате
        owner = User.objects.get(pk=self.kwargs['pk'])
        context['owner_services'] = owner.service_set.order_by('-date_created')
        return context


# Функция редактирования информиции пользователя
def update_user_account(request):

    # Проверка метода
    if request.method == 'POST':

        # Формы, которые принимают ифнормацию которую отсылает пользователь
        user_info = UserAccountUpdateForm(request.POST, request.FILES,
                                          instance=request.user.userinfo)
        user = UpdateUserForm(request.POST, instance=request.user)

        # Если пользователь сменит аватарку, старая картинка будет удалена из папки "MEDIA"
        if request.FILES:
            request.user.userinfo.image.delete()

        # Проверка на валидность и сохранение форм
        if user_info.is_valid() and user.is_valid():
            form = user_info.save()
            form.user = request.user
            form.save()
            user.save()
            return redirect('account', request.user.id)
    else:

        # Если ничего не случилось или проверка на валидность не прошла,
        # вернёт пользователю начальные формы для заполнения.
        user_info = UserAccountUpdateForm(instance=request.user.userinfo)
        user = UpdateUserForm(instance=request.user)
    context = {
        'user_info': user_info,
        'user': user,
    }
    return render(request, 'users/account_update.html', context)


# Базовые классы для смены пароля пользователя
class PasswordReset(PasswordResetView):
    template_name = 'registration/reset_form.html'


class PasswordResetDone(PasswordResetDoneView):
    template_name = 'registration/reset_done.html'


class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'registration/reset_confirm.html'


class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'registration/reset_complete.html'
