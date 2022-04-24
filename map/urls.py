"""Defines URL patterns for map app."""
from django.urls import path
from . import views

app_name = "map"
urlpatterns = [
    # Home page
    path('map/', views.map_hello_world, name='map'),
]