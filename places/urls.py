from django.urls import path

from .views import PlaceView

urlpatterns = [
    path('', PlaceView, name='place_view')
]
