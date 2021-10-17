# Generated by Django 3.2.6 on 2021-10-17 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(max_length=220, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='news_category',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='URL'),
        ),
        migrations.CreateModel(
            name='NewsComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Текст комментария')),
                ('time_create_com', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('name_news', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='news.news', verbose_name='Новость')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
            },
        ),
    ]
