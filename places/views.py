from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.template import loader

from places.models import Place
from places.utilities import slugify


def render_fp(request):
    template = loader.get_template('index.html')
    places = Place.objects.all()

    features = []
    for place in places:
        coordinates = [place.coordinates_lng, place.coordinates_lat]
        title = place.title
        place_id = slugify(place.title)

        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": coordinates,
            },
            "properties": {
                "title": title,
                "placeId": place_id,
                "detailsUrl": reverse('places:place_detail', args=[place.pk]),
            },
        }
        features.append(feature)

    geo_script = {
        "type": "FeatureCollection",
        "features": features,
    }
    context = {'geo_script': geo_script}
    render_page = template.render(context, request)
    return HttpResponse(render_page)


def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    title = place.title
    imgs = [image.image.url for image in place.images.all()]
    short_description = place.description_short
    long_description = place.text
    coords = {"lat": place.coordinates_lat, "lng": place.coordinates_lng}
    details = {
        "title": title,
        "imgs": imgs,
        "description_short": short_description,
        "description_long": long_description,
        "coordinates": coords,
    }
    return JsonResponse(details, safe=False, json_dumps_params={'ensure_ascii': False})
