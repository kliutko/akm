from django import forms
from .models import *
from django.forms import ModelForm, TextInput, Textarea, Select

class EntityForm(ModelForm):
    class Meta:
        model = Entity
        fields = ['name', ]
        widgets = {
            'name': Select(attrs={'class': 'form-control', 'id': 'fullname', 'placeholder': 'Объект'}),

        }


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['name_entity', 'name_subject']
        widgets = {
            'name_entity': Select(attrs={'class': 'form-control', 'id': 'fullname', 'placeholder': 'Объект'}),
            'name_subject': Select(attrs={'class': 'form-control', 'id': 'fullname', 'placeholder': 'Срочность'})
        }


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['name_subject', 'title', 'message', 'promptness']
        widgets = {

            'title': TextInput(attrs={'class': 'form-control', 'id': 'fullname', 'placeholder': 'Тема'}),
            'message': Textarea(attrs={'class': 'form-control', 'id': 'message', 'cols': '30', 'rows': '5','placeholder': 'Ваше сообщение'}),
            'name_subject': Select(attrs={'class': 'form-control', 'id': 'fullname', 'placeholder': 'Объект'}),
            'promptness': Select(attrs={'class': 'form-control', 'id': 'fullname', 'placeholder': 'Срочность'})


        }
class ProfileForm(forms.ModelForm):

        class Meta:
            model = Profile
            fields = ['last_name', 'first_name', 'post', 'tel', 'email', 'image', 'login']