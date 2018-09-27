from django.urls import path

from .views import PlaceView
from .api import get_places

urlpatterns = [
    path('', PlaceView.as_view(), name='place_view'),
    path('api/places', get_places, name='get_places')
]
