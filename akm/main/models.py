from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.
# class Feedback(models.Model):
#     pass
# #     CITY_CHOICES = (
#         ('minsk', 'Минск'),
#         ('brest', 'Брест'),
#         ('grodno', 'Гродно'),
#         ('vitebsk', 'Витебск'),
#         ('mogilev', 'Могилев'),
#         ('gomel', 'Гомель')
#
#     )
#
#     name = models.CharField('Имя', max_length=20)
#     email = models.EmailField('Почта', help_text='Только почта Яндекса')
#     message = models.TextField('Сообщение')
#     city = models.CharField('Город', max_length=20, choices=CITY_CHOICES)
#
#     class Meta:
#         verbose_name = 'Отзыв'
#         verbose_name_plural = 'Отзывы'
#
#
#     def __str__(self):
#         return self.email

class ReklamaCategory(models.Model):
    name = models.CharField('Категория', max_length=200)
    content = models.TextField('Описание, местоположение', blank=True)

    class Meta:
        verbose_name = 'Категория рекламы'
        verbose_name_plural = 'Категории рекламы'

    def __str__(self):
        return self.name

class ReklamaPost(models.Model):
    reklama_category = models.ForeignKey('ReklamaCategory', verbose_name='Категория', on_delete=models.PROTECT)
    name = models.CharField('Заголовок', max_length=200)
    content = models.TextField('Текст', blank=True)
    image = models.ImageField('Картинка', upload_to='static/recklama/banner/%Y/%m/%d/')
    time_create = models.DateTimeField('Дата публикации')
    time_update = models.DateTimeField('Дата окончания публикации')
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True)
    lname = models.CharField('Заказчик', max_length=200)


    class Meta:
        verbose_name = 'Реклама'
        verbose_name_plural = 'Реклама'
        ordering = ['time_create', 'name']
    def __str__(self):
        return self.name
