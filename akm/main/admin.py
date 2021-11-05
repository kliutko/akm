

from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# Register your models here.
class ReklamaCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'id')
    list_display_links = ('name',)



class ReklamaPostAdmin(admin.ModelAdmin):
    list_display = ('get_html_photo', 'reklama_category', 'name', 'time_create', 'time_update', 'is_published', 'id', 'content')
    list_display_links = ('name',)
    search_fields = ('name', 'reklama_category')
    list_editable = ('is_published', 'reklama_category')  # редактируемое поле
    list_filter = ('reklama_category', 'is_published', 'time_create', 'time_update')  # фильтрация
    list_per_page = 10
    list_max_show_all = 100
    # fields = ('name', 'time_create', 'time_update', 'reklama_category', 'get_html_photo', 'image', 'content')
    # readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    # inlines = [Comment, ]

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")
    get_html_photo.short_description = 'миниатюра'



admin.site.register(ReklamaPost, ReklamaPostAdmin)
admin.site.register(ReklamaCategory, ReklamaCategoryAdmin)



