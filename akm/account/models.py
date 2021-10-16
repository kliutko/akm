from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
# Create your models here.

class Role(models.Model):
    name_role = models.CharField('Роль пользователя', max_length=100)
    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


    def __str__(self):
        return self.name_role


class Profile(models.Model):
    name_role = models.ForeignKey('Role', verbose_name='Роль', on_delete=models.CASCADE)
    login = models.OneToOneField('auth.User', on_delete=models.CASCADE, primary_key=True)
    last_name = models.CharField('Имя', max_length=50)
    first_name = models.CharField('Фамилия', max_length=50, blank=True)
    post = models.CharField('Должность', max_length=100, blank=True)
    tel = PhoneNumberField(verbose_name='Контактный телефон', blank=True)
    email = models.EmailField('Email', max_length=100, blank=True)
    slug = models.SlugField(verbose_name='URL', unique=True, db_index=True, max_length=220)
    image =  models.ImageField('Картинка', upload_to='static/images/avatars/%Y/%m/%d/')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
    def __str__(self):
        return f'{self.last_name}, {self.first_name}, {self.login}'

    def get_absolute_url(self):
        return reverse('account', kwargs={'acc_slug': self.slug})

class Entity(models.Model):
    name = models.CharField('Организация', max_length=50)
    is_job = models.BooleanField(verbose_name='Договор', default=True)
    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.name

class Subject(models.Model):

    name_entity = models.ForeignKey('Entity', verbose_name='Организация', on_delete=models.CASCADE)
    name_subject = models.CharField('Объект', max_length=100)
    oblast = models.CharField('Область', max_length=100)
    sity = models.CharField('Город или район', max_length=100)
    address = models.CharField('адрес, улица, дом.', max_length=100)
    name = models.CharField('Имя ответственного на объекте',max_length=100, blank=True)
    tel = PhoneNumberField(verbose_name='Контактный телефон', blank=True)
    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'
    def __str__(self):
        return f'{self.name_entity} - {self.name_subject}'

class Service(models.Model):
    PROMPTNESS_CHOICES = (
        ('Срочно', 'Срочно'),
        ('Среднее', 'Среднее'),
        ('Не срочно', 'Не срочно'),
    )
    STATUS_CHOICES = (
        ('Ожидает', 'Ожидает'),
        ('Принята', 'Принята'),
        ('Выполнена', 'Выполнена'),

    )
    name_subject = models.ForeignKey('Subject', verbose_name='Объект', on_delete=models.CASCADE)
    title = models.CharField('Тема', max_length=100)
    message = models.TextField('Сообщение', help_text='Подробно опишите проблему')
    promptness = models.CharField('Срочность', max_length=50, choices=PROMPTNESS_CHOICES)
    status = models.CharField('Статус заявки', max_length=50, choices=STATUS_CHOICES, default='wait')
    time_create = models.DateTimeField('Дата подачи заявки', auto_now_add=True)
    time_update = models.DateTimeField('Дата последнего изменения заявки', auto_now=True)
    login = models.OneToOneField(Profile, on_delete=models.CASCADE, primary_key=True)
    #id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'{self.name_subject} - {self.title}'
