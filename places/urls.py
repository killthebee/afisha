from django.urls import path

from places import views


app_name = 'places'
urlpatterns = [
    path('<int:pk>/', views.place_detail, name='place_detail'),
]