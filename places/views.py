from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse

from places.models import Place


def show_page(request):
    template = loader.get_template('index.html')
    places = Place.objects.all()

    features = []
    for place in places:
        coordinates = [place.longitude, place.latitude]
        short_title = place.title.split('«')[-1][:-1]
        place_id = place.pk

        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": coordinates,
            },
            "properties": {
                "title": short_title,
                "placeId": place_id,
                "detailsUrl": reverse('place', kwargs={'pk':place_id})
            },
        }
        features.append(feature)

    places_geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    context = {"places_geojson": places_geojson}
    render_page = template.render(context, request)
    return HttpResponse(render_page)


def fetch_place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    imgs = [image.image.url for image in place.images.all()]
    coords = {"lat": place.latitude, "lng": place.longitude}
    details = {
        "title": place.title,
        "imgs": imgs,
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": coords,
    }
    return JsonResponse(details, safe=False, json_dumps_params={'ensure_ascii': False})