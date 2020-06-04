from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
import json

from places.models import Place

def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    title = place.title
    imgs = [image.get_absolute_image_url for image in place.images.all()]
    short_description = place.description_short
    long_description = place.description_long
    coords = {"lat": place.coordinates_lat, "lng": place.coordinates_lng}
    details = {
        "title": title,
        "imgs": imgs,
        "description_short": short_description,
        "description_long": long_description,
        "coordinates": coords,
    }
    return JsonResponse(details, safe=False, json_dumps_params={'ensure_ascii': False})
