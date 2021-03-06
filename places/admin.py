from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin


from places.models import Place, PlaceImage

class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    readonly_fields = ['preview_image',]


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PlaceImageInline,
    ]



admin.site.register(PlaceImage)
