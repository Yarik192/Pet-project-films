from datetime import datetime
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Genre(models.Model):
    title = models.CharField(verbose_name="Название", max_length=20)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("genre_page", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Producer(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=30)
    last_name = models.CharField(verbose_name="Фамилия", max_length=30)
    slug = models.SlugField()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.full_name}"

    def get_absolute_url(self):
        return reverse("producer_page", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Режиссёр"
        verbose_name_plural = "Режиссёры"


class Country(models.Model):
    title = models.CharField(verbose_name="Название", max_length=20)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("country_page", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class Year(models.Model):
    year = models.IntegerField(verbose_name="Год",
                               validators=[MinValueValidator(1895), MaxValueValidator(datetime.now().year)])
    slug = models.SlugField()

    def __str__(self):
        return f"{self.year}"

    def get_absolute_url(self):
        return reverse("year_page", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Год"
        verbose_name_plural = "Года"


class Film(models.Model):
    title = models.CharField(verbose_name="Название", max_length=80)
    poster = models.ImageField(verbose_name="Изображение")
    description = models.TextField(verbose_name="Описание")
    year = models.ForeignKey(Year, verbose_name="Год", on_delete = models.DO_NOTHING)
    country = models.ManyToManyField(Country, verbose_name="Страны")
    genre = models.ManyToManyField(Genre, verbose_name="Жанры")
    duration = models.CharField(max_length=7, verbose_name="Продолжительность")
    premiere = models.CharField(verbose_name="Премьера фильма", max_length=17)
    producer = models.ManyToManyField(Producer, verbose_name="Режиссёры")
    film_file = models.FileField()

    def __str__(self):
        return f"{self.title} ({self.year})"

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
