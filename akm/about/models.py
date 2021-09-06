from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Portfolio(models.Model):
    POST_CHOICES = (
        ('director', 'Директор'),
        ('zam_director', 'Заместитель Директора'),
        ('nachalnik_ceha', 'Начальник цеха'),
        ('injener', 'Инженер'),
        ('master', 'Мастер'),
    )

    avatar = models.ImageField('Аватарка', upload_to='static/images/portfolio')
    lname = models.CharField('Имя', max_length=20, default='')
    fname = models.CharField('Фамилия', max_length=50, default='')
    post = models.CharField('Должность', max_length=30, choices=POST_CHOICES)
    email = models.EmailField('Почта', default='')
    tel = PhoneNumberField(verbose_name='Телефон')
    message = models.TextField('Информация')

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Потфолио'
    def __str__(self):
        return f'{self.lname} {self.fname}'
