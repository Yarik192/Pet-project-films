from django.contrib import admin

from .models import CustomUser, Comment

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
	list_display = ["username", "email"]


@admin.register(Comment)
class ComentAdmin(admin.ModelAdmin):
	pass
