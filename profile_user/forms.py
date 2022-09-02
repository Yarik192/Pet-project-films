from django import forms
from django.forms import Textarea
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Comment
from captcha.fields import CaptchaField


class RegistrationUser(UserCreationForm):
	password1 = forms.CharField(label="пароль",required=True, widget=forms.PasswordInput)
	password2 = forms.CharField(label="повторите пароль",required=True, widget=forms.PasswordInput)
	captcha = CaptchaField(label="введите код с картинки")
	class Meta:
		model = CustomUser
		fields = ("username","email")


class CommentForm(forms.ModelForm):
	captcha = CaptchaField(label="введите код с картинки")
	class Meta:
		model = Comment
		fields = ("text",)
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["text"].widget = Textarea(attrs = {"rows": 5})