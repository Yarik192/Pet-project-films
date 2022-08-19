from django.contrib import admin

# Register your models here.
from films.models import Film, Genre, Producer, Country, Year


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name","last_name")}


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("year",)}
