from .forms import *
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView


class Registration(CreateView):
    form_class = RegistrationUser
    template_name = "registration/registration.html"
    success_url = reverse_lazy("login")


class Login(LoginView):
    template_name = "registration/login.html"
