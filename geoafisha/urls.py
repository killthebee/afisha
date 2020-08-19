from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from places import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce', include('tinymce.urls')),
    path('place/<int:pk>/', views.fetch_place_detail, name='place'),
    path('', views.show_page)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
