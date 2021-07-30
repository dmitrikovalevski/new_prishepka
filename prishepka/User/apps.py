from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'User'

    # Метод, который срабатывает при использовании сигнала
    def ready(self):
        import User.signals
