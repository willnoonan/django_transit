from django.shortcuts import render
from django.conf import settings

# Create your views here.


def map_hello_world(request):
    """
    Renders a page with embedded Google map. Passes variables to the associated html template via dictionary
    'context'. The URL associated with this view function is defined in urls.py.
    """

    context = {
        "google_api_key": settings.GOOGLE_API_KEY,
        "lat_coord": 29.4190,
        "lng_coord": -98.4836,
    }
    return render(request, 'map/map.html', context)
