# Generated by Django 3.2.6 on 2021-09-14 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_delete_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settingsheader',
            name='image_header',
        ),
        migrations.RemoveField(
            model_name='settingsheader',
            name='subtitle_main',
        ),
        migrations.RemoveField(
            model_name='settingsheader',
            name='title_main',
        ),
    ]
