from django.contrib import admin

from places.models import Place, PlaceImage


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    readonly_fields = ['preview_img']


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = (PlaceImageInline, )
