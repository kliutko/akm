from django import forms
from .models import NewsComment, News
from django.forms import ModelForm




class NewsCommentForms(ModelForm):
    class Meta:
        model = NewsComment
        fields = ['comment', ]
        widgets = {

            'comment': forms.Textarea(attrs={'class': 'form-control', 'id': 'message', 'cols':'30', 'rows':'5', 'placeholder': 'Ваше сообщение'}),
        }