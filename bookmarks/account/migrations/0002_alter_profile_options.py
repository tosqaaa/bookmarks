# Generated by Django 5.0.2 on 2024-03-31 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['user'], 'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
    ]
