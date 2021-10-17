from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

# Register your models here.
class NewsCategotyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title_category', )}

# class Comment(admin.StackedInline):
#     model = NewsComment
#     fields = ('comment', 'time_create_com')
#     readonly = ('comment', 'time_create_com')
#     extra = 0

class NewsAdmin(admin.ModelAdmin):
    list_display = ('get_html_photo', 'title', 'name_category', 'time_create', 'time_update', 'is_published', 'id')
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published', 'name_category')  # редактируемое поле
    list_filter = ('name_category', 'is_published', 'time_create')  # фильтрация
    list_per_page = 10
    list_max_show_all = 100
    fields = ('title', 'time_create','name_category', 'get_html_photo', 'image', 'content', 'time_update', 'slug')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    # inlines = [Comment, ]

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_html_photo.short_description = 'миниатюра'
class NewsCommentsAdmin(admin.ModelAdmin):
    list_display = ('name_news', 'time_create_com', 'comment')
    list_display_links = ('name_news',)
    search_fields = ('name_news', )
    list_filter = ('time_create_com',)  # фильтрация

admin.site.register(News_category, NewsCategotyAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(NewsComment, NewsCommentsAdmin)
