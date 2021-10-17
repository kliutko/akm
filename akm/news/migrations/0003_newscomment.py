# Generated by Django 3.2.6 on 2021-10-17 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210914_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Текст комментария')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('name_news', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.news', verbose_name='Новость')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
                'ordering': ['time_create', 'name_news'],
            },
        ),
    ]
