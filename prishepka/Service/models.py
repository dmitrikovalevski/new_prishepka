# Инструмент Django для моделей
from django.db import models

# Модель пользователя
from django.contrib.auth.models import User


# Модель услуги
class Service(models.Model):
    picture = models.ImageField(upload_to='service', null=True, blank=True)
    title = models.CharField(max_length=200)
    descriptions = models.TextField()
    price = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


# Модель комментария
class Comment(models.Model):
    body = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.comment
