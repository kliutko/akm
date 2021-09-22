from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Feedback(models.Model):


    name = models.CharField('Полное Имя', max_length=20)
    email = models.EmailField('Email адрес', help_text=' ')
    tel = PhoneNumberField(verbose_name='Телефон')
    message = models.TextField('Сообщение')
    time_create = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


    def __str__(self):
        return self.email + self.name
