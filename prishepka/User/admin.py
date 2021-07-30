# Инструмент Django для работы с админкой
from django.contrib import admin

# Модель для админки
from .models import UserInfo

# Добавим в админку модель
admin.site.register(UserInfo)
