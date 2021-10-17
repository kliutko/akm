from django import forms
from .models import NewsComment
from django.forms import ModelForm




class NewsCommentForms(ModelForm):
    class Meta:
        model = NewsComment
        fields = ['comment', ]
        widgets = {
            'name_news': forms.HiddenInput(),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'id': 'message', 'cols':'30', 'rows':'5', 'placeholder': 'Ваше сообщение'}),
        }