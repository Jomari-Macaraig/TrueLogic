from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class PlaceView(TemplateView):
    template = 'index.html'
