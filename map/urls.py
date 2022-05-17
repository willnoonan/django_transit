"""Defines URL patterns for map app."""
from django.urls import path
from . import views

app_name = "map"
urlpatterns = [
    path('map/', views.map_hello_world, name='map'),

    path('socket-test/', views.socket_view, name='socket-page'),
    path('ajax-test/', views.ajax_view, name='ajax-page'),
    path('ajax-hidden/', views.ajax_background_request_handler, name='ajax-hidden'),  # not seen by user, for
    # background processing use only
]