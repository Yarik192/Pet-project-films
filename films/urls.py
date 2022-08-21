from django.urls import path
from .views import MainPage, GenrePage, CountryPage, ProducerPage, YearPage, FilmView, SearchPage

urlpatterns = [
    path("", MainPage.as_view(), name="main_page"),
    path("country/<slug:slug>/", CountryPage.as_view(), name="country_page"),
    path("genre/<slug:slug>/", GenrePage.as_view(), name="genre_page"),
    path("producer/<slug:slug>/", ProducerPage.as_view(), name="producer_page"),
    path("year/<slug:slug>/", YearPage.as_view(), name="year_page"),
    path("film/<slug:slug>/", FilmView.as_view(), name="film"),
    path("search/", SearchPage.as_view(), name="search_page")
]
