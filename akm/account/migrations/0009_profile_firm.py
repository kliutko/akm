# Generated by Django 3.2.6 on 2021-09-22 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_remove_profile_firm'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='firm',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='account.entity', verbose_name='фирма'),
        ),
    ]
