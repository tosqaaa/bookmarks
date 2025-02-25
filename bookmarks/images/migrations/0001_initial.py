# Generated by Django 5.0.2 on 2024-03-31 08:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(max_length=256, verbose_name='Слаг')),
                ('url', models.URLField(max_length=2000, verbose_name='Изначальный URL')),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Файл изображения')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images_created', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('users_like', models.ManyToManyField(blank=True, related_name='images_liked', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
                'ordering': ['-created'],
                'indexes': [models.Index(fields=['-created'], name='images_imag_created_d57897_idx')],
            },
        ),
    ]
