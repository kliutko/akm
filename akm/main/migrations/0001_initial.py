# Generated by Django 3.2.6 on 2021-08-29 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('citi', models.CharField(choices=[('minsk', 'Минск'), ('brest', 'Брест'), ('grodno', 'Гродно'), ('vitebsk', 'Витебск'), ('mogilev', 'Могилев'), ('gomel', 'Гомель')], max_length=20, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
