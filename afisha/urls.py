from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import never_cache
from django.contrib.staticfiles.views import serve
from django.conf.urls.static import static

from afisha import settings
from places.views import render_fp


urlpatterns = [
    path('admin/', admin.site.urls),
    path('place/', include('places.urls', namespace='places')),
    path(r'^tinymce/', include('tinymce.urls')),
    path('', render_fp),
]
if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
