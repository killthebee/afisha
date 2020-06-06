from django.db import models
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description_short = models.TextField(verbose_name='Короткое описание')
    coordinates_lat = models.FloatField(verbose_name='Широта')
    coordinates_lng = models.FloatField(verbose_name='Долгота')
    text = HTMLField(default='Впиши вёрстку места, пожалуйста', verbose_name='Длинное описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Место', related_name='images')
    image = models.ImageField(verbose_name='Изображение', upload_to='place_images/')
    sort = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return f'Изображение {self.id}.{self.place.title}'

    def preview_img(self):
        return mark_safe(f'<img src="{self.image.url}" height="200"')

    class Meta:
        verbose_name = 'Изображение места'
        verbose_name_plural = 'Изображения места'
        ordering = ['sort']

