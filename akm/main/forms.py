from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
# from .models import Feedback
from django.forms import ModelForm




# class FeedbackForm(ModelForm):
#     class Meta:
#         model = Feedback
#         fields = ['name', 'email', 'message', 'city']

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='login', widget=forms.TextInput(attrs={'class': 'font-weight-bold'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'font-weight-bold'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'font-weight-bold'}))
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput(attrs={'class': 'font-weight-bold'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='login', widget=forms.TextInput(attrs={'class': 'font-weight-bold'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'font-weight-bold'}))


