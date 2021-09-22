# Generated by Django 3.2.6 on 2021-09-14 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_alter_portfolio_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/images', verbose_name='Картинка')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('subtitle', models.TextField(verbose_name='Подзаголовок')),
            ],
            options={
                'verbose_name': 'Наша специальность',
                'verbose_name_plural': 'Наши специальности',
            },
        ),
    ]
