from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from captcha.fields import CaptchaField


class RegistrationUser(UserCreationForm):
	password1 = forms.CharField(label="пароль",required=True, widget=forms.PasswordInput)
	password2 = forms.CharField(label="повторите пароль",required=True, widget=forms.PasswordInput)
	captcha = CaptchaField(label="введите код с картинки")
	class Meta:
		model = CustomUser
		fields = ("username","email")