
from django.utils.safestring import mark_safe

from .models import *
from django.contrib import admin




class Category_PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'text')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name', )}


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('get_html_photo', 'lname', 'fname', 'tel', 'email', 'post', 'is_jobs','id')
    list_display_links = ('lname', 'fname')
    search_fields = ('lname', 'fname')
    prepopulated_fields = {'slug': ('fname',)}
    list_editable = ('post', 'is_jobs')  # редоктируемое поле
    list_filter = ('post', 'is_jobs')  # фильтрация
    #fields = ('post', 'lname', 'fname', 'avatar', 'tel', 'email', 'is_jobs') # список выводимых редактируемых полей
    #readonly_fields = () поля только для чтения


    def get_html_photo(self, object):
        if object.avatar:
            return mark_safe(f"<img src='{object.avatar.url}' width=50>")

    get_html_photo.short_description = 'миниатюра'


# Register your models here.

admin.site.register(About)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Category_Portfolio, Category_PortfolioAdmin)
#admin.site.register(Specialty)









