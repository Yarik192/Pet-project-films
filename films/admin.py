from django.contrib import admin

# Register your models here.
from films.models import Film, Genre, Producer


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    pass
