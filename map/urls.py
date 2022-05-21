"""Defines URL patterns for map app."""
from django.urls import path
from . import views

app_name = "map"
urlpatterns = [
    # Map:
    path('map/', views.map_hello_world, name='map'),

    # Socket Test:
    path('socket-test/', views.socket_view, name='socket-page'),

    # AJAX Test:
    path('ajax-test/', views.ajax_view, name='ajax-page'),
    path('ajax-hidden/', views.ajax_background_request_handler, name='ajax-hidden'),  # not seen by user, for
    # background processing use only
]