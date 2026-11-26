from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Application, Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ("username", "email", "role", "password1", "password2")


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ("message",)
        widgets = {"message": forms.Textarea(attrs={"rows": 5})}
