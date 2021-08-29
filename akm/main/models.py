from django.db import models

# Create your models here.
class Feedback(models.Model):
    CITY_CHOICES = (
        ('minsk', 'Минск'),
        ('minsk', 'Минск'),
        ('minsk', 'Минск'),
        ('minsk', 'Минск'),
        ('minsk', 'Минск'),
        ('minsk', 'Минск')

    )

    name = models.CharField('Имя', max_length=20)
    email = models.EmailField('Почта')
    message = models.TextField('Сообщение')
    citi = models.CharField('Город', max_lenght=20, choices=CITY_CHOICES)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


    def __str__(self):
        return self.email
