from django.db import models
import time


class film(models.Model):
	title = models.CharField("Название")
	description = models.TextField("Описание")
	country = CharField("Страна")
	year = models.IntegerField(
		"Год",
		min_value = 1895,
		max_value = time.strftime('%Y\n', time.localtime()))
	# здесь будет связь с моделью жанра
	
	def __str__(self):
		pass

	class Meta:
		verbose_name = "фильм"
		verbose_name_plural = "фильмы"