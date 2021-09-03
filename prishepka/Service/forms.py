# Модели
from .models import Comment, Service

# Инструмент Django для создания форм
from django import forms


# Форма для комментария

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['picture', 'title', 'descriptions', 'price']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
