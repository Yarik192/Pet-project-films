from django.db import models
from django.contrib.auth.models import AbstractUser
from films.models import Film

class CustomUser(AbstractUser):
	username = models.CharField(verbose_name="Логин", max_length=30, unique=True)
	email = models.EmailField(unique=True)


class Comment(models.Model):
	film = models.ForeignKey(Film,
		                       verbose_name="Фильм",
		                       related_name='film',
		                       on_delete=models.DO_NOTHING
		                       )
	author = models.ForeignKey(CustomUser,
		                       verbose_name="Автор",
		                       related_name='comments',
		                       on_delete=models.DO_NOTHING
		                       )
	text = models.TextField(verbose_name="Текст", max_length=300)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
