from django.urls import path
from .views import Main_page

urlpatterns = [
    path("", Main_page.as_view(), name="main_page"),
]
