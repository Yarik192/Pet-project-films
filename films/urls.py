from django.urls import path
from .views import MainPage, GenrePage, CountryPage, ProducerPage

urlpatterns = [
    path("", MainPage.as_view(), name="main_page"),
    path("country/<slug>:slug", CountryPage.as_view(), name="country_page"),
    path("genre/<slug>:slug", GenrePage.as_view(), name="genre_page"),
    path("producer/<slug>:slug", ProducerPage.as_view(), name="producer_page"),
]
