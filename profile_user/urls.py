from django.urls import path
from .views import Login, Registration
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("registration/", Registration.as_view(), name="registration"),
    path("logout/", LogoutView.as_view(), name="logout")
] 