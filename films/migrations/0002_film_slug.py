# Generated by Django 4.1 on 2022-08-20 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='slug',
            field=models.SlugField(default='fuck'),
            preserve_default=False,
        ),
    ]
