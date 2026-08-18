from django.shortcuts import render

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class UserLoginView(LoginView):
    template_name = "accounts/login.html"

    def get_success_url(self):
        return reverse_lazy("tasks:task-list")


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("accounts:login")