# Generated by Django 4.1 on 2022-08-20 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='country',
        ),
        migrations.AddField(
            model_name='film',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='films.country', verbose_name='Страны'),
            preserve_default=False,
        ),
    ]