from django.conf import settings
from django.db import models
from django.urls import reverse
from pytils.translit import slugify


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created', on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    title = models.CharField(max_length=256, verbose_name='Название')
    slug = models.SlugField(max_length=256, verbose_name='Слаг')
    url = models.URLField(max_length=2000, verbose_name='Изначальный URL')
    image = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Файл изображения')
    description = models.TextField(blank=True, verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['-created'])
        ]
        ordering = ['-created']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])
