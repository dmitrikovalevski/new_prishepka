# Метод после которого сработает сигнал
from django.db.models.signals import post_save

# Декортатор который "слушает" функцию
from django.dispatch import receiver

# Группы пользователей
from django.contrib.auth.models import Group

# Модель пользователя
from django.contrib.auth.models import User

# Модель личной информации пользователя
from .models import UserInfo


# Сигнал, который после создания модели пользователя
# привязывает модель с личной информацией.
@receiver(post_save, sender=User)
def create_userinfo(instance, created, **kwargs):
    if created:
        UserInfo.objects.create(user=instance)


# Сигнал, который при создании модели пользователя
# добавляет его в группу, и если группа не существует
# создаёт группу и добавляет его к группе.
@receiver(post_save, sender=User)
def add_user_for_groups(instance, created, **kwargs):
    if created:
        try:

            # Если группа существует добавть её в переменную
            group = Group.objects.get(name='user')
        except:

            # Если группы нету, создать её
            group = Group.objects.create(name='user')

            # Добавть пользователя к группе
            instance.groups.add(group)
        else:

            # Добавть пользователя к группе
            instance.groups.add(group)