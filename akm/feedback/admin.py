from django.contrib import admin
from .models import *

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'email', 'time_create', 'message')
    list_display_links = ('name', 'tel', 'email')
    search_fields = ('name', 'tel',)
    list_filter = ('time_create',)  # фильтрация



admin.site.register(Feedback, FeedbackAdmin)


# Register your models here.
