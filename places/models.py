from django.db import models
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField


class Place(models.Model):

    title = models.CharField(max_length=200, verbose_name='Название')
    tooltip_title = models.CharField(max_length=200, verbose_name='Сокращенное название', blank=True, null=True)
    short_description = models.TextField(verbose_name='Короткое описание')
    long_description = HTMLField(default='Впиши сюда вёрстку!', verbose_name='Длинное описание')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.tooltip_title:
            self.tooltip_title = self.title.split('«')[-1][:-1]
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class PlaceImage(models.Model):

    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Место', related_name='images')
    image = models.ImageField(verbose_name='Изображение', upload_to='place_image/')
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return f'Изображение {self.id}.{self.place.title}'

    def preview_image(self):
        try:
            image = mark_safe(f'<img src="{self.image.url}" height="200px">')
            return image
        except ValueError:
            return 'Not loaded yet'

    class Meta:
        verbose_name = 'Изображение места'
        verbose_name_plural = 'Изображения места'
        ordering = ['order']
