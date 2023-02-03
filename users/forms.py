from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from hcaptcha.fields import hCaptchaField


class UserOurRegistration(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    captcha = hCaptchaField()

    class Meta():
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'captcha']

