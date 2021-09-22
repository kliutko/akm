from django import forms
from .models import *
from django.forms import ModelForm




class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['name_subject', 'title', 'message', 'promptness']
        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'fullname', 'placeholder': 'Тема'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'id': 'message', 'cols': '30', 'rows': '5','placeholder': 'Ваше сообщение'}),


        }
