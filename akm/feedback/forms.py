from django import forms
from .models import Feedback
from django.forms import ModelForm




class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'tel', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'id':'fullname', 'placeholder':'Полное имя'}),
            'tel': forms.TextInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Телефон'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Email адрес'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'id': 'message', 'cols':'30', 'rows':'5', 'placeholder': 'Ваше сообщение'}),
        }