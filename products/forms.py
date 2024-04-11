from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SearchForm(forms.Form):
    search_bar = forms.CharField(max_length=256)

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
