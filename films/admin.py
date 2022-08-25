from django.contrib import admin

# Register your models here.
from films.models import Film, Genre, Producer, Country, Year


class CountryInline(admin.TabularInline):
    prepopulated_fields = {"slug": ("title",)}
    model = Country
    extra = 0


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = (CountryInline,)

    # readonly_fields = ("slug",)
    #
    # def __init__(self, *args, **kwargs):
    #
    #     if not self.instance:
    #         self.prepopulated_fields = {'slug': ('title',)}
    #     super(FilmAdmin, self).__init__(*args, **kwargs)
    #
    # def get_readonly_fields(self, request, obj=None):
    #     fields = []
    #     if obj:
    #         fields += ['slug']
    #     return fields  # TODO


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name", "last_name")}


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("year",)}
