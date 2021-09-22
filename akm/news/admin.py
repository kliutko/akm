from django.contrib import admin
from .models import *

# Register your models here.
class NewsCategotyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title_category', )}


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name_category', 'time_create', 'time_update', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published',)  # редоктируемое поле
    list_filter = ('name_category', 'is_published', 'time_create')  # фильтрация



admin.site.register(News_category, NewsCategotyAdmin)
admin.site.register(News, NewsAdmin)
