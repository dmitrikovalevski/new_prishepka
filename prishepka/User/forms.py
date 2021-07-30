# Модель пользователя
from django.contrib.auth.models import User

# Форма создания пользователя
from django.contrib.auth.forms import UserCreationForm

# Инструмент Django для создания форм
from django import forms

# Модель личной информации пользователя
from .models import UserInfo


# Форма модели пользователя
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']


# Форма редактирования имени и фамилии пользователя
class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


# Форма редактирования личной информации пользования
class UserAccountUpdateForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['image', 'phone']