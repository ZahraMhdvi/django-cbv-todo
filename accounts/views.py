from django.shortcuts import render

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import RegisterForm

class UserLoginView(LoginView):
    template_name = "accounts/login.html"

    def get_success_url(self):
        return reverse_lazy("tasks:task-list")


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("accounts:login")



class RegisterView(FormView):
    template_name = "accounts/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("accounts:login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)