# Generated by Django 3.2.6 on 2021-09-07 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210907_2024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settingsheader',
            old_name='image_Header',
            new_name='image_header',
        ),
        migrations.AddField(
            model_name='settingsheader',
            name='subtitle_main',
            field=models.CharField(blank=True, max_length=20, verbose_name='подзаголовок на главной странице (на баннере)'),
        ),
        migrations.AddField(
            model_name='settingsheader',
            name='title_main',
            field=models.CharField(blank=True, max_length=20, verbose_name='Заголовок на главной странице (на баннере)'),
        ),
        migrations.AlterField(
            model_name='settingsheader',
            name='fb_url',
            field=models.CharField(blank=True, default='', max_length=25, verbose_name='Ссылка на facebook'),
        ),
        migrations.AlterField(
            model_name='settingsheader',
            name='inst_url',
            field=models.CharField(blank=True, default='', max_length=25, verbose_name='Ссылка на instagram'),
        ),
        migrations.AlterField(
            model_name='settingsheader',
            name='ld_url',
            field=models.CharField(blank=True, default='', max_length=25, verbose_name='Ссылка на linkedin'),
        ),
        migrations.AlterField(
            model_name='settingsheader',
            name='tw_url',
            field=models.CharField(blank=True, default='', max_length=25, verbose_name='Ссылка на twitter'),
        ),
    ]
