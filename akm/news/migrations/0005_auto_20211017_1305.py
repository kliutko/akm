# Generated by Django 3.2.6 on 2021-10-17 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_newscomment_avtor_comm'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newscomment',
            options={'verbose_name': 'Коментарий', 'verbose_name_plural': 'Коментарии'},
        ),
        migrations.RenameField(
            model_name='newscomment',
            old_name='time_create',
            new_name='time_create_com',
        ),
    ]
