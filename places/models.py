from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description_short = models.TextField(verbose_name='Короткое описание')
    description_long = models.TextField(verbose_name='Длинное описание')
    coordinates_lat = models.FloatField(verbose_name='Широта')
    coordinates_lng = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Место', related_name='images')
    image = models.ImageField(verbose_name='Изображение', upload_to='place_images/')

    def __str__(self):
        return f'Изображение {self.id}.{self.place.title}'

    class Meta:
        verbose_name = 'Изображение места'
        verbose_name_plural = 'Изображения места'
