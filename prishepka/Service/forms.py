# Модели
from .models import Comment

# Инструмент Django для создания форм
from django import forms


# Форма для комментария

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']