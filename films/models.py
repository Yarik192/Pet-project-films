from datetime import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Genre(models.Model):
    title = models.CharField(verbose_name="Название", max_length=20)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Producer(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=30)
    last_name = models.CharField(verbose_name="Фамилия", max_length=30)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        verbose_name = "Режиссёр"
        verbose_name_plural = "Режиссёры"


class Film(models.Model):
    title = models.CharField(verbose_name="Название", max_length=80)
    poster = models.ImageField(verbose_name="Изображение", height_field=200, width_field=300)
    description = models.TextField(verbose_name="Описание")
    year = models.IntegerField(verbose_name="Год",
                               validators=[MinValueValidator(1895), MaxValueValidator(datetime.now().year)])
    country = models.CharField(verbose_name="Страна", max_length=50)
    genre = models.ManyToManyField(Genre)
    duration = models.CharField(max_length=4, verbose_name="Продолжительность")
    premiere = models.CharField(verbose_name="Премьера фильма", max_length=16)
    producer = models.ManyToManyField(Producer)
    film_file = models.FileField()

    def __str__(self):
        return f"{self.title} ({self.year})"

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
