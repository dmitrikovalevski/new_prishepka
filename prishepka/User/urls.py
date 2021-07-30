# Пути
from django.urls import path

# Предаствления
from .views import (
    # Классы
    UserFormView,
    UserLogIn,
    UserLogOut,
    PasswordReset,
    PasswordResetConfirm,
    PasswordResetDone,
    PasswordResetComplete,
    UserAccountView,
    # Функция
    update_user_account,
)

urlpatterns = [
    path('add/', UserFormView.as_view(), name='add_user'),
    path('login/', UserLogIn.as_view(), name='login'),
    path('logout/', UserLogOut.as_view(), name='logout'),
    path('account/<int:pk>/', UserAccountView.as_view(), name='account'),
    path('update/', update_user_account, name='account_update'),
    path('forgot/', PasswordReset.as_view(), name='forgot'),
    path('reset_done/', PasswordResetDone.as_view(), name='password_reset_done'),
    path('reset_confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('change_your_password/', PasswordResetComplete.as_view(), name='password_reset_complete')
]