from django.views.generic import ListView
from .models import *


class Main_page(ListView):
    model = Film
    template_name = "films/main_page.html"
    context_object_name = "film"
