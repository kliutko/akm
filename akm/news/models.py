from django.db import models
from django.urls import reverse
#


class News_category(models.Model):
    title_category = models.CharField('Имя категории ', max_length=50, db_index=True, default='')
    subtitle_category = models.TextField('Описание категории', max_length=300, blank=True, default='')
    slug = models.SlugField(verbose_name='URL', unique=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title_category

    def get_absolute_url(self):
        return reverse('news_category', kwargs={'category_slug': self.slug})


class News(models.Model):
    name_category = models.ForeignKey('News_category', verbose_name='Категория', on_delete=models.PROTECT)
    title = models.CharField('Заголовок', max_length=200)
    content = models.TextField('Текст', blank=True)
    image = models.ImageField('Картинка', upload_to='static/images/%Y/%m/%d/')
    time_create = models.DateTimeField('Дата публикации', auto_now_add=True)
    time_update = models.DateTimeField('Дата последнего изменения', auto_now=True)
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True)
    slug = models.SlugField(verbose_name='URL', unique=True, db_index=True, max_length=220)


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['time_create', 'title']
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news', kwargs={'news_slug': self.slug})

    class News(models.Model):
        name_category = models.ForeignKey('News_category', verbose_name='Категория', on_delete=models.PROTECT)
        title = models.CharField('Заголовок', max_length=200)
        content = models.TextField('Текст', blank=True)
        image = models.ImageField('Картинка', upload_to='static/images/%Y/%m/%d/')
        time_create = models.DateTimeField('Дата публикации', auto_now_add=True)
        time_update = models.DateTimeField('Дата последнего изменения', auto_now=True)
        is_published = models.BooleanField(verbose_name='Опубликовано', default=True)
        slug = models.SlugField(verbose_name='URL', unique=True, db_index=True, max_length=220)

        class Meta:
            verbose_name = 'Новость'
            verbose_name_plural = 'Новости'
            ordering = ['time_create', 'title']

        def __str__(self):
            return self.title

        def get_absolute_url(self):
            return reverse('news', kwargs={'news_slug': self.slug})



class NewsComment(models.Model):
    name_news = models.ForeignKey('News', verbose_name='Новость', on_delete=models.PROTECT)
    avtor_comm = models.ForeignKey('auth.User',null=True, blank=True, verbose_name='Автор', on_delete=models.PROTECT)
    comment = models.TextField('Текст комментария',null=True, blank=True)
    time_create_com = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return f'Автор: {self.avtor_comm} Новость: {self.name_news}    Комментарий: {self.comment}'
