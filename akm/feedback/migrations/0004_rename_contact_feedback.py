# Generated by Django 3.2.6 on 2021-09-18 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_alter_contact_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Feedback',
        ),
    ]