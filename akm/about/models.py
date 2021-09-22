from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class About(models.Model):
    pass

class Category_Portfolio(models.Model):
    name = models.CharField('Наименование должности', max_length=100)
    text = models.TextField('Функциональные обязанности', )
    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
    def __str__(self):
        return self.name

class Portfolio(models.Model):

    post = models.ForeignKey('Category_Portfolio', verbose_name='Должность', on_delete=models.PROTECT)
    avatar = models.ImageField('Аватарка', upload_to='static/images/portfolio')
    lname = models.CharField('Имя', max_length=20, default='')
    fname = models.CharField('Фамилия', max_length=50, default='')
    tel = PhoneNumberField(verbose_name='Телефон')
    email = models.EmailField('Почта', default='')
    message = models.TextField('Информация')

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Потфолио'
    def __str__(self):
        return f'{self.lname} {self.fname}'

# class Specialty(models.Model):
#
#
#     image = models.ImageField('Картинка', upload_to='static/images')
#     title = models.CharField('Заголовок', max_length=50)
#     subtitle = models.TextField('Подзаголовок')
#
#     class Meta:
#         verbose_name = 'Наша специальность'
#         verbose_name_plural = 'Наши специальности'
#
#     def __str__(self):
#         return self.title

