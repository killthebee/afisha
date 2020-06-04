from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.template import loader
from afisha import settings
from django.views.decorators.cache import never_cache
from django.contrib.staticfiles.views import serve
from django.conf.urls.static import static

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
                "detailsUrl": "{% static 'afisha/places/moscow_legends.json' %}",
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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('place/', include('places.urls', namespace='places')),
    path('', render_fp),
]
if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
