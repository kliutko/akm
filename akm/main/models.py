from django.db import models

# Create your models here.
class Feedback(models.Model):
    CITY_CHICES = (
        ('minsk', 'Минск'),
        ('minsk', 'Минск'),
        ('minsk', 'Минск'),
        ('minsk', 'Минск'),
        ('minsk', 'Минск'),
        ('minsk', 'Минск')

    )

    name = models.CharField('', max_length=20)
    email = models.EmailField('Почта')
    message = models.TextField('Сообщение')
    citi = models.CharField('Город', ma_lenght=2, choices=CITY_CHOICES)

    class Meta:
        verbose_name = 'Отзыв '
        verbose_name_plural = 'Отзывы'


    def __str__(self):
        return self.email
