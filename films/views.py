from django.views.generic import ListView
from .models import *
from django.views.generic.base import ContextMixin


class AllGenreAllCountryMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_genre"] = Genre.objects.all()
        context["all_country"] = Country.objects.all()
        return context


class MainPage(AllGenreAllCountryMixin, ListView):
    model = Film
    template_name = "films/main_page.html"
    context_object_name = "films"


class GenrePage(AllGenreAllCountryMixin, ListView):
    model = Genre
    template_name = "films/genre_page.html"
    context_object_name = "films"

    def get_queryset(self, *args, **kwargs):
        return Film.objects.filter(genre__slug=self.kwargs['slug'])


class CountryPage(AllGenreAllCountryMixin, ListView):
    model = Country
    template_name = "films/country_page.html"
    context_object_name = "films"

    def get_queryset(self, *args, **kwargs):
        return Film.objects.filter(country__slug=self.kwargs['slug'])


class ProducerPage(AllGenreAllCountryMixin, ListView):
    model = Producer
    template_name = "films/producer_page.html"
    context_object_name = "films"

    def get_queryset(self, *args, **kwargs):
        return Film.objects.filter(producer__slug=self.kwargs['slug'])
