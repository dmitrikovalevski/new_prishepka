# Инструмент Django для создании модели
from django.db import models

# Модель пользователя
from django.contrib.auth.models import User


class UserInfo(models.Model):
    image = models.ImageField(upload_to='user', null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    # При обращении к объекту модели будет указан ник пользователя
    def __str__(self):
        return str(self.user)