from django.db import models

# Create your models here.
class Feedback(models.Model):
    CITY_CHOICES = (
        ('minsk', 'Минск'),
        ('brest', 'Брест'),
        ('grodno', 'Гродно'),
        ('vitebsk', 'Витебск'),
        ('mogilev', 'Могилев'),
        ('gomel', 'Гомель')

    )

    name = models.CharField('Имя', max_length=20)
    email = models.EmailField('Почта', help_text='Только почта Яндекса')
    message = models.TextField('Сообщение')
    city = models.CharField('Город', max_length=20, choices=CITY_CHOICES)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


    def __str__(self):
        return self.email
