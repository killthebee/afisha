from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse

from places.models import Place


def show_page(request):
    print(request)
    template = loader.get_template('index.html')
    places = Place.objects.all()
    print(places)

    features = []
    print(features)
    for place in places:
        coordinates = [place.longitude, place.latitude]
        short_title = place.title.split('«')[-1][:-1]
        place_id = place.pk
        print(place.images.all())

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
        print(features)

    places_geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    context = {"places_geojson": places_geojson}
    render_page = template.render(context, request)
    return HttpResponse(render_page)


def fetch_place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    title = place.title
    imgs = [image.image.url for image in place.images.all()]
    short_description = place.short_description
    long_description = place.long_description
    coords = {"lat": place.latitude, "lng": place.longitude}
    details = {
        "title": title,
        "imgs": imgs,
        "description_short": short_description,
        "description_long": long_description,
        "coordinates": coords,
    }
    return JsonResponse(details, safe=False, json_dumps_params={'ensure_ascii': False})