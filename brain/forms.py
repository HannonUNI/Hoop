
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class qustions_form(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "password1")
