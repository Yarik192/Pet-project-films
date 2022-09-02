from django.views.generic import ListView, DetailView
from .models import *
from django.views.generic.base import ContextMixin
from django.views.generic.edit import FormMixin
from profile_user.forms import CommentForm
from django.urls import reverse_lazy


class AllGenreAllCountryMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_genre"] = Genre.objects.all()
        context["all_country"] = Country.objects.all()
        context["all_year"] = Year.objects.all()
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


class YearPage(AllGenreAllCountryMixin, ListView):
    model = Year
    template_name = "films/year_page.html"
    context_object_name = "films"

    def get_queryset(self, *args, **kwargs):
        return Film.objects.filter(year__slug=self.kwargs['slug'])


class FilmView(AllGenreAllCountryMixin, DetailView, FormMixin):
    model = Film
    form_class = CommentForm
    pk_url_kwarg = "slug_field"
    template_name = "films/film_detail.html"
    
    def get_success_url(self, *args, **kwargs):
        return reverse_lazy("film", kwargs={"slug":self.get_object().slug})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid:
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.film = self.get_object()
        self.object.save()
        return super().form_valid(form)


class SearchPage(AllGenreAllCountryMixin, ListView):
    model = Film
    template_name = "films/search_page.html"
    context_object_name = "films"

    def get_queryset(self, *args, **kwargs):
        name_film = self.request.GET.get("name_film")
        return Film.objects.filter(title = name_film)

