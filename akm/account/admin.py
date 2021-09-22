from django.contrib import admin
from .models import *

# Register your models here.

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name_role',)
    list_filter = ('name_role',)  # фильтрация


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'post', 'tel', 'email')
    list_filter = ('name_role', 'post')  # фильтрация
    list_editable = ('tel', 'email')   # редактируемое поле

class EntityAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_job')
    list_display_links = ('name',)
    search_fields = ('name', )
    list_editable = ('is_job',)  # редактируемое поле
    list_filter = ('name', )  # фильтрация

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name_entity', 'name_subject', 'oblast', 'sity', 'address', 'name', 'tel')
    list_display_links = ('name_entity', 'name_subject', 'name',)
    search_fields = ('name_entity', 'name_subject', 'name')
    list_filter = ('name_entity', 'name_subject', 'oblast', 'sity')  # фильтрация

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('promptness', 'name_subject', 'title', 'message', 'time_create', 'status',)
    list_display_links = ('promptness', 'name_subject', 'title', 'message')
    search_fields = ('promptness', 'name_subject', 'title')
    list_editable = ('status',)  # редактируемое поле
    list_filter = ('promptness', 'name_subject', 'status')  # фильтрация


admin.site.register(Role, RoleAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Entity, EntityAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Service, ServiceAdmin)

