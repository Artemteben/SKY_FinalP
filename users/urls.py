from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from django.template.defaulttags import url
from django.urls import path

from config import settings
from users.apps import UsersConfig
from users.views import UserCreateView, email_verification, reset_password

app_name = UsersConfig.name

urlpatterns = [
    path('users/registration/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='users:login'), name='logout'),
    path("register/", UserCreateView.as_view(), name="register"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
    path("reset-password/", reset_password, name="reset_password"),
]