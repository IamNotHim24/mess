from django import forms
from .models import Review

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class resReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text','restaurant']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        Model = User
        fields = ('username','email','password1','password2')

