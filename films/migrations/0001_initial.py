# Generated by Django 4.1 on 2022-08-20 12:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Режиссёр',
                'verbose_name_plural': 'Режиссёры',
            },
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1895), django.core.validators.MaxValueValidator(2022)], verbose_name='Год')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Год',
                'verbose_name_plural': 'Года',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Название')),
                ('slug', models.SlugField(unique=True)),
                ('poster', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(verbose_name='Описание')),
                ('duration', models.CharField(max_length=7, verbose_name='Продолжительность')),
                ('premiere', models.CharField(max_length=17, verbose_name='Премьера фильма')),
                ('film_file', models.FileField(upload_to='')),
                ('country', models.ManyToManyField(to='films.country', verbose_name='Страны')),
                ('genre', models.ManyToManyField(to='films.genre', verbose_name='Жанры')),
                ('producer', models.ManyToManyField(to='films.producer', verbose_name='Режиссёры')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='films.year', verbose_name='Год')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
    ]
